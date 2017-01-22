import maya.OpenMaya as om
from imath import *
from alembic.Abc import *
from alembic.AbcGeom import *
import math
import alembic
from pymel.core import *


def get_mesh_data():
    selection = om.MSelectionList()
    om.MGlobal.getActiveSelectionList( selection )
    
    iter = om.MItSelectionList ( selection, om.MFn.kTransform )
    
    dagPath = om.MDagPath()
    iter.getDagPath( dagPath )
    dagNode = om.MFnDagNode(dagPath)
    child = dagNode.child(0)
    node = om.MFnDependencyNode(child)
    meshFn = om.MFnMesh(child)
    # points
    pointArray = om.MFloatPointArray()
    meshFn.getPoints(pointArray)
    points = []
    for i in range(pointArray.length()):
        pt = pointArray[i]
        points.append(V3f(pt.x, pt.y, pt.z))
    
    p_points = setArray(
        P3fTPTraits,
        *points
    )
    
    
    #poly
    iterPolys = om.MItMeshPolygon( child )
    topologyArray = []
    faceCount = []
    while not iterPolys.isDone():
        #vertex order
        verts = om.MIntArray()
        iterPolys.getVertices( verts )
    
        for v in reversed(list(verts)):
            topologyArray.append(v)
            
        verts = om.MIntArray()
        iterPolys.getVertices( verts )
        faceCount.append(verts.length())
        iterPolys.next()
        
    
    p_faceIndices = setArray(
        Int32TPTraits,
        *topologyArray
    ) 
    
    # fase count
    p_faceCounts = setArray( Int32TPTraits, *faceCount ) 
    # bounding box
    mx = dagNode.boundingBox().max()
    mn = dagNode.boundingBox().min()
    bb = Box3d( V3d(mn.x, mn.y, mn.z), V3d( mx.x, mx.y, mx.z) ) 

    # transform
    # rotate
    tmx = om.MTransformationMatrix(dagNode.transformationMatrix())
    t = tmx.translation(om.MSpace.kWorld)
    t = [t[x] for x in range(3)]
    #rotate
    
    q = tmx.rotation()
    v = om.MVector()
    angUtil = om.MScriptUtil()
    angUtil.createFromDouble(0)
    angDoub = angUtil.asDoublePtr()
    q.getAxisAngle(v, angDoub) 
    a = om.MScriptUtil.getDouble(angDoub)
    r = [[v[x] for x in range(3)],a]

    #scale
    scaleUtil = om.MScriptUtil()
    scaleUtil.createFromList([0,0,0],3)
    scaleVec = scaleUtil.asDoublePtr()
    tmx.getScale(scaleVec,om.MSpace.kWorld)
    s = [om.MScriptUtil.getDoubleArrayItem(scaleVec,i) for i in range(0,3)]

    return p_points, p_faceIndices, p_faceCounts, bb, [t, r, s]
    

def setArray( iTPTraits, *iList ):
    array = iTPTraits.arrayType( len( iList ) )
    for i in range( len( iList ) ):
        array[i] = iList[i]
    return array  


def saveSelected(filename):
    tvec = alembic.AbcCoreAbstract.TimeVector()
    tvec[:] = [1, 2, 3]
    timePerCycle = 3.0
    numSamplesPerCycle = len(tvec)
    tst = alembic.AbcCoreAbstract.TimeSamplingType(numSamplesPerCycle, timePerCycle)
    ts = alembic.AbcCoreAbstract.TimeSampling(tst, tvec)
       
    arch = alembic.Abc.OArchive(filename)
    tsidx = top.getArchive().addTimeSampling(ts)
    
    p_points, p_faceIndices, p_faceCounts, bb, tr = get_mesh_data()
    
    # create the top xform
    xform = OXform(arch.getTop(), 'cube1', tsidx)
    xsamp = XformSample()
    xsamp.setTranslation(V3d(*tr[0]))
    xsamp.setRotation(V3d(*tr[1][0]), math.degrees(tr[1][1]))
    xsamp.setScale(V3d(*tr[2]))
    xform.getSchema().set(xsamp)
    
    # the mesh shape
    meshObj = OPolyMesh(xform, 'cube1Shape', tsidx)
    mesh = meshObj.getSchema()
    
    mesh_samp = OPolyMeshSchemaSample(
        p_points, p_faceIndices, p_faceCounts
        )
    mesh_samp.setSelfBounds(bb)
    mesh.set(mesh_samp)
    
    arb = mesh.getArbGeomParams()
    # point attrib
    mass = ODoubleGeomParam(arb, "mass", False, GeometryScope.kVertexScope, 1) 
    array = Float64TPTraits.arrayType( len(p_points) )
    for i in range( len(p_points) ):
        array[i] = 1.23
    samp = ODoubleGeomParamSample()
    samp.setVals( array )
    mass.set(samp)

    #vertex Attribute
    area = ODoubleGeomParam(arb, "area", False, GeometryScope.kFacevaryingScope, 1) 
    array2 = Float64TPTraits.arrayType( len(p_faceIndices) )
    for i in range( len(p_faceIndices) ):
        array2[i] = 1.23
    samp2 = ODoubleGeomParamSample()
    samp2.setVals( array2 )
    area.set(samp2)


    #primitive Attribute
    count = ODoubleGeomParam(arb, "count", False, GeometryScope.kUniformScope, 1) 
    array3 = Float64TPTraits.arrayType( len(p_faceCounts) )
    for i in range( len(p_faceCounts) ):
        array3[i] = 0.5
    samp3 = ODoubleGeomParamSample()
    samp3.setVals( array3 )
    count.set(samp3)

    # point attrib vector
    color = OV3fGeomParam(arb, "Cd", False, GeometryScope.kVertexScope, 1)
    array = P3fTPTraits.arrayType( len(p_points) )
    for i in range( len(p_points) ):
        array[i] = V3f(1.0, 0.5, 1.0)
    samp = OV3fGeomParamSample()
    samp.setVals( array )
    color.set(samp)

    
    # face set1
    s1 = [x for x in range(len(p_faceCounts)) if x%2]
    arr = Int32TPTraits.arrayType(len(s1))
    for i in range( len(s1) ):
        arr[i] = s1[i]
    samp = OFaceSetSchemaSample() 
    samp.setFaces(arr)
    faceSet = mesh.createFaceSet('my_group_1')
    faceSetSchema = faceSet.getSchema()
    faceSetSchema.set(samp)
    
    # face set2
    s2 = [x for x in range(len(p_faceCounts)) if not x%2]    
    arr2 = Int32TPTraits.arrayType(len(s2))
    for i in range( len(s2) ):
        arr2[i] = s2[i]
    samp2 = OFaceSetSchemaSample() 
    samp2.setFaces(arr2)
    faceSet2 = mesh.createFaceSet('my_group_2')
    faceSetSchema2 = faceSet2.getSchema()
    faceSetSchema2.set(samp2)

