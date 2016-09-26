# -*- coding: utf-8 -*-
#
# author     YangJie
# mail      wowodeacha@gmail.com
# created   2016.09.21
# Nothing Impossible
#

import maya.cmds as mpy
import custom_global_function as cgf

CAS = cgf.CustomAttrSetCla()
PLUGIN_PATH = CAS.get_cur_dir_path_fun()
DATA_PATH = PLUGIN_PATH + "datafile/headbasebonedata.json"
FACE_JNT_PIV_DIR = CAS.load_data(DATA_PATH)


class FaceJntCreate(object):
    head_bone_key_dir = {'head': ['Head_base'],
                         'forehead': ["ForeHead_base_L", "ForeHead_base_M", "ForeHead_base_R"],
                         'brow': ['Brow_0_base_L', "Brow_0_base_R", "Brow_1_base_L", "Brow_1_base_R", "Brow_2_base_L",
                                  "Brow_2_base_R", "Brow_base_M"],
                         'eye': ["EyeSag_Dn_base_L", "EyeSag_Dn_base_R", "EyeSag_Up_base_L", "EyeSag_Up_base_R",
                                 "Eye_root_base_L", "Eye_root_base_R", "Eyelid_DnIn_base_L", "Eyelid_DnIn_base_R",
                                 "Eyelid_DnOut_base_L", "Eyelid_DnOut_base_R", "Eyelid_Dn_base_L", "Eyelid_Dn_base_R",
                                 "Eyelid_In_base_L", "Eyelid_In_base_R", "Eyelid_Out_base_L", "Eyelid_Out_base_R",
                                 "Eyelid_UpIn_base_L", "Eyelid_UpIn_base_R", "Eyelid_UpOut_base_L",
                                 "Eyelid_UpOut_base_R",
                                 "Eyelid_Up_base_L", "Eyelid_Up_base_R"],
                         'check': ["Check_base_L", "Check_base_R", "Cheek_In_base_L", "Cheek_In_base_R",
                                   "Cheek_Out_base_L", "Cheek_Out_base_R", "Cheek_Up_base_L",
                                   "Cheek_Up_base_R"],
                         'nose': ["Nose_base_L", "Nose_base_M", "Nose_base_R"],
                         'mouth': ["Mouth_Corner_base_L", "Mouth_Corner_base_R", "Mouth_Dn_base_L", "Mouth_Dn_base_R",
                                   "Mouth_Up_base_L", "Mouth_Up_base_R", "Mouth_Up_base_M", "NoseFold_base_L",
                                   "NoseFold_base_R"],
                         'jaw': ["Chin_base", "Jaw_base"],
                         'temple': ["Temple_base_L", "Temple_base_R"]}

    def __init__(self, char_name='test_char'):
        self.char_name = char_name

    # 创建基础骨骼
    def create_base_jnt(self, needed_parts_list):
        if needed_parts_list == ["base_list"]:
            needed_parts_list = list(self.head_bone_key_dir.keys())
        for i in needed_parts_list:
            self.create_base_jnt_step(i)

    # 子函数创建基础骨骼
    def create_base_jnt_step(self, in_flag):
        head_bone_name_dir = self.head_bone_key_dir
        flag_jnt_name_list = head_bone_name_dir[in_flag]
        for i in flag_jnt_name_list:
            piv = FACE_JNT_PIV_DIR[i]
            mpy.select(cl=1)
            mpy.joint(n=i, p=piv)


if __name__ == "__main__":
    fc = FaceJntCreate()
    fc.create_base_jnt(['base_list'])
