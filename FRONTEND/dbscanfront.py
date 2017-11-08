# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dbscanui.ui'
#
# Created: Mon Apr 06 09:19:57 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import ddbscan

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
        Form.resize(250, 401)
        self.eps=2
        self.minpt=3
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(40, 300, 161, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 330, 161, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 360, 161, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))

        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 221, 61))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))

        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(40, 20, 141, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))

        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 80, 221, 81))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))

        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(30, 20, 111, 16))
        self.label.setObjectName(_fromUtf8("label"))

        self.spinBox = QtGui.QSpinBox(self.groupBox_2)
        self.spinBox.setGeometry(QtCore.QRect(150, 20, 42, 22))
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.spinBox.valueChanged.connect(self.seteps)

        self.spinBox_2 = QtGui.QSpinBox(self.groupBox_2)
        self.spinBox_2.setGeometry(QtCore.QRect(150, 50, 42, 22))
        self.spinBox_2.setObjectName(_fromUtf8("spinBox_2"))
        self.spinBox_2.valueChanged.connect(self.setminpts)

        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(30, 50, 111, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.groupBox_3 = QtGui.QGroupBox(Form)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 170, 221, 111))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))

        self.textEdit = QtGui.QTextEdit(self.groupBox_3)
        self.textEdit.setGeometry(QtCore.QRect(10, 20, 201, 81))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))

        self.pushButton.clicked.connect(self.takeinput)
        self.pushButton_3.clicked.connect(self.startdb)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
    def seteps(self):
        self.eps=self.spinBox.value()
        print self.eps
        
    def setminpts(self):
        self.minpts=self.spinBox_2.value()
        print self.minpts

    def startdb(self):
        scan = ddbscan.DDBSCAN(self.eps, self.minpts)

        # Add points to model
        data = self.traindata
        data=[[float(y) for y in x] for x in data]
        #data = [[1,  100], [2,  2], [1,  3], [2, 3], [3, 3], [8, 9],[7,  6], [9,  7], [6, 9], [6, 8], [5, 5], [7, 8],[10,10],[0.002,-0.4]]
        for point in data:
            print point
            scan.add_point(point=point, count=2, desc="")

        # Compute clusters
        scan.compute()

        print 'Clusters found and its members points index:'
        cluster_number = 0
        for cluster in scan.clusters:
            print '=== Cluster %d ===' % cluster_number
            print 'Cluster points index: %s' % list(cluster)
            cluster_number += 1

        print '\nCluster assigned to each point:'
        for i in xrange(len(scan.points)):
            print '=== Point: %s ===' % scan.points[i]
            print 'Cluster: %2d' % scan.points_data[i].cluster,
            # If a point cluster is -1, it's an anomaly
            if scan.points_data[i].cluster == -1:
                print '\t <== Anomaly found!'
            else:
                print

        # Print ASCII plot
        print
        print ' ===== Data plot ====='
        print
        print 'Legend => x: anomaly'

        symbols = 'x#=~+-opwbcnkjhf@uyt()987654321asdfghjklpoiuytrewqzxcvbnm0)(*&^' # Symbols used to plot points
        cluster_number = 0
        for cluster in scan.clusters:
            print '          %s: cluster %d' % (symbols[cluster_number + 1], cluster_number)
            cluster_number += 1
        print

        print '-----------------------'
        for x in range(0,10):
            print '|',
            for y in range(0, 10):
                if [x, y] in data:
                    index = data.index([x,y])
                    cluster = scan.points_data[index].cluster + 1
                    #print cluster
                    print symbols[cluster],
                else:
                    print ' ',
            print '|'
        print '-----------------------'

        print "started"

    def takeinput(self):
        fname = QtGui.QFileDialog.getOpenFileName(None, 'Open file', 'C:')
        self.traindata=[]
        self.trainclass=[]
        for line in open(str(fname)):
            row=line.split("\n")[0].split(",")
            self.traindata.append(row)
            #print (self.trainclass)
        #print self.traindata
        print "-----training complete ----"
    

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButton.setText(_translate("Form", "Input File", None))
        self.pushButton_2.setText(_translate("Form", "Output Folder", None))
        self.pushButton_3.setText(_translate("Form", "Start", None))
        self.groupBox.setTitle(_translate("Form", "Classifier Name", None))
        self.lineEdit.setText(_translate("Form", "Dbscan", None))
        self.groupBox_2.setTitle(_translate("Form", "Parameters", None))
        self.label.setText(_translate("Form", "Eps", None))
        self.label_2.setText(_translate("Form", "Min points in cluster", None))
        self.groupBox_3.setTitle(_translate("Form", "output/Result", None))

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Form()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


