from pymel.core import *
from functools import partial
import maya.OpenMaya as om
import maya.OpenMayaFX as omx
import maya.utils as utils
from time import gmtime, strftime
import time, datetime, sys, os, subprocess, shutil, re, getpass
import maya.OpenMayaUI as omui
import maya.mel as mel
import gc
import platform
support = 1

qt = ''
try:
    from PyQt4.QtGui import *
    from PyQt4.QtCore import *
    qt = 'qt'
except ImportError:
    try:
        from PySide.QtGui import *
        from PySide.QtCore import *
        qt = 'side'
    except ImportError:
        try:
            from PySide2.QtGui import *
            from PySide2.QtCore import *
            from PySide2.QtWidgets import *
            qt = 'side2'
        except ImportError:
            cmds.error('PyQt or PySide not found!!!')
#Load modules
#get maya window
def getMayaWindow(qt):
    ptr = omui.MQtUtil.mainWindow()
    if ptr is not None:
        if qt: #PyQt
            return wrp(long(ptr), QObject)
        else: #PySide
            return wrp(long(ptr), QMainWindow)

if qt:
    if qt == 'qt':
        from sip import wrapinstance as wrp
        qMayaWindow = getMayaWindow(True)
        from PyQt4.QtCore import QSettings as qset
    elif qt == 'side':
        from shiboken import wrapInstance as wrp
        qMayaWindow = getMayaWindow(False)
        from  PySide.QtCore import QSettings as qset
    elif qt == 'side2':
        from  PySide2.QtCore import QSettings
        qMayaWindow = uitypes.toPySideWindow('MayaWindow')