# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fullfactorial.ui'
#
# Created: Wed Apr 08 07:09:29 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import numpy as np
from doe import *
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
        Form.resize(240, 182)
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 221, 61))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(40, 20, 141, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 140, 161, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_3.clicked.connect(self.startfull)
        
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 110, 161, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        #self.pushButton_2.clicked.connect(self.startknn)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(40, 80, 161, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.takeinput)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.groupBox.setTitle(_translate("Form", "DOE Name", None))
        self.lineEdit.setText(_translate("Form", "Full Factorial", None))
        self.pushButton_3.setText(_translate("Form", "Start", None))
        self.pushButton_2.setText(_translate("Form", "Output Folder", None))
        self.pushButton.setText(_translate("Form", "Input Levels  File", None))

    def takeinput(self):
        fname = QtGui.QFileDialog.getOpenFileName(None, 'Open file', 'C:')
        self.testdata=[]
        for line in open(str(fname)):
            row=line.split("\n")[0].split(",")
            self.testdata.append(row)
        self.testdata=np.array(self.testdata).astype(np.int)      
        print "---test data taken successfully---"
    def startfull(self):
        for i in self.testdata:
            print i
            print OSOEST_fullfact(i)
        print "started---"
        
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Form()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
    
