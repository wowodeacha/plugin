# -*- coding: utf-8 -*-
'''
autor yangjie
mail wowodeacha@gmail.com

'''


from UI.FaceRig import Ui_faceUI_Form
from PyQt4 import QtGui,QtCore
import maya.cmds as mpy
from customAttrSet import customAttrSetCla


#设置表情窗口
#lambda: self.on_button(1)
class FaceUISetUp(QtGui.QWidget):
    def __init__(self,parent = None):
        super(FaceUISetUp,self).__init__(parent = parent)
        customAttrSet = customAttrSetCla()
        self.PugPath = customAttrSet.getCurDirFun()
        self.ui = Ui_faceUI_Form()
        self.ui.setupUi(self)
        self.signalSetUpUI()

        

    #信号设置
    def signalSetUpUI(self):
        loadHeadMeshButton = self.ui.loadHeadMesh_pushButton
        importForeHeadBone_pushButton = self.ui.importForeHeadBone_pushButton

        loadHeadMeshButton.clicked.connect(self.loadMeshFun)
        importForeHeadBone_pushButton.clicked.connect(lambda:self.importNeedBaseJntFun('Face_ForeHead_Plane'))

    #载入头部模型
    def loadMeshFun(self):
        loadHeadMesh_lineEdit = self.ui.loadHeadMesh_lineEdit
        Mesh = mpy.ls(sl=1)[0]
        loadHeadMesh_lineEdit.setText(Mesh)

    #导入基础骨骼文件   
    def importNeedBaseJntFun(self,inS):
        TarFile = self.PugPath +'MayaFile'+'/'+ inS + '.ma'
        mpy.file(TarFile ,i=1,options="v=0;",mergeNamespacesOnClash=0,rpr = inS)
        return    
    #

if __name__ == '__main__':

    Face_Win = FaceUISetUp()
    Face_Win.show()