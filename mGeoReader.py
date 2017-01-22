import time as Time
import json

from exporters import dataReader


reload(dataReader)
from widgets.imports import *
import templateMaker as template
reload(template)


class jsonDataReaderClass():
    def __init__(self, options, parent):
        self.parent = parent
        self.op = options

        self.poly = dataReader.polyReader(options, self)
        self.curve = dataReader.curveReader(options, self)
        self.pivots = dataReader.pivotReader(options, self)
        self.particles = dataReader.particleReader(options, self)

        self.pointAttributes = {}
        self.vertexAttributes = {}
        self.primAttributes = {}

        self.topologyArray = []
        self.primArrayCurve = []
        self.curveKnots = []
        self.curveOrders = []

        self.primArrayPoly = []
        self.vertexCount = 0

        self.primGroupsArray = {}
        self.pointGroupsArray = {}

        self.tmpDirName = 'mgeo_tmp'

    ### returnData
    def isCanceled(self):
        return self.parent.isCacneled()



    def readData(self):
        #1. read scene
            #1.1. read geometry
            #1.2. Read curves
            #1.3. read particles
            #1.4. read pivots
        #2. combine data
        ##############################
        #get Selection
        selection = om.MSelectionList()
        om.MGlobal.getActiveSelectionList( selection )

        if self.op['exportgeo']:
            #exprort geometry
            result = self.poly.read(selection)
            if not result:self.parent.msg2(1, 'Error read mesh')
        if self.isCanceled():
            return self.cancelExport()

        if self.op['expcurve']:
            #export curves
            result = self.curve.read(selection)
            if not result:self.parent.msg2(1, 'Error read Curves')
        if self.isCanceled():
            return self.cancelExport()

        if self.op['expparticle']:
            #export particles
            result = self.particles.read(selection)
            if not result:self.parent.msg2(1, 'Error read particles')
        if self.isCanceled():
            return self.cancelExport()

        if self.op['exppiv']:
            #export pivots
            result = self.pivots.read(selection)
            if not result:self.parent.msg2(1, 'Error read pivots')
        if self.isCanceled():
            return self.cancelExport()

        self.collectData()
        #build data
        if self.isCanceled():
            return self.cancelExport()
        path = self.writeJSON(self.buildData())
        return path

    def cancelExport(self):
        self.parent.caselExport()
        return ''


