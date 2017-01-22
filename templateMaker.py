def create_P_attr(array):
    p = [
        [
            "scope","public",
            "type","numeric",
            "name","P",
            "options",{
            "type":{
                "type":"string",
                "value":"hpoint"
            }
        }
        ],
        [
            "size",4,
            "storage","fpreal32",
            "defaults",[
            "size",4,
            "storage","fpreal64",
            "values",[0,0,0,1]
        ],
            "values",[
            "size",4,
            "storage","fpreal32",
            "tuples",array
        ]
        ]
    ]
    return p

def create_attr(name, default, array):
    l = len(array[0])
    d = []
    for i in range(l):
        d.append(default)
    if len(d) == 4:d[3] = 1

    p = [
        [
            "scope","public",
            "type","numeric",
            "name",name,
            "options",getOptions(name)
        ],
        [
            "size",l,
            "storage","fpreal32",
            "defaults",[
            "size",l,
            "storage","fpreal64",
            "values",d
        ],
            "values",[
            "size",l,
            "storage","fpreal32",
            "tuples",array
        ]
        ]
    ]
    return p

def create_vertex_attr(name, default,array):
    l = len(array[0])
    d = []
    for i in range(l):
        d.append(default)
    v = [
        [
            "scope","public",
            "type","numeric",
            "name",name,
            "options",getOptions(name)
        ],
        [
            "size",l,
            "storage","fpreal32",
            "defaults",[
            "size",l,
            "storage","fpreal64",
            "values",d
        ],
            "values",[
            "size",l,
            "storage","fpreal32",
            "tuples",array
        ]
        ]
    ]
    return v

#PRIMITIVES
def create_PRIM_data(array, closed):
    pr = [
        [
            "type","run",
            "runtype","Poly",
            "varyingfields",["vertex"],
            "uniformfields",{
            "closed":closed
        }
        ], array
    ]
    return pr

def create_prim_group(name, array):
    grp = [
        [
            "name",name,
            "type","primitive"
        ],
        [
            "selection",[
            "defaults",[
                "size",1,
                "storage","int64",
                "values",[0]
            ],
            "unordered",[
                "boolRLE",array
                        ]
            ]
        ]
    ]
    return grp

def create_point_group(name, array):
    pgrp = [
        [
            "name",name,
            "type","point"
        ],
        [
            "selection",[
            "defaults",[
                "size",1,
                "storage","int64",
                "values",[0]
            ],
            "unordered",[
                "boolRLE",array
            ]
        ]
        ]
    ]
    return pgrp

def array_to_point_attributes( name, array):
    # print name, array
    # print type(array[0])
    data = None
    if array:
        # if type(array[0]) == type([]):
        if isinstance(array[0], list):
            if len(array[0]) == 4: # vector 4
                data =  [[
                    "scope","public",
                    "type","numeric",
                    "name",name,
                    "options",{
                        "type":{
                            "type":"string",
                            "value":"hpoint"
                        }}],
                    [
                        "size",4,
                        "storage","fpreal32",
                        "defaults",[
                        "size",4,
                        "storage","fpreal64",
                        "values",[0,0,0,1]
                    ],
                        "values",[
                        "size",4,
                        "storage","fpreal32",
                        "tuples",array
                    ]]]
            elif  len(array[0]) == 3: # vector 3
                data = [
                    [
                        "scope","public",
                        "type","numeric",
                        "name",name,
                        "options",{
                        "type":{
                            "type":"string",
                            "value":"vector"
                        }
                    }
                    ],
                    [
                        "size",3,
                        "storage","fpreal32",
                        "defaults",[
                        "size",3,
                        "storage","fpreal64",
                        "values",[0,0,0]
                    ],
                        "values",[
                        "size",3,
                        "storage","fpreal32",
                        "tuples",array
                    ]
                    ]
                ]
        elif isinstance(array[0],int) or isinstance(array[0], float) : # float or int
            data =[
                [
                    "scope","public",
                    "type","numeric",
                    "name",name,
                    "options",{
                }
                ],
                [
                    "size",1,
                    "storage","fpreal32",
                    "defaults",[
                    "size",1,
                    "storage","fpreal64",
                    "values",[0]
                ],
                    "values",[
                    "size",1,
                    "storage","fpreal32",
                    "arrays",[array]
                ]
                ]
            ]
        elif isinstance(array[0], str):
            values = list(set(array))
            while '' in values:values.remove('')
            index = []
            for a in array:
                if a == '':index.append(-1)
                else:
                    index.append(values.index(a))
            # print array
            # print values
            # print index
            data = [
				[
					"scope","public",
					"type","string",
					"name",name,
					"options",{
					}
				],
				[
					"size",1,
					"storage","int32",
					"strings",values,
					"indices",[
						"size",1,
						"storage","int32",
						"arrays",[index
						]
					]
				]
			]

    return data
