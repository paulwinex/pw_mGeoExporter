import maya.OpenMaya as om
import maya.OpenMaya as om
import maya.OpenMayaFX as omx
from maya import cmds
import re

class geoCollector(object):
    def __init__(self, parent=None):
        self.name = 'base'
        self.textVariables = {'setPref':'mgeo_',          #selection set prefix
                              'NoParent':'NotParet',       #No parent for parents group
                              'defShader':'defaultShader',  #default name of shader
                              'noShader':'errorShader',    #shader not found
                              'deflayer':'defaultLayer',   #display layer not in token
                              'noObject':'otherObjects',             #file format
                              'noCurveObj':'otherCurves',
                              'otherInstances':'otherInstances'
        }
        self.spetialObjectsList = {'stereoRigTransform':self.getStereoRigShapeNode}

        self.pointAttribArray = {}
        self.primAttribArray = {}
        self.vertxAttribArray = {}
        self.polyCount = 0
        self.pointsCount = 0
        self.defaultValueText = 'defaultValue'

        self.vertexCount = 0
        self.topologyArray = []
        self.vertexArray = []
        self.knotsArray = []
        self.orderArray = []
        self.openClose = []
        self.endInterpolation = []
        self.defaultValues = {'Cd':[1, 1, 1],
                              'P':[0,0,0],
                              'scale':[1, 1, 1],
                              'orient':[0, 0, 0, 1]}

        self.primGroupsArray = {}
        self.pointGroupsArray = {}

    def topology(self):
        return self.topologyArray

    def vertex(self):
        return self.vertexArray

    def attr(self):
        return self.pointAttribArray

    def offset(self):
        if self.pointAttribArray.get('P', False):
            return len(self.pointAttribArray['P'])
        else:
            return 0
    def getVertexCount(self):
        return self.vertexCount

    def pointGroups(self):
        return self.pointGroups

    def pointAttribs(self):
        return self.pointAttribArray

    def primGroups(self):
        return self.primGroupsArray

    def primAttribs(self):
        return self.primAttribArray

    def primCount(self):
        return self.polyCount
    def pointCount(self):
        return self.pointsCount

    def getParent(self,name, filter=None):
        if cmds.objExists(name):
            if cmds.nodeType(name) == 'mesh':
                name = cmds.listRelatives(name, p=True, f=True)
            par = cmds.listRelatives(name, p=True, f=True)
            if par:
                parent = par[0].split('|')[-1]
                if filter:
                    tok = self.tokenPrefix(filter)
                    for t in tok:
                        if t in parent:
                            return parent
                    return self.getParent(par[0], filter)
                else:
                    return parent
            else:
                return 'NoParent'

    def getTransform(self, name):
        if cmds.objExists(name):
            par = cmds.listRelatives(name, p=True, f=True)
            if par:
                return par[0]
        return None


    def checkLegalChar(self,string):
        pattern = '[^A-Za-z0-9]+'
        return re.sub(pattern, '_', string)

    def tokenPrefix(self, pref):
#        pref = self.checkLegalChar(pref)
        return re.findall(r'\S+', pref)

    def tokenAttributes(self, attrs):
        dict = {}
        for a in attrs:
            if '(' in a:
                d = a.split('(')[1].replace(')','')
                if d.replace('.','').isdigit():
                    d = float(d)
                a = a.split('(')[0]
                dict[a] = d
            else:
                dict[a] = None
        # print dict
        return dict

    def reorderAttrs(self, attrs):
        res = {}

        def convertDefaults(line):
            m = re.match(r'^\d+(\.?\d+)?$', str(line)) # float or int
            if m:
                return float(line)
            m = re.match(r'^(\d+(\.?\d+)?,?){1,4}$', line) #vector3 or vector4
            if m:
                return [float(x) for x in line.split(',')]

            return str(line)

        for a in attrs:
            a['default'] = convertDefaults(a['default'])
            res.update({a['src']: { k:v for k, v in a.items() if not k == 'src'}})
        return res


    def getDisplayLayer(self, obj,op):
        #try transform
        l = cmds.listConnections(obj, type="displayLayer")
        if not l:
            #try shape
            l = cmds.listConnections(cmds.listRelatives(obj, s=1)[0] , type="displayLayer")
        if not l:
            #find parent
            parents = True
            while parents:
                parents = cmds.listRelatives(obj, p=1)
                if parents:
                    l = cmds.listConnections(parents[0] , type="displayLayer")
                    if l:break
                    else:obj = parents[0]
        if l:
            if op[1]:
                tok = self.tokenPrefix(op[1])
                for t in tok:
                    if t in l[0]:
                        return l[0]
                return 'deflayer'
            else:
                return l[0]
        else:
            return self.textVariables['deflayer']

    def convertArrayDisplLayer(self, names, index):
        dict = {}
        for n in names:
            dict[n] = []
        for i, c in enumerate(index):
            name = names[i]
            for d in dict:
                if d == name:
                    dict[d] += [c, True]
                else:
                    dict[d] += [c, False]
        return dict

    def filterName(self, name, filter, default):
        if filter:
            tok = self.tokenPrefix(filter)
            for t in tok:
                if t in name:
                    return name
            return default
        else:
            return name

    def convertObjectNamesToGroupArray(self, data, names, group, filter, default):
        dict = {}

        for i in range(len(names)):
            names[i] = group+self.filterName(names[i], filter, default)
        for n in names:
            dict[n] = []

        for i, c in enumerate(data):
            name = names[i]
            for d in dict:
                if d == name:
                    dict[d] += [c, True]
                else:
                    dict[d] += [c, False]
        return dict

    def getAttribFromNode(self, name, attr, aType, default=None):
        #name mast be shape
        transformOnly = ['visibility']
        fAttr = '.'.join([name, attr])
        value = default
        if cmds.attributeQuery( attr, node=name, exists=True ) and not attr.lower() in transformOnly:
            value = cmds.getAttr( fAttr )
        else:
            trnsfrm = self.getTransform(name)
            if trnsfrm:
                if cmds.attributeQuery( attr, node=trnsfrm, exists=True ):
                    fAttr = '.'.join([trnsfrm, attr])
                    value = cmds.getAttr( fAttr )
        if not value is None:
            if isinstance(value, list):
                if isinstance(value[0], tuple):
                    value = list(value[0])
            try:
                value = aType(value)
            except:
                pass
        return value

    def shapeGenerator(self, dagPath, fn):
        dagNode = om.MFnDagNode(dagPath)
        for i in range(dagNode.childCount()):
            child = dagNode.child(i)
            if child.apiType() == fn:
                node = om.MFnDependencyNode(child)
                intermediatePlug = om.MPlug(node.findPlug( "intermediateObject" ))
                if not intermediatePlug.asBool():
                    yield child

    def getStereoRigShapeNode(self, name):
        sh = cmds.listRelatives(name, s=1)
        for s in sh:
            if cmds.nodeType(s) == 'stereoRigCamera':
                return s
            else:
                return name

    def checkAttribtypes(self, nodes, attrs):
        #check types
        allTypes = {'bool':bool,
                    'enum':int,
                    'string':str,
                    'byte':int,
                    'long':float,
                    'double3':list,
                    'doubleLinear':float,
                    'short':int,
                    'float':float,
                    'float3':list,
                    'time':float,
                    'doubleAngle':float,
                    'double':float,
                    'double4':list,
                    'double2':list,
                    'doubleArray':list,
                    'vectorArray':list}
        defaults = {'bool':False,
                    'enum':0,
                    'string':'',
                    'byte':0,
                    'long':0.0,
                    'double3':[0,0,0],
                    'doubleLinear':0,
                    'short':0,
                    'float':0.0,
                    'float3':[0,0,0],
                    'time':0.0,
                    'doubleAngle':0.0,
                    'double':0.0,
                    'double4':[0,0,0,1],
                    'double2':[0,0],
                    'doubleArray':0,
                    'vectorArray':[0,0,0]}
        newAttrs = {}
        pp = []
        for a in attrs:
            types = [] #all types for current attrib
            for n in nodes:
                aType = None
                atr = '.'.join([n,a])
                if cmds.attributeQuery( a, node=n, exists=True ):
                    aType = cmds.getAttr(atr, type=True)
                else:
                    n = self.getTransform(n)
                    if n:
                        if cmds.attributeQuery( a, node=n, exists=True ):
                            atr = '.'.join([n,a])
                            aType = cmds.getAttr(atr, type=True)
                types.append(aType)
            types = list(set(types))
            while None in types:
                types.remove(None)
            if len(types)>1:
                self.par.parent.msg2(1, 'Attributes have different type on different nodes and will be skipped:',a)
            elif len(types) == 0:
                self.par.parent.msg2(1, 'Attribute not found and will be skipped:',a)
            else:
                # print a, types
                if types[0] in allTypes or not attrs[a]['default']:
                    pyType = allTypes[types[0]]
                    if not attrs[a] is None:
                        df = attrs[a]['default']
                        if not df and isinstance(df, (str, unicode)):
                            df = defaults[types[0]]
                        if isinstance(df, pyType):
                            newAttrs[a] = [attrs[a]['default'], pyType, attrs[a]['rename']]
                        else:
                            # print type(df), pyType
                            self.par.parent.msg2(1, 'Default value is a wrong type, attribute will be skipped:',a)
                    else:

                        df = defaults[types[0]]
                        newAttrs[a] = [df, pyType, attrs[a]['rename']]
                else:
                    newAttrs[a] = [None, None]
            if types:
                if 'array' in types[0].lower():
                    pp.append(a)
        return newAttrs, pp

    def checkDefault(self, typ, val):
        if '3' in typ and isinstance(val, list):
            return val
        elif '4' in typ and isinstance(val, list):
            return val
        else:
            return val

