# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Dropbox\Dropbox\pw_prefs\RnD\maya\python\Export\pw_mGeo\widgets\attTable.ui'
#
# Created: Sun Jul 06 23:20:49 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.horizontalLayout = QtGui.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tableLayout = QtGui.QVBoxLayout()
        self.tableLayout.setObjectName("tableLayout")
        self.horizontalLayout.addLayout(self.tableLayout)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.addAttr_btn = QtGui.QPushButton(Form)
        self.addAttr_btn.setMaximumSize(QtCore.QSize(30, 16777215))
        self.addAttr_btn.setObjectName("addAttr_btn")
        self.verticalLayout.addWidget(self.addAttr_btn)
        self.removeAttr_btn = QtGui.QPushButton(Form)
        self.removeAttr_btn.setMaximumSize(QtCore.QSize(30, 16777215))
        self.removeAttr_btn.setObjectName("removeAttr_btn")
        self.verticalLayout.addWidget(self.removeAttr_btn)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout.setStretch(0, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.addAttr_btn.setText(QtGui.QApplication.translate("Form", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.removeAttr_btn.setText(QtGui.QApplication.translate("Form", "-", None, QtGui.QApplication.UnicodeUTF8))

