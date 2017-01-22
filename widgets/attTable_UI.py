# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Dropbox\Dropbox\pw_prefs\RnD\maya\python\Export\pw_mGeo\widgets\attTable.ui'
#
# Created: Sun Jul 06 22:54:37 2014
#      by: PyQt4 UI code generator 4.11
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 300)
        self.horizontalLayout = QtGui.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.tableLayout = QtGui.QVBoxLayout()
        self.tableLayout.setObjectName(_fromUtf8("tableLayout"))
        self.horizontalLayout.addLayout(self.tableLayout)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.addAttr_btn = QtGui.QPushButton(Form)
        self.addAttr_btn.setMaximumSize(QtCore.QSize(30, 16777215))
        self.addAttr_btn.setObjectName(_fromUtf8("addAttr_btn"))
        self.verticalLayout.addWidget(self.addAttr_btn)
        self.removeAttr_btn = QtGui.QPushButton(Form)
        self.removeAttr_btn.setMaximumSize(QtCore.QSize(30, 16777215))
        self.removeAttr_btn.setObjectName(_fromUtf8("removeAttr_btn"))
        self.verticalLayout.addWidget(self.removeAttr_btn)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout.setStretch(0, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.addAttr_btn.setText(_translate("Form", "+", None))
        self.removeAttr_btn.setText(_translate("Form", "-", None))

