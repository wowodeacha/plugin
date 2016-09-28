# -*- coding: utf-8 -*-
#
# author YangJie
# mail wowodeacha@gmail.com
#
#


from PyQt4 import QtGui, QtCore
import maya.cmds as mpy
from custom_global_function import CustomAttrSetCla
import customui.facerig as FRUI_D

reload(FRUI_D)


# 设置表情窗口
# lambda: self.on_button(1)
class FaceRigUISetUp(QtGui.QWidget):
    def __init__(self, parent=None):
        super(FaceRigUISetUp, self).__init__(parent=parent)
        customAttrSet = CustomAttrSetCla()
        self.PugPath = customAttrSet.get_cur_dir_path_fun()
        self.ui = FRUI_D.Ui_faceUI_Form()
        self.ui.setupUi(self)
        self.signalSetUpUI()

    # 信号设置
    def signalSetUpUI(self):
        # loadHeadMeshButton = self.ui.loadHeadMesh_pushButton
        importForeHeadBone_pushButton = self.ui.importForeHeadBone_pushButton

        # loadHeadMeshButton.clicked.connect(self.loadMeshFun)
        importForeHeadBone_pushButton.clicked.connect(lambda: self.import_need_base_jnt_fun('Face_ForeHead_Plane'))

    # 载入头部模型
    def loadMeshFun(self):
        loadHeadMesh_lineEdit = self.ui.loadHeadMesh_lineEdit
        Mesh = mpy.ls(sl=1)[0]
        loadHeadMesh_lineEdit.setText(Mesh)

    # 导入基础骨骼文件
    def import_need_base_jnt_fun(self, instr):
        target_file = self.PugPath + 'MayaFile' + '/' + instr + '.ma'
        mpy.file(target_file, i=1, options="v=0;", mergeNamespacesOnClash=0, rpr=instr)
        return
        #


if __name__ == '__main__':
    Face_Win = FaceRigUISetUp()
    Face_Win.show()