# ##############################################################################################
# POLYGONS
class polyReader(geoCollector):
    def __init__(self, op, parent=None):
        geoCollector.__init__(self)
        self.op = op
        self.par = parent
        self.name = 'Polygons'

    def printIter(self, iter):
        # print ' '.join([x.name() for x in toExport])
        dagPath = om.MDagPath()
        while not iter.isDone():
            iter.getDagPath( dagPath )
            # print dagPath.fullPathName()
            iter.next()
        iter.reset()

    def read(self, selection):
        iter = om.MItSelectionList ( selection, om.MFn.kTransform )
#        iter = om.MItSelectionList ( selection, om.MFn.kMesh )
        self.readPoints(iter)
        if self.par.isCanceled():
            return self.cacelExport()
        self.readPolygons(iter)
        if self.par.isCanceled():
            return self.cacelExport()
        if self.op['expuv']:
            self.readVertexUV(iter)
        if self.par.isCanceled():
            return self.cacelExport()
        if self.op['expcolor']:
            self.readVertexColor(iter)
        if self.par.isCanceled():
            return self.cacelExport()
        if self.op['expvertexnorm']:
            self.readVertexNormals(iter)
        if self.par.isCanceled():
            return self.cacelExport()
        if self.op['expcrease']:
            self.readCreaseData(iter)
        if self.par.isCanceled():
            return self.cacelExport()
        if self.op['geocustomattr'][0] and self.op['geocustomattr'][1]:
            self.readCustomAttrib(iter)
        if self.par.isCanceled():
            return self.cacelExport()
        self.parseGroups(iter, selection)
        return True

    def cacelExport(self):
        self.par.cancelExport()
        return True

    def readPoints(self, iter):
        points = []
        dagPath = om.MDagPath()
        scale = self.op['scale']
        while not iter.isDone():
            if self.par.isCanceled():
                return self.cacelExport()
            iter.getDagPath( dagPath )
            for child in self.shapeGenerator(dagPath, om.MFn.kMesh):
                meshFn = om.MFnMesh(child)
                pointArray = om.MFloatPointArray()
                meshFn.getPoints(pointArray)

                #local or world position
                matrix = 1
                if self.op['globalpos']: #to world coord
                    mx = dagPath.inclusiveMatrix()
                    matrix = om.MFloatMatrix(mx.matrix)
                if False:
                    trObj = dagPath.transform()
                    dag2 = om.MDagPath()
                    om.MDagPath.getAPathTo(trObj, dag2)
                    mx = dag2.inclusiveMatrixInverse()
                    matrix = om.MFloatMatrix(mx.matrix)

                for i in range(pointArray.length()):
                    pt = pointArray[i] * matrix
                    points.append([pt.x*scale, pt.y*scale, pt.z*scale, 1])
            iter.next()
        iter.reset()
        self.pointAttribArray['P'] = points
        self.pointsCount = len(points)

    def readPolygons(self, iter):
        self.vertexCount = 0
        vtxoffset = 0
        polygonCount = 0
        dagPath = om.MDagPath()
        while not iter.isDone():
            if self.par.isCanceled():
                return self.cacelExport()
            iter.getDagPath( dagPath)
            for child in self.shapeGenerator(dagPath, om.MFn.kMesh):
                iterPolys = om.MItMeshPolygon( child )
                while not iterPolys.isDone():
                    #vertex order
                    verts = om.MIntArray()
                    iterPolys.getVertices( verts )

                    for v in reversed(list(verts)):
                    #   for v in list(verts):
                        self.topologyArray.append(v+vtxoffset)
                        #vertex numder from order for poly
                    nextPoly = []
                    for vv in range(len(list(verts))):
                        nextPoly.append(self.vertexCount)
                        self.vertexCount +=1
                    self.vertexArray.append([nextPoly])
                    polygonCount += 1

                    iterPolys.next()
                meshFn = om.MFnMesh(child)
                MpointArray = om.MFloatPointArray()
                meshFn.getPoints(MpointArray)
                vtxoffset +=  MpointArray.length()
            iter.next()
        iter.reset()
        self.polyCount = polygonCount

    def parseGroups(self, iter, selection):
        if self.primCount():
            prefix = self.op['geoglobalname']
            #main geo group
            if prefix and self.op['geoglobalEnable']:
                self.primGroupsArray[prefix] = [self.primCount(), True]
            # else:
            #     prefix = 'POLY'

            #PER OBJECT GROUPS
            if self.op['expgeogrp_obj'][0]:
                #get Names
                dagPath = om.MDagPath()
                names = []
                data = []
                while not iter.isDone():
                    iter.getDagPath( dagPath )
                    allPoly = 0
                    dagNode = om.MFnDagNode(dagPath)
                    if dagNode.childCount():
                        child = dagNode.child(0)
                        if child.apiType() == om.MFn.kMesh:
                            for child in self.shapeGenerator(dagPath, om.MFn.kMesh):
                                meshFn = om.MFnMesh(child)
                                allPoly += meshFn.numPolygons()
                    if allPoly:
                        objName = om.MFnDependencyNode(dagPath.transform()).name()
                        names.append(objName)
                        data.append(allPoly)
                    iter.next()
                grpName = prefix+self.op['expgeogrp_obj'][2]
                objGroups = self.convertObjectNamesToGroupArray(data, names,grpName, self.op['expgeogrp_obj'][1],self.textVariables['noObject'])
                if objGroups:
                    self.primGroupsArray.update(objGroups)

