# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'attTable.ui'
#
# Created: Sun Jan 22 13:05:13 2017
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tableLayout = QtWidgets.QVBoxLayout()
        self.tableLayout.setObjectName("tableLayout")
        self.horizontalLayout.addLayout(self.tableLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.addAttr_btn = QtWidgets.QPushButton(Form)
        self.addAttr_btn.setMaximumSize(QtCore.QSize(30, 16777215))
        self.addAttr_btn.setObjectName("addAttr_btn")
        self.verticalLayout.addWidget(self.addAttr_btn)
        self.removeAttr_btn = QtWidgets.QPushButton(Form)
        self.removeAttr_btn.setMaximumSize(QtCore.QSize(30, 16777215))
        self.removeAttr_btn.setObjectName("removeAttr_btn")
        self.verticalLayout.addWidget(self.removeAttr_btn)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout.setStretch(0, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.addAttr_btn.setText(QtWidgets.QApplication.translate("Form", "+", None, -1))
        self.removeAttr_btn.setText(QtWidgets.QApplication.translate("Form", "-", None, -1))

