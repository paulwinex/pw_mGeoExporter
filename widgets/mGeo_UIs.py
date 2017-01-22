# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Dropbox\Dropbox\pw_pipeline\pw_pipeline\assets\maya\python\Export\pw_mGeo\widgets\mGeo.ui'
#
# Created: Thu Nov 19 11:07:19 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_mgeoWindow(object):
    def setupUi(self, mgeoWindow):
        mgeoWindow.setObjectName("mgeoWindow")
        mgeoWindow.resize(697, 852)
        self.centralwidget = QtGui.QWidget(mgeoWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_22 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.gridLayout_8 = QtGui.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.optionsWidget_wd = QtGui.QWidget(self.centralwidget)
        self.optionsWidget_wd.setObjectName("optionsWidget_wd")
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.optionsWidget_wd)
        self.verticalLayout_10.setSpacing(3)
        self.verticalLayout_10.setContentsMargins(3, 3, 3, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox_2 = QtGui.QGroupBox(self.optionsWidget_wd)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_9 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_9.setSpacing(3)
        self.gridLayout_9.setContentsMargins(9, 3, 5, 3)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.line = QtGui.QFrame(self.groupBox_2)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_9.addWidget(self.line, 0, 2, 2, 1)
        self.fileFormat_cbb = QtGui.QComboBox(self.groupBox_2)
        self.fileFormat_cbb.setObjectName("fileFormat_cbb")
        self.fileFormat_cbb.addItem("")
        self.fileFormat_cbb.addItem("")
        self.gridLayout_9.addWidget(self.fileFormat_cbb, 0, 1, 1, 1)
        self.compress_cbb = QtGui.QComboBox(self.groupBox_2)
        self.compress_cbb.setObjectName("compress_cbb")
        self.compress_cbb.addItem("")
        self.compress_cbb.addItem("")
        self.compress_cbb.addItem("")
        self.gridLayout_9.addWidget(self.compress_cbb, 0, 4, 1, 1)
        self.cacheOnly_cbb = QtGui.QCheckBox(self.groupBox_2)
        self.cacheOnly_cbb.setText("")
        self.cacheOnly_cbb.setChecked(False)
        self.cacheOnly_cbb.setObjectName("cacheOnly_cbb")
        self.gridLayout_9.addWidget(self.cacheOnly_cbb, 1, 4, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_9.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBox_2)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_9.addWidget(self.label_6, 1, 0, 1, 1)
        self.widget_2 = QtGui.QWidget(self.groupBox_2)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.widget_2)
        self.horizontalLayout_8.setSpacing(6)
        self.horizontalLayout_8.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_20 = QtGui.QLabel(self.widget_2)
        self.label_20.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_8.addWidget(self.label_20)
        self.gridLayout_9.addWidget(self.widget_2, 1, 3, 1, 1)
        self.cacheFormat_cbb = QtGui.QComboBox(self.groupBox_2)
        self.cacheFormat_cbb.setObjectName("cacheFormat_cbb")
        self.cacheFormat_cbb.addItem("")
        self.cacheFormat_cbb.addItem("")
        self.cacheFormat_cbb.addItem("")
        self.gridLayout_9.addWidget(self.cacheFormat_cbb, 1, 1, 1, 1)
        self.label_16 = QtGui.QLabel(self.groupBox_2)
        self.label_16.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.gridLayout_9.addWidget(self.label_16, 0, 3, 1, 1)
        self.horizontalLayout_2.addWidget(self.groupBox_2)
        self.verticalLayout_10.addLayout(self.horizontalLayout_2)
        self.gridLayout_8.addWidget(self.optionsWidget_wd, 0, 0, 1, 1)
        self.outFile_gb = QtGui.QGroupBox(self.centralwidget)
        self.outFile_gb.setObjectName("outFile_gb")
        self.verticalLayout_12 = QtGui.QVBoxLayout(self.outFile_gb)
        self.verticalLayout_12.setSpacing(1)
        self.verticalLayout_12.setContentsMargins(3, 1, 3, 1)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(1)
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.exportPath_ly = QtGui.QHBoxLayout()
        self.exportPath_ly.setObjectName("exportPath_ly")
        self.horizontalLayout_5.addLayout(self.exportPath_ly)
        self.exportPath_le = QtGui.QLineEdit(self.outFile_gb)
        self.exportPath_le.setText("")
        self.exportPath_le.setObjectName("exportPath_le")
        self.horizontalLayout_5.addWidget(self.exportPath_le)
        self.applets_btn = QtGui.QPushButton(self.outFile_gb)
        self.applets_btn.setMaximumSize(QtCore.QSize(20, 16777215))
        self.applets_btn.setObjectName("applets_btn")
        self.horizontalLayout_5.addWidget(self.applets_btn)
        self.verticalLayout_12.addLayout(self.horizontalLayout_5)
        self.resolve_path_le = QtGui.QLabel(self.outFile_gb)
        self.resolve_path_le.setText("")
        self.resolve_path_le.setObjectName("resolve_path_le")
        self.verticalLayout_12.addWidget(self.resolve_path_le)
        self.line_8 = QtGui.QFrame(self.outFile_gb)
        self.line_8.setFrameShape(QtGui.QFrame.HLine)
        self.line_8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.verticalLayout_12.addWidget(self.line_8)
        self.horizontalLayout_19 = QtGui.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.fileAsk_rb = QtGui.QRadioButton(self.outFile_gb)
        self.fileAsk_rb.setChecked(True)
        self.fileAsk_rb.setObjectName("fileAsk_rb")
        self.horizontalLayout_19.addWidget(self.fileAsk_rb)
        self.fileOverride_rb = QtGui.QRadioButton(self.outFile_gb)
        self.fileOverride_rb.setChecked(False)
        self.fileOverride_rb.setObjectName("fileOverride_rb")
        self.horizontalLayout_19.addWidget(self.fileOverride_rb)
        self.fileSkip_rb = QtGui.QRadioButton(self.outFile_gb)
        self.fileSkip_rb.setObjectName("fileSkip_rb")
        self.horizontalLayout_19.addWidget(self.fileSkip_rb)
        self.fileRename_rb = QtGui.QRadioButton(self.outFile_gb)
        self.fileRename_rb.setObjectName("fileRename_rb")
        self.horizontalLayout_19.addWidget(self.fileRename_rb)
        self.horizontalLayout_19.setStretch(3, 1)
        self.verticalLayout_12.addLayout(self.horizontalLayout_19)
        self.gridLayout_8.addWidget(self.outFile_gb, 1, 0, 1, 2)
        self.frameRangeSettings_gb = QtGui.QGroupBox(self.centralwidget)
        self.frameRangeSettings_gb.setObjectName("frameRangeSettings_gb")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frameRangeSettings_gb)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setContentsMargins(5, 2, 2, 2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_3 = QtGui.QWidget(self.frameRangeSettings_gb)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_15 = QtGui.QHBoxLayout(self.widget_3)
        self.horizontalLayout_15.setSpacing(2)
        self.horizontalLayout_15.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.singleFrame_rb = QtGui.QRadioButton(self.widget_3)
        self.singleFrame_rb.setChecked(True)
        self.singleFrame_rb.setObjectName("singleFrame_rb")
        self.horizontalLayout_15.addWidget(self.singleFrame_rb)
        self.rangeFrame_rb = QtGui.QRadioButton(self.widget_3)
        self.rangeFrame_rb.setObjectName("rangeFrame_rb")
        self.horizontalLayout_15.addWidget(self.rangeFrame_rb)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem)
        self.verticalLayout_2.addWidget(self.widget_3)
        self.range_wd = QtGui.QWidget(self.frameRangeSettings_gb)
        self.range_wd.setEnabled(False)
        self.range_wd.setObjectName("range_wd")
        self.verticalLayout_21 = QtGui.QVBoxLayout(self.range_wd)
        self.verticalLayout_21.setSpacing(2)
        self.verticalLayout_21.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setContentsMargins(0, -1, 5, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.startFrame_spb = QtGui.QSpinBox(self.range_wd)
        self.startFrame_spb.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.startFrame_spb.setMinimum(-999999999)
        self.startFrame_spb.setMaximum(999999999)
        self.startFrame_spb.setObjectName("startFrame_spb")
        self.horizontalLayout.addWidget(self.startFrame_spb)
        self.endFrame_spb = QtGui.QSpinBox(self.range_wd)
        self.endFrame_spb.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.endFrame_spb.setMinimum(-999999999)
        self.endFrame_spb.setMaximum(999999999)
        self.endFrame_spb.setObjectName("endFrame_spb")
        self.horizontalLayout.addWidget(self.endFrame_spb)
        self.stepFrame_spb = QtGui.QDoubleSpinBox(self.range_wd)
        self.stepFrame_spb.setMaximumSize(QtCore.QSize(40, 16777215))
        self.stepFrame_spb.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.stepFrame_spb.setMinimum(-999999999.0)
        self.stepFrame_spb.setMaximum(999999999.0)
        self.stepFrame_spb.setObjectName("stepFrame_spb")
        self.horizontalLayout.addWidget(self.stepFrame_spb)
        self.setrange_btn = QtGui.QPushButton(self.range_wd)
        self.setrange_btn.setMinimumSize(QtCore.QSize(60, 0))
        self.setrange_btn.setMaximumSize(QtCore.QSize(60, 16777215))
        self.setrange_btn.setObjectName("setrange_btn")
        self.horizontalLayout.addWidget(self.setrange_btn)
        self.verticalLayout_21.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addWidget(self.range_wd)
        self.gridLayout_8.addWidget(self.frameRangeSettings_gb, 0, 1, 1, 1)
        self.gridLayout_8.setColumnStretch(0, 1)
        self.gridLayout_8.setColumnStretch(1, 1)
        self.verticalLayout_22.addLayout(self.gridLayout_8)
        self.textWidget_sp = QtGui.QSplitter(self.centralwidget)
        self.textWidget_sp.setOrientation(QtCore.Qt.Vertical)
        self.textWidget_sp.setObjectName("textWidget_sp")
        self.splitter = QtGui.QSplitter(self.textWidget_sp)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.groupBox_5 = QtGui.QGroupBox(self.splitter)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_23 = QtGui.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_23.setSpacing(2)
        self.verticalLayout_23.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.horizontalLayout_18 = QtGui.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.createSet_btn = QtGui.QPushButton(self.groupBox_5)
        self.createSet_btn.setMinimumSize(QtCore.QSize(30, 30))
        self.createSet_btn.setMaximumSize(QtCore.QSize(30, 30))
        self.createSet_btn.setFlat(True)
        self.createSet_btn.setObjectName("createSet_btn")
        self.horizontalLayout_18.addWidget(self.createSet_btn)
        self.deleteSet_btn = QtGui.QPushButton(self.groupBox_5)
        self.deleteSet_btn.setMinimumSize(QtCore.QSize(30, 30))
        self.deleteSet_btn.setMaximumSize(QtCore.QSize(30, 30))
        self.deleteSet_btn.setFlat(True)
        self.deleteSet_btn.setObjectName("deleteSet_btn")
        self.horizontalLayout_18.addWidget(self.deleteSet_btn)
        self.reloadSets_btn = QtGui.QPushButton(self.groupBox_5)
        self.reloadSets_btn.setMinimumSize(QtCore.QSize(30, 30))
        self.reloadSets_btn.setMaximumSize(QtCore.QSize(30, 30))
        self.reloadSets_btn.setFlat(True)
        self.reloadSets_btn.setObjectName("reloadSets_btn")
        self.horizontalLayout_18.addWidget(self.reloadSets_btn)
        self.line_3 = QtGui.QFrame(self.groupBox_5)
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_18.addWidget(self.line_3)
        self.addToSet_btn = QtGui.QPushButton(self.groupBox_5)
        self.addToSet_btn.setMinimumSize(QtCore.QSize(30, 30))
        self.addToSet_btn.setMaximumSize(QtCore.QSize(30, 30))
        self.addToSet_btn.setFlat(True)
        self.addToSet_btn.setObjectName("addToSet_btn")
        self.horizontalLayout_18.addWidget(self.addToSet_btn)
        self.removeFromSet_btn = QtGui.QPushButton(self.groupBox_5)
        self.removeFromSet_btn.setMinimumSize(QtCore.QSize(30, 30))
        self.removeFromSet_btn.setMaximumSize(QtCore.QSize(30, 30))
        self.removeFromSet_btn.setFlat(True)
        self.removeFromSet_btn.setObjectName("removeFromSet_btn")
        self.horizontalLayout_18.addWidget(self.removeFromSet_btn)
        self.replaceSet_btn = QtGui.QPushButton(self.groupBox_5)
        self.replaceSet_btn.setMinimumSize(QtCore.QSize(30, 30))
        self.replaceSet_btn.setMaximumSize(QtCore.QSize(30, 30))
        self.replaceSet_btn.setFlat(True)
        self.replaceSet_btn.setObjectName("replaceSet_btn")
        self.horizontalLayout_18.addWidget(self.replaceSet_btn)
        self.clearSet_btn = QtGui.QPushButton(self.groupBox_5)
        self.clearSet_btn.setMinimumSize(QtCore.QSize(30, 30))
        self.clearSet_btn.setMaximumSize(QtCore.QSize(30, 30))
        self.clearSet_btn.setFlat(True)
        self.clearSet_btn.setObjectName("clearSet_btn")
        self.horizontalLayout_18.addWidget(self.clearSet_btn)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem1)
        self.verticalLayout_23.addLayout(self.horizontalLayout_18)
        self.scrollArea_5 = QtGui.QScrollArea(self.groupBox_5)
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollArea_5.setObjectName("scrollArea_5")
        self.scrollAreaWidgetContents_5 = QtGui.QWidget()
        self.scrollAreaWidgetContents_5.setGeometry(QtCore.QRect(0, 0, 292, 333))
        self.scrollAreaWidgetContents_5.setObjectName("scrollAreaWidgetContents_5")
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents_5)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.sets_ly = QtGui.QVBoxLayout()
        self.sets_ly.setSpacing(0)
        self.sets_ly.setObjectName("sets_ly")
        self.verticalLayout_8.addLayout(self.sets_ly)
        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_5)
        self.verticalLayout_23.addWidget(self.scrollArea_5)
        self.geoExport_btn = QtGui.QPushButton(self.groupBox_5)
        self.geoExport_btn.setMinimumSize(QtCore.QSize(100, 0))
        self.geoExport_btn.setObjectName("geoExport_btn")
        self.verticalLayout_23.addWidget(self.geoExport_btn)
        self.expoptions_gb = QtGui.QGroupBox(self.splitter)
        self.expoptions_gb.setObjectName("expoptions_gb")
        self.verticalLayout = QtGui.QVBoxLayout(self.expoptions_gb)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_10 = QtGui.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label = QtGui.QLabel(self.expoptions_gb)
        self.label.setObjectName("label")
        self.horizontalLayout_12.addWidget(self.label)
        self.widget_4 = QtGui.QWidget(self.expoptions_gb)
        self.widget_4.setMinimumSize(QtCore.QSize(50, 0))
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.widget_4)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.worldPos_rb = QtGui.QRadioButton(self.widget_4)
        self.worldPos_rb.setChecked(True)
        self.worldPos_rb.setObjectName("worldPos_rb")
        self.horizontalLayout_4.addWidget(self.worldPos_rb)
        self.localPos_rb = QtGui.QRadioButton(self.widget_4)
        self.localPos_rb.setObjectName("localPos_rb")
        self.horizontalLayout_4.addWidget(self.localPos_rb)
        self.horizontalLayout_12.addWidget(self.widget_4)
        self.gridLayout_10.addLayout(self.horizontalLayout_12, 0, 0, 1, 1)
        self.expVis_cb = QtGui.QCheckBox(self.expoptions_gb)
        self.expVis_cb.setObjectName("expVis_cb")
        self.gridLayout_10.addWidget(self.expVis_cb, 0, 2, 1, 1)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_8 = QtGui.QLabel(self.expoptions_gb)
        self.label_8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_9.addWidget(self.label_8)
        self.scale_le = QtGui.QLineEdit(self.expoptions_gb)
        self.scale_le.setMaximumSize(QtCore.QSize(50, 16777215))
        self.scale_le.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.scale_le.setObjectName("scale_le")
        self.horizontalLayout_9.addWidget(self.scale_le)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem2)
        self.gridLayout_10.addLayout(self.horizontalLayout_9, 1, 0, 1, 1)
        self.line_2 = QtGui.QFrame(self.expoptions_gb)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_10.addWidget(self.line_2, 0, 1, 2, 1)
        self.expHierarchy_cb = QtGui.QCheckBox(self.expoptions_gb)
        self.expHierarchy_cb.setChecked(True)
        self.expHierarchy_cb.setObjectName("expHierarchy_cb")
        self.gridLayout_10.addWidget(self.expHierarchy_cb, 1, 2, 1, 1)
        self.gridLayout_10.setColumnStretch(2, 1)
        self.verticalLayout.addLayout(self.gridLayout_10)
        self.line_12 = QtGui.QFrame(self.expoptions_gb)
        self.line_12.setFrameShape(QtGui.QFrame.HLine)
        self.line_12.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.verticalLayout.addWidget(self.line_12)
        self.mainTab = QtGui.QTabWidget(self.expoptions_gb)
        self.mainTab.setObjectName("mainTab")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_14 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.polyScroll_sa = QtGui.QScrollArea(self.tab)
        self.polyScroll_sa.setWidgetResizable(True)
        self.polyScroll_sa.setObjectName("polyScroll_sa")
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 360, 306))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.polyGroupEnable_cb = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.polyGroupEnable_cb.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.polyGroupEnable_cb.setChecked(True)
        self.polyGroupEnable_cb.setObjectName("polyGroupEnable_cb")
        self.verticalLayout_5.addWidget(self.polyGroupEnable_cb)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.expGeoGlobalGroupName_le = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.expGeoGlobalGroupName_le.setObjectName("expGeoGlobalGroupName_le")
        self.horizontalLayout_7.addWidget(self.expGeoGlobalGroupName_le)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.pointAttrib_gb = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.pointAttrib_gb.setObjectName("pointAttrib_gb")
        self.verticalLayout_13 = QtGui.QVBoxLayout(self.pointAttrib_gb)
        self.verticalLayout_13.setSpacing(2)
        self.verticalLayout_13.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.exportUv_cb = QtGui.QCheckBox(self.pointAttrib_gb)
        self.exportUv_cb.setChecked(False)
        self.exportUv_cb.setObjectName("exportUv_cb")
        self.horizontalLayout_13.addWidget(self.exportUv_cb)
        self.exportVertexColor_cb = QtGui.QCheckBox(self.pointAttrib_gb)
        self.exportVertexColor_cb.setObjectName("exportVertexColor_cb")
        self.horizontalLayout_13.addWidget(self.exportVertexColor_cb)
        self.exportVerNorm_cb = QtGui.QCheckBox(self.pointAttrib_gb)
        self.exportVerNorm_cb.setChecked(False)
        self.exportVerNorm_cb.setObjectName("exportVerNorm_cb")
        self.horizontalLayout_13.addWidget(self.exportVerNorm_cb)
        self.exportCrease_cb = QtGui.QCheckBox(self.pointAttrib_gb)
        self.exportCrease_cb.setObjectName("exportCrease_cb")
        self.horizontalLayout_13.addWidget(self.exportCrease_cb)
        self.horizontalLayout_13.setStretch(3, 1)
        self.verticalLayout_13.addLayout(self.horizontalLayout_13)
        self.verticalLayout_5.addWidget(self.pointAttrib_gb)
        self.groupBox_8 = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_8.setObjectName("groupBox_8")
        self.verticalLayout_15 = QtGui.QVBoxLayout(self.groupBox_8)
        self.verticalLayout_15.setSpacing(2)
        self.verticalLayout_15.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.customGeoAttr_cb = QtGui.QCheckBox(self.groupBox_8)
        self.customGeoAttr_cb.setChecked(True)
        self.customGeoAttr_cb.setObjectName("customGeoAttr_cb")
        self.horizontalLayout_14.addWidget(self.customGeoAttr_cb)
        self.customGeoAttr_le = QtGui.QLineEdit(self.groupBox_8)
        self.customGeoAttr_le.setObjectName("customGeoAttr_le")
        self.horizontalLayout_14.addWidget(self.customGeoAttr_le)
        self.verticalLayout_15.addLayout(self.horizontalLayout_14)
        self.attrTable_poly_ly = QtGui.QVBoxLayout()
        self.attrTable_poly_ly.setObjectName("attrTable_poly_ly")
        self.verticalLayout_15.addLayout(self.attrTable_poly_ly)
        self.verticalLayout_5.addWidget(self.groupBox_8)
        self.primGroups_gb = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.primGroups_gb.setObjectName("primGroups_gb")
        self.gridLayout = QtGui.QGridLayout(self.primGroups_gb)
        self.gridLayout.setContentsMargins(2, 2, 2, 2)
        self.gridLayout.setHorizontalSpacing(4)
        self.gridLayout.setVerticalSpacing(2)
        self.gridLayout.setObjectName("gridLayout")
        self.byMtl_cb = QtGui.QCheckBox(self.primGroups_gb)
        self.byMtl_cb.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.byMtl_cb.setObjectName("byMtl_cb")
        self.gridLayout.addWidget(self.byMtl_cb, 2, 0, 1, 1)
        self.byMtl_le = QtGui.QLineEdit(self.primGroups_gb)
        self.byMtl_le.setText("")
        self.byMtl_le.setObjectName("byMtl_le")
        self.gridLayout.addWidget(self.byMtl_le, 2, 2, 1, 1)
        self.byPar_cb = QtGui.QCheckBox(self.primGroups_gb)
        self.byPar_cb.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.byPar_cb.setObjectName("byPar_cb")
        self.gridLayout.addWidget(self.byPar_cb, 6, 0, 1, 1)
        self.byPar_le = QtGui.QLineEdit(self.primGroups_gb)
        self.byPar_le.setText("")
        self.byPar_le.setObjectName("byPar_le")
        self.gridLayout.addWidget(self.byPar_le, 6, 2, 1, 1)
        self.displayer_cb = QtGui.QCheckBox(self.primGroups_gb)
        self.displayer_cb.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.displayer_cb.setObjectName("displayer_cb")
        self.gridLayout.addWidget(self.displayer_cb, 11, 0, 1, 1)
        self.byLayer_le = QtGui.QLineEdit(self.primGroups_gb)
        self.byLayer_le.setText("")
        self.byLayer_le.setObjectName("byLayer_le")
        self.gridLayout.addWidget(self.byLayer_le, 11, 2, 1, 1)
        self.label_3 = QtGui.QLabel(self.primGroups_gb)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.primGroups_gb)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 2, 1, 1)
        self.line_4 = QtGui.QFrame(self.primGroups_gb)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout.addWidget(self.line_4, 1, 0, 1, 4)
        self.byMtlPref_le = QtGui.QLineEdit(self.primGroups_gb)
        self.byMtlPref_le.setObjectName("byMtlPref_le")
        self.gridLayout.addWidget(self.byMtlPref_le, 2, 1, 1, 1)
        self.byParPref_le = QtGui.QLineEdit(self.primGroups_gb)
        self.byParPref_le.setObjectName("byParPref_le")
        self.gridLayout.addWidget(self.byParPref_le, 6, 1, 1, 1)
        self.byLayerPref_le = QtGui.QLineEdit(self.primGroups_gb)
        self.byLayerPref_le.setObjectName("byLayerPref_le")
        self.gridLayout.addWidget(self.byLayerPref_le, 11, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.primGroups_gb)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 1, 1, 1)
        self.byObj_cb = QtGui.QCheckBox(self.primGroups_gb)
        self.byObj_cb.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.byObj_cb.setObjectName("byObj_cb")
        self.gridLayout.addWidget(self.byObj_cb, 4, 0, 1, 1)
        self.byObjPref_le = QtGui.QLineEdit(self.primGroups_gb)
        self.byObjPref_le.setObjectName("byObjPref_le")
        self.gridLayout.addWidget(self.byObjPref_le, 4, 1, 1, 1)
        self.byObj_le = QtGui.QLineEdit(self.primGroups_gb)
        self.byObj_le.setText("")
        self.byObj_le.setObjectName("byObj_le")
        self.gridLayout.addWidget(self.byObj_le, 4, 2, 1, 1)
        self.byShape_cb = QtGui.QCheckBox(self.primGroups_gb)
        self.byShape_cb.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.byShape_cb.setObjectName("byShape_cb")
        self.gridLayout.addWidget(self.byShape_cb, 5, 0, 1, 1)
        self.bySpahePref_le = QtGui.QLineEdit(self.primGroups_gb)
        self.bySpahePref_le.setObjectName("bySpahePref_le")
        self.gridLayout.addWidget(self.bySpahePref_le, 5, 1, 1, 1)
        self.byShape_le = QtGui.QLineEdit(self.primGroups_gb)
        self.byShape_le.setText("")
        self.byShape_le.setObjectName("byShape_le")
        self.gridLayout.addWidget(self.byShape_le, 5, 2, 1, 1)
        self.verticalLayout_5.addWidget(self.primGroups_gb)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem3)
        self.polyScroll_sa.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_14.addWidget(self.polyScroll_sa)
        self.mainTab.addTab(self.tab, "")
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_11 = QtGui.QVBoxLayout(self.tab_4)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.curvScroll_sa = QtGui.QScrollArea(self.tab_4)
        self.curvScroll_sa.setWidgetResizable(True)
        self.curvScroll_sa.setObjectName("curvScroll_sa")
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 200, 214))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_16 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_16.setSpacing(2)
        self.verticalLayout_16.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.curveGroupEnable_cb = QtGui.QCheckBox(self.scrollAreaWidgetContents_2)
        self.curveGroupEnable_cb.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.curveGroupEnable_cb.setChecked(True)
        self.curveGroupEnable_cb.setObjectName("curveGroupEnable_cb")
        self.verticalLayout_16.addWidget(self.curveGroupEnable_cb)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_15 = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_10.addWidget(self.label_15)
        self.expCurvesGlobalGroupName_le = QtGui.QLineEdit(self.scrollAreaWidgetContents_2)
        self.expCurvesGlobalGroupName_le.setObjectName("expCurvesGlobalGroupName_le")
        self.horizontalLayout_10.addWidget(self.expCurvesGlobalGroupName_le)
        self.verticalLayout_16.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_16 = QtGui.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.curvToNURBS_rb = QtGui.QRadioButton(self.scrollAreaWidgetContents_2)
        self.curvToNURBS_rb.setChecked(True)
        self.curvToNURBS_rb.setObjectName("curvToNURBS_rb")
        self.horizontalLayout_16.addWidget(self.curvToNURBS_rb)
        self.curvToPoly_rb = QtGui.QRadioButton(self.scrollAreaWidgetContents_2)
        self.curvToPoly_rb.setObjectName("curvToPoly_rb")
        self.horizontalLayout_16.addWidget(self.curvToPoly_rb)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem4)
        self.verticalLayout_16.addLayout(self.horizontalLayout_16)
        self.groupBox = QtGui.QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox.setObjectName("groupBox")
        self.attrTable_curve_ly = QtGui.QVBoxLayout(self.groupBox)
        self.attrTable_curve_ly.setSpacing(2)
        self.attrTable_curve_ly.setContentsMargins(2, 2, 2, 2)
        self.attrTable_curve_ly.setObjectName("attrTable_curve_ly")
        self.customCrvAttr_cbx = QtGui.QCheckBox(self.groupBox)
        self.customCrvAttr_cbx.setObjectName("customCrvAttr_cbx")
        self.attrTable_curve_ly.addWidget(self.customCrvAttr_cbx)
        self.verticalLayout_16.addWidget(self.groupBox)
        self.groupBox_6 = QtGui.QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox_6)
        self.gridLayout_4.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_4.setSpacing(2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.byCurvObj_le = QtGui.QLineEdit(self.groupBox_6)
        self.byCurvObj_le.setText("")
        self.byCurvObj_le.setObjectName("byCurvObj_le")
        self.gridLayout_4.addWidget(self.byCurvObj_le, 2, 2, 1, 1)
        self.byCrvObj_cb = QtGui.QCheckBox(self.groupBox_6)
        self.byCrvObj_cb.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.byCrvObj_cb.setObjectName("byCrvObj_cb")
        self.gridLayout_4.addWidget(self.byCrvObj_cb, 2, 0, 1, 1)
        self.label_9 = QtGui.QLabel(self.groupBox_6)
        self.label_9.setObjectName("label_9")
        self.gridLayout_4.addWidget(self.label_9, 0, 0, 1, 1)
        self.label_10 = QtGui.QLabel(self.groupBox_6)
        self.label_10.setObjectName("label_10")
        self.gridLayout_4.addWidget(self.label_10, 0, 2, 1, 1)
        self.line_5 = QtGui.QFrame(self.groupBox_6)
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout_4.addWidget(self.line_5, 1, 0, 1, 4)
        self.byCrvPar_cb = QtGui.QCheckBox(self.groupBox_6)
        self.byCrvPar_cb.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.byCrvPar_cb.setObjectName("byCrvPar_cb")
        self.gridLayout_4.addWidget(self.byCrvPar_cb, 3, 0, 1, 1)
        self.byCurvPar_le = QtGui.QLineEdit(self.groupBox_6)
        self.byCurvPar_le.setText("")
        self.byCurvPar_le.setObjectName("byCurvPar_le")
        self.gridLayout_4.addWidget(self.byCurvPar_le, 3, 2, 1, 1)
        self.curvDisplayer_cb = QtGui.QCheckBox(self.groupBox_6)
        self.curvDisplayer_cb.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.curvDisplayer_cb.setObjectName("curvDisplayer_cb")
        self.gridLayout_4.addWidget(self.curvDisplayer_cb, 4, 0, 1, 1)
        self.byCurvLayer_le = QtGui.QLineEdit(self.groupBox_6)
        self.byCurvLayer_le.setText("")
        self.byCurvLayer_le.setObjectName("byCurvLayer_le")
        self.gridLayout_4.addWidget(self.byCurvLayer_le, 4, 2, 1, 1)
        self.byCurvObjPref_le = QtGui.QLineEdit(self.groupBox_6)
        self.byCurvObjPref_le.setObjectName("byCurvObjPref_le")
        self.gridLayout_4.addWidget(self.byCurvObjPref_le, 2, 1, 1, 1)
        self.byCurvParPref_le = QtGui.QLineEdit(self.groupBox_6)
        self.byCurvParPref_le.setObjectName("byCurvParPref_le")
        self.gridLayout_4.addWidget(self.byCurvParPref_le, 3, 1, 1, 1)
        self.byCurvLayerPref_le = QtGui.QLineEdit(self.groupBox_6)
        self.byCurvLayerPref_le.setObjectName("byCurvLayerPref_le")
        self.gridLayout_4.addWidget(self.byCurvLayerPref_le, 4, 1, 1, 1)
        self.label_11 = QtGui.QLabel(self.groupBox_6)
        self.label_11.setObjectName("label_11")
        self.gridLayout_4.addWidget(self.label_11, 0, 1, 1, 1)
        self.verticalLayout_16.addWidget(self.groupBox_6)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_16.addItem(spacerItem5)
        self.curvScroll_sa.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_11.addWidget(self.curvScroll_sa)
        self.mainTab.addTab(self.tab_4, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.partScroll_sa = QtGui.QScrollArea(self.tab_2)
        self.partScroll_sa.setWidgetResizable(True)
        self.partScroll_sa.setObjectName("partScroll_sa")
        self.scrollAreaWidgetContents_4 = QtGui.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 200, 175))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.verticalLayout_18 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_18.setSpacing(2)
        self.verticalLayout_18.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.partGroupEnable_cb = QtGui.QCheckBox(self.scrollAreaWidgetContents_4)
        self.partGroupEnable_cb.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.partGroupEnable_cb.setChecked(True)
        self.partGroupEnable_cb.setObjectName("partGroupEnable_cb")
        self.horizontalLayout_11.addWidget(self.partGroupEnable_cb)
        self.expParticlesGlobalGroupName_le = QtGui.QLineEdit(self.scrollAreaWidgetContents_4)
        self.expParticlesGlobalGroupName_le.setObjectName("expParticlesGlobalGroupName_le")
        self.horizontalLayout_11.addWidget(self.expParticlesGlobalGroupName_le)
        self.verticalLayout_18.addLayout(self.horizontalLayout_11)
        self.groupBox_4 = QtGui.QGroupBox(self.scrollAreaWidgetContents_4)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_19 = QtGui.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_19.setSpacing(2)
        self.verticalLayout_19.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.customPartAttr_cb = QtGui.QCheckBox(self.groupBox_4)
        self.customPartAttr_cb.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.customPartAttr_cb.setChecked(True)
        self.customPartAttr_cb.setObjectName("customPartAttr_cb")
        self.verticalLayout_19.addWidget(self.customPartAttr_cb)
        self.customAttr_le = QtGui.QLineEdit(self.groupBox_4)
        self.customAttr_le.setText("")
        self.customAttr_le.setObjectName("customAttr_le")
        self.verticalLayout_19.addWidget(self.customAttr_le)
        self.verticalLayout_18.addWidget(self.groupBox_4)
        self.attrTable_part_ly = QtGui.QVBoxLayout()
        self.attrTable_part_ly.setObjectName("attrTable_part_ly")
        self.verticalLayout_18.addLayout(self.attrTable_part_ly)
        self.groupBox_3 = QtGui.QGroupBox(self.scrollAreaWidgetContents_4)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_2.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_2.setSpacing(2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.byPartObj_cb = QtGui.QCheckBox(self.groupBox_3)
        self.byPartObj_cb.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.byPartObj_cb.setObjectName("byPartObj_cb")
        self.gridLayout_2.addWidget(self.byPartObj_cb, 2, 0, 1, 1)
        self.byEmit_cb = QtGui.QCheckBox(self.groupBox_3)
        self.byEmit_cb.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.byEmit_cb.setObjectName("byEmit_cb")
        self.gridLayout_2.addWidget(self.byEmit_cb, 3, 0, 1, 1)
        self.label_12 = QtGui.QLabel(self.groupBox_3)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 0, 0, 1, 1)
        self.line_6 = QtGui.QFrame(self.groupBox_3)
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.gridLayout_2.addWidget(self.line_6, 1, 0, 1, 4)
        self.byPartObj_le = QtGui.QLineEdit(self.groupBox_3)
        self.byPartObj_le.setText("")
        self.byPartObj_le.setObjectName("byPartObj_le")
        self.gridLayout_2.addWidget(self.byPartObj_le, 2, 2, 1, 1)
        self.label_14 = QtGui.QLabel(self.groupBox_3)
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 0, 2, 1, 1)
        self.byEmit_le = QtGui.QLineEdit(self.groupBox_3)
        self.byEmit_le.setText("")
        self.byEmit_le.setObjectName("byEmit_le")
        self.gridLayout_2.addWidget(self.byEmit_le, 3, 2, 1, 1)
        self.byPartObjPref_le = QtGui.QLineEdit(self.groupBox_3)
        self.byPartObjPref_le.setObjectName("byPartObjPref_le")
        self.gridLayout_2.addWidget(self.byPartObjPref_le, 2, 1, 1, 1)
        self.byEmitPref_le = QtGui.QLineEdit(self.groupBox_3)
        self.byEmitPref_le.setObjectName("byEmitPref_le")
        self.gridLayout_2.addWidget(self.byEmitPref_le, 3, 1, 1, 1)
        self.label_13 = QtGui.QLabel(self.groupBox_3)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 0, 1, 1, 1)
        self.verticalLayout_18.addWidget(self.groupBox_3)
        spacerItem6 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_18.addItem(spacerItem6)
        self.partScroll_sa.setWidget(self.scrollAreaWidgetContents_4)
        self.verticalLayout_6.addWidget(self.partScroll_sa)
        self.mainTab.addTab(self.tab_2, "")
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tab_3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pivScroll_sa = QtGui.QScrollArea(self.tab_3)
        self.pivScroll_sa.setWidgetResizable(True)
        self.pivScroll_sa.setObjectName("pivScroll_sa")
        self.scrollAreaWidgetContents_3 = QtGui.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 213, 279))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayout_17 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_17.setSpacing(2)
        self.verticalLayout_17.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.expPivotsGlobalGroupName_le = QtGui.QLineEdit(self.scrollAreaWidgetContents_3)
        self.expPivotsGlobalGroupName_le.setObjectName("expPivotsGlobalGroupName_le")
        self.gridLayout_3.addWidget(self.expPivotsGlobalGroupName_le, 1, 2, 1, 1)
        self.label_22 = QtGui.QLabel(self.scrollAreaWidgetContents_3)
        self.label_22.setObjectName("label_22")
        self.gridLayout_3.addWidget(self.label_22, 2, 1, 1, 1)
        self.pivotFilter_le = QtGui.QLineEdit(self.scrollAreaWidgetContents_3)
        self.pivotFilter_le.setText("")
        self.pivotFilter_le.setObjectName("pivotFilter_le")
        self.gridLayout_3.addWidget(self.pivotFilter_le, 2, 2, 1, 1)
        self.pivSkipTransform_cb = QtGui.QCheckBox(self.scrollAreaWidgetContents_3)
        self.pivSkipTransform_cb.setObjectName("pivSkipTransform_cb")
        self.gridLayout_3.addWidget(self.pivSkipTransform_cb, 3, 1, 1, 2)
        self.pivotGroupEnable_cb = QtGui.QCheckBox(self.scrollAreaWidgetContents_3)
        self.pivotGroupEnable_cb.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pivotGroupEnable_cb.setChecked(True)
        self.pivotGroupEnable_cb.setObjectName("pivotGroupEnable_cb")
        self.gridLayout_3.addWidget(self.pivotGroupEnable_cb, 1, 1, 1, 1)
        self.verticalLayout_17.addLayout(self.gridLayout_3)
        self.pivotAttr_gb = QtGui.QGroupBox(self.scrollAreaWidgetContents_3)
        self.pivotAttr_gb.setCheckable(False)
        self.pivotAttr_gb.setObjectName("pivotAttr_gb")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.pivotAttr_gb)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.exportOrient_cb = QtGui.QCheckBox(self.pivotAttr_gb)
        self.exportOrient_cb.setChecked(True)
        self.exportOrient_cb.setObjectName("exportOrient_cb")
        self.gridLayout_5.addWidget(self.exportOrient_cb, 0, 0, 1, 1)
        self.scale_cb = QtGui.QCheckBox(self.pivotAttr_gb)
        self.scale_cb.setChecked(True)
        self.scale_cb.setObjectName("scale_cb")
        self.gridLayout_5.addWidget(self.scale_cb, 0, 1, 1, 1)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem7, 0, 2, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_5)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.customPivotAttr_cb = QtGui.QCheckBox(self.pivotAttr_gb)
        self.customPivotAttr_cb.setChecked(True)
        self.customPivotAttr_cb.setObjectName("customPivotAttr_cb")
        self.horizontalLayout_6.addWidget(self.customPivotAttr_cb)
        self.customPivotAttr_le = QtGui.QLineEdit(self.pivotAttr_gb)
        self.customPivotAttr_le.setObjectName("customPivotAttr_le")
        self.horizontalLayout_6.addWidget(self.customPivotAttr_le)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.attrTable_pivot_ly = QtGui.QVBoxLayout()
        self.attrTable_pivot_ly.setObjectName("attrTable_pivot_ly")
        self.verticalLayout_3.addLayout(self.attrTable_pivot_ly)
        self.verticalLayout_17.addWidget(self.pivotAttr_gb)
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_17.addLayout(self.verticalLayout_7)
        self.groupBox_9 = QtGui.QGroupBox(self.scrollAreaWidgetContents_3)
        self.groupBox_9.setObjectName("groupBox_9")
        self.gridLayout_7 = QtGui.QGridLayout(self.groupBox_9)
        self.gridLayout_7.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_7.setSpacing(2)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.expPivotObj_le = QtGui.QLineEdit(self.groupBox_9)
        self.expPivotObj_le.setObjectName("expPivotObj_le")
        self.gridLayout_7.addWidget(self.expPivotObj_le, 4, 2, 1, 1)
        self.expPivotParent_le = QtGui.QLineEdit(self.groupBox_9)
        self.expPivotParent_le.setObjectName("expPivotParent_le")
        self.gridLayout_7.addWidget(self.expPivotParent_le, 6, 2, 1, 1)
        self.expPivotShape_le = QtGui.QLineEdit(self.groupBox_9)
        self.expPivotShape_le.setObjectName("expPivotShape_le")
        self.gridLayout_7.addWidget(self.expPivotShape_le, 5, 2, 1, 1)
        self.label_17 = QtGui.QLabel(self.groupBox_9)
        self.label_17.setObjectName("label_17")
        self.gridLayout_7.addWidget(self.label_17, 2, 0, 1, 1)
        self.line_7 = QtGui.QFrame(self.groupBox_9)
        self.line_7.setFrameShape(QtGui.QFrame.HLine)
        self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.gridLayout_7.addWidget(self.line_7, 3, 0, 1, 4)
        self.label_18 = QtGui.QLabel(self.groupBox_9)
        self.label_18.setObjectName("label_18")
        self.gridLayout_7.addWidget(self.label_18, 2, 2, 1, 1)
        self.expPivotObj_cb = QtGui.QCheckBox(self.groupBox_9)
        self.expPivotObj_cb.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.expPivotObj_cb.setObjectName("expPivotObj_cb")
        self.gridLayout_7.addWidget(self.expPivotObj_cb, 4, 0, 1, 1)
        self.expPivotShape_cb = QtGui.QCheckBox(self.groupBox_9)
        self.expPivotShape_cb.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.expPivotShape_cb.setObjectName("expPivotShape_cb")
        self.gridLayout_7.addWidget(self.expPivotShape_cb, 5, 0, 1, 1)
        self.expPivotParent_cb = QtGui.QCheckBox(self.groupBox_9)
        self.expPivotParent_cb.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.expPivotParent_cb.setObjectName("expPivotParent_cb")
        self.gridLayout_7.addWidget(self.expPivotParent_cb, 6, 0, 1, 1)
        self.expPivotObjPref_le = QtGui.QLineEdit(self.groupBox_9)
        self.expPivotObjPref_le.setObjectName("expPivotObjPref_le")
        self.gridLayout_7.addWidget(self.expPivotObjPref_le, 4, 1, 1, 1)
        self.expPivotShapePref_le = QtGui.QLineEdit(self.groupBox_9)
        self.expPivotShapePref_le.setObjectName("expPivotShapePref_le")
        self.gridLayout_7.addWidget(self.expPivotShapePref_le, 5, 1, 1, 1)
        self.expPivotParentPref_le = QtGui.QLineEdit(self.groupBox_9)
        self.expPivotParentPref_le.setObjectName("expPivotParentPref_le")
        self.gridLayout_7.addWidget(self.expPivotParentPref_le, 6, 1, 1, 1)
        self.label_19 = QtGui.QLabel(self.groupBox_9)
        self.label_19.setObjectName("label_19")
        self.gridLayout_7.addWidget(self.label_19, 2, 1, 1, 1)
        self.expPivotLayer_cb = QtGui.QCheckBox(self.groupBox_9)
        self.expPivotLayer_cb.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.expPivotLayer_cb.setObjectName("expPivotLayer_cb")
        self.gridLayout_7.addWidget(self.expPivotLayer_cb, 7, 0, 1, 1)
        self.expPivotLayerPref_le = QtGui.QLineEdit(self.groupBox_9)
        self.expPivotLayerPref_le.setObjectName("expPivotLayerPref_le")
        self.gridLayout_7.addWidget(self.expPivotLayerPref_le, 7, 1, 1, 1)
        self.expPivotlayer_le = QtGui.QLineEdit(self.groupBox_9)
        self.expPivotlayer_le.setObjectName("expPivotlayer_le")
        self.gridLayout_7.addWidget(self.expPivotlayer_le, 7, 2, 1, 1)
        self.verticalLayout_17.addWidget(self.groupBox_9)
        spacerItem8 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_17.addItem(spacerItem8)
        self.pivScroll_sa.setWidget(self.scrollAreaWidgetContents_3)
        self.verticalLayout_4.addWidget(self.pivScroll_sa)
        self.mainTab.addTab(self.tab_3, "")
        self.verticalLayout.addWidget(self.mainTab)
        self.layoutWidget = QtGui.QWidget(self.textWidget_sp)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.output_te = QtGui.QTextEdit(self.layoutWidget)
        self.output_te.setReadOnly(True)
        self.output_te.setObjectName("output_te")
        self.verticalLayout_9.addWidget(self.output_te)
        self.clearText_btn = QtGui.QPushButton(self.layoutWidget)
        self.clearText_btn.setMaximumSize(QtCore.QSize(16777215, 10))
        self.clearText_btn.setText("")
        self.clearText_btn.setObjectName("clearText_btn")
        self.verticalLayout_9.addWidget(self.clearText_btn)
        self.verticalLayout_9.setStretch(1, 1)
        self.verticalLayout_22.addWidget(self.textWidget_sp)
        mgeoWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(mgeoWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 697, 21))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuMenu = QtGui.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        self.presets_menu = QtGui.QMenu(self.menubar)
        self.presets_menu.setObjectName("presets_menu")
        mgeoWindow.setMenuBar(self.menubar)
        self.statusBar = QtGui.QStatusBar(mgeoWindow)
        self.statusBar.setObjectName("statusBar")
        mgeoWindow.setStatusBar(self.statusBar)
        self.help_act = QtGui.QAction(mgeoWindow)
        self.help_act.setObjectName("help_act")
        self.about_act = QtGui.QAction(mgeoWindow)
        self.about_act.setObjectName("about_act")
        self.resetAll_act = QtGui.QAction(mgeoWindow)
        self.resetAll_act.setObjectName("resetAll_act")
        self.options_act = QtGui.QAction(mgeoWindow)
        self.options_act.setObjectName("options_act")
        self.default_act = QtGui.QAction(mgeoWindow)
        self.default_act.setCheckable(False)
        self.default_act.setObjectName("default_act")
        self.saveDefault_act = QtGui.QAction(mgeoWindow)
        self.saveDefault_act.setObjectName("saveDefault_act")
        self.extReport_act = QtGui.QAction(mgeoWindow)
        self.extReport_act.setCheckable(True)
        self.extReport_act.setObjectName("extReport_act")
        self.save_act = QtGui.QAction(mgeoWindow)
        self.save_act.setObjectName("save_act")
        self.load_act = QtGui.QAction(mgeoWindow)
        self.load_act.setObjectName("load_act")
        self.isolateExported_act = QtGui.QAction(mgeoWindow)
        self.isolateExported_act.setCheckable(True)
        self.isolateExported_act.setObjectName("isolateExported_act")
        self.colorInd_act = QtGui.QAction(mgeoWindow)
        self.colorInd_act.setCheckable(True)
        self.colorInd_act.setObjectName("colorInd_act")
        self.showWarnings_act = QtGui.QAction(mgeoWindow)
        self.showWarnings_act.setCheckable(True)
        self.showWarnings_act.setObjectName("showWarnings_act")
        self.save_preset_act = QtGui.QAction(mgeoWindow)
        self.save_preset_act.setObjectName("save_preset_act")
        self.preset_editor_act = QtGui.QAction(mgeoWindow)
        self.preset_editor_act.setObjectName("preset_editor_act")
        self.menuHelp.addAction(self.help_act)
        self.menuHelp.addAction(self.about_act)
        self.menuMenu.addAction(self.save_act)
        self.menuMenu.addAction(self.load_act)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.default_act)
        self.menuMenu.addAction(self.saveDefault_act)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.extReport_act)
        self.menuMenu.addAction(self.isolateExported_act)
        self.menuMenu.addAction(self.colorInd_act)
        self.menuMenu.addAction(self.showWarnings_act)
        self.presets_menu.addAction(self.save_preset_act)
        self.presets_menu.addAction(self.preset_editor_act)
        self.presets_menu.addSeparator()
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.presets_menu.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(mgeoWindow)
        self.mainTab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(mgeoWindow)

    def retranslateUi(self, mgeoWindow):
        mgeoWindow.setWindowTitle(QtGui.QApplication.translate("mgeoWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("mgeoWindow", "Formats", None, QtGui.QApplication.UnicodeUTF8))
        self.fileFormat_cbb.setItemText(0, QtGui.QApplication.translate("mgeoWindow", "geo", None, QtGui.QApplication.UnicodeUTF8))
        self.fileFormat_cbb.setItemText(1, QtGui.QApplication.translate("mgeoWindow", "bgeo", None, QtGui.QApplication.UnicodeUTF8))
        self.compress_cbb.setItemText(0, QtGui.QApplication.translate("mgeoWindow", "none", None, QtGui.QApplication.UnicodeUTF8))
        self.compress_cbb.setItemText(1, QtGui.QApplication.translate("mgeoWindow", ".gz", None, QtGui.QApplication.UnicodeUTF8))
        self.compress_cbb.setItemText(2, QtGui.QApplication.translate("mgeoWindow", ".sc (H14)", None, QtGui.QApplication.UnicodeUTF8))
        self.cacheOnly_cbb.setToolTip(QtGui.QApplication.translate("mgeoWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Write GEO and MDD / MDD only</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("mgeoWindow", "File format:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("mgeoWindow", "Cache:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_20.setText(QtGui.QApplication.translate("mgeoWindow", "Chache Only:", None, QtGui.QApplication.UnicodeUTF8))
        self.cacheFormat_cbb.setItemText(0, QtGui.QApplication.translate("mgeoWindow", "Geo Sequence", None, QtGui.QApplication.UnicodeUTF8))
        self.cacheFormat_cbb.setItemText(1, QtGui.QApplication.translate("mgeoWindow", "MDD", None, QtGui.QApplication.UnicodeUTF8))
        self.cacheFormat_cbb.setItemText(2, QtGui.QApplication.translate("mgeoWindow", "Alembic (points only)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("mgeoWindow", "Compress:", None, QtGui.QApplication.UnicodeUTF8))
        self.outFile_gb.setTitle(QtGui.QApplication.translate("mgeoWindow", "Output file", None, QtGui.QApplication.UnicodeUTF8))
        self.exportPath_le.setToolTip(QtGui.QApplication.translate("mgeoWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"result_box\"></a><span style=\" font-size:8pt;\">U</span><span style=\" font-size:8pt;\">se the </span><span style=\" font-size:8pt; font-weight:600;\">$ F#</span><span style=\" font-size:8pt;\"> to replace the frame number</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.applets_btn.setText(QtGui.QApplication.translate("mgeoWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.fileAsk_rb.setToolTip(QtGui.QApplication.translate("mgeoWindow", "Ask a new file name if exists", None, QtGui.QApplication.UnicodeUTF8))
        self.fileAsk_rb.setText(QtGui.QApplication.translate("mgeoWindow", "Ask", None, QtGui.QApplication.UnicodeUTF8))
        self.fileOverride_rb.setToolTip(QtGui.QApplication.translate("mgeoWindow", "Owerwrite old file", None, QtGui.QApplication.UnicodeUTF8))
        self.fileOverride_rb.setText(QtGui.QApplication.translate("mgeoWindow", "Overwrite", None, QtGui.QApplication.UnicodeUTF8))
        self.fileSkip_rb.setToolTip(QtGui.QApplication.translate("mgeoWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Skip export if file exists</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.fileSkip_rb.setText(QtGui.QApplication.translate("mgeoWindow", "Skip", None, QtGui.QApplication.UnicodeUTF8))
        self.fileRename_rb.setToolTip(QtGui.QApplication.translate("mgeoWindow", "Automatically rename", None, QtGui.QApplication.UnicodeUTF8))
        self.fileRename_rb.setText(QtGui.QApplication.translate("mgeoWindow", "Rename", None, QtGui.QApplication.UnicodeUTF8))
        self.frameRangeSettings_gb.setTitle(QtGui.QApplication.translate("mgeoWindow", "Frame range", None, QtGui.QApplication.UnicodeUTF8))
        self.singleFrame_rb.setToolTip(QtGui.QApplication.translate("mgeoWindow", "Export single frame", None, QtGui.QApplication.UnicodeUTF8))
        self.singleFrame_rb.setText(QtGui.QApplication.translate("mgeoWindow", "Single", None, QtGui.QApplication.UnicodeUTF8))
        self.rangeFrame_rb.setToolTip(QtGui.QApplication.translate("mgeoWindow", "Export frame range", None, QtGui.QApplication.UnicodeUTF8))
        self.rangeFrame_rb.setText(QtGui.QApplication.translate("mgeoWindow", "Range", None, QtGui.QApplication.UnicodeUTF8))
        self.setrange_btn.setToolTip(QtGui.QApplication.translate("mgeoWindow", "<html><head/><body><p>Presets</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.setrange_btn.setText(QtGui.QApplication.translate("mgeoWindow", "Set from:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_5.setTitle(QtGui.QApplication.translate("mgeoWindow", "Export sets", None, QtGui.QApplication.UnicodeUTF8))
        self.createSet_btn.setToolTip(QtGui.QApplication.translate("mgeoWindow", "Create new export set from selection", None, QtGui.QApplication.UnicodeUTF8))
        self.createSet_btn.setText(QtGui.QApplication.translate("mgeoWindow", "*", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteSet_btn.setToolTip(QtGui.QApplication.translate("mgeoWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Remove set</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteSet_btn.setText(QtGui.QApplication.translate("mgeoWindow", "x", None, QtGui.QApplication.UnicodeUTF8))
        self.reloadSets_btn.setToolTip(QtGui.QApplication.translate("mgeoWindow", "Reload sets from scene", None, QtGui.QApplication.UnicodeUTF8))
        self.reloadSets_btn.setText(QtGui.QApplication.translate("mgeoWindow", "R", None, QtGui.QApplication.UnicodeUTF8))
        self.addToSet_btn.setToolTip(QtGui.QApplication.translate("mgeoWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Add selected objects to set. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Supported types:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- Mesh objects (component skipped)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- Particles / nParticles</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- Nurbs curves</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- any transtorm node</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.addToSet_btn.setText(QtGui.QApplication.translate("mgeoWindow", "add", None, QtGui.QApplication.UnicodeUTF8))
        self.removeFromSet_btn.setToolTip(QtGui.QApplication.translate("mgeoWindow", "Remove selected objects from set", None, QtGui.QApplication.UnicodeUTF8))
        self.removeFromSet_btn.setText(QtGui.QApplication.translate("mgeoWindow", "rem", None, QtGui.QApplication.UnicodeUTF8))
        self.replaceSet_btn.setToolTip(QtGui.QApplication.translate("mgeoWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Replace all objects in set to the selected</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.replaceSet_btn.setText(QtGui.QApplication.translate("mgeoWindow", "repl", None, QtGui.QApplication.UnicodeUTF8))
        self.clearSet_btn.setToolTip(QtGui.QApplication.translate("mgeoWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Clear set</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.clearSet_btn.setText(QtGui.QApplication.translate("mgeoWindow", "CL", None, QtGui.QApplication.UnicodeUTF8))
        self.geoExport_btn.setToolTip(QtGui.QApplication.translate("mgeoWindow", "START EXPORT!!!", None, QtGui.QApplication.UnicodeUTF8))
        self.geoExport_btn.setText(QtGui.QApplication.translate("mgeoWindow", "EXPORT", None, QtGui.QApplication.UnicodeUTF8))
        self.expoptions_gb.setTitle(QtGui.QApplication.translate("mgeoWindow", "Export Options", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("mgeoWindow", "Global Position:", None, QtGui.QApplication.UnicodeUTF8))
        self.worldPos_rb.setToolTip(QtGui.QApplication.translate("mgeoWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Read position in world space</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.worldPos_rb.setText(QtGui.QApplication.translate("mgeoWindow", "World", None, QtGui.QApplication.UnicodeUTF8))
        self.localPos_rb.setToolTip(QtGui.QApplication.translate("mgeoWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Read position in local space</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.localPos_rb.setText(QtGui.QApplication.translate("mgeoWindow", "Local", None, QtGui.QApplication.UnicodeUTF8))
        self.expVis_cb.setToolTip(QtGui.QApplication.translate("mgeoWindow", "Export only visible objects", None, QtGui.QApplication.UnicodeUTF8))
        self.expVis_cb.setText(QtGui.QApplication.translate("mgeoWindow", "Visible only", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("mgeoWindow", "Global Scale:", None, QtGui.QApplication.UnicodeUTF8))
        self.scale_le.setToolTip(QtGui.QApplication.translate("mgeoWindow", "Global scale of geometry", None, QtGui.QApplication.UnicodeUTF8))
        self.scale_le.setText(QtGui.QApplication.translate("mgeoWindow", "1.0", None, QtGui.QApplication.UnicodeUTF8))
        self.expHierarchy_cb.setToolTip(QtGui.QApplication.translate("mgeoWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Export all parented objects</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.expHierarchy_cb.setText(QtGui.QApplication.translate("mgeoWindow", "Export Hierarchy", None, QtGui.QApplication.UnicodeUTF8))
        self.mainTab.setToolTip(QtGui.QApplication.translate("mgeoWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Export types</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.polyGroupEnable_cb.setToolTip(QtGui.QApplication.translate("mgeoWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Enable/disable global Poly group</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.polyGroupEnable_cb.setText(QtGui.QApplication.translate("mgeoWindow", "Create Global Poly Group", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("mgeoWindow", "Poly Groups Prefix", None, QtGui.QApplication.UnicodeUTF8))
        self.expGeoGlobalGroupName_le.setToolTip(QtGui.QApplication.translate("mgeoWindow", "Main polygons group name", None, QtGui.QApplication.UnicodeUTF8))
        self.expGeoGlobalGroupName_le.setText(QtGui.QApplication.translate("mgeoWindow", "POLY", None, QtGui.QApplication.UnicodeUTF8))
        self.pointAttrib_gb.setToolTip(QtGui.QApplication.translate("mgeoWindow", "Vertex Atributes", None, QtGui.QApplication.UnicodeUTF8))
        self.pointAttrib_gb.setTitle(QtGui.QApplication.translate("mgeoWindow", "Vertex attributes", None, QtGui.QApplication.UnicodeUTF8))
        self.exportUv_cb.setToolTip(QtGui.QApplication.translate("mgeoWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Export uv as vertex attribute.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">attrib: </span><span style=\" font-size:8pt; font-weight:600;\">uv</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">type: vector3</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">(RMB to select the method of naming)</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.exportUv_cb.setText(QtGui.QApplication.translate("mgeoWindow", "UV", None, QtGui.QApplication.UnicodeUTF8))
        self.exportVertexColor_cb.setToolTip(QtGui.QApplication.translate("mgeoWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Export vertex color as vertex attribute.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">attrib: </span><span style=\" font-size:8pt; font-weight:600;\">Cd</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">type: vector3</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">(RMB to select the method of naming)</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.exportVertexColor_cb.setText(QtGui.QApplication.translate("mgeoWindow", "Color", None, QtGui.QApplication.UnicodeUTF8))
        self.exportVerNorm_cb.setToolTip(QtGui.QApplication.translate("mgeoWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Export normals as vertex attribute (hard-soft edges).</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">attrib: </span><span style=\" font-size:8pt; font-weight:600;\">N</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">type: vector3</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.exportVerNorm_cb.setText(QtGui.QApplication.translate("mgeoWindow", "Vertex Normal", None, QtGui.QApplication.UnicodeUTF8))
        self.exportCrease_cb.setToolTip(QtGui.QApplication.translate("mgeoWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Export edge crease as vertex attribute.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">attrib: </span><span style=\" font-size:8pt; font-weight:600;\">creaseweight</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">type: float</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.exportCrease_cb.setText(QtGui.QApplication.translate("mgeoWindow", "Edge Crease", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_8.setTitle(QtGui.QApplication.translate("mgeoWindow", "Prim attributes", None, QtGui.QApplication.UnicodeUTF8))
        self.customGeoAttr_cb.setToolTip(QtGui.QApplication.translate("mgeoWindow", "Enable\\disable export custom attributes", None, QtGui.QApplication.UnicodeUTF8))
        self.customGeoAttr_cb.setText(QtGui.QApplication.translate("mgeoWindow", "Export Custom Attributes", None, QtGui.QApplication.UnicodeUTF8))
        self.customGeoAttr_le.setToolTip(QtGui.QApplication.translate("mgeoWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'sans-serif\'; font-size:8pt; color:#000000; background-color:#ffffff;\">Create </span><span style=\" font-family:\'sans-serif\'; font-size:8pt; text-decoration: underline; color:#000000; background-color:#ffffff;\">primitive</span><span style=\" font-family:\'sans-serif\'; font-size:8pt; color:#000000; background-color:#ffffff;\"> attributes from object (shape, transform). </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'sans-serif\'; font-size:8pt; color:#000000; background-color:#ffffff;\">Separate your attribute names with space.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'sans-serif\'; font-size:8pt; color:#000000; background-color:#ffffff;\">Supported types: </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'sans-serif\'; font-size:8pt; color:#000000;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'sans-serif\'; font-size:8pt; font-style:italic; color:#000000; background-color:#ffffff;\">bool (int)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'sans-serif\'; font-size:8pt; font-style:italic; color:#000000; background-color:#ffffff;\">int</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'sans-serif\'; font-size:8pt; font-style:italic; color:#000000; background-color:#ffffff;\">float</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'sans-serif\'; font-size:8pt; font-style:italic; color:#000000; background-color:#ffffff;\">vector2</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'sans-serif\'; font-size:8pt; font-style:italic; color:#000000; background-color:#ffffff;\">vector3</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'sans-serif\'; font-size:8pt; font-style:italic; color:#000000; background-color:#ffffff;\">vector4</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'sans-serif\'; font-size:8pt; font-style:italic; color:#000000;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'sans-serif\'; font-size:8pt; color:#000000; background-color:#ffffff;\">Default = 0</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.primGroups_gb.setTitle(QtGui.QApplication.translate("mgeoWindow", "Groups", None, QtGui.QApplication.UnicodeUTF8))
        self.byMtl_cb.setToolTip(QtGui.QApplication.translate("mgeoWindow", "Create primitive group by assigned material. \n"
"<prefix><matName>", None, QtGui.QApplication.UnicodeUTF8))
        self.byMtl_cb.setText(QtGui.QApplication.translate("mgeoWindow", "Material", None, QtGui.QApplication.UnicodeUTF8))
        self.byMtl_le.setToolTip(QtGui.QApplication.translate("mgeoWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Material name filter</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.byPar_cb.setToolTip(QtGui.QApplication.translate("mgeoWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Create primitive group by parent.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">&lt;prefix&gt;&lt;parentNodeName&gt; </span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.byPar_cb.setText(QtGui.QApplication.translate("mgeoWindow", "Parent", None, QtGui.QApplication.UnicodeUTF8))
        self.byPar_le.setToolTip(QtGui.QApplication.translate("mgeoWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Parent group filter.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"result_box\"></a><span style=\" font-size:8pt;\">T</span><span style=\" font-size:8pt;\">o use a specific node, use the prefix in naming</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">&lt;findPrefix&gt;&lt;name&gt; </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"result_box\"></a><span style=\" font-size:8pt;\">I</span><span style=\" font-size:8pt;\">f the prefix is empty, use the closest parent.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">If the prefix is not found, use default group name &lt;prefis&gt;&quot;noParent&quot;</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.displayer_cb.setToolTip(QtGui.QApplication.translate("mgeoWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Groups by display layers</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">&lt;prefix&gt;&lt;layerName&gt;</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.displayer_cb.setText(QtGui.QApplication.translate("mgeoWindow", "Display layer", None, QtGui.QApplication.UnicodeUTF8))
        self.byLayer_le.setToolTip(QtGui.QApplication.translate("mgeoWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Display layer name filter</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">If the prefix is not found, use default group name &lt;prefis&gt;&quot;deflayer&quot;</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("mgeoWindow", "Prim groups by:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("mgeoWindow", "Filter:", None, QtGui.QApplication.UnicodeUTF8))
        self.byMtlPref_le.setToolTip(QtGui.QApplication.translate("mgeoWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Material group prefix</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.byMtlPref_le.setText(QtGui.QApplication.translate("mgeoWindow", "MTL_", None, QtGui.QApplication.UnicodeUTF8))
        self.byParPref_le.setToolTip(QtGui.QApplication.translate("mgeoWindow", "Parent group prefix", None, QtGui.QApplication.UnicodeUTF8))
        self.byParPref_le.setText(QtGui.QApplication.translate("mgeoWindow", "PRNT_", None, QtGui.QApplication.UnicodeUTF8))
        self.byLayerPref_le.setToolTip(QtGui.QApplication.translate("mgeoWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Display layer group prefix</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.byLayerPref_le.setText(QtGui.QApplication.translate("mgeoWindow", "LAYER_", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("mgeoWindow", "Prefix:", None, QtGui.QApplication.UnicodeUTF8))
        self.byObj_cb.setToolTip(QtGui.QApplication.translate("mgeoWindow", "Create primitive group by object name. \n"
"<prefix><nodeName>", None, QtGui.QApplication.UnicodeUTF8))
        self.byObj_cb.setText(QtGui.QApplication.translate("mgeoWindow", "Object name", None, QtGui.QApplication.UnicodeUTF8))
        self.byObjPref_le.setToolTip(QtGui.QApplication.translate("mgeoWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Object group prefix</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.byObjPref_le.setText(QtGui.QApplication.translate("mgeoWindow", "OBJ_", None, QtGui.QApplication.UnicodeUTF8))
        self.byObj_le.setToolTip(QtGui.QApplication.translate("mgeoWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Object name filter</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.byShape_cb.setToolTip(QtGui.QApplication.translate("mgeoWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Create primitive group by shape name. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">&lt;prefix&gt;&lt;nodeName&gt;</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.byShape_cb.setText(QtGui.QApplication.translate("mgeoWindow", "Shape name", None, QtGui.QApplication.UnicodeUTF8))
        self.bySpahePref_le.setToolTip(QtGui.QApplication.translate("mgeoWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Shape group prefix</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.bySpahePref_le.setText(QtGui.QApplication.translate("mgeoWindow", "SHAPE_", None, QtGui.QApplication.UnicodeUTF8))
        self.byShape_le.setToolTip(QtGui.QApplication.translate("mgeoWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Shape name filter</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.mainTab.setTabText(self.mainTab.indexOf(self.tab), QtGui.QApplication.translate("mgeoWindow", "Polygons", None, QtGui.QApplication.UnicodeUTF8))
        self.curveGroupEnable_cb.setToolTip(QtGui.QApplication.translate("mgeoWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Enable/disable global Curve group</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.curveGroupEnable_cb.setText(QtGui.QApplication.translate("mgeoWindow", "Create Global Curves Group:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("mgeoWindow", "Curves Groups Prefix", None, QtGui.QApplication.UnicodeUTF8))
        self.expCurvesGlobalGroupName_le.setToolTip(QtGui.QApplication.translate("mgeoWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Main curves group</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.expCurvesGlobalGroupName_le.setText(QtGui.QApplication.translate("mgeoWindow", "CURV", None, QtGui.QApplication.UnicodeUTF8))
        self.curvToNURBS_rb.setToolTip(QtGui.QApplication.translate("mgeoWindow", "Export as NURBS", None, QtGui.QApplication.UnicodeUTF8))
        self.curvToNURBS_rb.setText(QtGui.QApplication.translate("mgeoWindow", "NURBS", None, QtGui.QApplication.UnicodeUTF8))
        self.curvToPoly_rb.setToolTip(QtGui.QApplication.translate("mgeoWindow", "Export as Poly line", None, QtGui.QApplication.UnicodeUTF8))
        self.curvToPoly_rb.setText(QtGui.QApplication.translate("mgeoWindow", "Polyline", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("mgeoWindow", "Prim Attributes", None, QtGui.QApplication.UnicodeUTF8))
        self.customCrvAttr_cbx.setText(QtGui.QApplication.translate("mgeoWindow", "Export Custom Attributes", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_6.setTitle(QtGui.QApplication.translate("mgeoWindow", "Groups", None, QtGui.QApplication.UnicodeUTF8))
        self.byCurvObj_le.setToolTip(QtGui.QApplication.translate("mgeoWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Object name filter</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.byCrvObj_cb.setToolTip(QtGui.QApplication.translate("mgeoWindow", "Create primitive group by object name. \n"
"<prefix><nodeName>", None, QtGui.QApplication.UnicodeUTF8))
        self.byCrvObj_cb.setText(QtGui.QApplication.translate("mgeoWindow", "Object name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("mgeoWindow", "Group by:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("mgeoWindow", "Filter:", None, QtGui.QApplication.UnicodeUTF8))
        self.byCrvPar_cb.setToolTip(QtGui.QApplication.translate("mgeoWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Create primitive group by parent name. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">&lt;prefix&gt;&lt;nodeName&gt;</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.byCrvPar_cb.setText(QtGui.QApplication.translate("mgeoWindow", "Parent", None, QtGui.QApplication.UnicodeUTF8))
        self.byCurvPar_le.setToolTip(QtGui.QApplication.translate("mgeoWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Parent group filter.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"result_box\"></a><span style=\" font-size:8pt;\">T</span><span style=\" font-size:8pt;\">o use a specific node, use the prefix in naming</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">&lt;findPrefix&gt;&lt;name&gt; </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"result_box\"></a><span style=\" font-size:8pt;\">I</span><span style=\" font-size:8pt;\">f the prefix is empty, use the closest parent.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">If the prefix is not found, use default group name &lt;prefis&gt;&quot;noParent&quot;</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.curvDisplayer_cb.setToolTip(QtGui.QApplication.translate("mgeoWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Create primitive group by layer name. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">&lt;prefix&gt;&lt;layerName&gt;</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.curvDisplayer_cb.setText(QtGui.QApplication.translate("mgeoWindow", "Display layer", None, QtGui.QApplication.UnicodeUTF8))
        self.byCurvLayer_le.setToolTip(QtGui.QApplication.translate("mgeoWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Display layer name filter</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">If the prefix is not found, use default group name &lt;prefis&gt;&quot;deflayer&quot;</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.byCurvObjPref_le.setToolTip(QtGui.QApplication.translate("mgeoWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Object group prefix</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.byCurvObjPref_le.setText(QtGui.QApplication.translate("mgeoWindow", "OBJ_", None, QtGui.QApplication.UnicodeUTF8))
        self.byCurvParPref_le.setToolTip(QtGui.QApplication.translate("mgeoWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Parent group prefix</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.byCurvParPref_le.setText(QtGui.QApplication.translate("mgeoWindow", "PAR_", None, QtGui.QApplication.UnicodeUTF8))
        self.byCurvLayerPref_le.setToolTip(QtGui.QApplication.translate("mgeoWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Display layer group prefix</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.byCurvLayerPref_le.setText(QtGui.QApplication.translate("mgeoWindow", "LAYER_", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("mgeoWindow", "Prefix:", None, QtGui.QApplication.UnicodeUTF8))
        self.mainTab.setTabText(self.mainTab.indexOf(self.tab_4), QtGui.QApplication.translate("mgeoWindow", "Curves", None, QtGui.QApplication.UnicodeUTF8))
        self.partGroupEnable_cb.setToolTip(QtGui.QApplication.translate("mgeoWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Enable/disable global Particles group</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.partGroupEnable_cb.setText(QtGui.QApplication.translate("mgeoWindow", "Particles Group:", None, QtGui.QApplication.UnicodeUTF8))
        self.expParticlesGlobalGroupName_le.setToolTip(QtGui.QApplication.translate("mgeoWindow", "Main particles group name", None, QtGui.QApplication.UnicodeUTF8))
        self.expParticlesGlobalGroupName_le.setText(QtGui.QApplication.translate("mgeoWindow", "PART", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("mgeoWindow", "Particle  attributes", None, QtGui.QApplication.UnicodeUTF8))
        self.customPartAttr_cb.setToolTip(QtGui.QApplication.translate("mgeoWindow", "Enable\\ disable export custom attributes", None, QtGui.QApplication.UnicodeUTF8))
        self.customPartAttr_cb.setText(QtGui.QApplication.translate("mgeoWindow", "Export Custom Attributes", None, QtGui.QApplication.UnicodeUTF8))
        self.customAttr_le.setToolTip(QtGui.QApplication.translate("mgeoWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Export custom attrubutes from shape, transform or particles (per particle attributes)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Names must be separated by a space. </span><span style=\" font-size:8pt;\">In brackets, you can specify a default value.</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Example: </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">float - </span><span style=\" font-size:8pt; font-style:italic;\">raduisPP(1)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">vector - </span><span style=\" font-size:8pt; font-style:italic;\">rgbPP(1)</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Value  will be automatically converted into a vector if need.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("mgeoWindow", "Groups", None, QtGui.QApplication.UnicodeUTF8))
        self.byPartObj_cb.setToolTip(QtGui.QApplication.translate("mgeoWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Create point groups by objects name (particle system)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">&lt;prefix&gt;&lt;nodeName&gt;</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.byPartObj_cb.setText(QtGui.QApplication.translate("mgeoWindow", "Object name", None, QtGui.QApplication.UnicodeUTF8))
        self.byEmit_cb.setToolTip(QtGui.QApplication.translate("mgeoWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Create point groups by emitter name</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">&lt;prefix&gt;&lt;nodeName&gt;</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.byEmit_cb.setText(QtGui.QApplication.translate("mgeoWindow", "Emitter", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("mgeoWindow", "Group by:", None, QtGui.QApplication.UnicodeUTF8))
        self.byPartObj_le.setToolTip(QtGui.QApplication.translate("mgeoWindow", "Object name filter", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("mgeoWindow", "Filter:", None, QtGui.QApplication.UnicodeUTF8))
        self.byEmit_le.setToolTip(QtGui.QApplication.translate("mgeoWindow", "Emitter name filter", None, QtGui.QApplication.UnicodeUTF8))
        self.byPartObjPref_le.setToolTip(QtGui.QApplication.translate("mgeoWindow", "Object group prefix", None, QtGui.QApplication.UnicodeUTF8))
        self.byPartObjPref_le.setText(QtGui.QApplication.translate("mgeoWindow", "OBJ_", None, QtGui.QApplication.UnicodeUTF8))
        self.byEmitPref_le.setToolTip(QtGui.QApplication.translate("mgeoWindow", "Emitter group prefix", None, QtGui.QApplication.UnicodeUTF8))
        self.byEmitPref_le.setText(QtGui.QApplication.translate("mgeoWindow", "EMITTER_", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("mgeoWindow", "Prefix:", None, QtGui.QApplication.UnicodeUTF8))
        self.mainTab.setTabText(self.mainTab.indexOf(self.tab_2), QtGui.QApplication.translate("mgeoWindow", "Particles", None, QtGui.QApplication.UnicodeUTF8))
        self.expPivotsGlobalGroupName_le.setToolTip(QtGui.QApplication.translate("mgeoWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Main pivots group name</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.expPivotsGlobalGroupName_le.setText(QtGui.QApplication.translate("mgeoWindow", "PIVOT", None, QtGui.QApplication.UnicodeUTF8))
        self.label_22.setText(QtGui.QApplication.translate("mgeoWindow", "Object filter", None, QtGui.QApplication.UnicodeUTF8))
        self.pivotFilter_le.setToolTip(QtGui.QApplication.translate("mgeoWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Filter objects by name</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pivSkipTransform_cb.setToolTip(QtGui.QApplication.translate("mgeoWindow", "Do not export transfom nodes without shape", None, QtGui.QApplication.UnicodeUTF8))
        self.pivSkipTransform_cb.setText(QtGui.QApplication.translate("mgeoWindow", "Skip transform without shape", None, QtGui.QApplication.UnicodeUTF8))
        self.pivotGroupEnable_cb.setToolTip(QtGui.QApplication.translate("mgeoWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Enable/disable global Pivot group</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pivotGroupEnable_cb.setText(QtGui.QApplication.translate("mgeoWindow", "Pivots Group:", None, QtGui.QApplication.UnicodeUTF8))
        self.pivotAttr_gb.setTitle(QtGui.QApplication.translate("mgeoWindow", "Object Attributes", None, QtGui.QApplication.UnicodeUTF8))
        self.exportOrient_cb.setToolTip(QtGui.QApplication.translate("mgeoWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Export rotate as point attribute.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">attrib: </span><span style=\" font-size:8pt; font-weight:600;\">orient</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">type: vector4 (Quaternion)</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.exportOrient_cb.setText(QtGui.QApplication.translate("mgeoWindow", "Orient", None, QtGui.QApplication.UnicodeUTF8))
        self.scale_cb.setToolTip(QtGui.QApplication.translate("mgeoWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Export scale as point attribute.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">attrib: </span><span style=\" font-size:8pt; font-weight:600;\">scale</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">type: vector3</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.scale_cb.setText(QtGui.QApplication.translate("mgeoWindow", "Scale", None, QtGui.QApplication.UnicodeUTF8))
        self.customPivotAttr_cb.setToolTip(QtGui.QApplication.translate("mgeoWindow", "Enable\\disable export custom attributes", None, QtGui.QApplication.UnicodeUTF8))
        self.customPivotAttr_cb.setText(QtGui.QApplication.translate("mgeoWindow", "Export Custom Attributes", None, QtGui.QApplication.UnicodeUTF8))
        self.customPivotAttr_le.setToolTip(QtGui.QApplication.translate("mgeoWindow", "<html>\n"
"    <head>\n"
"        <title>HTML Online Editor Sample</title>\n"
"    </head>\n"
"    <body>\n"
"        <p>\n"
"            <span style=\" font-family:\'sans-serif\'; font-size:8pt; color:#000000; background-color:#ffffff;\">Create </span><span style=\" font-family:\'sans-serif\'; font-size:8pt; text-decoration: underline; color:#000000; background-color:#ffffff;\">point</span><span style=\" font-family:\'sans-serif\'; font-size:8pt; color:#000000; background-color:#ffffff;\"> attributes from object (shape, transform). </span></p>\n"
"        <p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\n"
"            <span style=\" font-family:\'sans-serif\'; font-size:8pt; color:#000000; background-color:#ffffff;\">Separate your attribute names with space.</span></p>\n"
"        <p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\n"
"            <span style=\" font-family:\'sans-serif\'; font-size:8pt; color:#000000; background-color:#ffffff;\">Supported types: </span></p>\n"
"        <p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\n"
"            <span style=\" font-family:\'sans-serif\'; font-size:8pt; font-style:italic; color:#000000; background-color:#ffffff;\">bool (int)</span></p>\n"
"        <p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\n"
"            <span style=\" font-family:\'sans-serif\'; font-size:8pt; font-style:italic; color:#000000; background-color:#ffffff;\">int</span></p>\n"
"        <p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\n"
"            <span style=\" font-family:\'sans-serif\'; font-size:8pt; font-style:italic; color:#000000; background-color:#ffffff;\">float</span></p>\n"
"        <p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\n"
"            <span style=\" font-family:\'sans-serif\'; font-size:8pt; font-style:italic; color:#000000; background-color:#ffffff;\">vector2</span></p>\n"
"        <p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\n"
"            <span style=\" font-family:\'sans-serif\'; font-size:8pt; font-style:italic; color:#000000; background-color:#ffffff;\">vector3</span></p>\n"
"        <p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\n"
"            <span style=\" font-family:\'sans-serif\'; font-size:8pt; font-style:italic; color:#000000; background-color:#ffffff;\">vector4</span></p>\n"
"        <p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\n"
"            <span style=\" font-family:\'sans-serif\'; font-size:8pt; color:#000000; background-color:#ffffff;\">Default = 0</span></p>\n"
"        <p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\n"
"            <span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\">In brackets, you can specify a default value</span></p>\n"
"        <p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\n"
"            <span style=\" font-family:\'sans-serif\'; font-size:8pt; color:#000000; background-color:#ffffff;\">Example:</span></p>\n"
"        <p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\n"
"            <span style=\" font-family:\'sans-serif\'; font-size:8pt; font-style:italic; color:#000000; background-color:#ffffff;\">myAttr(1)</span></p></body>\n"
"</html>", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_9.setTitle(QtGui.QApplication.translate("mgeoWindow", "Groups", None, QtGui.QApplication.UnicodeUTF8))
        self.expPivotObj_le.setToolTip(QtGui.QApplication.translate("mgeoWindow", "Object name filter", None, QtGui.QApplication.UnicodeUTF8))
        self.expPivotParent_le.setToolTip(QtGui.QApplication.translate("mgeoWindow", "Parent name filter", None, QtGui.QApplication.UnicodeUTF8))
        self.expPivotShape_le.setToolTip(QtGui.QApplication.translate("mgeoWindow", "Shape name filter", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(QtGui.QApplication.translate("mgeoWindow", "Group by:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_18.setText(QtGui.QApplication.translate("mgeoWindow", "Filter:", None, QtGui.QApplication.UnicodeUTF8))
        self.expPivotObj_cb.setToolTip(QtGui.QApplication.translate("mgeoWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Create point groups by object name</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">&lt;prefix&gt;&lt;nodeName&gt;</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.expPivotObj_cb.setText(QtGui.QApplication.translate("mgeoWindow", "Object name", None, QtGui.QApplication.UnicodeUTF8))
        self.expPivotShape_cb.setToolTip(QtGui.QApplication.translate("mgeoWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Create point groups by shape name</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">&lt;prefix&gt;&lt;nodeName&gt;</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.expPivotShape_cb.setText(QtGui.QApplication.translate("mgeoWindow", "Shape name", None, QtGui.QApplication.UnicodeUTF8))
        self.expPivotParent_cb.setToolTip(QtGui.QApplication.translate("mgeoWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Create point groups by parent name</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">&lt;prefix&gt;&lt;nodeName&gt;</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.expPivotParent_cb.setText(QtGui.QApplication.translate("mgeoWindow", "Parent", None, QtGui.QApplication.UnicodeUTF8))
        self.expPivotObjPref_le.setToolTip(QtGui.QApplication.translate("mgeoWindow", "Object group prefix", None, QtGui.QApplication.UnicodeUTF8))
        self.expPivotObjPref_le.setText(QtGui.QApplication.translate("mgeoWindow", "OBJ_", None, QtGui.QApplication.UnicodeUTF8))
        self.expPivotShapePref_le.setToolTip(QtGui.QApplication.translate("mgeoWindow", "Shape group prefix", None, QtGui.QApplication.UnicodeUTF8))
        self.expPivotShapePref_le.setText(QtGui.QApplication.translate("mgeoWindow", "INSTATCE_", None, QtGui.QApplication.UnicodeUTF8))
        self.expPivotParentPref_le.setToolTip(QtGui.QApplication.translate("mgeoWindow", "Parent group prefix", None, QtGui.QApplication.UnicodeUTF8))
        self.expPivotParentPref_le.setText(QtGui.QApplication.translate("mgeoWindow", "PAR_", None, QtGui.QApplication.UnicodeUTF8))
        self.label_19.setText(QtGui.QApplication.translate("mgeoWindow", "Prefix:", None, QtGui.QApplication.UnicodeUTF8))
        self.expPivotLayer_cb.setToolTip(QtGui.QApplication.translate("mgeoWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Groups by display layers</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">&lt;prefix&gt;&lt;layerName&gt;</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.expPivotLayer_cb.setText(QtGui.QApplication.translate("mgeoWindow", "Display layer", None, QtGui.QApplication.UnicodeUTF8))
        self.expPivotLayerPref_le.setToolTip(QtGui.QApplication.translate("mgeoWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Display layer group prefix</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.expPivotLayerPref_le.setText(QtGui.QApplication.translate("mgeoWindow", "LAYER_", None, QtGui.QApplication.UnicodeUTF8))
        self.expPivotlayer_le.setToolTip(QtGui.QApplication.translate("mgeoWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Display layer name filter</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">If the prefix is not found, use default group name &lt;prefis&gt;&quot;deflayer&quot;</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.mainTab.setTabText(self.mainTab.indexOf(self.tab_3), QtGui.QApplication.translate("mgeoWindow", "Pivots", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("mgeoWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menuMenu.setTitle(QtGui.QApplication.translate("mgeoWindow", "Menu", None, QtGui.QApplication.UnicodeUTF8))
        self.presets_menu.setTitle(QtGui.QApplication.translate("mgeoWindow", "Presets", None, QtGui.QApplication.UnicodeUTF8))
        self.help_act.setText(QtGui.QApplication.translate("mgeoWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.about_act.setText(QtGui.QApplication.translate("mgeoWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.resetAll_act.setText(QtGui.QApplication.translate("mgeoWindow", "Reset All", None, QtGui.QApplication.UnicodeUTF8))
        self.options_act.setText(QtGui.QApplication.translate("mgeoWindow", "Options...", None, QtGui.QApplication.UnicodeUTF8))
        self.default_act.setText(QtGui.QApplication.translate("mgeoWindow", "Default", None, QtGui.QApplication.UnicodeUTF8))
        self.saveDefault_act.setText(QtGui.QApplication.translate("mgeoWindow", "Save as default", None, QtGui.QApplication.UnicodeUTF8))
        self.extReport_act.setText(QtGui.QApplication.translate("mgeoWindow", "Extended report", None, QtGui.QApplication.UnicodeUTF8))
        self.save_act.setText(QtGui.QApplication.translate("mgeoWindow", "Save settings...", None, QtGui.QApplication.UnicodeUTF8))
        self.load_act.setText(QtGui.QApplication.translate("mgeoWindow", "Load settinds...", None, QtGui.QApplication.UnicodeUTF8))
        self.isolateExported_act.setText(QtGui.QApplication.translate("mgeoWindow", "Isolate exported", None, QtGui.QApplication.UnicodeUTF8))
        self.colorInd_act.setText(QtGui.QApplication.translate("mgeoWindow", "Color indicators", None, QtGui.QApplication.UnicodeUTF8))
        self.showWarnings_act.setText(QtGui.QApplication.translate("mgeoWindow", "Show Warnings", None, QtGui.QApplication.UnicodeUTF8))
        self.save_preset_act.setText(QtGui.QApplication.translate("mgeoWindow", "Save New Preset...", None, QtGui.QApplication.UnicodeUTF8))
        self.preset_editor_act.setText(QtGui.QApplication.translate("mgeoWindow", "Preset Editor...", None, QtGui.QApplication.UnicodeUTF8))