#            PER SHAPE GROUPS
            if self.op['expgeogrp_shp'][0]:
                #get Names
                iter.reset()
                dagPath = om.MDagPath()
                names = []
                data = []
                while not iter.isDone():
                    iter.getDagPath( dagPath )
                    for child in self.shapeGenerator(dagPath, om.MFn.kMesh):
                        shapeName = om.MFnDependencyNode(child).name()
                        names.append(shapeName)
                        meshFn = om.MFnMesh(child)
                        data.append(meshFn.numPolygons())
                    iter.next()
                objGroups = self.convertObjectNamesToGroupArray(data, names,prefix+self.op['expgeogrp_shp'][2], self.op['expgeogrp_shp'][1],self.textVariables['noObject'])
                if objGroups:
                    self.primGroupsArray.update(objGroups)

            #PER SHADER GROUPS
            if self.op['expgeogrp_mtl'][0]:
                iter.reset()
                matArray = [] #materials
                indexArray = [] #indecis
                while not iter.isDone():
                    dagPath = om.MDagPath()
                    iter.getDagPath( dagPath )
                    for child in self.shapeGenerator(dagPath, om.MFn.kMesh):
                        meshFn = om.MFnMesh(child)
                        indices = om.MIntArray()
                        shaders = om.MObjectArray()
                        instanceNumber = 0
                        meshFn.getConnectedShaders(	instanceNumber, shaders, indices )
                        #matNames array
                        mats = [] #per object mat
                        for i in range(shaders.length()):
                            dg = om.MFnDependencyNode(shaders[i])
                            name = self.getMaterialName(str(dg.name()))
                            mats.append(self.checkLegalChar(prefix+self.op['expgeogrp_mtl'][2]+name))
                        ind = []
                        for i in range(indices.length()):
                            ind.append(int( indices[i]))

                        matArray.append(mats)
                        indexArray.append(ind)

                    iter.next()
                    #convert to dic
                result = self.convertArrayMtl(matArray, indexArray)
                if result:
                    self.primGroupsArray.update(result)

            #PER PARENT GROUPS
            if self.op['expgeogrp_parent'][0]:
                prntGroups = {}         #parent groups
                iter.reset()
                names = []
                counts = []
                while not iter.isDone():
                    dagPath = om.MDagPath()
                    iter.getDagPath( dagPath )
                    for child in self.shapeGenerator(dagPath, om.MFn.kMesh):
                        meshFn = om.MFnMesh(child)
                        name = om.MDagPath.getAPathTo(child).fullPathName()
                        par = self.getParent(name, self.op['expgeogrp_parent'][1])
                        names.append(self.checkLegalChar(prefix+self.op['expgeogrp_parent'][2]+par))
                        counts.append(meshFn.numPolygons())
                    iter.next()
                prntGroups = self.convertArrayDisplLayer(names, counts)
                if prntGroups:
                    self.primGroupsArray.update(prntGroups)

            # PER DISPLAY LAYER GROUPS
            if self.op['expgeogrp_layer'][0]:
                titer = om.MItSelectionList ( selection, om.MFn.kTransform )
                names = []
                counts = []
                dagPath = om.MDagPath()
                mObj = om.MObject()
                while not titer.isDone():
                    titer.getDagPath( dagPath )
                    dagNode = om.MFnDagNode(dagPath)
                    if dagNode.childCount():
                        child = dagNode.child(0)
                        if child.apiType() == om.MFn.kMesh:
                            titer.getDependNode( mObj )
                            meshFn = om.MFnMesh(dagPath)
                            #polyCount
                            counts.append(meshFn.numPolygons())
                            #read layer
                            name = om.MDagPath.getAPathTo(mObj).fullPathName()
                            layer = self.getDisplayLayer(name,self.op['expgeogrp_layer'])
                            names.append(self.checkLegalChar(prefix+self.op['expgeogrp_layer'][2]+layer))
                    titer.next()
                displLayerGroups = self.convertArrayDisplLayer(names, counts)
                if displLayerGroups:
                    self.primGroupsArray.update(displLayerGroups)

            iter.reset()

    def readVertexUV(self,iter):
        dagPath = om.MDagPath()
        mObj = om.MObject()
        setNum = 0 #numUVSets
        UVArray = []
        #get max uv setCount
        while not iter.isDone():
            iter.getDagPath( dagPath )
            for child in self.shapeGenerator(dagPath, om.MFn.kMesh):
                meshFn = om.MFnMesh(child)
                n = meshFn.numUVSets()
                if n > setNum:setNum = n
            iter.next()
        iter.reset()
        if setNum:
            while not iter.isDone():
                iter.getDagPath( dagPath )
                for child in self.shapeGenerator(dagPath, om.MFn.kMesh):
                    meshFn = om.MFnMesh(child)
                    iterPolys = om.MItMeshPolygon( child )
                    names = []
                    meshFn.getUVSetNames(names)

                    for i, uvName in enumerate(names):
                        if self.op['uvnaming'] == 1:
                            setName = 'uv'
                            if i:setName += str(i)
                        elif self.op['uvnaming'] == 2:
                            if not i:
                                setName = 'uv'
                            else:
                                setName = 'uv_'+uvName
                        else:
                            setName = 'uv_'+uvName
                        UVArray = []
                        while not iterPolys.isDone():
                            try:
                                if iterPolys.hasUVs(uvName):
        #                            try:
                                    uArray= om.MFloatArray()
                                    vArray= om.MFloatArray()
                                    iterPolys.getUVs(uArray, vArray, uvName)
                                    u = list(uArray)
                                    v = list(vArray)
                                    for i in reversed(range(len(u))):
                                        UVArray.append([u[i],v[i],0])
                                else:
                                    polyVertCount = iterPolys.polygonVertexCount()
                                    UVArray += [[0,0,0]]*polyVertCount
                            except:
                                polyVertCount = iterPolys.polygonVertexCount()
                                UVArray += [[0,0,0]]*polyVertCount
                                print 'Error object!!!!'
                            iterPolys.next()
                        iterPolys.reset()

                        if not setName in self.vertxAttribArray:
                            self.vertxAttribArray[setName] = UVArray
                        else:
                            self.vertxAttribArray[setName] += UVArray
                iter.next()

        iter.reset()

    def readVertexColor(self, iter):
        defaultColor = 1

        dagPath = om.MDagPath()
