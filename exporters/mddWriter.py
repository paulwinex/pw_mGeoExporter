import struct

import maya.cmds as cmds

from ..widgets.imports import *


class mddWriterClass():
    valList = (1, 0, 0, 0,
               0, 1, 0, 0,
               0, 0, -1, 0,
               0, 0, 0, 1)
    reversMatrix = om.MMatrix()
    om.MScriptUtil.createMatrixFromList(valList, reversMatrix)

    def __init__(self, par, op):
        self.par = par
        self.op = op
        self.pointCount = 0

    def export(self, path, start, end, step, scale):
        #open file
        res = True
        try:
            mddFile = open(path, 'wb')
        except IOError:
            self.par.msg2(1, 'Error open file ' + path)
            return False
        #get objects
        selection = om.MSelectionList()
        om.MGlobal.getActiveSelectionList(selection)
        pivotFilterSelection = self.filterObjects(selection)

        #first frame
        cmds.currentTime(start, edit=True)
        vertexPositionList = self.getPoints(selection, scale, pivotFilterSelection)
        #variables
        fps = float(mel.eval('currentTimeUnitToFPS'))
        self.par.msg2(2, 'FPS:', fps)
        numframes = int((end - start + 1)/step)
        numverts = len(vertexPositionList)/3
        self.pointCount = numverts
        print 'Frames', numframes
        print  'Point count', numverts
        #start write to file
        mddFile.write(struct.pack(">2i", numframes, numverts))
        times = [(frame/fps)*step for frame in xrange(numframes)]
        # print times
        mddFile.write(struct.pack(">%df" % numframes, *times))
        mddFile.write(struct.pack(">%df" % (numverts*3), *[v for v in vertexPositionList]))
        prev = 0
        #write sequence
        cmds.progressBar(self.par.progress, edit=True, pr=0)
        frame = start
        while frame < end+1:
            # if cmds.progressBar(self.par.progress, q=1, ic=1):
            if self.par.isCacneled():
                self.par.caselExport()
                res =  False
                break
            rng = end-start
            prc = (frame*100.0)/(end-start)
            cmds.progressBar(self.par.progress, edit=True, pr=int(prc))
            prev = int(prc)
            cmds.currentTime(frame, edit=True)
            self.par.statusMsg('Write cache frame '+str(frame))
            vertexPositionList = self.getPoints(selection, scale, pivotFilterSelection)
            if not (numverts*3) == len(vertexPositionList):
                om.MGlobal.displayError('TOPOLOGY HAS CHANGED!!!')
                self.par.msg2(1, 'TOPOLOGY HAS CHANGED!!!')
                res =  False
                break
            mddFile.write(struct.pack(">%df" % (numverts*3), *[v for v in vertexPositionList]))
            frame += step
        #close file
        mddFile.close()
        cmds.currentTime(start, edit=True)
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
                    position = objIt.position(om.MSpace.kObject) * (transformMatrix * self.reversMatrix)
                    polyPoints += [position.x*scale, position.y*scale, position.z*scale]
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
                    position = objIt.position(om.MSpace.kObject) * (transformMatrix * self.reversMatrix)
                    curvPolints += [position.x*scale, position.y*scale, position.z*scale]
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
                    pt = points[i] * matrix * self.reversMatrix
                    posPoints += [pt.x*scale, pt.y*scale, pt.z*scale]
                    num += 1
            elif curve.form() == om.MFnNurbsCurve.kClosed:
                length = points.length() - 1
                for i in range(length):
                    pt = points[i] * matrix * self.reversMatrix
                    posPoints += [pt.x*scale, pt.y*scale, pt.z*scale]
                    num += 1
            elif curve.form() == om.MFnNurbsCurve.kPeriodic:
                for i in range(points.length()-curve.degree()):
                    pt = points[i] * matrix * self.reversMatrix
                    posPoints += [pt.x*scale, pt.y*scale, pt.z*scale]
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
                partPoints += [vec[i].x*scale, vec[i].y*scale, vec[i].z*scale*-1]
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
                partPoints += [vec[i].x*scale, vec[i].y*scale, vec[i].z*scale*-1]
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
                mx = mx * self.reversMatrix
                tmx = om.MTransformationMatrix(mx)
                tr = tmx.getTranslation(om.MSpace.kWorld)
                pivPoints += [tr.x*scale, tr.y*scale, tr.z*scale]
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