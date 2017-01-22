from pymel.core import *

def export(path, start, end, step):
    if not loadPlugin():
        return False
    toExport = getObjects()
    select(toExport)
    roots = ' -root '  + ' -root '.join([x.fullPath() for x in toExport])
    # print ' '.join([x.name() for x in toExport])
    j = "-frameRange {start} {end} -step {step} -dataFormat ogawa {roots} -file {path}".format(start=start,
                                                                                                           end=end,
                                                                                                           path=path,
                                                                                                           roots=roots,
                                                                                                           step=step)
    mel.AbcExport(j=j)
    return True

def getObjects():
    toExport = []
    select(hi=1)
    sel = selected(transforms=1)
    def isGeo(obj):
        types = [u'mesh', u'nurbsCurve', u'particle', u'nParticle']
        if obj.type() == 'transform':
            ch = obj.getChildren()
            if ch:
                if all([x.type() in types for x in ch]):
                    if nodeIsVisible(obj):
                        return True
    for s in sel:
        if isGeo(s):
            toExport.append(s)
    return toExport

def loadPlugin():
    if not pluginInfo('AbcExport', loaded=1, query=True):
        try:
            cmds.loadPlugin( 'AbcExport' )
        except:
            warning('Error import Alembic plugin!!!')
            return False
    return True

def nodeIsVisible( node ):
    if not objExists(node): return False
    if not attributeQuery("visibility", node=node, exists=1):
        return False
    visible = node.visibility.get()


    if attributeQuery("intermediateObject", node=node, exists=1):
        visible = visible and not node.intermediateObject.get()

    if attributeQuery("overrideEnabled", node=node, exists=1) and  node.overrideEnabled.get():
        visible = visible and node.overrideVisibility.get()
    if visible:
        parents = listRelatives(node, parent=1)
        if parents:
            for p in parents:
                visible = visible and nodeIsVisible( p )
    return visible


import maya.OpenMaya as om
import alembic
import imath
import maya.OpenMayaFX as omx


def save_test_alembic(path):
    arch = alembic.Abc.OArchive(path)

    root = arch.getTop()
    fps = 24.0
    start_frame = 1
    end_frame = 5
    timesamp = alembic.AbcCoreAbstract.TimeSampling(1.0 / fps, start_frame / fps)
    index = arch.addTimeSampling(timesamp)
    opoints = alembic.AbcGeom.OPoints(root, "test", index)

    for i in range(start_frame, end_frame):
        opoints_sample = alembic.AbcGeom.OPointsSchemaSample()
        points = imath.V3fArray(40)
        ids = imath.IntArray(40)
        for y in range(40):
            points[y] = imath.V3f(y*0.01, (y+i)*0.01, y*0.01)
            ids[y] = y
        opoints_sample.setPositions(points)
        opoints_sample.setIds(ids)
        opoints.getSchema().set(opoints_sample)

# save_test_alembic("c:/points2.abc")