#        mObj = om.MObject()

        df = [defaultColor for i in range(3)]
        names = set()
        while not iter.isDone():
            n = []
            iter.getDagPath( dagPath )
            for child in self.shapeGenerator(dagPath, om.MFn.kMesh):
                meshFn = om.MFnMesh(child)
                meshFn.getColorSetNames(n)
                names.update(n)
            iter.next()
        iter.reset()
        if names:
            while not iter.isDone():
                iter.getDagPath( dagPath )
                for child in self.shapeGenerator(dagPath, om.MFn.kMesh):
                    meshFn = om.MFnMesh(child)
                    for i, n in enumerate( names ):
                        colorArray = []
                        if meshFn.hasColorChannels(n):
#                                iter.getDependNode( mObj )
                            iterPolys = om.MItMeshPolygon( child )
                            while not iterPolys.isDone():
                                colors = om.MColorArray()
                                iterPolys.getColors(colors, n)
                                for j in reversed( range( colors.length() ) ):
                                    colorArray += [[max(0,colors[j].r),max(0,colors[j].g),max(0,colors[j].b)]]
                                iterPolys.next()
                        else:
                            colorArray +=[df]*meshFn.numFaceVertices()
                        ##########
                        #get set name
                        if self.op['colornaming'] == 1:
                            setName = 'Cd'
                            if i:setName += str(i)

                        elif self.op['colornaming'] == 2:
                            setName = 'Cd'
                            if i:
                                setName = 'Cd_'+n
                        else:
                            setName = 'Cd_'+n
                        ##########
                        #write attribs
                        if not setName in self.vertxAttribArray:
                            self.vertxAttribArray[setName] = colorArray
                        else:
                            self.vertxAttribArray[setName] += colorArray


                iter.next()
            iter.reset()

    def readVertexNormals(self, iter):
        iter.reset()
        NArray = []
        if iter:
#            mObj = om.MObject()
            while not iter.isDone():
                dagPath = om.MDagPath()
#                iter.getDependNode( mObj )
                iter.getDagPath( dagPath )
                for child in self.shapeGenerator(dagPath, om.MFn.kMesh):
