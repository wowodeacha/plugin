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
import facerigmodule.faceBoneCreate as FBC
import facerigmodule.faceRigPubFun as FRPF


reload(FBC)
reload(FRUI_D)
reload(FRPF)

F_J_C = FBC.FaceJntCreate()
FRPF_C = FRPF.FaceRigPubFuc()


# 设置表情窗口
# lambda: self.on_button(1)
class FaceRigUISetUp(QtGui.QWidget):
    def __init__(self, parent=None):
        super(FaceRigUISetUp, self).__init__(parent=parent)
        customAttrSet = CustomAttrSetCla()
        self.PugPath = customAttrSet.get_cur_dir_path_fun()
        self.ui = FRUI_D.Ui_faceUI_Form()
        self.ui.setupUi(self)
        self.signal_setup_ui()

    # 信号设置
    def signal_setup_ui(self):
        rebulidAllBone_pushButton = self.ui.rebulidAllBone_pushButton
        rebulidAllBone_pushButton.hide()

        load_mesh_list_button = self.ui.loadmeshList__pushButton
        setheadmesh_pushButton = self.ui.setheadmesh_pushButton
        setforeheadbone_pushButton = self.ui.setforeheadbone_pushButton
        snapForeHeadMeshToHeadMesh_pushButton = self.ui.snapForeHeadMeshToHeadMesh_pushButton

        load_mesh_list_button.clicked.connect(self.load_mesh_list_fun)
        setheadmesh_pushButton.clicked.connect(self.set_current_face_fun)
        setforeheadbone_pushButton.clicked.connect(self.create_base_jnt_fun)
        snapForeHeadMeshToHeadMesh_pushButton.clicked.connect(self.snap_sel_obj_to_face_mesh)


    # 载入模型列表
    def load_mesh_list_fun(self):
        sel = mpy.ls(sl=1)
        if (len(sel) == 0):
            return
        headmeshlist_listWidget = self.ui.headmeshlist_listWidget

        headmeshlist_listWidget.clear()
        print "dd"
        for i in range(len(sel)):
            shape = mpy.listRelatives(sel[i], s=1, f=1)
            print sel[i]
            if (shape == None):
                continue
            if (mpy.objectType(shape[0]) != 'mesh'):
                continue
            headmeshlist_listWidget.insertItem(i, sel[i])

            # mpy.textField('frFaceMeshTF', e=1, tx='')
            # TODO: 添加控件生效mpy.button('frSetFaceMeshB', e=1, en=1)


    # 载面部部模型
    def set_current_face_fun(self):
        #     loadHeadMesh_lineEdit = self.ui.loadHeadMesh_lineEdit
        #     Mesh = mpy.ls(sl=1)
        #     loadHeadMesh_lineEdit.setText(Mesh)
        headmeshlist_listWidget = self.ui.headmeshlist_listWidget
        face_mesh_lineEdit = self.ui.face_mesh_lineEdit
        sel_item = headmeshlist_listWidget.currentItem()
        sel_item_text = sel_item.text()
        sel_item_str = str(sel_item_text)
        # if (selI == None):
        #     return
        # skinMesh = selI[0]
        face_mesh_lineEdit.setText(sel_item_str)
        # mpy.button('frSdkRiggingB', e=1, en=1)


    # 生成基础骨骼文件
    def create_base_jnt_fun(self):
        # 获取需要的骨骼标签
        cur_flag_list = ["base_list"]
        F_J_C.create_base_grp()
        F_J_C.create_base_jnt(cur_flag_list)  #

    # 吸附选择到模型
    def snap_sel_obj_to_face_mesh(self):
        face_mesh_lineEdit = self.ui.face_mesh_lineEdit
        sel_list = mpy.ls(sl=1)
        face_mesh = face_mesh_lineEdit.text()
        face_mesh = str(face_mesh)
        FRPF_C.matchObjToCloset(face_mesh,sel_list)

    # Rig、


if __name__ == '__main__':
    Face_Win = FaceRigUISetUp()
    Face_Win.show()
