# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pca.ui'
#
# Created: Mon Apr 06 16:07:40 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import numpy as np
import numpy
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
        Form.resize(229, 243)
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 201, 51))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(40, 20, 141, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 70, 201, 81))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(20, 20, 111, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.spinBox = QtGui.QSpinBox(self.groupBox_2)
        self.spinBox.setGeometry(QtCore.QRect(141, 20, 51, 22))
        self.spinBox.setMaximum(10000)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.spinBox_2 = QtGui.QSpinBox(self.groupBox_2)
        self.spinBox_2.setGeometry(QtCore.QRect(140, 50, 51, 22))
        self.spinBox_2.setMaximum(100000)
        self.spinBox_2.setObjectName(_fromUtf8("spinBox_2"))
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(19, 50, 111, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 200, 161, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(40, 170, 161, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.takeinput)
        self.fname=''
        self.pushButton_3.clicked.connect(self.startpca)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    def takeinput(self):
        self.fname = QtGui.QFileDialog.getOpenFileName(None, 'Open file', 'C:')
    
    def startpca(self):
        
        ##np.random.seed(23423842)
        ##mu_vec1 = np.array([0,0,2,2])
        ##cov_mat1 = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
        ##class1_sample = np.random.multivariate_normal(mu_vec1, cov_mat1, 20).T

        fname=str(self.fname)
        testdata=[]
        for line in open(str(fname)):
            row=line.split("\n")[0].split(",")
            testdata.append(row)
        #print self.testdata
        print "---test data taken successfully---"

        class1_sample=np.array(testdata).astype(np.float)
        print class1_sample

        from matplotlib import pyplot as plt
        from mpl_toolkits.mplot3d import Axes3D
        from mpl_toolkits.mplot3d import proj3d

        fig = plt.figure(figsize=(10,10))
        ax = fig.add_subplot(111, projection='3d')
        plt.rcParams['legend.fontsize'] = 10
        ax.plot(class1_sample[0,:], class1_sample[1,:],\
            class1_sample[2,:], 'o', markersize=8, color='blue', alpha=0.5, label='class1')

        plt.title('Samples for class 1 and class 2')
        ax.legend(loc='upper right')
        plt.show()


        all_samples = class1_sample
        print all_samples


        mean_x = np.mean(all_samples[0,:])
        mean_y = np.mean(all_samples[1,:])
        mean_z = np.mean(all_samples[2,:])
        mean_zz = np.mean(all_samples[3,:])

        print all_samples[0:]

        mean_vector = np.array([[mean_x],[mean_y],[mean_z],[mean_zz]])

        print('Mean Vector:\n', mean_vector)


        scatter_matrix = np.zeros((4,4))##add no of rows parameter hee
        for i in range(all_samples.shape[1]):
            scatter_matrix += (all_samples[:,i].reshape(4,1)- mean_vector).dot((all_samples[:,i].reshape(4,1) - mean_vector).T)##add no of rows parameter hee
        print('Scatter Matrix:\n', scatter_matrix)


        cov_mat = np.cov([all_samples[0,:],all_samples[1,:],all_samples[2,:],all_samples[3,:]])
        print('Covariance Matrix:\n', cov_mat)



        eig_val_sc, eig_vec_sc = np.linalg.eig(scatter_matrix)

        #eigenvectors and eigenvalues for the from the covariance matrix
        eig_val_cov, eig_vec_cov = np.linalg.eig(cov_mat)

        for i in range(len(eig_val_sc)):
            eigvec_sc = eig_vec_sc[:,i].reshape(1,4).T##add no of rows parameter hee
            eigvec_cov = eig_vec_cov[:,i].reshape(1,4).T##add no of rows parameter hee
            assert eigvec_sc.all() == eigvec_cov.all(), 'Eigenvectors are not identical'

            print('Eigenvector {}: \n{}'.format(i+1, eigvec_sc))
            print('Eigenvalue {} from scatter matrix: {}'.format(i+1, eig_val_sc[i]))
            print('Eigenvalue {} from covariance matrix: {}'.format(i+1, eig_val_cov[i]))
            print('Scaling factor: ', eig_val_sc[i]/eig_val_cov[i])
            print(40 * '-')


        for i in range(len(eig_val_sc)):
            eigv = eig_vec_sc[:,i].reshape(1,4).T##add no of rows parameter hee
            np.testing.assert_array_almost_equal(scatter_matrix.dot(eigv),\
                    eig_val_sc[i] * eigv, decimal=6,\
                    err_msg='', verbose=True)

        from matplotlib import pyplot as plt
        from mpl_toolkits.mplot3d import Axes3D
        from mpl_toolkits.mplot3d import proj3d
        from matplotlib.patches import FancyArrowPatch


        class Arrow3D(FancyArrowPatch):
            def __init__(self, xs, ys, zs, *args, **kwargs):
                FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **kwargs)
                self._verts3d = xs, ys, zs

            def draw(self, renderer):
                xs3d, ys3d, zs3d = self._verts3d
                xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
                self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
                FancyArrowPatch.draw(self, renderer)

        fig = plt.figure(figsize=(7,7))
        ax = fig.add_subplot(111, projection='3d')

        ax.plot(all_samples[0,:], all_samples[1,:],\
            all_samples[2,:], 'o', markersize=8, color='green', alpha=0.2)
        ax.plot([mean_x], [mean_y], [mean_z], 'o', \
            markersize=10, color='red', alpha=0.5)
        for v in eig_vec_sc.T:
            a = Arrow3D([mean_x, v[0]], [mean_y, v[1]],\
                [mean_z, v[2]], mutation_scale=20, lw=3, arrowstyle="-|>", color="r")
            ax.add_artist(a)
        ax.set_xlabel('x_values')
        ax.set_ylabel('y_values')
        ax.set_zlabel('z_values')

        plt.title('Eigenvectors')

        plt.show()
        for ev in eig_vec_sc:
            np.testing.assert_array_almost_equal(1.0, np.linalg.norm(ev))
            # instead of 'assert' because of rounding errors
        eig_pairs = [(np.abs(eig_val_sc[i]), eig_vec_sc[:,i]) for i in range(len(eig_val_sc))]

        # Sort the (eigenvalue, eigenvector) tuples from high to low
        eig_pairs.sort()
        eig_pairs.reverse()

         #Visually confirm that the list is correctly sorted by decreasing eigenvalues
        for i in eig_pairs:
            print(i[0])

        matrix_w = np.hstack((eig_pairs[0][1].reshape(4,1), eig_pairs[1][1].reshape(4,1)))##add no of rows parameter hee
        print('Matrix W:\n', matrix_w)


        transformed = matrix_w.T.dot(all_samples)
        ##assert transformed.shape == (2,4000), "The matrix is not 2x40 dimensional."
        fig1 = plt.figure(figsize=(7,7))
        #ax = fig1.add_subplot(111, projection='3d')

        plt.plot(transformed[0,0:20], transformed[1,0:20],\
             'o', markersize=7, color='blue', alpha=0.5, label='class1')

        plt.xlim([-4,4])
        plt.ylim([-4,4])
        plt.xlabel('x_values')
        plt.ylabel('y_values')
        plt.legend()
        plt.title('Transformed samples with class labels')

        plt.show()

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.groupBox.setTitle(_translate("Form", "Dimensionality Reduction", None))
        self.lineEdit.setText(_translate("Form", "PCA", None))
        self.groupBox_2.setTitle(_translate("Form", "Neighbors", None))
        self.label.setText(_translate("Form", "Number of features", None))
        self.label_2.setText(_translate("Form", "Number of records", None))
        self.pushButton_3.setText(_translate("Form", "Start", None))
        self.pushButton.setText(_translate("Form", "Input File", None))



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Form()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

                          