#                        meshFn = om.MFnMesh(child)
#                       iter.getDagPath( dagPath )
                    iterPolys = om.MItMeshPolygon( child )
                    mx =  dagPath.inclusiveMatrix()
                    #matrix = om.MFloatMatrix(mx.matrix)
                    while not iterPolys.isDone():
                        verts = om.MIntArray()
                        iterPolys.getVertices( verts )
                        vn = []
                        space = om.MSpace.kPreTransform
                        nrm = om.MVectorArray()
                        iterPolys.getNormals(nrm, space)
                        for i in reversed(range(nrm.length())):
                            tn = nrm[i].transformAsNormal( mx )
                            vn.append([tn.x,tn.y,tn.z])
                        NArray += vn
                        iterPolys.next()

                iter.next()
        self.vertxAttribArray['N'] = NArray
        iter.reset()

    def readCreaseData(self, iter):
        allVtxData = []
        dagPath = om.MDagPath()
        edgeIds = om.MUintArray()
        edgeCreaseData= om.MDoubleArray()

        while not iter.isDone():
            iter.getDagPath( dagPath )
            for child in self.shapeGenerator(dagPath, om.MFn.kMesh):
                meshFn = om.MFnMesh(child)
                iterp = om.MItMeshPolygon( child )
                try:
                    meshFn.getCreaseEdges(edgeIds, edgeCreaseData)
                    while not iterp.isDone():
                        vtxArray = om.MIntArray()
                        iterp.getVertices(vtxArray)
                        polyCreaseArray = []
                        edgeArr = om.MIntArray()
                        iterp.getEdges(edgeArr)
                        edgeArr = list(edgeArr)
                        for edge in edgeArr:
                            if edge in edgeIds:
                                polyCreaseArray.append(edgeCreaseData[list(edgeIds).index(edge)])
                            else:
                                polyCreaseArray.append(0)
                        iterp.next()
                        polyCreaseArray = list(reversed(polyCreaseArray))
                        pop = polyCreaseArray.pop(0)
                        polyCreaseArray.append(pop)
                        allVtxData += polyCreaseArray
                except:
                    numVtx = meshFn.numFaceVertices()
                    allVtxData += [0]*numVtx
                    # iter.next()
                    # continue
            iter.next()
        self.vertxAttribArray['creaseweight'] = allVtxData
        iter.reset()

    def readCustomAttrib(self, iter):
        #check attrib types
        # collect attrib+type+default
        #read attribs
        # attribs = self.tokenPrefix(self.op['geocustomattr'][1])
        # attribs = self.tokenAttributes(attribs)
        attribs = self.reorderAttrs(self.op['geocustomattr'][1])
        dagPath = om.MDagPath()
        types = []
        nodes = []
        counts = []
        while not iter.isDone():
            iter.getDagPath( dagPath )
            for child in self.shapeGenerator(dagPath, om.MFn.kMesh):
                meshFn = om.MFnMesh(child)
                objName = om.MDagPath.getAPathTo(child).fullPathName()
                nodes.append(objName)
                counts.append(meshFn.numPolygons())
            iter.next()
        iter.reset()
        #attribs = attributes + default
        #nodes = shapes
        #checkAttrs
        checkedAttrb, pp = self.checkAttribtypes(nodes, attribs)
        if not checkedAttrb:
            return
        for i, node in enumerate(nodes):
            for attr in checkedAttrb:
                default = checkedAttrb[attr][0]
                attrType = checkedAttrb[attr][1]
                renamed = self.checkLegalChar(checkedAttrb[attr][2]) or self.checkLegalChar(attr)
                if not renamed in self.primAttribArray:
                    self.primAttribArray[renamed] = []
                value = self.getAttribFromNode(node, attr, attrType)
                if value is None:
                    value = default
                self.primAttribArray[renamed] += ([value]*counts[i])

    def getMaterialName(self, sg):
        mat = cmds.listConnections(sg + ".surfaceShader")
        if not mat:
            if cmds.attributeQuery("miMaterialShader",n=sg, ex=1):
                mat = cmds.listConnections(sg + ".miMaterialShader")
            if not mat:
                return 'noShader'
        if self.op['expgeogrp_mtl'][1]:
            tok = self.tokenPrefix(self.op['expgeogrp_mtl'][1])
            for t in tok:
                if t in mat[0]:
                    return mat[0]
            return self.textVariables['defShader']
        return mat[0]

    def convertArrayMtl(self,names, index):
        ofs = 0
        indArray = []
        for x in index:
            l = len(names[index.index(x)])
            nx = []
            for i in x:
                nx.append(i + ofs)
            indArray += nx
            ofs += l
        mtlArray = []
        for m in names:mtlArray += m

        dict = {}
        for m in mtlArray:
            #if not m in dict:dict[m] = []
            if not m in dict:
                dict[m] = []
            #self.options['mtlgrp'][2]
        for i in indArray:
            mname = mtlArray[i]
            for d in dict.keys():
                if d == mname:
                    if dict[d]:
                        if dict[d][-1] == True:
                            dict[d][-2] += 1
                        else:
                            dict[d]+=[1,True]
                    else:
                        dict[d]+=[1,True]

                else:
                    if dict[d]:
                        if dict[d][-1] == False:
                            dict[d][-2] +=1
                        else:
                            dict[d]+=[1,False]
                    else:
                        dict[d]+=[1,False]

        return dict