######### DUILD DATA ####################################################################
    def generatedefaultValue(self, val,k,default):
        if val:
            val = val[0]
        if k in default:
            v = default[k]
            return v
        else:
            v = 0
        if type(val) == type(1) or type(val) == type(1.0):
            return v
        elif isinstance(val, list):
            if len(val) == 4:
                return ([v]*3) + [1]
            else:
                return [v]*len(val)

    def collectData(self):
        #emptyGroup
        primGroupOffset = 0
        pointGroupOffset = 0

        self.vertexCount = 0
        vertexOffset = 0
        pointOffset = 0

        for typeData in self.poly, self.curve, self.particles, self.pivots:
            #points attrib
            for k in typeData.pointAttribArray.keys():
                if not k in self.pointAttributes:
                    if pointOffset:
                        # default = self.generatedefaultValue(typeData.pointAttribArray[k],k,typeData.defaultValues)
                        default = typeData.defaultValues[k]
                        self.pointAttributes[k] = [default] * pointOffset
                        self.pointAttributes[k] += typeData.pointAttribArray[k]
                    else:
                        self.pointAttributes[k] = typeData.pointAttribArray[k]
                else:
                    self.pointAttributes[k] += typeData.pointAttribArray[k]

            #vertexAttrib
            for k in typeData.vertxAttribArray.keys():
                if not k in self.vertexAttributes:
                    if vertexOffset:
                        default = self.generatedefaultValue(typeData.vertexAttributes[k][0],k,typeData.defaultValues)
                        self.vertexAttributes[k] = [default] * vertexOffset
                        self.vertexAttributes[k] += typeData.vertexAttributes[k]
                    else:
                        self.vertexAttributes[k] = typeData.vertxAttribArray[k]
                else:
                    self.vertexAttributes[k] += typeData.vertxAttribArray[k]

            #primAttrib
            for k in typeData.primAttribArray.keys():
                if not k in self.primAttributes:
                    self.primAttributes[k] = typeData.primAttribArray[k]
                else:
                    self.primAttributes[k] += typeData.primAttribArray[k]

            #topology
            for t in typeData.topology():
                self.topologyArray.append(t+vertexOffset)

            #veretx count
            self.vertexCount += typeData.getVertexCount()

            #groups prim
            for grp in typeData.primGroupsArray.keys():
                array = []
                if primGroupOffset:
                        array += [primGroupOffset, False]
                for i in range(0, len(typeData.primGroupsArray[grp]),2):
                    array += [typeData.primGroupsArray[grp][i], typeData.primGroupsArray[grp][i+1]]
                self.primGroupsArray[grp] = array

            #groups points
            for grp in typeData.pointGroupsArray.keys():
                array = []
                #optimize array
                for i in range(0, len(typeData.pointGroupsArray[grp]),2):
                    bol = typeData.pointGroupsArray[grp][i+1]
                    val = typeData.pointGroupsArray[grp][i]
                    if array:
                        if array[-1] == bol:
                            array[-2] += val
                        else:
                            array += [val, bol]
                    else:
                        array += [val, bol]

                if not grp in self.pointGroupsArray:
                    if pointGroupOffset:
                        if not array[1]:
                            array[0] = array[0] + pointGroupOffset
                        else:
                            array = [pointGroupOffset, False] + array
                    self.pointGroupsArray[grp] = array
                else:
                    self.pointGroupsArray[grp] += array

            pointGroupOffset += typeData.pointCount()
            primGroupOffset += typeData.primCount()
            pointOffset += typeData.pointCount()
            vertexOffset += typeData.offset()

            self.parent.msg2(2, typeData.name,'|', 'Prims:', typeData.primCount(),',', 'Points:', typeData.pointCount())

        #clear
        gc.collect()

        if self.pointGroupsArray:
            self.parent.msg2(2, 'Point groups:', ', '.join(sorted([x for x in self.pointGroupsArray.keys()])))
        if self.primGroupsArray:
            self.parent.msg2(2, 'Prim groups:', ', '.join(sorted([x for x in self.primGroupsArray.keys()])))
        if self.vertexAttributes:
            self.parent.msg2(2, 'Vertex attrib:', ', '.join(sorted([x for x in self.vertexAttributes.keys()])))
        if self.pointAttributes:
            self.parent.msg2(2, 'Point attrib:', ', '.join(sorted([x for x in self.pointAttributes.keys()])))
        if self.primAttributes:
            self.parent.msg2(2, 'Point attrib:', ', '.join(sorted([x for x in self.primAttributes.keys()])))

        ###########################################
        #prim connects
        #polygons
        self.primArrayPoly = self.poly.vertexArray

        #curves
        crvVertexOffset = self.poly.vertexCount
        for prim in self.curve.vertex():
                face = []
                for i in prim[0]:
                    face.append(i+crvVertexOffset)
                self.primArrayCurve.append([face])
        self.curveOrders = self.curve.orderArray
        self.curveKnots = self.curve.knotsArray

    def buildData(self, ):
        data = []
        #Header
        data += self.getDefaultHeader()
        #Topology
        data += ['topology',self.getTopology()]
        #Attributes
        data += ["attributes"] + self.getAttributes()
        #Primitives
        prim = self.getPrimitives()
        data += ["primitives"] + [prim]
        #poly groups
        data += ["primitivegroups"] + [self.getPolyGroups()]

        data += ["pointgroups"] + [self.getPointGroups()]
        return data