# select poly object
saveSelected('c:/maya_geo.abc')


############################  ANIMATION

from pymel.core import *
import maya.OpenMaya as om
from imath import *
from alembic.Abc import *
from alembic.AbcGeom import *
import math
import alembic


def get_mesh_data():
    selection = om.MSelectionList()
    om.MGlobal.getActiveSelectionList( selection )

    iter = om.MItSelectionList ( selection, om.MFn.kTransform )

    dagPath = om.MDagPath()
    iter.getDagPath( dagPath )
    dagNode = om.MFnDagNode(dagPath)
    child = dagNode.child(0)
    node = om.MFnDependencyNode(child)
    meshFn = om.MFnMesh(child)
    # points
    pointArray = om.MFloatPointArray()
    meshFn.getPoints(pointArray)
    points = []
    for i in range(pointArray.length()):
        pt = pointArray[i]
        points.append(V3f(pt.x, pt.y, pt.z))

    p_points = setArray(
        P3fTPTraits,
        *points
    )


    #poly

    iterPolys = om.MItMeshPolygon( child )
    topologyArray = []
    faceCount = []
    UVArray = []
    NArray = []
    while not iterPolys.isDone():
        #vertex order
        verts = om.MIntArray()
        iterPolys.getVertices( verts )

        for v in reversed(list(verts)):
            topologyArray.append(v)

        verts = om.MIntArray()
        iterPolys.getVertices( verts )
        faceCount.append(verts.length())

        uArray= om.MFloatArray()
        vArray= om.MFloatArray()
        iterPolys.getUVs(uArray, vArray, 'map1')
        u = list(uArray)
        v = list(vArray)
        for i in reversed(range(len(u))):
            UVArray.append([u[i],v[i]])

        mx =  dagPath.inclusiveMatrix()
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


    p_faceIndices = setArray(
        Int32TPTraits,
        *topologyArray
    )

    # fase count
    p_faceCounts = setArray( Int32TPTraits, *faceCount )
    # bounding box
    mx = dagNode.boundingBox().max()
    mn = dagNode.boundingBox().min()
    bb = Box3d( V3d(mn.x, mn.y, mn.z), V3d( mx.x, mx.y, mx.z) )

    # transform
    # rotate
    tmx = om.MTransformationMatrix(dagNode.transformationMatrix())
    t = tmx.translation(om.MSpace.kWorld)
    t = [t[x] for x in range(3)]
    #rotate

    q = tmx.rotation()
    v = om.MVector()
    angUtil = om.MScriptUtil()
    angUtil.createFromDouble(0)
    angDoub = angUtil.asDoublePtr()
    q.getAxisAngle(v, angDoub)
    a = om.MScriptUtil.getDouble(angDoub)
    r = [[v[x] for x in range(3)],a]

    #scale
    scaleUtil = om.MScriptUtil()
    scaleUtil.createFromList([0,0,0],3)
    scaleVec = scaleUtil.asDoublePtr()
    tmx.getScale(scaleVec,om.MSpace.kWorld)
    s = [om.MScriptUtil.getDoubleArrayItem(scaleVec,i) for i in range(0,3)]

    UVArray = setArray( V2fTPTraits, *[V2f(x) for x in UVArray] )
    NArray = setArray( V3fTPTraits, *[V3f(x) for x in NArray] )
    return p_points, p_faceIndices, p_faceCounts, UVArray , NArray, bb, [t, r, s]

