'''menuData
act={name:mGeo exporter,action:show()}
'''
'''moduleInfo
Pipline exporter Maya to Houdini
'''
# mGeo Exporter v1.0
# By PaulWinex (paulwinex@gmail.com http://paulwinex.com/) 2013
# Much thanks for the help:
#   Somesanctus (somesanctus.blogspot.ru)
# This product is not licensed

# Using:
# 1. Copy folder pw_mGeo to the PYTHONPATH folder ( <mayaInstallFolder>\Python\Lib\site-packages )
# 2. In ScriptEditor execute code:
#import pw_mGeoExporter
#pw_mGeoExporter.show()
# import sys, os
# root = os.path.dirname(__file__)
# if not root in sys.path:
#     sys.path.append(root)
def show():
    from . import mGeo
    reload(mGeo)
    mGeo.show()
