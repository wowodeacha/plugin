# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Texture_Replace_UI.ui'
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

class Ui_Material_Form(object):
    def setupUi(self, Material_Form):
        Material_Form.setObjectName(_fromUtf8("Material_Form"))
        Material_Form.resize(485, 590)
        self.gridLayout = QtGui.QGridLayout(Material_Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.SGJson_lineEdit = QtGui.QLineEdit(Material_Form)
        self.SGJson_lineEdit.setObjectName(_fromUtf8("SGJson_lineEdit"))
        self.horizontalLayout_2.addWidget(self.SGJson_lineEdit)
        self.getCurrentPath_pushButton = QtGui.QPushButton(Material_Form)
        self.getCurrentPath_pushButton.setObjectName(_fromUtf8("getCurrentPath_pushButton"))
        self.horizontalLayout_2.addWidget(self.getCurrentPath_pushButton)
        self.selectFileDir_pushButton = QtGui.QPushButton(Material_Form)
        self.selectFileDir_pushButton.setObjectName(_fromUtf8("selectFileDir_pushButton"))
        self.horizontalLayout_2.addWidget(self.selectFileDir_pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.SGJson_comboBox = QtGui.QComboBox(Material_Form)
        self.SGJson_comboBox.setMaximumSize(QtCore.QSize(16777215, 20))
        self.SGJson_comboBox.setIconSize(QtCore.QSize(16, 20))
        self.SGJson_comboBox.setObjectName(_fromUtf8("SGJson_comboBox"))
        self.gridLayout_2.addWidget(self.SGJson_comboBox, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 15, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 2, 1, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.method_checkBox = QtGui.QCheckBox(Material_Form)
        self.method_checkBox.setObjectName(_fromUtf8("method_checkBox"))
        self.horizontalLayout_4.addWidget(self.method_checkBox)
        self.LoadMesh_pushButton = QtGui.QPushButton(Material_Form)
        self.LoadMesh_pushButton.setObjectName(_fromUtf8("LoadMesh_pushButton"))
        self.horizontalLayout_4.addWidget(self.LoadMesh_pushButton)
        self.outPut_pushButton = QtGui.QPushButton(Material_Form)
        self.outPut_pushButton.setObjectName(_fromUtf8("outPut_pushButton"))
        self.horizontalLayout_4.addWidget(self.outPut_pushButton)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 3, 2, 1, 1)
        self.LoadJson_pushButton = QtGui.QPushButton(Material_Form)
        self.LoadJson_pushButton.setObjectName(_fromUtf8("LoadJson_pushButton"))
        self.gridLayout_2.addWidget(self.LoadJson_pushButton, 3, 0, 1, 1)
        self.matJson_label = QtGui.QLabel(Material_Form)
        self.matJson_label.setStyleSheet(_fromUtf8("background-color: rgb(230, 248, 255);\n"
"color: rgb(0, 0, 0);"))
        self.matJson_label.setAlignment(QtCore.Qt.AlignCenter)
        self.matJson_label.setObjectName(_fromUtf8("matJson_label"))
        self.gridLayout_2.addWidget(self.matJson_label, 1, 0, 1, 1)
        self.modelList_label = QtGui.QLabel(Material_Form)
        self.modelList_label.setStyleSheet(_fromUtf8("background-color: rgb(230, 248, 255);\n"
"color: rgb(0, 0, 0);"))
        self.modelList_label.setAlignment(QtCore.Qt.AlignCenter)
        self.modelList_label.setObjectName(_fromUtf8("modelList_label"))
        self.gridLayout_2.addWidget(self.modelList_label, 1, 2, 1, 1)
        self.mat_listWidget = QtGui.QListWidget(Material_Form)
        self.mat_listWidget.setObjectName(_fromUtf8("mat_listWidget"))
        self.gridLayout_2.addWidget(self.mat_listWidget, 2, 0, 1, 1)
        self.currentModelList_listWidget = QtGui.QListWidget(Material_Form)
        self.currentModelList_listWidget.setObjectName(_fromUtf8("currentModelList_listWidget"))
        self.gridLayout_2.addWidget(self.currentModelList_listWidget, 2, 2, 1, 1)
        self.changeEditType_label = QtGui.QLabel(Material_Form)
        self.changeEditType_label.setStyleSheet(_fromUtf8("background-color: rgb(20, 170, 255);\n"
"color: rgb(0, 0, 255);\n"
""))
        self.changeEditType_label.setAlignment(QtCore.Qt.AlignCenter)
        self.changeEditType_label.setObjectName(_fromUtf8("changeEditType_label"))
        self.gridLayout_2.addWidget(self.changeEditType_label, 0, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.MatReplace_progressBar = QtGui.QProgressBar(Material_Form)
        self.MatReplace_progressBar.setProperty("value", 0)
        self.MatReplace_progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.MatReplace_progressBar.setObjectName(_fromUtf8("MatReplace_progressBar"))
        self.verticalLayout.addWidget(self.MatReplace_progressBar)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.MatReplace_pushButton = QtGui.QPushButton(Material_Form)
        self.MatReplace_pushButton.setObjectName(_fromUtf8("MatReplace_pushButton"))
        self.horizontalLayout_5.addWidget(self.MatReplace_pushButton)
        self.gridLayout.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)

        self.retranslateUi(Material_Form)
        QtCore.QMetaObject.connectSlotsByName(Material_Form)

    def retranslateUi(self, Material_Form):
        Material_Form.setWindowTitle(_translate("Material_Form", "Material_Tool", None))
        self.getCurrentPath_pushButton.setText(_translate("Material_Form", "获取当前场景路径", None))
        self.selectFileDir_pushButton.setText(_translate("Material_Form", "浏览...", None))
        self.method_checkBox.setText(_translate("Material_Form", "点击切换", None))
        self.LoadMesh_pushButton.setText(_translate("Material_Form", "载入", None))
        self.outPut_pushButton.setText(_translate("Material_Form", "输出", None))
        self.LoadJson_pushButton.setText(_translate("Material_Form", "导入", None))
        self.matJson_label.setText(_translate("Material_Form", "材质资源", None))
        self.modelList_label.setText(_translate("Material_Form", "当前模型列表", None))
        self.changeEditType_label.setText(_translate("Material_Form", "点击切换列表操作模式（点我切换）", None))
        self.MatReplace_pushButton.setText(_translate("Material_Form", "》上材质》", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Material_Form = QtGui.QWidget()
    ui = Ui_Material_Form()
    ui.setupUi(Material_Form)
    Material_Form.show()
    sys.exit(app.exec_())