def setArray( iTPTraits, *iList ):
    array = iTPTraits.arrayType( len( iList ) )
    for i in range( len( iList ) ):
        array[i] = iList[i]
    return array

def nextfile():
    p = 'C:/abc'
    num = len(os.listdir(p))+1
    return p + '/mayafile%s.abc' % str(num).zfill(3)

def saveSelected(filename, start, end):
    writeAttribandgroups = True
    fps = 25
    tvec = alembic.AbcCoreAbstract.TimeVector()
    tvec[:] = [0]
    timePerCycle = 1.0 / fps
    numSamplesPerCycle = len(tvec)
    tSampTyp = alembic.AbcCoreAbstract.TimeSamplingType(numSamplesPerCycle, timePerCycle)
    tSamp = alembic.AbcCoreAbstract.TimeSampling(tSampTyp, tvec)


    arch= alembic.Abc.OArchive(filename)
    tsidx = arch.addTimeSampling(tSamp)



    # create the top xform
    xform = OXform(arch.getTop(), 'cube1', tsidx)
    xschema = xform.getSchema()
    # the mesh shape
    meshObj = OPolyMesh(xform, 'cube1Shape', tsidx)
    mesh = meshObj.getSchema()

    if writeAttribandgroups:
        arb = mesh.getArbGeomParams()

        # point attr
        mass = ODoubleGeomParam(arb, "mass", False, GeometryScope.kVertexScope, 1)
        # vertex attr
        area = ODoubleGeomParam(arb, "area", False, GeometryScope.kFacevaryingScope, 1)
        #primitive Attribute
        count = ODoubleGeomParam(arb, "count", False, GeometryScope.kUniformScope, 1)
        # point attrib vector
        color = OV3fGeomParam(arb, "Cd", False, GeometryScope.kVertexScope, 1)

        faceSet = mesh.createFaceSet('my_group_1')
        faceSetSchema = faceSet.getSchema()

        faceSet2 = mesh.createFaceSet('my_group_2')
        faceSetSchema2 = faceSet2.getSchema()

    for f in range(start, end+1):
        currentTime(f)
        p_points, p_faceIndices, p_faceCounts, uvs, normals, bb, tr = get_mesh_data()

        xsamp = XformSample()
        xsamp.setTranslation(V3d(*tr[0]))
        xsamp.setRotation(V3d(*tr[1][0]), math.degrees(tr[1][1]))
        xsamp.setScale(V3d(*tr[2]))
        xschema.set(xsamp)

        uvsamp = alembic.AbcGeom.OV2fGeomParamSample(uvs, GeometryScope.kFacevaryingScope)
        nsamp = alembic.AbcGeom.ON3fGeomParamSample(normals, GeometryScope.kFacevaryingScope)

        mesh_samp = OPolyMeshSchemaSample(p_points, p_faceIndices, p_faceCounts, uvsamp, nsamp)
        mesh_samp.setSelfBounds(bb)
        mesh.set(mesh_samp)


        # point attrib
        if writeAttribandgroups:
            array = Float64TPTraits.arrayType( len(p_points) )
            for i in range( len(p_points) ):
                array[i] = 1.23
            samp = ODoubleGeomParamSample()
            samp.setVals( array )
            mass.set(samp)

            #vertex Attribute

            array2 = Float64TPTraits.arrayType( len(p_faceIndices) )
            for i in range( len(p_faceIndices) ):
                array2[i] = 1.23
            samp2 = ODoubleGeomParamSample()
            samp2.setVals( array2 )
            area.set(samp2)


            #primitive Attribute
            array3 = Float64TPTraits.arrayType( len(p_faceCounts) )
            for i in range( len(p_faceCounts) ):
                array3[i] = 0.5
            samp3 = ODoubleGeomParamSample()
            samp3.setVals( array3 )
            count.set(samp3)

            # point attrib vector
            array = P3fTPTraits.arrayType( len(p_points) )
            for i in range( len(p_points) ):
                array[i] = V3f(1.0, 0.5, 1.0)
            samp = OV3fGeomParamSample()
            samp.setVals( array )
            color.set(samp)


            # face set1
            s1 = [x for x in range(len(p_faceCounts)) if x%2]
            arr = Int32TPTraits.arrayType(len(s1))
            for i in range( len(s1) ):
                arr[i] = s1[i]
            samp = OFaceSetSchemaSample()
            samp.setFaces(arr)

            faceSetSchema.set(samp)

            # face set2
            s2 = [x for x in range(len(p_faceCounts)) if not x%2]
            arr2 = Int32TPTraits.arrayType(len(s2))
            for i in range( len(s2) ):
                arr2[i] = s2[i]
            samp2 = OFaceSetSchemaSample()
            samp2.setFaces(arr2)

            faceSetSchema2.set(samp2)

# select poly object
saveSelected(nextfile(), 1, 20)

