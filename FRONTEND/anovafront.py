# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'anova.ui'
#
# Created: Sat Apr 11 09:33:51 2015
#      by: PyQt4 UI code generator 4.10.4
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
        Form.resize(238, 435)
        self.scale=0.4
        self.test="F"
        self.fname=""
        self.type=1
        self.robust="hc3"
        
        
        
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 221, 61))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        
        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(40, 20, 141, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))

        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 80, 221, 231))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))

        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(20, 20, 161, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        
        self.doubleSpinBox = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox.setGeometry(QtCore.QRect(120, 50, 62, 22))
        self.doubleSpinBox.setMaximum(999999.99)
        self.doubleSpinBox.setObjectName(_fromUtf8("doubleSpinBox"))
        self.doubleSpinBox.valueChanged.connect(self.setscale)

        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(50, 50, 46, 13))
        self.label.setObjectName(_fromUtf8("label"))

        self.comboBox = QtGui.QComboBox(self.groupBox_2)
        self.comboBox.setGeometry(QtCore.QRect(110, 80, 69, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.activated[str].connect(self.settest)

        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(40, 80, 46, 13))
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(40, 120, 46, 13))
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.comboBox_2 = QtGui.QComboBox(self.groupBox_2)
        self.comboBox_2.setGeometry(QtCore.QRect(110, 120, 69, 22))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.activated[str].connect(self.settype)

        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(40, 160, 46, 13))
        self.label_4.setObjectName(_fromUtf8("label_4"))

        self.comboBox_3 = QtGui.QComboBox(self.groupBox_2)
        self.comboBox_3.setGeometry(QtCore.QRect(110, 160, 69, 22))
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.activated[str].connect(self.sethc)

        self.checkBox = QtGui.QCheckBox(self.groupBox_2)
        self.checkBox.setGeometry(QtCore.QRect(50, 190, 131, 17))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))

        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 320, 161, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 360, 161, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_3.clicked.connect(self.startanova)
        self.pushButton_2.clicked.connect(self.takeinput)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def sethc(self,txt):
        self.robust=str(txt)
        print self.robust

    def settest(self,txt):
        self.test=str(txt)
        print self.test

    def settype(self,txt):
        self.type=int(txt)
        print self.type

    def setscale(self):
        self.scale=self.doubleSpinBox.value()
        print self.scale
    def takeinput(self):
        self.fname = QtGui.QFileDialog.getOpenFileName(None, 'Open file', 'C:')
        from urllib2 import urlopen
        import numpy as np
        import pandas
        import matplotlib.pyplot as plt
        from statsmodels.formula.api import ols
        from statsmodels.graphics.api import interaction_plot, abline_plot
        from statsmodels.stats.anova import anova_lm


        try:
             rehab_table = pandas.read_csv('rehab.table')
        except:
             url = 'http://stats191.stanford.edu/data/rehab.csv'
             #the next line is not necessary with recent version of pandas
             url = urlopen(url)
             rehab_table = pandas.read_table(url, delimiter=",")
             rehab_table.to_csv('rehab.table')

        print rehab_table

        plt.figure(figsize=(6, 6));
        rehab_table.boxplot('Time', 'Fitness', ax=plt.gca())
        rehab_lm = ols('Time ~ C(Fitness)', data=rehab_table).fit()
        table9 = anova_lm(rehab_lm,test=self.test,robust=self.robust)
        print table9
        print rehab_lm.model.data.orig_exog
        print rehab_lm.summary()
        plt.show()

        

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.groupBox.setTitle(_translate("Form", "Statistical estimator", None))
        self.lineEdit.setText(_translate("Form", "ANOVA", None))
        self.groupBox_2.setTitle(_translate("Form", "Options", None))
        self.pushButton.setText(_translate("Form", "Model equation file", None))
        self.label.setText(_translate("Form", "Scale", None))
        self.comboBox.setItemText(0, _translate("Form", "F", None))
        self.comboBox.setItemText(1, _translate("Form", "Cp", None))
        self.comboBox.setItemText(2, _translate("Form", "ChiSq", None))
        self.label_2.setText(_translate("Form", "Test", None))
        self.label_3.setText(_translate("Form", "Type", None))
        self.comboBox_2.setItemText(0, _translate("Form", "1", None))
        self.comboBox_2.setItemText(1, _translate("Form", "2", None))
        self.comboBox_2.setItemText(2, _translate("Form", "3", None))
        self.label_4.setText(_translate("Form", "Robust", None))
        self.comboBox_3.setItemText(0, _translate("Form", "Noene", None))
        self.comboBox_3.setItemText(1, _translate("Form", "hc0", None))
        self.comboBox_3.setItemText(2, _translate("Form", "hc1", None))
        self.comboBox_3.setItemText(3, _translate("Form", "hc2", None))
        self.comboBox_3.setItemText(4, _translate("Form", "hc3", None))
        self.checkBox.setText(_translate("Form", "                print to a file", None))
        self.pushButton_2.setText(_translate("Form", "Input File", None))
        self.pushButton_3.setText(_translate("Form", "Start", None))
    def startanova(self):
        from urllib2 import urlopen
        import numpy as np
        import pandas
        import matplotlib.pyplot as plt
        from statsmodels.formula.api import ols
        from statsmodels.graphics.api import interaction_plot, abline_plot
        from statsmodels.stats.anova import anova_lm


        try:
             rehab_table = pandas.read_csv('rehab.table')
        except:
             url = 'http://stats191.stanford.edu/data/rehab.csv'
             #the next line is not necessary with recent version of pandas
             url = urlopen(url)
             rehab_table = pandas.read_table(url, delimiter=",")
             rehab_table.to_csv('rehab.table')

        print rehab_table

        plt.figure(figsize=(6, 6));
        rehab_table.boxplot('Time', 'Fitness', ax=plt.gca())
        rehab_lm = ols('Time ~ C(Fitness)', data=rehab_table).fit()
        table9 = anova_lm(rehab_lm,test=self.test,robust=self.robust)
        print table9
        print rehab_lm.model.data.orig_exog
        print rehab_lm.summary()
        plt.show()
    


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Form()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
