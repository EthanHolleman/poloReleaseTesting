# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ethan/Documents/github/HWI/Marco_Polo/pyqt_designer/multi_run_importer.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_multiImporter(object):
    def setupUi(self, multiImporter):
        multiImporter.setObjectName("multiImporter")
        multiImporter.resize(702, 515)
        self.gridLayout_2 = QtWidgets.QGridLayout(multiImporter)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox = QtWidgets.QGroupBox(multiImporter)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.listWidget = QtWidgets.QListWidget(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.listWidget.setFont(font)
        self.listWidget.setAlternatingRowColors(True)
        self.listWidget.setMovement(QtWidgets.QListView.Free)
        self.listWidget.setResizeMode(QtWidgets.QListView.Adjust)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout_3.addWidget(self.listWidget, 0, 0, 1, 2)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 2)
        self.groupBox_4 = QtWidgets.QGroupBox(multiImporter)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_4.addWidget(self.pushButton_4, 0, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_4.addWidget(self.pushButton_5, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_4, 1, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(multiImporter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.label_13 = QtWidgets.QLabel(self.groupBox_2)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 3, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.groupBox_2)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 0, 4, 1, 1)
        self.radioButton = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout.addWidget(self.radioButton, 1, 0, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout.addWidget(self.radioButton_2, 1, 1, 1, 2)
        self.comboBox_3 = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_3.setObjectName("comboBox_3")
        self.gridLayout.addWidget(self.comboBox_3, 1, 3, 1, 1)
        self.dateEdit_2 = QtWidgets.QDateEdit(self.groupBox_2)
        self.dateEdit_2.setCalendarPopup(True)
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.gridLayout.addWidget(self.dateEdit_2, 1, 4, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 2)
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout.addWidget(self.comboBox_2, 3, 0, 1, 2)
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 3, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 3, 3, 1, 2)
        self.gridLayout_2.addWidget(self.groupBox_2, 1, 1, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(multiImporter)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton.setDefault(True)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.gridLayout_2.addWidget(self.groupBox_3, 2, 0, 1, 2)

        self.retranslateUi(multiImporter)
        QtCore.QMetaObject.connectSlotsByName(multiImporter)

    def retranslateUi(self, multiImporter):
        _translate = QtCore.QCoreApplication.translate
        multiImporter.setWindowTitle(_translate("multiImporter", "Run Importer"))
        self.groupBox.setTitle(_translate("multiImporter", "Selected Paths"))
        self.listWidget.setToolTip(_translate("multiImporter", "<html><head/><body><p>Potential imports will be shown here. Selecting a potential import will display the metadata Polo as infered in the <span style=\" font-style:italic;\">Adjust Default Values </span>box.</p></body></html>"))
        self.groupBox_4.setToolTip(_translate("multiImporter", "<html><head/><body><p>Browse for rar archives or uncompressed directories of images to import into Polo.</p><p><span style=\" font-weight:600;\">Note</span>: If you are an HWI user it is important to maintain the integrity of your image data. Polo uses the metadata files and folder/file names to infer important information about your screening images. </p><p><span style=\" font-weight:600;\">IT IS THEREFORE NOT RECOMMENDED TO RENAME OR EDIT ANY FILES DOWNLOADED FROM THE HWI SERVER.</span></p></body></html>"))
        self.groupBox_4.setTitle(_translate("multiImporter", "Browse"))
        self.pushButton_4.setToolTip(_translate("multiImporter", "<html><head/><body><p>Browse your computer for rar archives to import into Polo.</p></body></html>"))
        self.pushButton_4.setText(_translate("multiImporter", "Browse For Rar"))
        self.pushButton_5.setToolTip(_translate("multiImporter", "<html><head/><body><p>Browse your computer for uncompressed directories (folders) of images to import.</p></body></html>"))
        self.pushButton_5.setText(_translate("multiImporter", "Browse For Folder"))
        self.groupBox_2.setTitle(_translate("multiImporter", "Adjust Default Values"))
        self.label_13.setText(_translate("multiImporter", "Screen Type"))
        self.label_5.setText(_translate("multiImporter", "Cocktail File"))
        self.label_14.setText(_translate("multiImporter", "Imaging Date"))
        self.radioButton.setText(_translate("multiImporter", "Membrane"))
        self.radioButton_2.setText(_translate("multiImporter", "Soluble"))
        self.label_4.setText(_translate("multiImporter", "Imaging Spectrum"))
        self.comboBox_2.setItemText(0, _translate("multiImporter", "Visible"))
        self.comboBox_2.setItemText(1, _translate("multiImporter", "UV-TPEF"))
        self.comboBox_2.setItemText(2, _translate("multiImporter", "SHG"))
        self.label_7.setText(_translate("multiImporter", "Run Name"))
        self.groupBox_3.setTitle(_translate("multiImporter", "Controls"))
        self.pushButton_2.setToolTip(_translate("multiImporter", "<html><head/><body><p>Remove the currently selected import.</p></body></html>"))
        self.pushButton_2.setText(_translate("multiImporter", "Remove Selected Run"))
        self.pushButton.setToolTip(_translate("multiImporter", "<html><head/><body><p>Attempt to import all paths listed in the <span style=\" font-style:italic;\">Selected Paths</span> box.</p></body></html>"))
        self.pushButton.setText(_translate("multiImporter", "Import Runs"))