def array_to_vertex_attributes( name, array):
    # print '>>>', name
    data = None
    if array:
        if name == 'N':
            data = [
                [
                    "scope","public",
                    "type","numeric",
                    "name","N",
                    "options",{
                    "type":{
                        "type":"string",
                        "value":"normal"
                    }
                }
                ],
                [
                    "size",3,
                    "storage","fpreal32",
                    "defaults",[
                    "size",0,
                    "storage","fpreal64",
                    "values",[]
                ],
                    "values",[
                    "size",3,
                    "storage","fpreal32",
                    "tuples",array
                ]
                ]
            ]
        elif type(array[0]) == type([]):
            if len(array[0]) == 3: # vector 3
                data =  [
                    [
                        "scope","public",
                        "type","numeric",
                        "name",name,
                        "options",{
                        "type":{}
                    }
                    ],
                    [
                        "size",3,
                        "storage","fpreal32",
                        "defaults",[
                        "size",3,
                        "storage","fpreal64",
                        "values",[0,0,0]
                    ],
                        "values",[
                        "size",3,
                        "storage","fpreal32",
                        "tuples",array
                    ]
                    ]
                ]
        elif type(array[0]) == type(1)or type(array[0]) == type(0.0): # float or int
            data =[
                [
                    "scope","public",
                    "type","numeric",
                    "name",name,
                    "options",{
                }
                ],
                [
                    "size",1,
                    "storage","fpreal32",
                    "defaults",[
                    "size",1,
                    "storage","fpreal64",
                    "values",[0]
                ],
                    "values",[
                    "size",1,
                    "storage","fpreal32",
                    "arrays",[array]
                ]
                ]
            ]

    return data

def array_to_prim_attributes( name, array):
    # print '>>', type(array[0])
    data = None
    # if type(array[0]) == type(1):
    if isinstance(array[0], int):
        data = [
            [
                "scope","public",
                "type","numeric",
                "name",name,
                "options",{
                "type":{
                    "type":"string",
                    "value":"nonarithmetic_integer"
                }
            }
            ],
            [
                "size",1,
                "storage","int32",
                "defaults",[
                "size",1,
                "storage","fpreal64",
                "values",[0]
            ],
                "values",[
                "size",1,
                "storage","int32",
                "arrays",[array
                ]
            ]
            ]
        ]
    elif isinstance(array[0], float):
    # elif type(array[0]) == type(1.0):
        data = [
            [
                "scope","public",
                "type","numeric",
                "name",name,
                "options",{
            }
            ],
            [
                "size",1,
                "storage","fpreal32",
                "defaults",[
                "size",1,
                "storage","fpreal64",
                "values",[0]
            ],
                "values",[
                "size",1,
                "storage","fpreal32",
                "arrays",[array
                ]
            ]
            ]
        ]
    # elif type(array[0]) == type([]):
    elif isinstance(array[0], list):
        l = len(array[0])
        opt = {3:'"type":{"type":"string","value":"vector"}', 4:''}
        data = [
            [
                "scope","public",
                "type","numeric",
                "name",name,
                "options",{
            }
            ],
            [
                "size",l,
                "storage","fpreal32",
                "defaults",[
                "size",l,
                "storage","fpreal64",
                "values",[0]*l
            ],
                "values",[
                "size",l,
                "storage","fpreal32",
                "tuples",array
            ]
            ]
        ]

    elif isinstance(array[0], str):
    # elif type(array[0]) == type(''):
        string , index = stringArrayToDataAttrib(array)
        data = [
            [
                "scope","public",
                "type","string",
                "name",name,
                "options",{
            }
            ],
            [
                "size",1,
                "storage","int32",
                "strings",string,
                "indices",[
                "size",1,
                "storage","int32",
                "arrays",[index
                ]
            ]
            ]
        ]
    return data

def stringArrayToDataAttrib(array):
    string = list(set(array))
    index = []
    for a in array:
        index.append(string.index(a))
    return string, index

################################################################
def getOptions(name):
    opt = {
        'P':{"type":{"type":"string","value":"hpoint"}},
        'Cd':{"type":{"type":"string","value":"color"}},
        'N':{"type":{"type":"string","value":"normal"}},
        'uv':{}

    }
    print 'GET OPt'
    if name in opt:
        return opt[name]
    else:
        return {}

def getGlobalVariables(count, attrs):
    data = [
            [
                "scope","public",
                "type","string",
                "name","varmap",
                "options",{}
            ],
                [
                    "size",count,
                    "storage","int32",
                    "strings",attrs,
                    "indices",[
                    "size",count,
                    "storage","int32",
                    "tuples",[list(range(count))
                                ]
                        ]
                ]
            ]
    return [data]

def getHeader(parent):
    header =["fileversion", parent.parent.version,
             "pointcount", parent.getPointCount(),
             "vertexcount", parent.getVertexCount(),
             "primitivecount", parent.getPrimCount(),
             "info", {
                "artist": "",
                "date": "",
                "hostname": "",
                "software": "pw_mGeo",
                "bounds": parent.getBound(),
                "attribute_summary": parent.getAttribSummary()
            }]
    if parent.primArrayPoly or parent.primArrayCurve:
        count = parent.getPrimCount()
        header[9]['primcount_summary'] = "  " + str(count) + " polygons\n"
    return header