# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ethan/Documents/github/HWI/Marco_Polo/pyqt_designer/run_updater_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_runUpdater(object):
    def setupUi(self, runUpdater):
        runUpdater.setObjectName("runUpdater")
        runUpdater.resize(286, 515)
        self.gridLayout_4 = QtWidgets.QGridLayout(runUpdater)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.groupBox = QtWidgets.QGroupBox(runUpdater)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 1, 0, 1, 2)
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout.addWidget(self.radioButton, 2, 0, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout.addWidget(self.radioButton_2, 2, 1, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox, 0, 0, 1, 2)
        self.groupBox_2 = QtWidgets.QGroupBox(runUpdater)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.dateEdit = QtWidgets.QDateEdit(self.groupBox_2)
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout_2.addWidget(self.dateEdit, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_2.setObjectName("comboBox_2")
        self.gridLayout_2.addWidget(self.comboBox_2, 3, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_2, 1, 0, 1, 2)
        self.groupBox_3 = QtWidgets.QGroupBox(runUpdater)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_3.addWidget(self.lineEdit_2, 1, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_3, 2, 0, 1, 2)
        self.pushButton_2 = QtWidgets.QPushButton(runUpdater)
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_4.addWidget(self.pushButton_2, 3, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(runUpdater)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(True)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_4.addWidget(self.pushButton, 3, 1, 1, 1)

        self.retranslateUi(runUpdater)
        QtCore.QMetaObject.connectSlotsByName(runUpdater)

    def retranslateUi(self, runUpdater):
        _translate = QtCore.QCoreApplication.translate
        runUpdater.setWindowTitle(_translate("runUpdater", "Update Run"))
        self.groupBox.setToolTip(_translate("runUpdater", "Change the cocktail menu assigned to this run."))
        self.groupBox.setTitle(_translate("runUpdater", "Cocktail Selection"))
        self.label_3.setText(_translate("runUpdater", "Cocktail Menu"))
        self.radioButton.setText(_translate("runUpdater", "Soluble"))
        self.radioButton_2.setText(_translate("runUpdater", "Membrane"))
        self.groupBox_2.setTitle(_translate("runUpdater", "Image Data"))
        self.label_2.setText(_translate("runUpdater", "Imaging Date"))
        self.dateEdit.setToolTip(_translate("runUpdater", "Change the imaging date assigned to this run."))
        self.label_4.setText(_translate("runUpdater", "Image Spectrum"))
        self.comboBox_2.setToolTip(_translate("runUpdater", "Change the image spectrum assigned to this run."))
        self.groupBox_3.setTitle(_translate("runUpdater", "Run Labels"))
        self.label_5.setText(_translate("runUpdater", "Plate ID"))
        self.lineEdit_2.setToolTip(_translate("runUpdater", "Change the plate ID assigned to this run."))
        self.pushButton_2.setToolTip(_translate("runUpdater", "Discard your updates, if any."))
        self.pushButton_2.setText(_translate("runUpdater", "Cancel"))
        self.pushButton.setToolTip(_translate("runUpdater", "Submit your updates, if any."))
        self.pushButton.setText(_translate("runUpdater", "Update Run"))