###### CONVERT DATA #################################################################
    def getDefaultHeader(self):
        """
        Build header
        """
        header = template.getHeader(self)
        return header

    def getBound(self):
        return [0,0,0,0,0,0]

    def getPointCount(self):
        if self.pointAttributes.get('P', False):
            return len(self.pointAttributes['P'])
        else:
            return 0
    def getVertexCount(self):
        return self.vertexCount

    def getPrimCount(self):
        return len(self.primArrayPoly) + len(self.primArrayCurve)

    def getAttribSummary(self):

        result = ''
        if self.pointAttributes:
            result += '   ' + str(len(self.pointAttributes)) + ' point attributes:\t' + ', '.join(self.pointAttributes.keys()) + '\n '
        if self.vertexAttributes:
            result += '   ' + str(len(self.vertexAttributes)) + ' vertex attributes:\t' + ', '.join(self.vertexAttributes.keys()) + '\n '
        if self.primAttributes:
            result += '   ' + str(len(self.primAttributes)) + ' primitive attributes:\t' + ', '.join(self.primAttributes.keys()) + '\n '
        return result

    def getTopology(self):

        return ['pointref',['indices',self.topologyArray]]

    def getAttributes(self):
        attr = []
        data = []
        points = []
        vertex = []
        prim = []
        if self.pointAttributes:
            for name in self.pointAttributes.keys():
                array = self.pointAttributes[name]
                data = template.array_to_point_attributes(name, array)
                if data:
                    points.append(data)
                else:
                    pass
                    # 'NO DATA FOR', name

        if self.vertexAttributes:
            for name in self.vertexAttributes.keys():
                array = self.vertexAttributes[name]
                data = template.array_to_vertex_attributes(name, array)
                if data:
                    vertex.append(data)
        if self.primAttributes:
            for name in self.primAttributes:
                data = template.array_to_prim_attributes(name, self.primAttributes[name])
                if data:
                    prim.append(data)

        attribArrays = []

        if vertex:
            attribArrays += ['vertexattributes', vertex]
        if points:
            attribArrays += ['pointattributes', points]
        if prim:
            attribArrays += ['primitiveattributes', prim]

        glob = self.createGlobalVariables()
        if glob:
            attribArrays += ['globalattributes', glob]

        if attribArrays:
            attr += [attribArrays]


        return attr

    def createGlobalVariables(self):
        skip = ['P', 'uv', 'Cd', 'N']
        attrs = []
        count = 0
        keys = self.pointAttributes.keys() + self.vertexAttributes.keys() + self.primAttributes.keys()
        keys = list(set(keys))
        for k in keys:
            if not k in skip:
                attrs += self.nameToGlobalName(k)
                count +=1
        if count:
            data = template.getGlobalVariables(count, attrs)
            return data
        return False

    def nameToGlobalName(self, name):
        return [name + ' -> ' + name.upper()]


    def getPrimitives(self):
        prim = []
        if self.primArrayPoly:
            prim.append([
                [
                    "type","run",
                    "runtype","Poly",
                    "varyingfields",["vertex"],
                    "uniformfields",{
                    "closed":True
                }
                ],self.primArrayPoly

            ])

        if self.primArrayCurve:
            if self.op['asnurmbs']:
                #to NURBS
                for i, arr in enumerate(self.primArrayCurve):
                    prim.append([
                        [
                            "type","NURBCurve"
                        ],
                        [
                            "vertex",arr[0],
                            "closed",self.curve.openClose[i],
                            "basis",[
                            "type","NURBS",
                            "order",self.curveOrders[i]+1,
                            "endinterpolation",self.curve.endInterpolation[i],
                            "knots",self.curveKnots[i]
                        ]
                        ]
                    ])
            else: #to POLYLINE
                for i, arr in enumerate(self.primArrayCurve):
                    prim.append([
                        [
                            "type","Poly"
                        ],
                        [
                            "vertex",arr[0],
                            "closed",self.curve.openClose[i]
                        ]
                    ])

        return prim

    def getPrimitives2(self):
        prim = []
        for pc in self.primArrayPoly:
            prim.append([pc[0],True])
        for po in self.primArrayCurve:
            prim.append([po[0],False])
        if prim:
            result = [
                [
                    "type","run",
                    "runtype","Poly",
                    "varyingfields",["vertex","closed"]
                ],
                prim
            ]
            return [result]

    ############################################ GROUPS
    def getPolyGroups(self):
        groups = []
        if self.primGroupsArray:
            for g in self.primGroupsArray.keys():
                groups.append(template.create_prim_group(g, self.primGroupsArray[g] ))
        return groups

    def getPointGroups(self):
        groups = []
        if self.pointGroupsArray:
            for g in self.pointGroupsArray.keys():
                groups.append(template.create_point_group(g, self.pointGroupsArray[g] ))
        return groups