#################################################################################################
# CURVES
class curveReader(geoCollector):
    def __init__(self, op, parent=None):
        geoCollector.__init__(self)
        self.op = op
        self.par = parent
        self.name = 'Curves'


    def read(self, selection):
        iter = om.MItSelectionList ( selection, om.MFn.kTransform )
        points, curvesCount = self.readPoints(iter)
        if points:
            self.pointAttribArray['P'] = points
            iter.reset()
            if self.op['curvcustomattrib'][0]:
                self.readCustomAttributes(iter)
            self.pointsCount = len(points)
            self.polyCount = curvesCount
            self.parseGroups(iter, selection)
        return True

    def readCustomAttributes(self, iter):
        attribs = self.reorderAttrs(self.op['curvcustomattrib'][1])
        dagPath = om.MDagPath()
        types = []
        nodes = []
        # counts = []
        while not iter.isDone():
            iter.getDagPath( dagPath )
            for child in self.shapeGenerator(dagPath, om.MFn.kNurbsCurve):
                # meshFn = om.MFnNurbsCurve(child)
                objName = om.MDagPath.getAPathTo(child).fullPathName()
                nodes.append(objName)
                # counts.append(1)
            iter.next()
        iter.reset()
        checkedAttrb, pp = self.checkAttribtypes(nodes, attribs)
        if not checkedAttrb:
            return
        for i, node in enumerate(nodes):
            for attr in checkedAttrb:
                default = checkedAttrb[attr][0]
                attrType = checkedAttrb[attr][1]
                renamed = checkedAttrb[attr][2] or attr
                if not renamed in self.primAttribArray:
                    self.primAttribArray[renamed] = []
                value = self.getAttribFromNode(node, attr, attrType)
                if value is None:
                    value = default
                self.primAttribArray[renamed] += ([value])

    def readPoints(self, iter):
        formInterp = {1:False, 3:True, 2:True}
        dagPath = om.MDagPath()
        posPoints = []
        curvesCount = 0
        vtx = 0
        scale = self.op['scale']
        while not iter.isDone():
            iter.getDagPath( dagPath )
            for child in self.shapeGenerator(dagPath, om.MFn.kNurbsCurve):
                curve = om.MFnNurbsCurve(child)
                matrix = 1
                if self.op['globalpos']:
                    matrix =  dagPath.inclusiveMatrix()
                #points
                points = om.MPointArray()
                curve.getCVs(points)
                curvPoints = []
                primPoints = []
                if curve.form() == om.MFnNurbsCurve.kOpen:
                    j = 0
                    for i in range(points.length()):
                        pt = points[i] * matrix
                        pos = [pt.x*scale, pt.y*scale, pt.z*scale, 1]
                        curvPoints.append(pos)
                        primPoints.append(self.vertexCount)
                        self.topologyArray.append(j+vtx)
                        j+=1
                        self.vertexCount+=1
                    vtx+=j
                    posPoints += curvPoints
                    self.vertexArray.append([primPoints])
                    #knots
                    order = curve.degree()
                    self.orderArray.append(order)
                    mKnots = om.MDoubleArray()
                    curve.getKnots(mKnots)
                    knots = [float(mKnots[0])] +  list((x for x in mKnots )) + [float(mKnots[-1])]
                    self.knotsArray.append(knots)
                    self.openClose.append(formInterp[curve.form()]) #false
                    self.endInterpolation.append(not formInterp[curve.form()]) #true
                    curvesCount += 1

                elif curve.form() == om.MFnNurbsCurve.kClosed:
                    j = 0
                    length = points.length()-1#-curve.degree()
                    for i in range(length):
                        pt = points[i] * matrix
                        pos = [pt.x*scale, pt.y*scale, pt.z*scale, 1]
                        curvPoints.append(pos)
                        primPoints.append(self.vertexCount)
                        self.topologyArray.append(j+vtx)
                        j+=1
                        self.vertexCount+=1
                    vtx+=j
                    posPoints += curvPoints
                    self.vertexArray.append([primPoints])
                    #knots
                    order = curve.degree()
                    self.orderArray.append(order)
                    mKnots = om.MDoubleArray()
                    curve.getKnots(mKnots)
                    knots = [float(mKnots[0])] +  list((x for x in mKnots )) + [float(mKnots[-1])]
                    self.knotsArray.append(knots)
                    self.openClose.append(formInterp[curve.form()]) #false
                    self.endInterpolation.append(formInterp[curve.form()]) #true
                    curvesCount += 1

                elif curve.form() == om.MFnNurbsCurve.kPeriodic:
                    j = 0
                    for i in range(points.length()-curve.degree()):
                        pt = points[i] * matrix
                        pos = [pt.x*scale, pt.y*scale, pt.z*scale, 1]
                        curvPoints.append(pos)
                        primPoints.append(self.vertexCount)
                        self.topologyArray.append(j+vtx)
                        j+=1
                        self.vertexCount+=1
                    vtx+=j
                    posPoints += curvPoints
                    self.vertexArray.append([primPoints])
                    #knots
                    order = curve.degree()
                    self.orderArray.append(order)
                    mKnots = om.MDoubleArray()
                    curve.getKnots(mKnots)
                    knots = [float(mKnots[0])] +  list((x for x in mKnots )) + [float(mKnots[-1])]
                    self.knotsArray.append(knots)
                    self.openClose.append(formInterp[curve.form()]) #false
                    self.endInterpolation.append(not formInterp[curve.form()]) #true
                    curvesCount += 1
            iter.next()
        #add result
        iter.reset()
        return posPoints, curvesCount

    def getNodeType(self, iter):
        obj = om.MObject()
        iter.getDependNode(obj)
        dep = om.MFnDependencyNode(obj)
        return cmds.nodeType(dep.name())

    def parseGroups(self, iter, selection):
        if self.primCount():
            prefix = self.op['expcurveglobname']
            if prefix and self.op['expcurveglobEnable']:
                self.primGroupsArray[prefix] = [self.primCount(), True]
            # else:prefix = 'CURV'???
            #OBJECT NAME
            if self.op['curvgrp_obj'][0]:
                #get Names
                dagPath = om.MDagPath()
                names = []
                data = []
                while not iter.isDone():
                    iter.getDagPath( dagPath )
                    for child in self.shapeGenerator(dagPath, om.MFn.kNurbsCurve):
                        objName = om.MFnDependencyNode(dagPath.transform()).name()
                        names.append(objName)
                        data.append(1)
                    iter.next()
                objGroups = self.convertObjectNamesToGroupArray(data, names,prefix+self.op['curvgrp_obj'][2], self.op['curvgrp_obj'][1],self.textVariables['noCurveObj'])
                if objGroups:
                    self.primGroupsArray.update(objGroups)
            #parent group
            if self.op['curvgrp_par'][0]:
                iter.reset()
                names = []
                counts = []
                while not iter.isDone():
                    dagPath = om.MDagPath()
                    iter.getDagPath( dagPath )
                    isCurve = False
                    dagNode = om.MFnDagNode(dagPath)
                    for child in self.shapeGenerator(dagPath, om.MFn.kNurbsCurve):
                            isCurve = True
                    if isCurve:
                        counts.append(dagNode.childCount())
                        name = dagPath.fullPathName()
                        par = self.getParent(name, self.op['curvgrp_par'][1])
                        names.append(self.checkLegalChar(prefix+self.op['curvgrp_par'][2]+par))
                    iter.next()
                prntGroups = self.convertArrayDisplLayer(names, counts)
                if prntGroups:
                    self.primGroupsArray.update(prntGroups)
            #display layers
            if self.op['curvgrp_layer'][0]:
                titer = om.MItSelectionList ( selection, om.MFn.kTransform )
                names = []
                counts = []
                dagPath = om.MDagPath()
                mObj = om.MObject()
                while not titer.isDone():
                    titer.getDagPath( dagPath )
                    dagNode = om.MFnDagNode(dagPath)
                    if dagNode.childCount():
                        child = dagNode.child(0)
                        if child.apiType() == om.MFn.kNurbsCurve:
                            titer.getDependNode( mObj )
                            name = om.MDagPath.getAPathTo(mObj).fullPathName()
                            counts.append(1)
                            #read layer
                            layer = self.getDisplayLayer(name,self.op['curvgrp_layer'])
                            names.append(self.checkLegalChar(prefix+self.op['curvgrp_layer'][2]+layer))
                    titer.next()
                displLayerGroups = self.convertArrayDisplLayer(names, counts)
                if displLayerGroups:
                    self.primGroupsArray.update(displLayerGroups)

