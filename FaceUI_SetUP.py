'''
autor yangjie
mail wowodeacha@gmail.com

'''

from UI.face import Ui_FaceWin_Form
from PyQt4 import QtCore,QtGui


class faceUIEdit(QtGui.QWidget):
    def __init__(self,parent = None):
        super(faceUIEdit, self).__init__(parent = parent)

        self.ui = Ui_FaceWin_Form()
        self.ui.setupUi(self)
        self._setUpgui()

    def _setUpgui(self):
        _importBaseJnt_BT = self.ui._importBaseJnt_pushButton
        _setPath_BT = self.ui._setPath_pushButton
        
        #self.ui.pushButton_4.clicked.connect(self.close)
        pass

    #set save base jnt path
    def _setPath(self):

        print "setPath"
    def _help(self):
        print ("help")



if __name__ == "__main__":

    faceWin =  faceUIEdit()
    faceWin.show()