class AlembicPointWriterClass():
    def __init__(self, par, op):
        self.par = par
        self.op = op
        self.pointCount = 0

    def export(self, path, start, end, step, scale=1):
        #open file
        res = True

        # try:
        arch = alembic.Abc.OArchive(path)
        # except IOError:
        #     self.par.msg2(1, 'Error open file ' + path)
        #     return False
        arch.setCompressionHint(9)
        root = arch.getTop()
        fps = float(mel.eval('currentTimeUnitToFPS'))
        timesamp = alembic.AbcCoreAbstract.TimeSampling(1.0 / fps, start / fps)
        index = arch.addTimeSampling(timesamp)
        opoints = alembic.AbcGeom.OPoints(root, "alembic_points", index)

        #get objects
        selection = om.MSelectionList()
        om.MGlobal.getActiveSelectionList(selection)
        pivotFilterSelection = self.filterObjects(selection)

        #first frame
        cmds.currentTime(start, edit=True)
        # vertexPositionList = self.getPoints(selection, scale, pivotFilterSelection)
        #variables
        self.par.msg2(2, 'FPS:', fps)
        numframes = int((end - start + 1)/step)
        # numverts = len(vertexPositionList)
        # self.pointCount = numverts
        print 'Frames', numframes
        # print  'Point count', numverts
        prev = 0
        #write sequence
        cmds.progressBar(self.par.progress, edit=True, pr=0)
        frame = start
        #start write to file
        while frame < end+1:
            # if cmds.progressBar(self.par.progress, q=1, ic=1):
            if self.par.isCacneled():
                self.par.caselExport()
                res =  False
                break
            prc = (frame*100.0)/(end-start)
            cmds.progressBar(self.par.progress, edit=True, pr=int(prc))
            prev = int(prc)
            cmds.currentTime(frame, edit=True)
            self.par.statusMsg('Write cache frame '+str(frame))

            vertexPositionList = self.getPoints(selection, scale, pivotFilterSelection)
            self.pointCount = len(vertexPositionList)
            points = imath.V3fArray(self.pointCount)
            ids = imath.IntArray(self.pointCount)
            for i, pt in enumerate(vertexPositionList):
                points[i] = imath.V3f(*pt)
                ids[i] = i

            opoints_sample = alembic.AbcGeom.OPointsSchemaSample()
            opoints_sample.setPositions(points)
            opoints_sample.setIds(ids)
            opoints.getSchema().set(opoints_sample)
            frame += step
        #close file
        cmds.currentTime(start, edit=True)
        arch = None
        del arch
        return res

    def getPoints(self, selection, scale, piv):
        poslist = []
        #mesh
        if self.op['exportgeo']:
            polyPoints = self.polyPoints(selection, scale)
            if polyPoints:
                poslist += polyPoints
            del polyPoints

        #curves
        if self.op['expcurve']:
            curvPolints = self.curvePoints2(selection, scale)
            if curvPolints:
                poslist += curvPolints
            del curvPolints

        #particles
        if self.op['expparticle']:
            partPoints = self.particlePoints2(selection, scale)
            if partPoints:
                poslist += partPoints
            del partPoints

        #pivots
        if self.op['exppiv']:
            pivPoints = self.pivotPoints(piv, scale)
            if pivPoints:
                poslist += pivPoints
        return poslist

    #################################################

    def polyPoints(self, selection, scale):
        dagPath = om.MDagPath()
        iter = om.MItSelectionList(selection, om.MFn.kTransform)
        polyPoints = []
        while not iter.isDone():
            iter.getDagPath(dagPath)
            transformMatrix = dagPath.inclusiveMatrix()
            for child in self.shapeGenerator(dagPath, om.MFn.kMesh):
                objIt = om.MItMeshVertex(child)
                while not objIt.isDone():
                    position = objIt.position(om.MSpace.kObject) * transformMatrix# * self.reversMatrix)
                    polyPoints.append([position.x*scale, position.y*scale, position.z*scale])
                    objIt.next()
            iter.next()
        return polyPoints

    def curvePoints(self, selection, scale):
        dagPath = om.MDagPath()
        iter = om.MItSelectionList(selection, om.MFn.kTransform)
        curvPolints = []
        #print curvPolints
        while not iter.isDone():
            num = 0
            iter.getDagPath(dagPath)
            for child in self.shapeGenerator(dagPath, om.MFn.kNurbsCurve):
                transformMatrix = dagPath.exclusiveMatrix()
                objIt = om.MItCurveCV(child)
                while not objIt.isDone():
                    position = objIt.position(om.MSpace.kObject) * transformMatrix# * self.reversMatrix)
                    curvPolints.append([position.x*scale, position.y*scale, position.z*scale])
                    objIt.next()
                    num += 1
            iter.next()
        return curvPolints

    def curvePoints2(self, selection, scale):
        dagPath = om.MDagPath()
        posPoints = []
        iter = om.MItSelectionList(selection, om.MFn.kNurbsCurve )
        while not iter.isDone():
            iter.getDagPath(dagPath)
            curve = om.MFnNurbsCurve(dagPath)
            matrix = dagPath.inclusiveMatrix()
            points = om.MPointArray()
            curve.getCVs(points)
            num = 0
            if curve.form() == om.MFnNurbsCurve.kOpen:
                for i in range(points.length()):
                    pt = points[i] * matrix# * self.reversMatrix
                    posPoints.append([pt.x*scale, pt.y*scale, pt.z*scale])
                    num += 1
            elif curve.form() == om.MFnNurbsCurve.kClosed:
                length = points.length() - 1
                for i in range(length):
                    pt = points[i] * matrix# * self.reversMatrix
                    posPoints.append([pt.x*scale, pt.y*scale, pt.z*scale])
                    num += 1
            elif curve.form() == om.MFnNurbsCurve.kPeriodic:
                for i in range(points.length()-curve.degree()):
                    pt = points[i] * matrix# * self.reversMatrix
                    posPoints.append([pt.x*scale, pt.y*scale, pt.z*scale])
                    num += 1
            iter.next()
        return posPoints

    def particlePoints(self, selection, scale):
        dagPath = om.MDagPath()
        iter = om.MItSelectionList(selection, om.MFn.kParticle)
        partPoints = []
        vec = om.MVectorArray()
        while not iter.isDone():
            iter.getDagPath(dagPath)
            part = omx.MFnParticleSystem(dagPath)
            part.position(vec)
            for i in range(vec.length()):
                partPoints.append([vec[i].x*scale, vec[i].y*scale, vec[i].z*scale*-1])
            iter.next()
        return partPoints

    def particlePoints2(self, selection, scale):
        dagPath = om.MDagPath()
        iter = om.MItSelectionList(selection, om.MFn.kParticle)
        partPoints = []
        vec = om.MVectorArray()
        if self.op['globalpos']:
            space = 'worldPosition'
        else:space = 'position'
        while not iter.isDone():
            iter.getDagPath(dagPath)
            part = omx.MFnParticleSystem(dagPath)
            part.getPerParticleAttribute(space, vec)
            for i in range(vec.length()):
                partPoints.append([vec[i].x*scale, vec[i].y*scale, vec[i].z*scale*-1])
            iter.next()
        return partPoints

    def pivotPoints(self, selection, scale):
        dagPath = om.MDagPath()
        if selection:
            iter = om.MItSelectionList(selection, om.MFn.kTransform)
            pivPoints = []
            p = 0
            while not iter.isDone():
                iter.getDagPath(dagPath)
                mx = dagPath.inclusiveMatrix()
                # mx = mx * self.reversMatrix
                tmx = om.MTransformationMatrix(mx)
                tr = tmx.getTranslation(om.MSpace.kWorld)
                pivPoints.append([tr.x*scale, tr.y*scale, tr.z*scale])
                p += 1
                iter.next()
            iter.reset()
            return pivPoints
        return None

    def shapeGenerator(self, dagPath, fn):
        dagNode = om.MFnDagNode(dagPath)
        for i in range(dagNode.childCount()):
            child = dagNode.child(i)
            if child.apiType() == fn:
                node = om.MFnDependencyNode(child)
                intermediatePlug = om.MPlug(node.findPlug("intermediateObject"))
                if not intermediatePlug.asBool():
                    yield child

    def filterObjects(self, selection):
        '''
        copy from mGeoDatareader.pivots
        '''
        names = []
        selection.getSelectionStrings(names)

        exportnames = []
        token = self.tokenPrefix(self.op['exppivfilter'])

        if token:
            for i, n  in enumerate(names):
                for t in token:
                    if t in n:
                        exportnames.append(n)
        else:
            exportnames = names

        if self.op['exppivskipnoshape']:
            exportnames = self.checkShape(exportnames)

        if exportnames:
            pivExport = om.MSelectionList()
            for name in exportnames:
                pivExport.add(name)
            return pivExport
        return None

    def tokenPrefix(self, pref):
        return re.findall(r'\S+', pref)

    def checkShape(self, array):
        result = []
        for a in array:
            if cmds.listRelatives(a, s=1):
                result.append(a)
        return result


class AlembicGeoWriterClass(object):
    pass