#################################################################################################
# PARTICLES
class particleReader(geoCollector):
    def __init__(self, op, parent=None):
        geoCollector.__init__(self)
        self.op = op
        self.par = parent
        self.name = 'Particles'

    def read(self, selection):
        iter = om.MItSelectionList(selection, om.MFn.kParticle)
        self.readPoints(iter)
        self.readAttributes(iter)
        self.parseGroups(iter)
        return True

    def readPoints(self, iter):
        points = []
        dagPath = om.MDagPath()
        vec = om.MVectorArray()
        scale = self.op['scale']
        if self.op['globalpos']:space = 'worldPosition'
        else:space = 'position'
        while not iter.isDone():
            iter.getDagPath( dagPath )
            part = omx.MFnParticleSystem(dagPath)
            part.getPerParticleAttribute(space, vec)
            for i in range(vec.length()):
                points.append([vec[i].x*scale, vec[i].y*scale, vec[i].z*scale,1])
            iter.next()
        if points:
            self.pointAttribArray['P'] = points
        self.pointsCount = len(points)
        iter.reset()

    def parseGroups(self, iter):
        prefix = self.op['expparticlglobname']
        if self.pointCount():
            if prefix and self.op['expparticlglobEnable']:
                self.pointGroupsArray[prefix] = [self.pointCount(), True]
            # else:???
            #     prefix = 'PART'
            #OBJECT NAME
            if self.op['exppartgrp_shape'][0]:
                #get Names
                dagPath = om.MDagPath()
                names = []
                data = []
                while not iter.isDone():
                    iter.getDagPath( dagPath )
                    objName = om.MFnDependencyNode(dagPath.transform()).name()
                    names.append(objName)
                    part = omx.MFnParticleSystem(dagPath)
                    data.append(part.count())
                    iter.next()
                #make data array by groups
                objGroups = self.convertObjectNamesToGroupArray(data, names,prefix+self.op['exppartgrp_shape'][2], self.op['exppartgrp_shape'][1],self.textVariables['noObject'])
                if objGroups:
                    self.pointGroupsArray.update(objGroups)
                iter.reset()

            if self.op['exppartgrp_emit'][0]:
                dagPath = om.MDagPath()
                emitArray = []
                emitGroups = {}
                names = []
                while not iter.isDone():
                    iter.getDagPath( dagPath )
                    objName = om.MFnDependencyNode(dagPath.transform()).name()
                    names.append(objName)
                    emitArray += cmds.listConnections( objName+'.newParticles', d=False, s=True )
                    iter.next()
                iter.reset()
                for em in emitArray:
                    tok = self.tokenPrefix(self.op['exppartgrp_emit'][1])
                    if tok:
                        for t in tok:
                            if t in em:
                                emitGroups[em] = []
                            else:
                                emitGroups['otherEmitters'] = []
                    else:
                        emitGroups[em] = []
                while not iter.isDone():
                    iter.getDagPath( dagPath )
                    objName = om.MFnDependencyNode(dagPath.transform()).name()
                    emitters = cmds.listConnections( objName+'.newParticles', d=False, s=True )
                    part = omx.MFnParticleSystem(dagPath)
                    count = part.count()
                    if count:
                        add = []
                        for em in emitArray:
                            if em in emitters:
                                add.append(em)
                        for key in emitGroups:
                            if key in add:
                                if emitGroups[key]:
                                    if emitGroups[key][-1] == False:
                                        emitGroups[key] += [count, True]
                                    else:
                                        emitGroups[key][-2] += count
                                else:
                                    emitGroups[key] += [count, True]
                            else:
                                if emitGroups[key]:
                                    if emitGroups[key][-1] == True:
                                        emitGroups[key] += [count, False]
                                    else:
                                        emitGroups[key][-2] += count
                                else:
                                    emitGroups[key] += [count, False]
                    iter.next()
                resultEmitgroup = {}
                for k in emitGroups:
                    if emitGroups[k]:
                        resultEmitgroup[prefix+self.op['exppartgrp_emit'][2]+k]=emitGroups[k]
                if resultEmitgroup:
                    self.pointGroupsArray.update(resultEmitgroup)

        iter.reset()

    def readAttributes(self, iter):
        '''
        http://download.novedge.com/Brands/Alias/Helps/Maya6.5/en_US/Dynamics/listofparticleattributes.html
        '''
        if self.op['exppartattrib'][0]:
            # attrs = self.tokenPrefix(self.op['exppartattrib'][1])
            # attrs = self.tokenAttributes(attrs)
            attrs = self.reorderAttrs(self.op['exppartattrib'][1])
            dagPath = om.MDagPath()
            offs = 0
            attrTypes = {}
            nodes = []
            while not iter.isDone():
                iter.getDagPath( dagPath )
                name = dagPath.fullPathName()
                nodes.append(name)
                iter.next()
            iter.reset()
            checked, ppAttrs = self.checkAttribtypes(nodes, attrs)
            #read attributes
            while not iter.isDone():
                iter.getDagPath( dagPath )
                part = omx.MFnParticleSystem(dagPath)
                for atr in checked:
                    # attrName =
                    renamed = self.checkLegalChar(checked[atr][2]) or self.checkLegalChar(atr)
                    default = checked[atr][0]
                    if atr in ppAttrs: #from particles
                        if part.isPerParticleIntAttribute(atr) or part.isPerParticleDoubleAttribute(atr):
                            var = om.MDoubleArray()
                            part.getPerParticleAttribute(atr, var)
                            value = []
                            for i in range(var.length()):
                                value.append(var[i])
                            if not renamed in self.defaultValues:
                                self.defaultValues[renamed] = 0
                        elif part.isPerParticleVectorAttribute (atr):
                            var = om.MVectorArray()
                            part.getPerParticleAttribute(atr, var)
                            value = []
                            for i in range(var.length()):
                                value.append([var[i].x,var[i].y,var[i].z])
                            if not renamed in self.defaultValues:
                                self.defaultValues[renamed] = default
                        else:
                            value = default
                            value = [value]*part.count()
                    else: #from node
                        name = dagPath.fullPathName()
                        v = self.getAttribFromNode(name, atr, checked[atr][1], default)
                        if v is None:
                            v = default
                        value = [v]*part.count()
                        if not renamed in self.defaultValues:
                            self.defaultValues[renamed] = default
                    #add value
                    if not atr in self.pointAttribArray:
                        offsArray = [default]*offs
                        self.pointAttribArray[renamed] = offsArray + value
                    else:
                        self.pointAttribArray[renamed] += value

                offs += part.count()
                iter.next()
        iter.reset()

    def tokenAttributes(self, attrs):
        dict = {}
        for a in attrs:
            if '(' in a:
                d = float(a.split('(')[1].replace(')',''))
                a = a.split('(')[0]
                dict[a] = d
            else:
                dict[a] = None
        return dict

