# -*- coding: utf-8 -*-
#
# author     YangJie
# mail      wowodeacha@gmail.com
# created   2016.09.21
# Nothing Impossible
#
#
import maya.cmds as mpy
import custom_global_function as cgf


class FaceJntCreate():
    head_bone_key_dir = {'forehead': [],
                         'brow': ['Brow_0_base_L', "Brow_0_base_R", "Brow_1_base_L", "Brow_1_base_R", "Brow_2_base_L",
                                  "Brow_2_base_R", "Brow_base_M"],
                         'eye': [], 'check': ["Check_base_L", "Check_base_R", "Cheek_In_base_L", "Cheek_In_base_R",
                                              "Cheek_Out_base_L", "Cheek_Out_base_R", "Cheek_Up_base_L",
                                              "Cheek_Up_base_R"],
                         'nose': [], 'mouth': [], 'jaw': []}

    def __init__(self, char_name='test_char'):
        self.char_name = char_name

    # 创建基础骨骼
    def create_base_jnt(self, needed_parts_list):
        base_dir = self.head_bone_key_dir

    def test(self):
        _newDis = self._baseDis
        print _newDis


if __name__ == "__main__":
    # _FaceJntCreate = FaceJntCreate()
    #
    # _FaceJntCreate.import_base_loc()
    cgf_c = cgf.CustomAttrSetCla()
    rig_path = cgf_c.get_cur_dir_fun()
    data_path = rig_path + "datafile/headbasebonedata.json"
    # jnt_dir =
    jnt_dir = cgf_c.load_data(data_path)
    print jnt_dir

    cgf_c.write_data(data_path, jnt_dir)
