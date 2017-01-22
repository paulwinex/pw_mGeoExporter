'''menuData
act={name:mGeo exporter,action:show()}
'''
'''moduleInfo
Pipline exporter Maya to Houdini
'''
# mGeo Exporter v1.2
# By PaulWinex (paulwinex@gmail.com http://paulwinex.com/) 2013-2017
# Much thanks for the help:
#   Somesanctus (somesanctus.blogspot.ru)
# This product is not licensed

# Using:
# 1. Copy folder pw_mGeoExporter to the PYTHONPATH folder ( <mayaInstallFolder>\Python\Lib\site-packages )
# 2. In ScriptEditor execute code:
# import pw_mGeoExporter
# pw_mGeoExporter.show()
# import sys, os


def show():
    from . import mGeo
    reload(mGeo)
    mGeo.show()