###### WRITE ########################################################################
    def writeJSON(self, data, bin = False):
        # write main file
        indents = {True:None, False:4}
        start_time = Time.time()# TIMER START
        path = self.op['exportpath'].replace('.bgeo','.geo')
        path = self.toTmp(path)
        f = open(path, 'w')
        json.dump(data, f,separators=(',',':'), indent=indents[False])
        f.close()
        self.parent.msg2(2, 'Geo write', round((Time.time() - start_time), 3) , 'sec')

        if self.op['fileformat']: #to bgeo
            if not self.op['gconvert']:
                self.parent.msg2(1,'HFS not set')
            else:
                pathb = self.bgeoConvert(path, self.op['gconvert'], self.op['compress'])
                self.parent.msg2(2, 'bGeo convert', round((Time.time() - start_time), 3) , 'sec' )
                if isinstance(pathb, (str, unicode)):
                    path = self.fromTmp(pathb)
                    return path
                else:
                    self.parent.msg2(2, 'Error path' )
        #compress
        else:
            if self.op['compress'] == 1:
                path = self.compressGZ(path)
                self.parent.msg2(2, 'GZip compress', round((Time.time() - start_time), 3) , 'sec' )
            elif self.op['compress'] == 2:
                path = self.compressSC(path, self.op['gconvert'])
                self.parent.msg2(2, 'GZip compress', round((Time.time() - start_time), 3) , 'sec' )
        #to bgeo
        path = self.fromTmp(path)
        return path

    def compressGZ(self, path):
        import gzip
        pathgz = path + '.gz'
        f = open(path, 'rb')
        z = gzip.GzipFile(pathgz, 'wb')
        for line in f.xreadlines():
            z.write(line)
        f.close()
        z.close()
        self.deleteGeo(path)
        return pathgz

    def compressSC(self, path, convert):
        if not os.path.exists(convert):
            self.parent.msg2(2, 'Error Convertor %s' % convert )
            return
        pathsc = path + '.sc'
        process = self.launchWithoutConsole(convert, [path, pathsc])
        if process == 0:
            self.deleteGeo(path)
        else:
            self.parent.msg2(1,'Error write to bgeo. File saved to geo')
            return False
        return pathsc

    def bgeoConvert(self, geo, convert, compress=''):
        compext = {0: '', 1: '.gz', 2:'.sc'}
        bgeo = geo.replace('.geo','.bgeo') + compext[compress]
        process = self.launchWithoutConsole(convert, [geo, bgeo])
        if process == 0:
            self.deleteGeo(geo)
        else:
            self.parent.msg2(1,'Error write to bgeo. File saved to geo')
            return False
        return bgeo

    def launchWithoutConsole(self, command, args):
        # startupinfo = None
        # if os.name == 'nt':
        #     startupinfo = subprocess.STARTUPINFO()
        #     startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        # return subprocess.Popen([command] + args, startupinfo=startupinfo,
        #     stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=False).wait()
        args = [x.replace('\\','/') for x in args]
        p = QProcess()
        p.start(command, args)
        p.waitForFinished()
        return p.exitCode()


    def deleteGeo(self,path):
        try:
            os.remove(path)
        except IOError:
            self.parent.msg2(1,'Error delete file', path)

    def toTmp(self, path):
        f = os.path.basename(path)
        tmpDir = os.path.join(os.path.dirname(path), self.tmpDirName)
        try:
            if not os.path.exists(tmpDir):
                os.mkdir(tmpDir, 0777)
        except:
            self.parent.msg2(1,'Error create TEMP folder')
            return path
        result = os.path.join(tmpDir, f)
        return result

    def fromTmp(self, path):
        new = os.path.abspath(path.replace(self.tmpDirName,''))
        if os.path.exists(new):
            if self.op['fileExists'] == 1:
                os.remove(new)
            else:
                while os.path.exists(new):
                    new = self.parent.incrementName(new)
        os.rename(path, new)
        try:
            os.removedirs(os.path.dirname(path))
        except:
            pass
        return new
