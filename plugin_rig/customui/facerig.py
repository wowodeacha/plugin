# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'facerig.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_faceUI_Form(object):
    def setupUi(self, faceUI_Form):
        faceUI_Form.setObjectName(_fromUtf8("faceUI_Form"))
        faceUI_Form.resize(463, 534)
        faceUI_Form.setStyleSheet(_fromUtf8("background-color: rgb(71, 71, 71);"))
        self.gridLayout = QtGui.QGridLayout(faceUI_Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(faceUI_Form)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setStyleSheet(_fromUtf8("background-color: rgb(55, 56, 62);\n"
"color: rgb(255, 255, 255);"))
        self.tabWidget.setTabPosition(QtGui.QTabWidget.West)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tabWidgetPage1 = QtGui.QWidget()
        self.tabWidgetPage1.setObjectName(_fromUtf8("tabWidgetPage1"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tabWidgetPage1)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.groupBox_2 = QtGui.QGroupBox(self.tabWidgetPage1)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_5 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.rebulidAllBone_pushButton = QtGui.QPushButton(self.groupBox_2)
        self.rebulidAllBone_pushButton.setStyleSheet(_fromUtf8("background-color: rgb(138, 141, 156);"))
        self.rebulidAllBone_pushButton.setObjectName(_fromUtf8("rebulidAllBone_pushButton"))
        self.gridLayout_5.addWidget(self.rebulidAllBone_pushButton, 2, 0, 1, 1)
        self.gridLayout_18 = QtGui.QGridLayout()
        self.gridLayout_18.setObjectName(_fromUtf8("gridLayout_18"))
        self.scrollArea = QtGui.QScrollArea(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 359, 221))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout_3 = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.toolBox = QtGui.QToolBox(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBox.sizePolicy().hasHeightForWidth())
        self.toolBox.setSizePolicy(sizePolicy)
        self.toolBox.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.toolBox.setAcceptDrops(True)
        self.toolBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toolBox.setAutoFillBackground(False)
        self.toolBox.setStyleSheet(_fromUtf8("background-color: rgb(179, 183, 202);\n"
""))
        self.toolBox.setFrameShape(QtGui.QFrame.Panel)
        self.toolBox.setFrameShadow(QtGui.QFrame.Plain)
        self.toolBox.setObjectName(_fromUtf8("toolBox"))
        self.page_4 = QtGui.QWidget()
        self.page_4.setGeometry(QtCore.QRect(0, 0, 339, 69))
        self.page_4.setObjectName(_fromUtf8("page_4"))
        self.gridLayout_4 = QtGui.QGridLayout(self.page_4)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.checkBox_9 = QtGui.QCheckBox(self.page_4)
        self.checkBox_9.setText(_fromUtf8(""))
        self.checkBox_9.setChecked(True)
        self.checkBox_9.setObjectName(_fromUtf8("checkBox_9"))
        self.verticalLayout_7.addWidget(self.checkBox_9)
        self.importForeHeadBone_pushButton_15 = QtGui.QPushButton(self.page_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.importForeHeadBone_pushButton_15.sizePolicy().hasHeightForWidth())
        self.importForeHeadBone_pushButton_15.setSizePolicy(sizePolicy)
        self.importForeHeadBone_pushButton_15.setStyleSheet(_fromUtf8("background-color: rgba(46, 76, 113, 247);"))
        self.importForeHeadBone_pushButton_15.setObjectName(_fromUtf8("importForeHeadBone_pushButton_15"))
        self.verticalLayout_7.addWidget(self.importForeHeadBone_pushButton_15)
        self.gridLayout_4.addLayout(self.verticalLayout_7, 0, 0, 1, 1)
        self.toolBox.addItem(self.page_4, _fromUtf8(""))
        self.page_5 = QtGui.QWidget()
        self.page_5.setGeometry(QtCore.QRect(0, 0, 339, 69))
        self.page_5.setObjectName(_fromUtf8("page_5"))
        self.gridLayout_7 = QtGui.QGridLayout(self.page_5)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.splitter_2 = QtGui.QSplitter(self.page_5)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.layoutWidget_2 = QtGui.QWidget(self.splitter_2)
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.checkBox_3 = QtGui.QCheckBox(self.layoutWidget_2)
        self.checkBox_3.setText(_fromUtf8(""))
        self.checkBox_3.setChecked(True)
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.verticalLayout_2.addWidget(self.checkBox_3)
        self.importForeHeadBone_pushButton_9 = QtGui.QPushButton(self.layoutWidget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.importForeHeadBone_pushButton_9.sizePolicy().hasHeightForWidth())
        self.importForeHeadBone_pushButton_9.setSizePolicy(sizePolicy)
        self.importForeHeadBone_pushButton_9.setStyleSheet(_fromUtf8("background-color: rgba(46, 76, 113, 247);"))
        self.importForeHeadBone_pushButton_9.setObjectName(_fromUtf8("importForeHeadBone_pushButton_9"))
        self.verticalLayout_2.addWidget(self.importForeHeadBone_pushButton_9)
        self.gridLayout_7.addWidget(self.splitter_2, 0, 0, 1, 1)
        self.toolBox.addItem(self.page_5, _fromUtf8(""))
        self.page_6 = QtGui.QWidget()
        self.page_6.setGeometry(QtCore.QRect(0, 0, 339, 69))
        self.page_6.setObjectName(_fromUtf8("page_6"))
        self.gridLayout_8 = QtGui.QGridLayout(self.page_6)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.splitter_3 = QtGui.QSplitter(self.page_6)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName(_fromUtf8("splitter_3"))
        self.layoutWidget_4 = QtGui.QWidget(self.splitter_3)
        self.layoutWidget_4.setObjectName(_fromUtf8("layoutWidget_4"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.checkBox_5 = QtGui.QCheckBox(self.layoutWidget_4)
        self.checkBox_5.setText(_fromUtf8(""))
        self.checkBox_5.setChecked(True)
        self.checkBox_5.setObjectName(_fromUtf8("checkBox_5"))
        self.verticalLayout_3.addWidget(self.checkBox_5)
        self.importForeHeadBone_pushButton_11 = QtGui.QPushButton(self.layoutWidget_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.importForeHeadBone_pushButton_11.sizePolicy().hasHeightForWidth())
        self.importForeHeadBone_pushButton_11.setSizePolicy(sizePolicy)
        self.importForeHeadBone_pushButton_11.setStyleSheet(_fromUtf8("background-color: rgba(46, 76, 113, 247);"))
        self.importForeHeadBone_pushButton_11.setObjectName(_fromUtf8("importForeHeadBone_pushButton_11"))
        self.verticalLayout_3.addWidget(self.importForeHeadBone_pushButton_11)
        self.gridLayout_8.addWidget(self.splitter_3, 0, 0, 1, 1)
        self.toolBox.addItem(self.page_6, _fromUtf8(""))
        self.page_7 = QtGui.QWidget()
        self.page_7.setGeometry(QtCore.QRect(0, 0, 339, 69))
        self.page_7.setObjectName(_fromUtf8("page_7"))
        self.gridLayout_9 = QtGui.QGridLayout(self.page_7)
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.splitter_4 = QtGui.QSplitter(self.page_7)
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName(_fromUtf8("splitter_4"))
        self.layoutWidget_3 = QtGui.QWidget(self.splitter_4)
        self.layoutWidget_3.setObjectName(_fromUtf8("layoutWidget_3"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.checkBox_4 = QtGui.QCheckBox(self.layoutWidget_3)
        self.checkBox_4.setText(_fromUtf8(""))
        self.checkBox_4.setChecked(True)
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))
        self.verticalLayout_4.addWidget(self.checkBox_4)
        self.importForeHeadBone_pushButton_10 = QtGui.QPushButton(self.layoutWidget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.importForeHeadBone_pushButton_10.sizePolicy().hasHeightForWidth())
        self.importForeHeadBone_pushButton_10.setSizePolicy(sizePolicy)
        self.importForeHeadBone_pushButton_10.setStyleSheet(_fromUtf8("background-color: rgba(46, 76, 113, 247);"))
        self.importForeHeadBone_pushButton_10.setObjectName(_fromUtf8("importForeHeadBone_pushButton_10"))
        self.verticalLayout_4.addWidget(self.importForeHeadBone_pushButton_10)
        self.gridLayout_9.addWidget(self.splitter_4, 0, 0, 1, 1)
        self.toolBox.addItem(self.page_7, _fromUtf8(""))
        self.page_8 = QtGui.QWidget()
        self.page_8.setGeometry(QtCore.QRect(0, 0, 339, 69))
        self.page_8.setObjectName(_fromUtf8("page_8"))
        self.gridLayout_10 = QtGui.QGridLayout(self.page_8)
        self.gridLayout_10.setObjectName(_fromUtf8("gridLayout_10"))
        self.splitter_5 = QtGui.QSplitter(self.page_8)
        self.splitter_5.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_5.setObjectName(_fromUtf8("splitter_5"))
        self.layoutWidget_5 = QtGui.QWidget(self.splitter_5)
        self.layoutWidget_5.setObjectName(_fromUtf8("layoutWidget_5"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.layoutWidget_5)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.checkBox_6 = QtGui.QCheckBox(self.layoutWidget_5)
        self.checkBox_6.setText(_fromUtf8(""))
        self.checkBox_6.setChecked(True)
        self.checkBox_6.setObjectName(_fromUtf8("checkBox_6"))
        self.verticalLayout_5.addWidget(self.checkBox_6)
        self.importForeHeadBone_pushButton_12 = QtGui.QPushButton(self.layoutWidget_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.importForeHeadBone_pushButton_12.sizePolicy().hasHeightForWidth())
        self.importForeHeadBone_pushButton_12.setSizePolicy(sizePolicy)
        self.importForeHeadBone_pushButton_12.setStyleSheet(_fromUtf8("background-color: rgba(46, 76, 113, 247);"))
        self.importForeHeadBone_pushButton_12.setObjectName(_fromUtf8("importForeHeadBone_pushButton_12"))
        self.verticalLayout_5.addWidget(self.importForeHeadBone_pushButton_12)
        self.gridLayout_10.addWidget(self.splitter_5, 0, 0, 1, 1)
        self.toolBox.addItem(self.page_8, _fromUtf8(""))
        self.page_9 = QtGui.QWidget()
        self.page_9.setGeometry(QtCore.QRect(0, 0, 339, 69))
        self.page_9.setObjectName(_fromUtf8("page_9"))
        self.gridLayout_11 = QtGui.QGridLayout(self.page_9)
        self.gridLayout_11.setObjectName(_fromUtf8("gridLayout_11"))
        self.splitter_6 = QtGui.QSplitter(self.page_9)
        self.splitter_6.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_6.setObjectName(_fromUtf8("splitter_6"))
        self.layoutWidget_6 = QtGui.QWidget(self.splitter_6)
        self.layoutWidget_6.setObjectName(_fromUtf8("layoutWidget_6"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.layoutWidget_6)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.checkBox_7 = QtGui.QCheckBox(self.layoutWidget_6)
        self.checkBox_7.setText(_fromUtf8(""))
        self.checkBox_7.setChecked(True)
        self.checkBox_7.setObjectName(_fromUtf8("checkBox_7"))
        self.verticalLayout_6.addWidget(self.checkBox_7)
        self.importForeHeadBone_pushButton_13 = QtGui.QPushButton(self.layoutWidget_6)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.importForeHeadBone_pushButton_13.sizePolicy().hasHeightForWidth())
        self.importForeHeadBone_pushButton_13.setSizePolicy(sizePolicy)
        self.importForeHeadBone_pushButton_13.setStyleSheet(_fromUtf8("background-color: rgba(46, 76, 113, 247);"))
        self.importForeHeadBone_pushButton_13.setObjectName(_fromUtf8("importForeHeadBone_pushButton_13"))
        self.verticalLayout_6.addWidget(self.importForeHeadBone_pushButton_13)
        self.gridLayout_11.addWidget(self.splitter_6, 0, 0, 1, 1)
        self.toolBox.addItem(self.page_9, _fromUtf8(""))
        self.gridLayout_3.addWidget(self.toolBox, 1, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_18.addWidget(self.scrollArea, 5, 0, 1, 1)
        self.listWidget = QtGui.QListWidget(self.groupBox_2)
        self.listWidget.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.gridLayout_18.addWidget(self.listWidget, 1, 0, 1, 1)
        self.setheadmesh_pushButton = QtGui.QPushButton(self.groupBox_2)
        self.setheadmesh_pushButton.setStyleSheet(_fromUtf8("background-color: rgb(138, 141, 156);"))
        self.setheadmesh_pushButton.setObjectName(_fromUtf8("setheadmesh_pushButton"))
        self.gridLayout_18.addWidget(self.setheadmesh_pushButton, 3, 0, 1, 1)
        self.splitter_7 = QtGui.QSplitter(self.groupBox_2)
        self.splitter_7.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_7.setObjectName(_fromUtf8("splitter_7"))
        self.label_3 = QtGui.QLabel(self.splitter_7)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit = QtGui.QLineEdit(self.splitter_7)
        self.lineEdit.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout_18.addWidget(self.splitter_7, 2, 0, 1, 1)
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setStyleSheet(_fromUtf8("background-color: rgb(75, 78, 99);"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout_18.addWidget(self.pushButton, 0, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_18, 0, 0, 1, 1)
        self.snapForeHeadMeshToHeadMesh_pushButton = QtGui.QPushButton(self.groupBox_2)
        self.snapForeHeadMeshToHeadMesh_pushButton.setStyleSheet(_fromUtf8("background-color: rgb(138, 141, 156);"))
        self.snapForeHeadMeshToHeadMesh_pushButton.setObjectName(_fromUtf8("snapForeHeadMeshToHeadMesh_pushButton"))
        self.gridLayout_5.addWidget(self.snapForeHeadMeshToHeadMesh_pushButton, 3, 0, 1, 1)
        self.importForeHeadBone_pushButton = QtGui.QPushButton(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.importForeHeadBone_pushButton.sizePolicy().hasHeightForWidth())
        self.importForeHeadBone_pushButton.setSizePolicy(sizePolicy)
        self.importForeHeadBone_pushButton.setStyleSheet(_fromUtf8("background-color: rgb(138, 141, 156);"))
        self.importForeHeadBone_pushButton.setObjectName(_fromUtf8("importForeHeadBone_pushButton"))
        self.gridLayout_5.addWidget(self.importForeHeadBone_pushButton, 1, 0, 1, 1)
        self.splitter = QtGui.QSplitter(self.groupBox_2)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.bneMir_pushButton = QtGui.QPushButton(self.splitter)
        self.bneMir_pushButton.setStyleSheet(_fromUtf8("background-color: rgb(138, 141, 156);"))
        self.bneMir_pushButton.setObjectName(_fromUtf8("bneMir_pushButton"))
        self.bneMir_pushButton_2 = QtGui.QPushButton(self.splitter)
        self.bneMir_pushButton_2.setStyleSheet(_fromUtf8("background-color: rgb(138, 141, 156);"))
        self.bneMir_pushButton_2.setObjectName(_fromUtf8("bneMir_pushButton_2"))
        self.gridLayout_5.addWidget(self.splitter, 4, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_2, 2, 0, 1, 1)
        self.tabWidget.addTab(self.tabWidgetPage1, _fromUtf8(""))
        self.tabWidgetPage2 = QtGui.QWidget()
        self.tabWidgetPage2.setObjectName(_fromUtf8("tabWidgetPage2"))
        self.pushButton_2 = QtGui.QPushButton(self.tabWidgetPage2)
        self.pushButton_2.setGeometry(QtCore.QRect(410, 30, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.tabWidgetPage2)
        self.pushButton_3.setGeometry(QtCore.QRect(80, 460, 75, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.tabWidget.addTab(self.tabWidgetPage2, _fromUtf8(""))
        self.tabWidgetPage3 = QtGui.QWidget()
        self.tabWidgetPage3.setObjectName(_fromUtf8("tabWidgetPage3"))
        self.groupBox_3 = QtGui.QGroupBox(self.tabWidgetPage3)
        self.groupBox_3.setGeometry(QtCore.QRect(40, 30, 301, 371))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.tabWidget.addTab(self.tabWidgetPage3, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        self.line = QtGui.QFrame(faceUI_Form)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(faceUI_Form)
        self.tabWidget.setCurrentIndex(0)
        self.toolBox.setCurrentIndex(2)
        self.toolBox.layout().setSpacing(2)
        QtCore.QMetaObject.connectSlotsByName(faceUI_Form)

    def retranslateUi(self, faceUI_Form):
        faceUI_Form.setWindowTitle(_translate("faceUI_Form", "faceUI_Win", None))
        self.groupBox_2.setTitle(_translate("faceUI_Form", "Jnt_Import", None))
        self.rebulidAllBone_pushButton.setText(_translate("faceUI_Form", "重置所有骨骼", None))
        self.importForeHeadBone_pushButton_15.setText(_translate("faceUI_Form", "导入基础骨骼", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), _translate("faceUI_Form", "ForeHead_Create", None))
        self.importForeHeadBone_pushButton_9.setText(_translate("faceUI_Form", "导入基础骨骼", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_5), _translate("faceUI_Form", "Brow_Create", None))
        self.importForeHeadBone_pushButton_11.setText(_translate("faceUI_Form", "导入基础骨骼", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_6), _translate("faceUI_Form", "Eye_Create", None))
        self.importForeHeadBone_pushButton_10.setText(_translate("faceUI_Form", "导入基础骨骼", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_7), _translate("faceUI_Form", "Check_Create", None))
        self.importForeHeadBone_pushButton_12.setText(_translate("faceUI_Form", "导入基础骨骼", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_8), _translate("faceUI_Form", "Nose_Create", None))
        self.importForeHeadBone_pushButton_13.setText(_translate("faceUI_Form", "导入基础骨骼", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_9), _translate("faceUI_Form", "Mouth_Create", None))
        self.setheadmesh_pushButton.setText(_translate("faceUI_Form", "设置面部模型", None))
        self.label_3.setText(_translate("faceUI_Form", "当前面部模型：", None))
        self.pushButton.setText(_translate("faceUI_Form", "载入模型列表", None))
        self.snapForeHeadMeshToHeadMesh_pushButton.setText(_translate("faceUI_Form", "吸附模型", None))
        self.importForeHeadBone_pushButton.setText(_translate("faceUI_Form", "导入基础骨骼", None))
        self.bneMir_pushButton.setText(_translate("faceUI_Form", "L>TO>R镜像", None))
        self.bneMir_pushButton_2.setText(_translate("faceUI_Form", "R>TO>L镜像", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage1), _translate("faceUI_Form", "导入骨骼", None))
        self.pushButton_2.setText(_translate("faceUI_Form", "LoadMesh", None))
        self.pushButton_3.setText(_translate("faceUI_Form", "Rigging", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage2), _translate("faceUI_Form", "绑定", None))
        self.groupBox_3.setTitle(_translate("faceUI_Form", "BlendShape", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage3), _translate("faceUI_Form", "修形", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    faceUI_Form = QtGui.QWidget()
    ui = Ui_faceUI_Form()
    ui.setupUi(faceUI_Form)
    faceUI_Form.show()
    sys.exit(app.exec_())

