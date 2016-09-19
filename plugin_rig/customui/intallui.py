# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'installui.ui'
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

class Ui_install_win(object):
    def setupUi(self, install_win):
        install_win.setObjectName(_fromUtf8("install_win"))
        install_win.resize(309, 75)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(install_win.sizePolicy().hasHeightForWidth())
        install_win.setSizePolicy(sizePolicy)
        self.gridLayout = QtGui.QGridLayout(install_win)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pushButton = QtGui.QPushButton(install_win)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)
        self.install_label = QtGui.QLabel(install_win)
        self.install_label.setText(_fromUtf8(""))
        self.install_label.setObjectName(_fromUtf8("install_label"))
        self.verticalLayout.addWidget(self.install_label)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(install_win)
        QtCore.QMetaObject.connectSlotsByName(install_win)

    def retranslateUi(self, install_win):
        install_win.setWindowTitle(_translate("install_win", "Install", None))
        self.pushButton.setText(_translate("install_win", "安装", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    install_win = QtGui.QWidget()
    ui = Ui_install_win()
    ui.setupUi(install_win)
    install_win.show()
    sys.exit(app.exec_())

