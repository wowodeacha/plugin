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
    head_bone_key_dir = {'head': ['Head_base'],
                         'forehead': ["ForeHead_base_L", "ForeHead_base_M", "ForeHead_base_R"],
                         'brow': ['Brow_0_base_L', "Brow_0_base_R", "Brow_1_base_L", "Brow_1_base_R", "Brow_2_base_L",
                                  "Brow_2_base_R", "Brow_base_M"],
                         'eye': ["EyeSag_Dn_base_L", "EyeSag_Dn_base_R", "EyeSag_Up_base_L", "EyeSag_Up_base_R",
                                 "Eye_root_base_L", "Eye_root_base_R", "Eyelid_DnIn_base_L", "Eyelid_DnIn_base_R",
                                 "Eyelid_DnOut_base_L", "Eyelid_DnOut_base_R", "Eyelid_Dn_base_L", "Eyelid_Dn_base_R",
                                 "Eyelid_In_base_L", "Eyelid_In_base_R", "Eyelid_Out_base_L", "Eyelid_Out_base_R",
                                 "Eyelid_UpIn_base_L", "Eyelid_UpOut_base_L", "Eyelid_UpOut_base_R",
                                 "Eyelid_Up_base_L", "Eyelid_Up_base_R"],
                         'check': ["Check_base_L", "Check_base_R", "Cheek_In_base_L", "Cheek_In_base_R",
                                   "Cheek_Out_base_L", "Cheek_Out_base_R", "Cheek_Up_base_L",
                                   "Cheek_Up_base_R"],
                         'nose': ["Nose_base_L", "Nose_base_M", "Nose_base_R"],
                         'mouth': ["Mouth_Corner_base_L", "Mouth_Corner_base_R", "Mouth_Dn_base_L", "Mouth_Dn_base_R",
                                   "Mouth_Up_base_M", "Mouth_Up_base_R", "NoseFold_base_L", "NoseFold_base_R"],
                         'jaw': ["Chin_base", "Jaw_base"],
                         'temple': ["Temple_base_L", "Temple_base_R"]}

    def __init__(self, char_name='test_char'):
        self.char_name = char_name

    # 创建基础骨骼
    def create_base_jnt(self, needed_parts_list):
        for i in needed_parts_list:
            # todo: 缺少一个子函数（创建基础骨骼）
            print ''

    # 子函数创建基础骨骼
    def create_base_jnt_step(self,in_flag):
        head_bone_name_dir = self.head_bone_key_dir
        flag_jnt_name_list = head_bone_name_dir[in_flag]
        for i in head_bone_name_dir:
            # todo: 用pymel写一个根据点坐标创建骨骼（learning）
            print ''




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
