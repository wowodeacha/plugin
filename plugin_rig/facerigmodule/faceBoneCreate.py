# -*- coding: utf-8 -*-
#
# author     YangJie
# mail      wowodeacha@gmail.com
# created   2016.09.21
# Nothing Impossible
#

import maya.cmds as mpy
import custom_global_function as cgf
import facerigmodule.faceRigPubFun as frpfd

reload(cgf)
reload(frpfd)

FRPF = frpfd.FaceRigPubFuc()
CAS = cgf.CustomAttrSetCla()
PLUGIN_PATH = CAS.get_cur_dir_path_fun()
DATA_PATH = PLUGIN_PATH + "datafile/headbasebonedata.json"
NAME_DIR_PATH = PLUGIN_PATH + "datafile/name_dir.json"
FACE_JNT_PIV_DIR = CAS.load_data(DATA_PATH)
NAME_DIR = CAS.load_data(NAME_DIR_PATH)
suffix_dir = frpfd.suffix_dir


class FaceJntCreate(object):
    head_bone_key_dir = {'head': ['Head_base'],
                         'forehead': ["ForeHead_base_L", "ForeHead_base_M", "ForeHead_base_R"],
                         'brow': ['Brow_0_base_L', "Brow_0_base_R", "Brow_1_base_L", "Brow_1_base_R", "Brow_2_base_L",
                                  "Brow_2_base_R", "Brow_base_M"],
                         'eye': ["EyeSag_Dn_base_L", "EyeSag_Dn_base_R", "EyeSag_Up_base_L", "EyeSag_Up_base_R",
                                 "Eye_ball_base_L", "Eye_ball_base_R", "Eye_root_base_L", "Eye_root_base_R",
                                 "Eyelid_DnIn_base_L", "Eyelid_DnIn_base_R", "Eyelid_DnOut_base_L",
                                 "Eyelid_DnOut_base_R", "Eyelid_Dn_base_L", "Eyelid_Dn_base_R", "Eyelid_In_base_L",
                                 "Eyelid_In_base_R", "Eyelid_Out_base_L", "Eyelid_Out_base_R",
                                 "Eyelid_UpIn_base_L", "Eyelid_UpIn_base_R", "Eyelid_UpOut_base_L",
                                 "Eyelid_UpOut_base_R", "Eyelid_Up_base_L", "Eyelid_Up_base_R"],
                         'check': ["Check_base_L", "Check_base_R", "Cheek_In_base_L", "Cheek_In_base_R",
                                   "Cheek_Out_base_L", "Cheek_Out_base_R", "Cheek_Up_base_L",
                                   "Cheek_Up_base_R"],
                         'nose': ["Nose_base_L", "Nose_base_M", "Nose_base_R"],
                         'mouth': ["Mouth_Corner_base_L", "Mouth_Corner_base_R", "Mouth_Dn_base_L", "Mouth_Dn_base_R",
                                   "Mouth_Up_base_L", "Mouth_Up_base_R", "Mouth_Up_base_M", "Mouth_Dn_base_M",
                                   "NoseFold_base_L", "NoseFold_base_R"],
                         'jaw': ["Chin_base", "Jaw_base"],
                         'temple': ["Temple_base_L", "Temple_base_R"]}

    def __init__(self, char_name='test_char'):
        self.char_name = char_name

    # TODO: 重构此处代码  这里是垃圾
    @staticmethod
    def create_base_grp():
        mpy.group(em=True, name=NAME_DIR["faceMoveCur"])
        mpy.group(em=True, name=NAME_DIR["face_base_rig_grp"])
        FRPF.try_parent(NAME_DIR["face_base_rig_grp"], NAME_DIR["faceMoveCur"])
        print "here"

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
            # TODO: 这里整理层级的方式需要重构
            FRPF.try_parent(i, NAME_DIR["face_base_rig_grp"])
        # TODO:此处有一大坑
        try:
            FRPF.try_parent("Eye_ball_base_L", "Eye_root_base_L")
            FRPF.try_parent("Eye_ball_base_R", "Eye_root_base_R")
            FRPF.try_parent("Chin_base", "Jaw_base")
        except:
            pass

    @staticmethod
    def mirr_jnt_pos(typ):
        TName = suffix_dir
        left_side = TName['_L']
        right_side = TName['_R']

        tv = 1
        rv = 1

        faceSdkSkinGrp = NAME_DIR["face_base_rig_grp"]
        if (not mpy.objExists(faceSdkSkinGrp)):
            return
        allJnt = mpy.listRelatives(faceSdkSkinGrp, c=1, ad=1, typ='joint')
        axis = [-1, 1, 1, 1, -1, -1, 1, 1, 1]
        print allJnt
        for i in allJnt:
            if (typ == 'L>>R'):
                if (i[-2:] == left_side):
                    getObj = i
                    mirObj = i[:-2] + right_side
                else:
                    continue
            else:
                if (i[-2:] == right_side):
                    getObj = i
                    mirObj = i[:-2] + left_side
                else:
                    continue

            if (not mpy.objExists(mirObj)):
                continue
            if (tv):
                pos = mpy.xform(getObj, ws=1, q=1, t=1)
                mpy.xform(mirObj, ws=1, t=[pos[0] * axis[0], pos[1] * axis[1], pos[2] * axis[2]])
            if (rv):
                rot = mpy.xform(getObj, ws=1, q=1, ro=1)
                mpy.xform(mirObj, ws=1, ro=[rot[0] * axis[3], rot[1] * axis[4], rot[2] * axis[5]])
        mpy.refresh(cv=1, f=1)


if __name__ == "__main__":
    fc = FaceJntCreate()
    # fc.create_base_grp()
    fc.mirr_jnt_pos('L>>R')
    print "done"