#################################################################################################
# PIVOTS
class pivotReader(geoCollector):
    def __init__(self, op, parent=None):
        geoCollector.__init__(self)
        self.op = op
        self.par = parent
        self.name = 'Pivots'

    def read(self, selection):
        select = self.filterObjects(selection)
        if select:
            iter = om.MItSelectionList( select, om.MFn.kTransform )
            points = self.readPivotPoints(iter)
            if points:
                self.pointAttribArray['P'] = points
                self.pointsCount = len(points)
                if self.op['exppivorient']:
                    self.readOrient(iter)
                if self.op['exppivscale']:
                    self.readScale(iter)
                self.parseGroups(iter)
                self.readCustomAttrib(iter)
        return True

    def filterObjects(self, selection):
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

    def checkShape(self, array):
        result = []
        for a in array:
            if cmds.listRelatives(a, s=1):
                result.append(a)
        return result

    # def checkShape(self, array):
    #     result = []
    #     for a in array:
    #         if cmds.listRelatives(a, s=1):
    #             result.append(a)
    #     return result

    def readPivotPoints(self, iter):
        points = []
        while not iter.isDone():
            dagPath = om.MDagPath()
            iter.getDagPath( dagPath )
            mx =  dagPath.inclusiveMatrix()
            tmx = om.MTransformationMatrix(mx)
            points.append( self.getMatrixTranslate(tmx) +[1])
            iter.next()
        iter.reset()
        return points

    def readOrient(self, iter):
        self.pointAttribArray['orient'] = []
        while not iter.isDone():
            dagPath = om.MDagPath()
            iter.getDagPath( dagPath )
            mx =  dagPath.inclusiveMatrix()
            tmx = om.MTransformationMatrix(mx)
            self.pointAttribArray['orient'] .append(self.getMatrixRotate(tmx))
            iter.next()
        iter.reset()

    def readScale(self, iter):
        self.pointAttribArray['scale'] = []
        while not iter.isDone():
            dagPath = om.MDagPath()
            iter.getDagPath( dagPath )
            mx =  dagPath.inclusiveMatrix()
            tmx = om.MTransformationMatrix(mx)
            self.pointAttribArray['scale'] .append(self.getMatrixScale(tmx))
            iter.next()
        iter.reset()

    def parseGroups(self, iter):
        #Main group fot polugons
        prefix = self.op['exppivotglobname']
        if self.pointCount():
            if prefix and self.op['exppivotglobEnable']:
                self.pointGroupsArray[prefix] = [self.pointCount(), True]
            # else:???
            #     prefix = 'PIVOT'
            #OBJECT GROUP
            if self.op['exppivgrp_obj'][0]:
                dagPath = om.MDagPath()
                names = []
                data = []
                while not iter.isDone():
                    iter.getDagPath( dagPath )
                    objName = om.MFnDependencyNode(dagPath.transform()).name()
                    names.append(objName)
                    data.append(1)
                    iter.next()
                objGroups = self.convertObjectNamesToGroupArray(data, names,prefix + self.op['exppivgrp_obj'][2], self.op['exppivgrp_obj'][1],self.textVariables['noObject'])
                if objGroups:
                    self.pointGroupsArray.update(objGroups)
                iter.reset()
            #PARENT GROUP
            if self.op['exppivgrp_parent'][0]:
                prntGroups = {}         #parent groups
                iter.reset()
                names = []
                counts = []
                while not iter.isDone():
                    dagPath = om.MDagPath()
                    iter.getDagPath( dagPath )
                    name =dagPath.fullPathName()
                    par = self.getParent(name, self.op['exppivgrp_parent'][1])
                    names.append(self.checkLegalChar(prefix+self.op['exppivgrp_parent'][2]+par))
                    counts.append(1)
                    iter.next()
                prntGroups = self.convertArrayDisplLayer(names, counts)
                if prntGroups:
                    self.pointGroupsArray.update(prntGroups)
                iter.reset()
            #SHAPE GROUP
            if self.op['exppivgrp_shape'][0]:
                dagPath = om.MDagPath()
                names = []
                data = []
                while not iter.isDone():
                    iter.getDagPath( dagPath )
                    dagPath.extendToShape()
                    objName = om.MFnDependencyNode(dagPath.node()).name()
                    names.append(objName)
                    data.append(1)
                    iter.next()
                objGroups = self.convertObjectNamesToGroupArray(data, names,prefix+self.op['exppivgrp_shape'][2], self.op['exppivgrp_shape'][1],self.textVariables['otherInstances'])
                if objGroups:
                    self.pointGroupsArray.update(objGroups)
                iter.reset()
            #DISPLAY LAYER GROUP
        if self.op['exppivgrp_layer'][0]:
            names = []
            counts = []
            dagPath = om.MDagPath()
            mObj = om.MObject()
            while not iter.isDone():
                iter.getDagPath( dagPath )
                iter.getDependNode( mObj )
                counts.append(1)
                name = om.MDagPath.getAPathTo(mObj).fullPathName()
                layer = self.getDisplayLayer(name,self.op['exppivgrp_layer'])
                names.append(self.checkLegalChar(prefix+self.op['exppivgrp_layer'][2]+layer))
                iter.next()
            displLayerGroups = self.convertArrayDisplLayer(names, counts)
            if displLayerGroups:
                    self.pointGroupsArray.update(displLayerGroups)
            iter.reset()

    def readCustomAttrib(self, iter):
        # attribs = self.tokenPrefix(self.op['exppivattrib'][1])
        # attribs = self.tokenAttributes(attribs)
        attribs = self.reorderAttrs(self.op['exppivattrib'][1])
        dagPath = om.MDagPath()
        nodes = []
        while not iter.isDone():
            iter.getDagPath( dagPath )
            nd = cmds.nodeType(dagPath.fullPathName())
            if nd in self.spetialObjectsList:
                proc = self.spetialObjectsList[nd]
                objName = proc(dagPath.fullPathName())
            else:
                try:
                    dagPath.extendToShape()
                except:
                    pass
                    print 'No shape for', dagPath.fullPathName()
                objName = dagPath.fullPathName()
            nodes.append(objName)
            iter.next()
        iter.reset()
        checked, pp = self.checkAttribtypes(nodes, attribs)
        for i, node in enumerate(nodes):
            for attr in checked:
                renamed = self.checkLegalChar(checked[attr][2]) or self.checkLegalChar(attr)
                if not renamed in self.pointAttribArray:
                    self.pointAttribArray[renamed] = []
                default = checked[attr][0]
                value = self.getAttribFromNode(node, attr, checked[attr][1], default)
                if value is None:
                    value = default
                self.defaultValues[renamed] = default
                self.pointAttribArray[renamed] += ([value])


###################################

    def getMatrixTranslate(self, mx):
        scale = self.op['scale']
        space = om.MSpace.kWorld
        tr = mx.getTranslation(space)
        return [tr.x*scale, tr.y*scale, tr.z*scale]

    def getMatrixRotate(self, mx):
        rot = mx.rotation()
        return [rot.x,rot.y,rot.z,rot.w]

    def getMatrixScale(self, mx):
        scale = self.op['scale']
        util = om.MScriptUtil()
        util.createFromDouble(0.0, 0.0, 0.0)
        ptr = util.asDoublePtr()
        mx.getScale(ptr, om.MSpace.kObject)
        return [util.getDoubleArrayItem(ptr, 0)*scale, util.getDoubleArrayItem(ptr, 1)*scale, util.getDoubleArrayItem(ptr, 2)*scale]