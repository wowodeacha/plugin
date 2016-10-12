# -*- coding: utf-8 -*-
#
# author YangJie
# mail wowodeacha@gmail.com
#
#
import maya.OpenMaya as OpenMaya
import maya.cmds as mpy
import custom_global_function as CGF
import facerigmodule.faceRigPubFun as FRPF

reload(FRPF)

CGF_C = CGF.CustomAttrSetCla()
FRPF_C = FRPF.FaceRigPubFuc()

PLUGIN_PATH = CGF_C.get_cur_dir_path_fun()
DATA_PATH = PLUGIN_PATH + "datafile/headbasebonedata.json"
NAME_DIR_PATH = PLUGIN_PATH + "datafile/name_dir.json"
FACE_JNT_PIV_DIR = CGF_C.load_data(DATA_PATH)
NAME_DIR = CGF_C.load_data(NAME_DIR_PATH)


class FaceRiggingClass(object):
    head_bone_key_dir_reset = {'head_base': 'Head_base',
                               "L_brow_a_base": 'Brow_0_base_L',
                               "R_brow_a_base": "Brow_0_base_R",
                               "L_brow_b_base": "Brow_1_base_L",
                               "R_brow_b_base": "Brow_1_base_R",
                               "L_brow_c_base": "Brow_2_base_L",
                               "R_brow_c_base": "Brow_2_base_R",
                               "M_brow_base": "Brow_base_M",
                               "L_eyeSag_Dn_base": "EyeSag_Dn_base_L",
                               "R_eyeSag_Dn_base": "EyeSag_Dn_base_R",
                               "L_eyeSag_Up_base": "EyeSag_Up_base_L",
                               "R_eyeSag_Up_base": "EyeSag_Up_base_R",
                               "L_eyeBall_base": "Eye_ball_base_L",
                               "R_eyeBall_base": "Eye_ball_base_R",
                               "L_eye_root_base": "Eye_root_base_L",
                               "R_eye_root_base": "Eye_root_base_R",
                               "L_eyelid_DnIn_base": "Eyelid_DnIn_base_L",
                               "R_eyelid_DnIn_base": "Eyelid_DnIn_base_R",
                               "L_eyelid_DnOut_base": "Eyelid_DnOut_base_L",
                               "R_eyelid_DnOut_base": "Eyelid_DnOut_base_R",
                               "L_eyelid_Dn_base": "Eyelid_Dn_base_L",
                               "R_eyelid_Dn_base": "Eyelid_Dn_base_R",
                               "L_eyelid_In_base": "Eyelid_In_base_L",
                               "R_eyelid_In_base": "Eyelid_In_base_R",
                               "L_eyelid_Out_base": "Eyelid_Out_base_L",
                               "R_eyelid_Out_base": "Eyelid_Out_base_R",
                               "L_eyelid_UpIn_base": "Eyelid_UpIn_base_L",
                               "R_eyelid_UpIn_base": "Eyelid_UpIn_base_R",
                               "L_eyelid_UpOut_base": "Eyelid_UpOut_base_L",
                               "R_eyelid_UpOut_base": "Eyelid_UpOut_base_R",
                               "L_eyelid_Up_base": "Eyelid_Up_base_L",
                               "R_eyelid_Up_base": "Eyelid_Up_base_R",
                               "L_cheek_base": "Check_base_L",
                               "R_cheek_base": "Check_base_R",
                               "L_cheek_In_base": "Cheek_In_base_L",
                               "R_cheek_In_base": "Cheek_In_base_R",
                               "L_cheek_Out_base": "Cheek_Out_base_L",
                               "R_cheek_Out_base": "Cheek_Out_base_R",
                               "L_cheek_Up_base": "Cheek_Up_base_L",
                               "R_cheek_Up_base": "Cheek_Up_base_R",
                               "L_nose_base": "Nose_base_L",
                               "M_nose_base": "Nose_base_M",
                               "R_nose_base": "Nose_base_R",
                               "L_mouth_Corner_base": "Mouth_Corner_base_L",
                               "R_mouth_Corner_base": "Mouth_Corner_base_R",
                               "L_mouth_Dn_base": "Mouth_Dn_base_L",
                               "R_mouth_Dn_base": "Mouth_Dn_base_R",
                               "L_mouth_Up_base": "Mouth_Up_base_L",
                               "R_mouth_Up_base": "Mouth_Up_base_R",
                               "M_mouth_Up_base": "Mouth_Up_base_M",
                               "M_mouth_Dn_base": "Mouth_Dn_base_M",
                               "L_noseFold_base": "NoseFold_base_L",
                               "R_noseFold_base": "NoseFold_base_R",
                               "chin_base": "Chin_base",
                               "jaw_base": "Jaw_base",
                               "L_temple_base": "Temple_base_L",
                               "R_temple_base": "Temple_base_R"}

    def __init__(self, author="yangjie"):
        author = author

    def returnTempNameDirc(self):
        TName = {'_fol': '_fol', '_loc': '_loc', '_final': '_final', '_target': '_target', 'face': 'face',
                 '_base': '_base', '_bsNode': '_bsNode', '_bs': '_bs', '_skin': '_skin', 'M_': 'M_', 'L_': 'L_',
                 'R_': 'R_', '_ctrl': '_ctrl', '_rig': '_rig', '_jnt': '_jnt', '_root': '_root', '_rot': '_rot',
                 '_cur': '_cur', '_cnt': '_cnt', '_sdk': '_sdk', '_grp': '_grp', '_anim': '_anim'}
        return TName

    def createSdkJointRigging(self, face_mesh, mesh_lsit):

        faceSdkSkinGrp = 'face_base_rig_grp'
        if not (mpy.objExists(faceSdkSkinGrp)):
            return
        faceCur = 'faceMoveCur'
        faceBaseGrp = 'face_base_rig_grp'
        if (not mpy.objExists(faceBaseGrp)):
            return
        faceBsGrp = 'face_bs_grp'

        if not (mpy.objExists(faceBsGrp)):
            faceBsGrp = mpy.group(em=1, n=faceBsGrp)
            mpy.setAttr(faceBsGrp + '.it', 0)
            mpy.parent(faceBsGrp, faceBaseGrp)

        faceAnimCtrlGrp = 'face_anim_ctrl_grp'
        if not (mpy.objExists(faceAnimCtrlGrp)):
            faceAnimCtrlGrp = mpy.group(em=1, n=faceAnimCtrlGrp)
            mpy.parent(faceAnimCtrlGrp, faceCur)

        faceMesh = face_mesh
        print face_mesh
        if (faceMesh == '' or not mpy.objExists(faceMesh)):
            return
        faceSdkRigGrp = 'face_sdk_rig_grp'
        if mpy.objExists(faceSdkRigGrp):
            return

        faceMeshGrp = 'face_mesh_grp'
        if not (mpy.objExists(faceMeshGrp)):
            faceMeshGrp = mpy.group(n=faceMeshGrp, em=1)
            mpy.setAttr(faceMeshGrp + '.it', 0)
            mpy.parent(faceMeshGrp, faceCur)

        faceSkinMeshGrp = 'face_skin_mesh_grp'
        if not (mpy.objExists(faceSkinMeshGrp)):
            faceSkinMeshGrp = mpy.group(n=faceSkinMeshGrp, em=1)
            mpy.addAttr(faceSkinMeshGrp, ln='faceMesh', at='bool', dv=1, k=1)
            mpy.addAttr(faceSkinMeshGrp, ln='boxWidthF', at='float')
            mpy.addAttr(faceSkinMeshGrp, ln='boxWidthS', at='float')
            mpy.setAttr(faceSkinMeshGrp + '.boxWidthF', cb=1)
            mpy.setAttr(faceSkinMeshGrp + '.boxWidthS', cb=1)
            mpy.parent(faceSkinMeshGrp, faceMeshGrp)
            mpy.setAttr(faceSkinMeshGrp + '.it', 0)

        meshList = mesh_lsit
        for i in meshList:
            FRPF_C.try_parent(i, faceSkinMeshGrp)

        bbox = self.getBoundingBox(faceSkinMeshGrp)
        mpy.setAttr(faceSkinMeshGrp + '.boxWidthF', bbox[0])
        mpy.setAttr(faceSkinMeshGrp + '.boxWidthS', bbox[1])

        faceOrigMeshGrp = 'face_orig_mesh_grp'
        if mpy.objExists(faceOrigMeshGrp):
            mpy.delete(faceOrigMeshGrp)
        faceOrigMeshGrp = mpy.group(em=1, n=faceOrigMeshGrp)
        mpy.parent(faceOrigMeshGrp, faceBsGrp)
        mpy.setAttr(faceOrigMeshGrp + '.v', 0)

        self.connectAttrForce(faceMesh + '.msg', faceSkinMeshGrp + '.faceMesh')
        allMesh = mesh_lsit

        for i in range(len(allMesh)):
            origMeshName = allMesh[i] + '_OrigMesh'
            origMeshName = mpy.duplicate(allMesh[i], n=origMeshName)[0]
            FRPF_C.try_parent(origMeshName, faceOrigMeshGrp)
            iOrigAttr = self.tryAddMessageAttr(allMesh[i], 'origMesh')
            nOrigAttr = self.tryAddMessageAttr(origMeshName, 'origMesh')
            self.connectAttrForce(nOrigAttr, iOrigAttr)

            ctrGrp = chr(65 + i) + '_CorrectiveGrp'
            nCtrAttr = self.tryAddMessageAttr(origMeshName, 'ctrGrp')
            mpy.setAttr(nCtrAttr, ctrGrp, typ='string')

        self.createSdkJntRig()
        self.sdd_createDefultSdk()

        faceJntList = mpy.listRelatives(faceSdkSkinGrp, c=1, ad=1, typ='joint')
        for i in allMesh:
            mpy.skinCluster(faceJntList, i, mi=1, nw=1, tsb=1)
        mpy.textField('frCurrentMeshTF', e=1, tx='')

        self.importAndConnectPanel()
        if (mpy.objExists('Face_Panel_grp')):
            mpy.parent('Face_Panel_grp', faceAnimCtrlGrp)

        self.reloadFaceMeshInfo()

    def getBoundingBox(self, obj):
        box = mpy.xform(obj, q=1, bbi=1)
        return [box[3] - box[0], box[4] - box[1], box[5] - box[2]]

    def createSdkJntRig(self):
        T = self.returnTempNameDirc()
        FR, FRJntPos, FRUIPos = self.frTNameDirc()
        _base = T['_base']
        _skin = T['_skin']
        _sdk = T['_sdk']
        _grp = T['_grp']
        _cnt = T['_cnt']
        _root = T['_root']
        _cur = T['_cur']
        L_ = T['L_']
        R_ = T['R_']
        M_ = T['M_']
        _rig = T['_rig']
        _loc = T['_loc']

        faceCur = 'faceMoveCur'
        if (not mpy.objExists(faceCur)):
            return

        _rad = mpy.getAttr(faceCur + '.sx')
        if (mpy.getAttr(faceCur + '.globalScale') == 0):
            mpy.setAttr(faceCur + '.globalScale', _rad)
        _rad = mpy.getAttr(faceCur + '.globalScale')
        _rad *= 0.5
        mpy.makeIdentity(faceCur, a=1, t=1, r=1, s=1)

        faceBaseGrp = 'face_base_rig_grp'
        # face sdk cnt rig
        faceSdkRigGrp = 'face_sdk_rig_grp'
        faceSdkRigGrp = mpy.group(n=faceSdkRigGrp, em=1)
        mpy.parent(faceSdkRigGrp, faceBaseGrp)

        faceSdkSkinGrp = 'face_base_rig_grp'
        if not (mpy.objExists(faceSdkSkinGrp)):
            return
        # all setDrivenKey mpy.control group
        for i in FR.keys():
            baseName = FR[i]
            cur = FRPF_C.create_curve_cnt(baseName + _cnt, typ='Cube', r=_rad)
            curGrp = self.sdd_zeroSdkGrp(baseName, cur)
            skin_jnt = self.head_bone_key_dir_reset[baseName + _base]
            mpy.delete(mpy.parentConstraint(skin_jnt, curGrp))
            mpy.parent(curGrp, faceSdkRigGrp)
            mpy.parentConstraint(cur, skin_jnt)
            mpy.scaleConstraint(cur, skin_jnt)

            pCtrl = mpy.listRelatives(skin_jnt, p=1)[0]
            if (faceSdkSkinGrp != pCtrl):
                mpy.parent(skin_jnt, faceSdkSkinGrp)

        # eyelid rig
        # L Eyelid

        lEyelidList = ['L_eyelid_In', 'L_eyelid_UpIn', 'L_eyelid_DnIn', 'L_eyelid_Up', 'L_eyelid_Dn', 'L_eyelid_UpOut',
                       'L_eyelid_DnOut', 'L_eyelid_Out']
        for i in lEyelidList:
            baseName = FR[i] + _root
            sdk = mpy.group(n=baseName + _sdk, em=1)
            grp = mpy.group(n=baseName + _grp, em=1)
            mpy.parent(sdk, grp)
            mpy.delete(mpy.parentConstraint(FR['L_eye_root'] + _cnt, grp))
            mpy.parent(FR[i] + _grp, sdk)
            mpy.parent(grp, FR['L_eye_root'] + _cnt)

        baseName = FR['L_eyelid_Up'] + _root
        cnt = FRPF_C.create_curve_cnt(baseName + _cnt, typ='Triangle', r=_rad)
        mpy.delete(mpy.parentConstraint(FR['L_eyelid_Up'] + _cnt, cnt))
        rPos = mpy.xform(FR['L_eye_root'] + _cnt, rp=1, q=1, ws=1)
        mpy.xform(cnt, rp=rPos, ws=1)
        mpy.parent(cnt, baseName + _sdk)
        mpy.makeIdentity(cnt, a=1, t=1, r=1, s=1)
        mpy.parent(FR['L_eyelid_UpOut'] + _root + _grp, FR['L_eyelid_UpIn'] + _root + _grp, FR['L_eyelid_Up'] + _grp,
                   cnt)
        followGrp = mpy.duplicate(baseName + _grp, n=baseName + '_follow', po=1)[0]
        follCon = mpy.parentConstraint(followGrp, FR['L_eye_root'] + _cnt, baseName + _grp)[0]
        mpy.parentConstraint(FR['L_eyeBall'] + _cnt, followGrp)
        mpy.addAttr(cnt, ln='eydlidFollow', at='double', min=0, max=1, dv=0.05, k=1)
        mpy.connectAttr(cnt + '.eydlidFollow', follCon + '.w0')

        baseName = FR['L_eyelid_Dn'] + _root
        cnt = FRPF_C.create_curve_cnt(baseName + _cnt, typ='Triangle', r=_rad)
        mpy.delete(mpy.parentConstraint(FR['L_eyelid_Dn'] + _cnt, cnt))
        rPos = mpy.xform(FR['L_eye_root'] + _cnt, rp=1, q=1, ws=1)
        mpy.xform(cnt, rp=rPos, ws=1)
        mpy.parent(cnt, baseName + _sdk)
        mpy.makeIdentity(cnt, a=1, t=1, r=1, s=1)
        mpy.parent(FR['L_eyelid_DnOut'] + _root + _grp, FR['L_eyelid_DnIn'] + _root + _grp, FR['L_eyelid_Dn'] + _grp,
                   cnt)
        followGrp = mpy.duplicate(baseName + _grp, n=baseName + '_follow', po=1)[0]
        follCon = mpy.parentConstraint(followGrp, FR['L_eye_root'] + _cnt, baseName + _grp)[0]
        mpy.parentConstraint(FR['L_eyeBall'] + _cnt, followGrp)
        mpy.addAttr(cnt, ln='eydlidFollow', at='double', min=0, max=1, dv=0.05, k=1)
        mpy.connectAttr(cnt + '.eydlidFollow', follCon + '.w0')

        mpy.parent(FR['L_eyeSag_Up'] + _grp, FR['L_eyeSag_Dn'] + _grp, FR['L_eyeBall'] + _grp, FR['L_eye_root'] + _cnt)
        mpy.parent(FR['L_brow_a'] + _grp, FR['L_brow_b'] + _grp, FR['L_brow_c'] + _grp, FR['L_eye_root'] + _cnt)

        # R Eyelid
        rEyelidList = ['R_eyelid_In', 'R_eyelid_UpIn', 'R_eyelid_DnIn', 'R_eyelid_Up', 'R_eyelid_Dn', 'R_eyelid_UpOut',
                       'R_eyelid_DnOut', 'R_eyelid_Out']
        for i in rEyelidList:
            baseName = FR[i] + _root
            sdk = mpy.group(n=baseName + _sdk, em=1)
            grp = mpy.group(n=baseName + _grp, em=1)
            mpy.parent(sdk, grp)
            mpy.delete(mpy.parentConstraint(FR['R_eye_root'] + _cnt, grp))
            mpy.parent(FR[i] + _grp, sdk)
            mpy.parent(grp, FR['R_eye_root'] + _cnt)

        baseName = FR['R_eyelid_Up'] + _root
        cnt = FRPF_C.create_curve_cnt(baseName + _cnt, typ='Triangle', r=_rad)
        mpy.delete(mpy.parentConstraint(FR['R_eyelid_Up'] + _cnt, cnt))
        rPos = mpy.xform(FR['R_eye_root'] + _cnt, rp=1, q=1, ws=1)
        mpy.xform(cnt, rp=rPos, ws=1)
        mpy.parent(cnt, baseName + _sdk)
        mpy.makeIdentity(cnt, a=1, t=1, r=1, s=1)
        mpy.parent(FR['R_eyelid_UpOut'] + _root + _grp, FR['R_eyelid_UpIn'] + _root + _grp, FR['R_eyelid_Up'] + _grp,
                   cnt)
        followGrp = mpy.duplicate(baseName + _grp, n=baseName + '_follow', po=1)[0]
        follCon = mpy.parentConstraint(followGrp, FR['R_eye_root'] + _cnt, baseName + _grp)[0]
        mpy.parentConstraint(FR['R_eyeBall'] + _cnt, followGrp)
        mpy.addAttr(cnt, ln='eydlidFollow', at='double', min=0, max=1, dv=0.05, k=1)
        mpy.connectAttr(cnt + '.eydlidFollow', follCon + '.w0')

        baseName = FR['R_eyelid_Dn'] + _root
        cnt = FRPF_C.create_curve_cnt(baseName + _cnt, typ='Triangle', r=_rad)
        mpy.delete(mpy.parentConstraint(FR['R_eyelid_Dn'] + _cnt, cnt))
        rPos = mpy.xform(FR['R_eye_root'] + _cnt, rp=1, q=1, ws=1)
        mpy.xform(cnt, rp=rPos, ws=1)
        mpy.parent(cnt, baseName + _sdk)
        mpy.makeIdentity(cnt, a=1, t=1, r=1, s=1)
        mpy.parent(FR['R_eyelid_DnOut'] + _root + _grp, FR['R_eyelid_DnIn'] + _root + _grp, FR['R_eyelid_Dn'] + _grp,
                   cnt)
        followGrp = mpy.duplicate(baseName + _grp, n=baseName + '_follow', po=1)[0]
        follCon = mpy.parentConstraint(followGrp, FR['R_eye_root'] + _cnt, baseName + _grp)[0]
        mpy.parentConstraint(FR['R_eyeBall'] + _cnt, followGrp)
        mpy.addAttr(cnt, ln='eydlidFollow', at='double', min=0, max=1, dv=0.05, k=1)
        mpy.connectAttr(cnt + '.eydlidFollow', follCon + '.w0')

        mpy.parent(FR['R_eyeSag_Up'] + _grp, FR['R_eyeSag_Dn'] + _grp, FR['R_eyeBall'] + _grp, FR['R_eye_root'] + _cnt)

        mpy.parent(FR['R_brow_a'] + _grp, FR['R_brow_b'] + _grp, FR['R_brow_c'] + _grp, FR['R_eye_root'] + _cnt)

        # #cheek rig
        # mpy.parent(FR['L_cheek_In']+_grp,FR['L_cheek_Out']+_grp,FR['L_cheek_Up']+_cnt)
        # mpy.parent(FR['R_cheek_In']+_grp,FR['R_cheek_Out']+_grp,FR['R_cheek_Up']+_cnt)

        # nose rig
        # nose root
        noseRoot = FR['M_nose'] + _root
        noseRootCnt = FRPF_C.create_curve_cnt(noseRoot + _cnt, typ='Cube', r=_rad)
        noseRootGrp = self.sdd_zeroSdkGrp(noseRoot, noseRootCnt)
        mpy.delete(mpy.parentConstraint(FR['L_cheek_In'] + _cnt, FR['R_cheek_In'] + _cnt, noseRootGrp))
        mpy.parent(FR['L_nose'] + _grp, noseRootCnt)
        mpy.parent(FR['R_nose'] + _grp, noseRootCnt)
        mpy.parent(FR['M_nose'] + _grp, noseRootCnt)
        mpy.parent(noseRootGrp, faceSdkRigGrp)
        # mouth rig

        # chin
        mpy.parent(FR['chin'] + _grp, FR['jaw'] + _cnt)
        # jaw_root
        mouthDnRoot = FR['jaw'] + _root
        mouthDnRootCnt = FRPF_C.create_curve_cnt(mouthDnRoot + _cnt, typ='Triangle', r=_rad)
        mouthDnRootGrp = self.sdd_zeroSdkGrp(mouthDnRoot, mouthDnRootCnt)
        mpy.delete(mpy.parentConstraint(FR['jaw'] + _cnt, mouthDnRootGrp))
        mpy.parent(mouthDnRootGrp, faceSdkRigGrp)

        # mouth dn loc
        jawDnLoc = FR['jaw'] + _loc
        jawDnLoc = mpy.spaceLocator(n=jawDnLoc)[0]
        mpy.delete(mpy.parentConstraint(FR['jaw'] + _grp, jawDnLoc))
        mpy.parentConstraint(FR['jaw'] + _cnt, jawDnLoc)
        mpy.parent(jawDnLoc, FR['jaw'] + _grp, mouthDnRootGrp)
        mpy.setAttr(jawDnLoc + '.v', 0)

        # attr
        jawCnt = FR['jaw'] + _cnt
        mpy.addAttr(jawCnt, ln='__MouthFollow__', at='double', min=0, max=1, k=1)
        mpy.setAttr(jawCnt + '.' + '__MouthFollow__', l=1)

        mpy.addAttr(jawCnt, ln='Lip_Sticky', at='double', min=0, max=1, k=1)
        mpy.addAttr(jawCnt, ln='L_Lip_Corner', at='double', min=-1, max=1, k=1)
        mpy.addAttr(jawCnt, ln='R_Lip_Corner', at='double', min=-1, max=1, k=1)

        # attr
        mpy.addAttr(jawCnt, ln='__Hide__', at='double', min=0, max=1, k=1)
        mpy.setAttr(jawCnt + '.' + '__Hide__', l=1)
        mpy.addAttr(jawCnt, ln=FR['M_mouth_Up'], at='double', min=0, max=1, k=1)
        mpy.addAttr(jawCnt, ln=FR['L_mouth_Up'], at='double', min=0, max=1, k=1, dv=0.05)
        mpy.addAttr(jawCnt, ln=FR['R_mouth_Up'], at='double', min=0, max=1, k=1, dv=0.05)
        mpy.addAttr(jawCnt, ln=FR['L_mouth_Corner'], at='double', min=0, max=1, k=1, dv=0.5)
        mpy.addAttr(jawCnt, ln=FR['R_mouth_Corner'], at='double', min=0, max=1, k=1, dv=0.5)
        mpy.addAttr(jawCnt, ln=FR['M_mouth_Dn'], at='double', min=0, max=1, k=1, dv=1)
        mpy.addAttr(jawCnt, ln=FR['L_mouth_Dn'], at='double', min=0, max=1, k=1, dv=0.95)
        mpy.addAttr(jawCnt, ln=FR['R_mouth_Dn'], at='double', min=0, max=1, k=1, dv=0.95)
        mpy.addAttr(jawCnt, ln='Lip_Sticky_H', at='double', min=0, max=1, k=1)
        mpy.addAttr(jawCnt, ln='L_Lip_Corner_H', at='double', min=-1, max=1, k=1)
        mpy.addAttr(jawCnt, ln='R_Lip_Corner_H', at='double', min=-1, max=1, k=1)
        mpy.addAttr(jawCnt, ln='Lip_Sticky_P', at='double', min=0, max=1, k=1)
        mpy.addAttr(jawCnt, ln='L_Lip_Corner_P', at='double', min=-1, max=1, k=1)
        mpy.addAttr(jawCnt, ln='R_Lip_Corner_P', at='double', min=-1, max=1, k=1)

        sPlus = mpy.createNode('plusMinusAverage', n='Lip_Sticky' + '_plus')
        mpy.connectAttr(jawCnt + '.Lip_Sticky_P', sPlus + '.i1[0]')
        mpy.connectAttr(jawCnt + '.Lip_Sticky', sPlus + '.i1[1]')
        mpy.connectAttr(sPlus + '.output1D', jawCnt + '.Lip_Sticky_H')

        sPlus = mpy.createNode('plusMinusAverage', n='L_Lip_Corner' + '_plus')
        mpy.connectAttr(jawCnt + '.L_Lip_Corner_P', sPlus + '.i1[0]')
        mpy.connectAttr(jawCnt + '.L_Lip_Corner', sPlus + '.i1[1]')
        mpy.connectAttr(sPlus + '.output1D', jawCnt + '.L_Lip_Corner_H')

        sPlus = mpy.createNode('plusMinusAverage', n='R_Lip_Corner' + '_plus')
        mpy.connectAttr(jawCnt + '.R_Lip_Corner_P', sPlus + '.i1[0]')
        mpy.connectAttr(jawCnt + '.R_Lip_Corner', sPlus + '.i1[1]')
        mpy.connectAttr(sPlus + '.output1D', jawCnt + '.R_Lip_Corner_H')

        # M_mouth_Up
        mouthList = ['M_mouth_Up', 'L_mouth_Up', 'L_mouth_Corner', 'L_mouth_Dn', 'M_mouth_Dn', 'R_mouth_Dn',
                     'R_mouth_Corner', 'R_mouth_Up']
        for i in mouthList:
            baseName = FR[i]
            Root = baseName + _root
            RootGrp = self.sdd_zeroSdkGrp(Root, FR['jaw'] + _grp, FR[i] + _grp)
            mpy.parent(RootGrp, mouthDnRootCnt)

            btaNode = mpy.createNode('blendTwoAttr', n=i + '_bta')
            mpy.connectAttr(jawCnt + '.Lip_Sticky_H', btaNode + '.ab')
            mpy.connectAttr(jawCnt + '.' + i, btaNode + '.i[0]')
            mpy.setAttr(btaNode + '.i[1]', 0.5)

            TBc = mpy.createNode('blendColors', n=baseName + '_TBC')
            mpy.setAttr(TBc + '.c2', 0, 0, 0, typ='float3')
            mpy.connectAttr(jawDnLoc + '.t', TBc + '.c1')
            mpy.connectAttr(btaNode + '.o', TBc + '.b')
            RBc = mpy.createNode('blendColors', n=baseName + '_RBC')
            mpy.setAttr(RBc + '.c2', 0, 0, 0, typ='float3')
            mpy.connectAttr(jawDnLoc + '.r', RBc + '.c1')
            mpy.connectAttr(btaNode + '.o', RBc + '.b')
            CDt = mpy.createNode('condition', n=baseName + '_cdt')
            mpy.setAttr(CDt + '.op', 4)
            mpy.connectAttr(jawDnLoc + '.rx', CDt + '.ft')
            mpy.connectAttr(jawDnLoc + '.rx', CDt + '.ctr')
            mpy.connectAttr(RBc + '.opg', CDt + '.ctg')
            mpy.connectAttr(RBc + '.opb', CDt + '.ctb')
            mpy.connectAttr(RBc + '.op', CDt + '.cf')
            mpy.connectAttr(TBc + '.op', Root + _rig + '.t')
            mpy.connectAttr(CDt + '.oc', Root + _rig + '.r')

        lipMd = mpy.createNode('multiplyDivide', n='Lip_Corner_md')
        mpy.setAttr(lipMd + '.i1x', -1)
        mpy.setAttr(lipMd + '.i1y', -1)
        mpy.connectAttr(jawCnt + '.L_Lip_Corner_H', lipMd + '.i2x')
        mpy.connectAttr(jawCnt + '.R_Lip_Corner_H', lipMd + '.i2y')

        lCornerRv = mpy.createNode('remapValue', n=FR['L_mouth_Corner'] + '_rv')
        mpy.connectAttr(lipMd + '.ox', lCornerRv + '.i')
        mpy.setAttr(lCornerRv + '.imn', -1)
        mpy.connectAttr(lCornerRv + '.ov', FR['L_mouth_Corner'] + '_bta' + '.i[0]', f=1)

        lMouthUpRv = mpy.createNode('remapValue', n=FR['L_mouth_Up'] + '_rv')
        mpy.connectAttr(lipMd + '.ox', lMouthUpRv + '.i')
        mpy.setAttr(lMouthUpRv + '.imn', -1)
        mpy.setAttr(lMouthUpRv + '.imx', 0)
        mpy.connectAttr(jawCnt + '.L_mouth_Up', lMouthUpRv + '.omx')
        mpy.connectAttr(lMouthUpRv + '.ov', FR['L_mouth_Up'] + '_bta' + '.i[0]', f=1)

        lMouthDnRv = mpy.createNode('remapValue', n=FR['L_mouth_Dn'] + '_rv')
        mpy.connectAttr(lipMd + '.ox', lMouthDnRv + '.i')
        mpy.connectAttr(jawCnt + '.L_mouth_Dn', lMouthDnRv + '.omn')
        mpy.connectAttr(lMouthDnRv + '.ov', FR['L_mouth_Dn'] + '_bta' + '.i[0]', f=1)

        rCornerRv = mpy.createNode('remapValue', n=FR['R_mouth_Corner'] + '_rv')
        mpy.connectAttr(lipMd + '.oy', rCornerRv + '.i')
        mpy.setAttr(rCornerRv + '.imn', -1)
        mpy.connectAttr(rCornerRv + '.ov', FR['R_mouth_Corner'] + '_bta' + '.i[0]', f=1)

        rMouthUpRv = mpy.createNode('remapValue', n=FR['R_mouth_Up'] + '_rv')
        mpy.connectAttr(lipMd + '.oy', rMouthUpRv + '.i')
        mpy.setAttr(rMouthUpRv + '.imn', -1)
        mpy.setAttr(rMouthUpRv + '.imx', 0)
        mpy.connectAttr(jawCnt + '.R_mouth_Up', rMouthUpRv + '.omx')
        mpy.connectAttr(rMouthUpRv + '.ov', FR['R_mouth_Up'] + '_bta' + '.i[0]', f=1)

        rMouthDnRv = mpy.createNode('remapValue', n=FR['R_mouth_Dn'] + '_rv')
        mpy.connectAttr(lipMd + '.oy', rMouthDnRv + '.i')
        mpy.connectAttr(jawCnt + '.R_mouth_Dn', rMouthDnRv + '.omn')
        mpy.connectAttr(rMouthDnRv + '.ov', FR['R_mouth_Dn'] + '_bta' + '.i[0]', f=1)
        M_mouth_Up_base = self.head_bone_key_dir_reset[FR['M_mouth_Up'] + _base]
        M_mouth_Dn_base = self.head_bone_key_dir_reset[FR['M_mouth_Dn'] + _base]
        dis = self.sdd_getDistanceTwoPoint(M_mouth_Up_base, M_mouth_Dn_base)
        for i in mouthList:
            cnt = FR[i] + _cnt
            vtxList = mpy.ls(cnt + '.cv[*]')
            mpy.move(0, 0, dis * 0.3, vtxList, r=1, os=1, wd=1)

    def sdd_getDistanceTwoPoint(self, objList, objRoot):
        sel = mpy.ls(sl=1)
        grp = mpy.group(n='Tmp_arc_grp', em=1)
        mpy.delete(mpy.parentConstraint(objList, grp))
        p1 = mpy.xform(grp, q=1, ws=1, t=1)
        p2 = mpy.xform(objRoot, q=1, ws=1, t=1)
        mp1 = OpenMaya.MPoint(p1[0], p1[1], p1[2])
        mp2 = OpenMaya.MPoint(p2[0], p2[1], p2[2])
        dis = mp1.distanceTo(mp2)
        mpy.delete(grp)
        if (len(sel) != 0):
            mpy.select(sel)
        return round(dis, 2)

    def sdd_zeroSdkGrp(self, baseName, curName, grpName=None):
        T = self.returnTempNameDirc()
        FR, FRJntPos, FRUIPos = self.frTNameDirc()
        _rig = T['_rig']
        _sdk = T['_sdk']
        _grp = T['_grp']

        cursdk = mpy.group(n=baseName + _sdk, em=1)
        curRig = mpy.group(n=baseName + _rig, em=1)
        mpy.parent(curRig, cursdk)
        curGrp = mpy.group(n=baseName + _grp, em=1)
        mpy.parent(cursdk, curGrp)

        mpy.delete(mpy.parentConstraint(curName, curGrp))
        if (grpName == None):
            mpy.parent(curName, curRig)
        else:
            mpy.parent(grpName, curRig)
        return curGrp

    def frTNameDirc(self):
        # procName:labelName,jointPos,uiPos
        FR = {
            'head': 'head',
            'jaw': 'jaw',

            'chin': 'chin',
            'L_eyeBall': 'L_eyeBall',
            'R_eyeBall': 'R_eyeBall',

            'L_eye_root': 'L_eye_root',
            'R_eye_root': 'R_eye_root',

            'M_mouth_Up': 'M_mouth_Up',
            'L_mouth_Up': 'L_mouth_Up',
            'L_mouth_Corner': 'L_mouth_Corner',
            'L_mouth_Dn': 'L_mouth_Dn',
            'M_mouth_Dn': 'M_mouth_Dn',
            'R_mouth_Dn': 'R_mouth_Dn',
            'R_mouth_Corner': 'R_mouth_Corner',
            'R_mouth_Up': 'R_mouth_Up',

            'R_brow_c': 'R_brow_c',
            'R_brow_b': 'R_brow_b',
            'R_brow_a': 'R_brow_a',
            'M_brow': 'M_brow',

            'L_brow_a': 'L_brow_a',
            'L_brow_b': 'L_brow_b',
            'L_brow_c': 'L_brow_c',

            'L_eyelid_In': 'L_eyelid_In',
            'L_eyelid_UpIn': 'L_eyelid_UpIn',
            'L_eyelid_DnIn': 'L_eyelid_DnIn',
            'L_eyelid_Up': 'L_eyelid_Up',
            'L_eyelid_Dn': 'L_eyelid_Dn',
            'L_eyelid_UpOut': 'L_eyelid_UpOut',
            'L_eyelid_DnOut': 'L_eyelid_DnOut',
            'L_eyelid_Out': 'L_eyelid_Out',

            'R_eyelid_In': 'R_eyelid_In',
            'R_eyelid_UpIn': 'R_eyelid_UpIn',
            'R_eyelid_DnIn': 'R_eyelid_DnIn',
            'R_eyelid_Up': 'R_eyelid_Up',
            'R_eyelid_Dn': 'R_eyelid_Dn',
            'R_eyelid_UpOut': 'R_eyelid_UpOut',
            'R_eyelid_DnOut': 'R_eyelid_DnOut',
            'R_eyelid_Out': 'R_eyelid_Out',

            'M_nose': 'M_nose',
            'L_nose': 'L_nose',
            'R_nose': 'R_nose',
            'L_noseFold': 'L_noseFold',
            'R_noseFold': 'R_noseFold',

            'L_eyeSag_Up': 'L_eyeSag_Up',
            'R_eyeSag_Up': 'R_eyeSag_Up',

            'L_eyeSag_Dn': 'L_eyeSag_Dn',
            'R_eyeSag_Dn': 'R_eyeSag_Dn',

            'L_cheek_Up': 'L_cheek_Up',
            'L_cheek_In': 'L_cheek_In',
            'L_cheek_Out': 'L_cheek_Out',
            'R_cheek_Up': 'R_cheek_Up',
            'R_cheek_In': 'R_cheek_In',
            'R_cheek_Out': 'R_cheek_Out',

            'L_cheek': 'L_cheek',
            'R_cheek': 'R_cheek',

            'R_temple': 'R_temple',
            'L_temple': 'L_temple',

        }

        FRJntPos = {
            'head': [0, -3, 0],
            'jaw': [0, -2, 0.8],

            'chin': [0, -4, 4],
            'L_eyeBall': [1.3, 0, 2.6],
            'R_eyeBall': [-1.3, 0, 2.6],

            'L_eye_root': [1.3, 0, 2.6],
            'R_eye_root': [-1.3, 0, 2.6],

            'M_mouth_Up': [0, -2.4, 3.8],
            'L_mouth_Up': [0.45, -2.4, 3.7],
            'L_mouth_Corner': [0.8, -2.5, 3.5],
            'L_mouth_Dn': [0.45, -2.6, 3.7],
            'M_mouth_Dn': [0, -2.6, 3.8],
            'R_mouth_Dn': [-0.45, -2.6, 3.7],
            'R_mouth_Corner': [-0.8, -2.5, 3.5],
            'R_mouth_Up': [-0.45, -2.4, 3.7],

            'R_brow_c': [-2.3, 1, 3],
            'R_brow_b': [-1.65, 1, 3.65],
            'R_brow_a': [-0.7, 1, 4],
            'M_brow': [0, 1, 4],
            'L_brow_a': [0.7, 1, 4],
            'L_brow_b': [1.65, 1, 3.65],
            'L_brow_c': [2.3, 1, 3],

            'L_eyelid_In': [0.8, 0, 3.4],
            'L_eyelid_UpIn': [1, 0.2, 3.45],
            'L_eyelid_DnIn': [1, -0.2, 3.45],
            'L_eyelid_Up': [1.3, 0.25, 3.5],
            'L_eyelid_Dn': [1.3, -0.25, 3.5],
            'L_eyelid_UpOut': [1.6, 0.2, 3.45],
            'L_eyelid_DnOut': [1.6, -0.2, 3.45],
            'L_eyelid_Out': [1.8, 0, 3.4],

            'R_eyelid_In': [-0.8, 0, 3.4],
            'R_eyelid_UpIn': [-1, 0.2, 3.45],
            'R_eyelid_DnIn': [-1, -0.2, 3.45],
            'R_eyelid_Up': [-1.3, 0.25, 3.5],
            'R_eyelid_Dn': [-1.3, -0.25, 3.5],
            'R_eyelid_UpOut': [-1.6, 0.2, 3.45],
            'R_eyelid_DnOut': [-1.6, -0.2, 3.45],
            'R_eyelid_Out': [-1.8, 0, 3.4],

            'M_nose': [0, -1.5, 4],
            'L_nose': [0.4, -1.5, 3.7],
            'R_nose': [-0.4, -1.5, 3.7],
            'L_noseFold': [0.75, -1.65, 3.7],
            'R_noseFold': [-0.75, -1.65, 3.7],

            'L_eyeSag_Up': [1.3, 0.5, 3.4],
            'R_eyeSag_Up': [-1.3, 0.5, 3.4],

            'L_eyeSag_Dn': [1.3, -0.5, 3.4],
            'R_eyeSag_Dn': [-1.3, -0.5, 3.4],

            'L_cheek_Up': [1.3, -1, 3.4],
            'L_cheek_In': [0.5, -0.65, 3.4],
            'L_cheek_Out': [2, -0.65, 3.4],
            'R_cheek_Up': [-1.3, -1, 3.4],
            'R_cheek_In': [-0.5, -0.65, 3.4],
            'R_cheek_Out': [-2, -0.65, 3.4],

            'L_cheek': [2.5, -2, 3],
            'R_cheek': [-2.5, -2, 3],

            'R_temple': [-2.5, 1, 2],
            'L_temple': [2.5, 1, 2],

        }
        FRUIPos = {
            # procName: labelName,jointPos,uiPos ,
            'head': None,
            'jaw': None,

            'chin': [48, 90],

            'L_eyeBall': None,
            'R_eyeBall': None,

            'L_eye_root': [72, 35],
            'R_eye_root': [24, 35],

            'M_mouth_Up': [48, 69],
            'L_mouth_Up': [56, 69],
            'L_mouth_Corner': [63, 72],
            'L_mouth_Dn': [56, 76],
            'M_mouth_Dn': [48, 77],
            'R_mouth_Dn': [39, 75],
            'R_mouth_Corner': [33, 72],
            'R_mouth_Up': [40, 69],

            'R_brow_c': [12, 17],
            'R_brow_b': [24, 16],
            'R_brow_a': [38, 17],
            'M_brow': [48, 18],
            'L_brow_a': [58, 17],
            'L_brow_b': [72, 16],
            'L_brow_c': [86, 17],

            'L_eyelid_In': [60, 38],
            'L_eyelid_UpIn': [65, 32],
            'L_eyelid_DnIn': [65, 40],
            'L_eyelid_Up': [72, 30],
            'L_eyelid_Dn': [72, 40],
            'L_eyelid_UpOut': [79, 30],
            'L_eyelid_DnOut': [79, 38],
            'L_eyelid_Out': [84, 33],

            'R_eyelid_In': [37, 38],
            'R_eyelid_UpIn': [32, 32],
            'R_eyelid_DnIn': [32, 40],
            'R_eyelid_Up': [24, 30],
            'R_eyelid_Dn': [24, 40],
            'R_eyelid_UpOut': [18, 30],
            'R_eyelid_DnOut': [17, 38],
            'R_eyelid_Out': [12, 33],

            'M_nose': [48, 59],
            'L_nose': [55, 60],
            'R_nose': [41, 60],
            'L_noseFold': [61, 62],
            'R_noseFold': [35, 62],

            'L_eyeSag_Up': [72, 25],
            'R_eyeSag_Up': [24, 25],

            'L_eyeSag_Dn': [72, 44],
            'R_eyeSag_Dn': [24, 44],

            'L_cheek_Up': [72, 52],
            'L_cheek_In': [57, 46],
            'L_cheek_Out': [85, 46],
            'R_cheek_Up': [24, 52],
            'R_cheek_In': [40, 46],
            'R_cheek_Out': [12, 46],

            'L_cheek': [77, 66],
            'R_cheek': [19, 66],

            'R_temple': [8, 20],
            'L_temple': [90, 20],

        }
        return FR, FRJntPos, FRUIPos

    def connectAttrForce(self, attr1, attr2):
        cnn = mpy.listConnections(attr2, p=1)
        if (cnn != None):
            mpy.disconnectAttr(attr2, cnn[0])
        mpy.connectAttr(attr1, attr2, f=1)

    def reloadFaceMeshInfo(self):
        faceSdkRigGrp = 'face_sdk_rig_grp'
        if (mpy.objExists(faceSdkRigGrp)):
            mpy.button('frLoadAllMeshB', e=1, en=0)
            mpy.button('frSdkRiggingB', e=1, en=1, l='Reset Joint Position', c='sdd_resetJointPosition()')
        else:
            mpy.button('frLoadAllMeshB', e=1, en=1)
            mpy.button('frSdkRiggingB', e=1, en=1, l='Rigging', c='createSdkJntRig()')

        faceBsGrp = 'face_bs_grp'
        if not (mpy.objExists(faceBsGrp)):
            return
        faceSkinMeshGrp = 'face_skin_mesh_grp'
        if not (mpy.objExists(faceSkinMeshGrp)):
            return
        faceAllList = mpy.listRelatives(faceSkinMeshGrp, c=1)
        mpy.textScrollList('frFaceMeshTSL', e=1, ra=1)
        for i in faceAllList:
            mpy.textScrollList('frFaceMeshTSL', e=1, a=i)
        skinMesh = mpy.listConnections(faceSkinMeshGrp + '.faceMesh')[0]
        # origMeshName=mpy.listConnections(skinMesh+'.origMesh')[0]
        # if not(mpy.objExists(origMeshName)):
        #     return
        mpy.textField('frFaceMeshTF', e=1, tx=skinMesh)

    def importAndConnectPanel(self):
        global frRootPath
        T = self.returnTempNameDirc()
        FR, FRJntPos, FRUIPos = self.frTNameDirc()
        _root = T['_root']
        _sdk = T['_sdk']
        _cnt = T['_cnt']

        mpy.file(frRootPath + 'files/facePanel.ma', i=1, type="mayaAscii")
        faceCur = 'faceMoveCur'
        panelGrp = 'Face_Panel_grp'
        mpy.delete(mpy.parentConstraint(faceCur, panelGrp))
        bbox = self.getBoundingBox(faceCur)
        mpy.setAttr(panelGrp + '.tx', bbox[0])

        self.sdd_connectPanelAttr('M_brow_U', 'Face_M_brow_anim.ty', 1)
        self.sdd_connectPanelAttr('M_brow_D', 'Face_M_brow_anim.ty', -1)
        self.sdd_connectPanelAttr('L_brow_In_U', 'Face_L_brow_a_anim.ty', 1)
        self.sdd_connectPanelAttr('L_brow_In_D', 'Face_L_brow_a_anim.ty', -1)
        self.sdd_connectPanelAttr('L_brow_In_In', 'Face_L_brow_a_anim.tx', 1)
        self.sdd_connectPanelAttr('L_brow_Out_U', 'Face_L_brow_b_anim.ty', 1)
        self.sdd_connectPanelAttr('L_brow_Out_D', 'Face_L_brow_b_anim.ty', -1)

        self.sdd_connectPanelAttr('R_brow_In_U', 'Face_R_brow_a_anim.ty', 1)
        self.sdd_connectPanelAttr('R_brow_In_D', 'Face_R_brow_a_anim.ty', -1)
        self.sdd_connectPanelAttr('R_brow_In_In', 'Face_R_brow_a_anim.tx', 1)
        self.sdd_connectPanelAttr('R_brow_Out_U', 'Face_R_brow_b_anim.ty', 1)
        self.sdd_connectPanelAttr('R_brow_Out_D', 'Face_R_brow_b_anim.ty', -1)

        self.sdd_connectPanelAttr('L_brow_Mid_U', 'Face_L_brow_b_anim.rz', -15)
        self.sdd_connectPanelAttr('L_brow_Mid_D', 'Face_L_brow_b_anim.rz', 15)

        self.sdd_connectPanelAttr('R_brow_Mid_U', 'Face_R_brow_b_anim.rz', 15)
        self.sdd_connectPanelAttr('R_brow_Mid_D', 'Face_R_brow_b_anim.rz', -15)

        self.sdd_connectPanelAttr('L_eyelid_Up_U', 'Face_L_eyelid_Up_anim.ty', 1)
        self.sdd_connectPanelAttr('L_eyelid_Up_D', 'Face_L_eyelid_Up_anim.ty', -1)
        self.sdd_connectPanelAttr('L_eyelid_Dn_U', 'Face_L_eyelid_Dn_anim.ty', 1)
        self.sdd_connectPanelAttr('L_eyelid_Dn_D', 'Face_L_eyelid_Dn_anim.ty', -1)

        self.sdd_connectPanelAttr('R_eyelid_Up_U', 'Face_R_eyelid_Up_anim.ty', 1)
        self.sdd_connectPanelAttr('R_eyelid_Up_D', 'Face_R_eyelid_Up_anim.ty', -1)
        self.sdd_connectPanelAttr('R_eyelid_Dn_U', 'Face_R_eyelid_Dn_anim.ty', 1)
        self.sdd_connectPanelAttr('R_eyelid_Dn_D', 'Face_R_eyelid_Dn_anim.ty', -1)

        self.sdd_connectPanelAttr('L_eyelid_close', 'Face_L_eyelid_close_anim.ty', -1)
        self.sdd_connectPanelAttr('R_eyelid_close', 'Face_R_eyelid_close_anim.ty', -1)

        self.sdd_connectPanelAttr('L_eyelid_Squint', 'Face_L_squint_anim.tx', -1)
        self.sdd_connectPanelAttr('R_eyelid_Squint', 'Face_R_squint_anim.tx', -1)

        self.sdd_connectPanelAttr('L_eyelid_Up_side_O', 'Face_L_eyelid_Up_anim.tx', 1)
        self.sdd_connectPanelAttr('L_eyelid_Up_side_I', 'Face_L_eyelid_Up_anim.tx', -1)
        self.sdd_connectPanelAttr('L_eyelid_Dn_side_I', 'Face_L_eyelid_Dn_anim.tx', -1)
        self.sdd_connectPanelAttr('L_eyelid_Dn_side_O', 'Face_L_eyelid_Dn_anim.tx', 1)

        self.sdd_connectPanelAttr('R_eyelid_Up_side_O', 'Face_R_eyelid_Up_anim.tx', 1)
        self.sdd_connectPanelAttr('R_eyelid_Up_side_I', 'Face_R_eyelid_Up_anim.tx', -1)
        self.sdd_connectPanelAttr('R_eyelid_Dn_side_I', 'Face_R_eyelid_Dn_anim.tx', -1)
        self.sdd_connectPanelAttr('R_eyelid_Dn_side_O', 'Face_R_eyelid_Dn_anim.tx', 1)

        self.sdd_connectPanelAttr('L_mouth_corner_O', 'Face_L_mouth_anim.txLink', 1)
        self.sdd_connectPanelAttr('L_mouth_corner_I', 'Face_L_mouth_anim.txLink', -1)
        self.sdd_connectPanelAttr('L_mouth_corner_U', 'Face_L_mouth_anim.tyLink', 1)
        self.sdd_connectPanelAttr('L_mouth_corner_D', 'Face_L_mouth_anim.tyLink', -1)

        self.sdd_connectPanelAttr('R_mouth_corner_O', 'Face_R_mouth_anim.txLink', 1)
        self.sdd_connectPanelAttr('R_mouth_corner_I', 'Face_R_mouth_anim.txLink', -1)
        self.sdd_connectPanelAttr('R_mouth_corner_U', 'Face_R_mouth_anim.tyLink', 1)
        self.sdd_connectPanelAttr('R_mouth_corner_D', 'Face_R_mouth_anim.tyLink', -1)

        self.sdd_connectPanelAttr('L_mouth_Up_U', 'Face_L_lip_side_Up_anim.ty', 1)
        self.sdd_connectPanelAttr('L_mouth_Up_D', 'Face_L_lip_side_Up_anim.ty', -1)
        self.sdd_connectPanelAttr('L_mouth_Dn_U', 'Face_L_lip_side_Dn_anim.ty', 1)
        self.sdd_connectPanelAttr('L_mouth_Dn_D', 'Face_L_lip_side_Dn_anim.ty', -1)

        self.sdd_connectPanelAttr('R_mouth_Up_U', 'Face_R_lip_side_Up_anim.ty', 1)
        self.sdd_connectPanelAttr('R_mouth_Up_D', 'Face_R_lip_side_Up_anim.ty', -1)
        self.sdd_connectPanelAttr('R_mouth_Dn_U', 'Face_R_lip_side_Dn_anim.ty', 1)
        self.sdd_connectPanelAttr('R_mouth_Dn_D', 'Face_R_lip_side_Dn_anim.ty', -1)

        self.sdd_connectPanelAttr('mouth_Up_roll_O', 'Face_lip_roll_Up_anim.ty', 1)
        self.sdd_connectPanelAttr('mouth_Up_roll_I', 'Face_lip_roll_Up_anim.ty', -1)
        self.sdd_connectPanelAttr('mouth_Dn_roll_O', 'Face_lip_roll_Dn_anim.ty', 1)
        self.sdd_connectPanelAttr('mouth_Dn_roll_I', 'Face_lip_roll_Dn_anim.ty', -1)

        self.sdd_connectPanelAttr('mouth_A', 'Face_L_mouth_A_anim.tx', 1)
        self.sdd_connectPanelAttr('mouth_E', 'Face_L_mouth_E_anim.tx', 1)
        self.sdd_connectPanelAttr('mouth_F', 'Face_L_mouth_F_anim.tx', 1)
        self.sdd_connectPanelAttr('mouth_H', 'Face_L_mouth_H_anim.tx', 1)
        self.sdd_connectPanelAttr('mouth_M', 'Face_L_mouth_M_anim.tx', 1)
        self.sdd_connectPanelAttr('mouth_O', 'Face_L_mouth_O_anim.tx', 1)
        self.sdd_connectPanelAttr('mouth_U', 'Face_L_mouth_U_anim.tx', 1)

        self.sdd_connectPanelAttr('L_eyeBall_U', 'Face_L_eye_anim.ty', 1)
        self.sdd_connectPanelAttr('L_eyeBall_D', 'Face_L_eye_anim.ty', -1)
        self.sdd_connectPanelAttr('L_eyeBall_O', 'Face_L_eye_anim.tx', 1)
        self.sdd_connectPanelAttr('L_eyeBall_I', 'Face_L_eye_anim.tx', -1)

        self.sdd_connectPanelAttr('R_eyeBall_U', 'Face_R_eye_anim.ty', 1)
        self.sdd_connectPanelAttr('R_eyeBall_D', 'Face_R_eye_anim.ty', -1)
        self.sdd_connectPanelAttr('R_eyeBall_I', 'Face_R_eye_anim.tx', 1)
        self.sdd_connectPanelAttr('R_eyeBall_O', 'Face_R_eye_anim.tx', -1)

        self.sdd_connectPanelAttr('L_eyeAll_U', 'Face_L_eye_all_anim.ty', 1)
        self.sdd_connectPanelAttr('L_eyeAll_D', 'Face_L_eye_all_anim.ty', -1)
        self.sdd_connectPanelAttr('L_eyeAll_O', 'Face_L_eye_all_anim.tx', 1)
        self.sdd_connectPanelAttr('L_eyeAll_I', 'Face_L_eye_all_anim.tx', -1)

        mpy.connectAttr('Face_L_eye_all_anim.sx', FR['L_eye_root'] + _sdk + '.sx')
        mpy.connectAttr('Face_L_eye_all_anim.sy', FR['L_eye_root'] + _sdk + '.sy')

        self.sdd_connectPanelAttr('R_eyeAll_U', 'Face_R_eye_all_anim.ty', 1)
        self.sdd_connectPanelAttr('R_eyeAll_D', 'Face_R_eye_all_anim.ty', -1)
        self.sdd_connectPanelAttr('R_eyeAll_O', 'Face_R_eye_all_anim.tx', 1)
        self.sdd_connectPanelAttr('R_eyeAll_I', 'Face_R_eye_all_anim.tx', -1)
        mpy.connectAttr('Face_R_eye_all_anim.sx', FR['R_eye_root'] + _sdk + '.sx')
        mpy.connectAttr('Face_R_eye_all_anim.sy', FR['R_eye_root'] + _sdk + '.sy')

        mpy.connectAttr('Face_mouth_all_anim.sx', FR['jaw'] + _root + _sdk + '.sx')
        mpy.connectAttr('Face_mouth_all_anim.sy', FR['jaw'] + _root + _sdk + '.sy')

        self.sdd_connectPanelAttr('M_nose_U', 'Face_nose_anim.ty', 1)
        self.sdd_connectPanelAttr('M_nose_D', 'Face_nose_anim.ty', -1)
        self.sdd_connectPanelAttr('M_nose_L', 'Face_nose_anim.tx', 1)
        self.sdd_connectPanelAttr('M_nose_R', 'Face_nose_anim.tx', -1)

        self.sdd_connectPanelAttr('L_nose_U', 'Face_L_nose_anim.ty', 1)
        self.sdd_connectPanelAttr('L_nose_D', 'Face_L_nose_anim.ty', -1)
        self.sdd_connectPanelAttr('L_nose_O', 'Face_L_nose_anim.tx', 1)
        self.sdd_connectPanelAttr('L_nose_I', 'Face_L_nose_anim.tx', -1)

        self.sdd_connectPanelAttr('R_nose_U', 'Face_R_nose_anim.ty', 1)
        self.sdd_connectPanelAttr('R_nose_D', 'Face_R_nose_anim.ty', -1)
        self.sdd_connectPanelAttr('R_nose_O', 'Face_R_nose_anim.tx', 1)
        self.sdd_connectPanelAttr('R_nose_I', 'Face_R_nose_anim.tx', -1)

        self.sdd_connectPanelAttr('L_cheek_U', 'Face_L_cheek_anim.ty', 1)
        self.sdd_connectPanelAttr('L_cheek_O', 'Face_L_cheek_anim.tx', 1)
        self.sdd_connectPanelAttr('L_cheek_I', 'Face_L_cheek_anim.tx', -1)

        self.sdd_connectPanelAttr('R_cheek_U', 'Face_R_cheek_anim.ty', 1)
        self.sdd_connectPanelAttr('R_cheek_O', 'Face_R_cheek_anim.tx', 1)
        self.sdd_connectPanelAttr('R_cheek_I', 'Face_R_cheek_anim.tx', -1)

        mpy.connectAttr('Face_mouth_sticky_anim.ty', FR['jaw'] + _cnt + '.Lip_Sticky_P')
        mpy.connectAttr('Face_L_lip_corner_anim.ty', FR['jaw'] + _cnt + '.L_Lip_Corner_P')
        mpy.connectAttr('Face_R_lip_corner_anim.ty', FR['jaw'] + _cnt + '.R_Lip_Corner_P')

        self.sdd_connectPanelAttr('M_jaw_U', 'Face_jaw_anim.ty', 1)
        self.sdd_connectPanelAttr('M_jaw_D', 'Face_jaw_anim.ty', -1)
        self.sdd_connectPanelAttr('M_jaw_L', 'Face_jaw_anim.tx', 1)
        self.sdd_connectPanelAttr('M_jaw_R', 'Face_jaw_anim.tx', -1)

        self.sdd_connectPanelAttr('M_jaw_all_U', 'Face_mouth_all_anim.ty', 1)
        self.sdd_connectPanelAttr('M_jaw_all_D', 'Face_mouth_all_anim.ty', -1)
        self.sdd_connectPanelAttr('M_jaw_all_L', 'Face_mouth_all_anim.tx', 1)
        self.sdd_connectPanelAttr('M_jaw_all_R', 'Face_mouth_all_anim.tx', -1)

        self.sdd_connectPanelAttr('M_mouth_Up_U', 'Face_lip_open_Up_anim.ty', 1)
        self.sdd_connectPanelAttr('M_mouth_Dn_U', 'Face_lip_open_Dn_anim.ty', 1)
        self.sdd_connectPanelAttr('M_mouth_Dn_D', 'Face_lip_open_Dn_anim.ty', -1)

        self.sdd_connectPanelAttr('L_pump_O', 'Face_L_Pump_anim.tx', 1)
        self.sdd_connectPanelAttr('R_pump_O', 'Face_R_Pump_anim.tx', 1)

    def sdd_connectPanelAttr(self, sdkAttr, pCtrlAttr, dv, v=None):
        faceSdkHandle = 'face_sdk_handle'
        if not (mpy.objExists(faceSdkHandle)):
            return
        if (v == None):
            v = 1
        mpy.setDrivenKeyframe(faceSdkHandle + '.' + sdkAttr, cd=pCtrlAttr, v=0, dv=0, itt='linear', ott='linear')
        mpy.setDrivenKeyframe(faceSdkHandle + '.' + sdkAttr, cd=pCtrlAttr, v=v, dv=dv, itt='linear', ott='linear')

    def tryAddMessageAttr(self, i, attr):
        attrList = mpy.listAttr(i, ud=1)
        if (attrList == None or not (attr in attrList)):
            mpy.addAttr(i, ln=attr, dt='string')
        return i + '.' + attr

    def sdd_createDefultSdk(self):
        FR, _sdk, _root, _cnt, faceSdkHandle = self.sdd_getDefultSdkName()
        faceBaseGrp = 'face_base_rig_grp'
        if (not mpy.objExists(faceBaseGrp)):
            return
        faceSdkHandle = mpy.group(n=faceSdkHandle, em=1)
        mpy.parent(faceSdkHandle, faceBaseGrp)
        attrList = ['tx', 'ty', 'tz', 'rx', 'ry', 'rz', 'sx', 'sy', 'sz', 'v']
        self.sdd_frLockAndAttr(faceSdkHandle, attrList)
        self.sdd_browDefultSdk()
        self.sdd_eyeballDefultSdk()
        self.sdd_eyelidDefultSdk()
        self.sdd_noseDefultSdk()
        self.sdd_cheekDefultSdk()
        self.sdd_mouthDefultSdk()
        self.sdd_mouthShapeDefultSdk()

    @staticmethod
    def sdd_frLockAndAttr(obj, attrList):
        for i in attrList:
            mpy.setAttr(obj + '.' + i, l=1, k=0)

    @staticmethod
    def sdd_browDefultSdk():
        FR, _sdk, _root, _cnt, faceSdkHandle = self.sdd_getDefultSdkName()

        # brow
        mpy.addAttr(faceSdkHandle, ln='______brow________', at='double', min=0, max=0, k=0)
        mpy.setAttr(faceSdkHandle + '.' + '______brow________', cb=1)

        dis = sdd_getDistanceTwoPoint([FR['M_brow'] + _cnt], FR['L_brow_a'] + _cnt)

        cdAttr = sdd_addAttrToHandle('M_brow_U', None, faceSdkHandle)
        self.sdd_setDrivenKeyframe(FR['M_brow'] + _sdk, 'ty', dis, faceSdkHandle, cdAttr, 1)
        cdAttr = sdd_addAttrToHandle('M_brow_D', None, faceSdkHandle)
        self.sdd_setDrivenKeyframe(FR['M_brow'] + _sdk, 'ty', -dis, faceSdkHandle, cdAttr, 1)

        cdAttr, mircdAttr = sdd_addAttrToHandle('L_brow_In_U', 'R_brow_In_U', faceSdkHandle)
        self.sdd_setDrivenKeyframe(FR['L_brow_a'] + _sdk, 'ty', dis, faceSdkHandle, cdAttr, 1, mircdAttr)
        self.sdd_setDrivenKeyframe(FR['L_brow_b'] + _sdk, 'ty', dis * 0.5, faceSdkHandle, cdAttr, 1, mircdAttr)

        cdAttr, mircdAttr = sdd_addAttrToHandle('L_brow_In_D', 'R_brow_In_D', faceSdkHandle)
        self.sdd_setDrivenKeyframe(FR['L_brow_a'] + _sdk, 'ty', -dis, faceSdkHandle, cdAttr, 1, mircdAttr)
        self.sdd_setDrivenKeyframe(FR['L_brow_b'] + _sdk, 'ty', -dis * 0.5, faceSdkHandle, cdAttr, 1, mircdAttr)

        cdAttr, mircdAttr = sdd_addAttrToHandle('L_brow_Out_U', 'R_brow_Out_U', faceSdkHandle)
        self.sdd_setDrivenKeyframe(FR['L_brow_c'] + _sdk, 'ty', dis, faceSdkHandle, cdAttr, 1, mircdAttr)
        self.sdd_setDrivenKeyframe(FR['L_brow_b'] + _sdk, 'ty', dis * 0.5, faceSdkHandle, cdAttr, 1, mircdAttr)

        cdAttr, mircdAttr = sdd_addAttrToHandle('L_brow_Out_D', 'R_brow_Out_D', faceSdkHandle)
        self.sdd_setDrivenKeyframe(FR['L_brow_c'] + _sdk, 'ty', -dis, faceSdkHandle, cdAttr, 1, mircdAttr)
        self.sdd_setDrivenKeyframe(FR['L_brow_b'] + _sdk, 'ty', -dis * 0.5, faceSdkHandle, cdAttr, 1, mircdAttr)

        cdAttr, mircdAttr = sdd_addAttrToHandle('L_brow_Mid_U', 'R_brow_Mid_U', faceSdkHandle)
        self.sdd_setDrivenKeyframe(FR['L_brow_b'] + _sdk, 'ty', dis * 0.5, faceSdkHandle, cdAttr, 1, mircdAttr)

        cdAttr, mircdAttr = sdd_addAttrToHandle('L_brow_Mid_D', 'R_brow_Mid_D', faceSdkHandle)
        self.sdd_setDrivenKeyframe(FR['L_brow_b'] + _sdk, 'ty', -dis * 0.5, faceSdkHandle, cdAttr, 1, mircdAttr)

        cdAttr, mircdAttr = sdd_addAttrToHandle('L_brow_In_In', 'R_brow_In_In', faceSdkHandle)
        self.sdd_setDrivenKeyframe(FR['L_brow_a'] + _sdk, 'tx', -dis * 0.5, faceSdkHandle, cdAttr, 1, mircdAttr)

    @staticmethod
    def sdd_eyeballDefultSdk():
        FR, _sdk, _root, _cnt, faceSdkHandle = self.sdd_getDefultSdkName()

        # eyeball
        dis = sdd_getDistanceTwoPoint([FR['R_eyeBall'] + _cnt], FR['L_eyeBall'] + _cnt)
        mpy.addAttr(faceSdkHandle, ln='______eyeBall______', at='double', min=0, max=0, k=0)
        mpy.setAttr(faceSdkHandle + '.______eyeBall______', cb=1)
        cdAttr, mircdAttr = sdd_addAttrToHandle('L_eyeBall_U', 'R_eyeBall_U', faceSdkHandle)
        self.sdd_setDrivenKeyframe(FR['L_eyeBall'] + _sdk, 'rx', -70, faceSdkHandle, cdAttr, 1, mircdAttr)
        cdAttr, mircdAttr = sdd_addAttrToHandle('L_eyeBall_D', 'R_eyeBall_D', faceSdkHandle)
        self.sdd_setDrivenKeyframe(FR['L_eyeBall'] + _sdk, 'rx', 70, faceSdkHandle, cdAttr, 1, mircdAttr)
        cdAttr, mircdAttr = sdd_addAttrToHandle('L_eyeBall_O', 'R_eyeBall_O', faceSdkHandle)
        self.sdd_setDrivenKeyframe(FR['L_eyeBall'] + _sdk, 'ry', 70, faceSdkHandle, cdAttr, 1, mircdAttr)
        cdAttr, mircdAttr = sdd_addAttrToHandle('L_eyeBall_I', 'R_eyeBall_I', faceSdkHandle)
        self.sdd_setDrivenKeyframe(FR['L_eyeBall'] + _sdk, 'ry', -70, faceSdkHandle, cdAttr, 1, mircdAttr)

        cdAttr, mircdAttr = sdd_addAttrToHandle('L_eyeAll_U', 'R_eyeAll_U', faceSdkHandle)
        self.sdd_setDrivenKeyframe(FR['L_eye_root'] + _sdk, 'ty', dis * 0.25, faceSdkHandle, cdAttr, 1, mircdAttr)
        cdAttr, mircdAttr = sdd_addAttrToHandle('L_eyeAll_D', 'R_eyeAll_D', faceSdkHandle)
        self.sdd_setDrivenKeyframe(FR['L_eye_root'] + _sdk, 'ty', -dis * 0.25, faceSdkHandle, cdAttr, 1, mircdAttr)
        cdAttr, mircdAttr = sdd_addAttrToHandle('L_eyeAll_O', 'R_eyeAll_O', faceSdkHandle)
        self.sdd_setDrivenKeyframe(FR['L_eye_root'] + _sdk, 'tx', dis * 0.25, faceSdkHandle, cdAttr, 1, mircdAttr)
        cdAttr, mircdAttr = sdd_addAttrToHandle('L_eyeAll_I', 'R_eyeAll_I', faceSdkHandle)
        self.sdd_setDrivenKeyframe(FR['L_eye_root'] + _sdk, 'tx', -dis * 0.25, faceSdkHandle, cdAttr, 1, mircdAttr)

    @staticmethod
    def sdd_eyelidDefultSdk():
        FR, _sdk, _root, _cnt, faceSdkHandle = self.sdd_getDefultSdkName()
        # eyelid
        mpy.addAttr(faceSdkHandle, ln='______eyelid______', at='double', min=0, max=0, k=0)
        mpy.setAttr(faceSdkHandle + '.______eyelid______', cb=1)

        arcMid = sdd_getAngleThreePoint(FR['L_eyelid_Up'] + _cnt, FR['L_eye_root'] + _cnt, FR['L_eyelid_Dn'] + _cnt)

        cdAttr, mircdAttr = sdd_addAttrToHandle('L_eyelid_Up_U', 'R_eyelid_Up_U', faceSdkHandle)
        self.sdd_setDrivenKeyframe(FR['L_eyelid_Up'] + _root + _sdk, 'rx', -5, faceSdkHandle, cdAttr, 1, mircdAttr)

        cdAttr, mircdAttr = sdd_addAttrToHandle('L_eyelid_Up_D', 'R_eyelid_Up_D', faceSdkHandle)
        self.sdd_setDrivenKeyframe(FR['L_eyelid_Up'] + _root + _sdk, 'rx', arcMid + 2, faceSdkHandle, cdAttr, 1,
                                   mircdAttr)

        cdAttr, mircdAttr = sdd_addAttrToHandle('L_eyelid_Dn_U', 'R_eyelid_Dn_U', faceSdkHandle)
        self.sdd_setDrivenKeyframe(FR['L_eyelid_Dn'] + _root + _sdk, 'rx', -arcMid - 2, faceSdkHandle, cdAttr, 1,
                                   mircdAttr)

        cdAttr, mircdAttr = sdd_addAttrToHandle('L_eyelid_Dn_D', 'R_eyelid_Dn_D', faceSdkHandle)
        self.sdd_setDrivenKeyframe(FR['L_eyelid_Dn'] + _root + _sdk, 'rx', 5, faceSdkHandle, cdAttr, 1, mircdAttr)

        cdAttr, mircdAttr = sdd_addAttrToHandle('L_eyelid_Up_side_O', 'R_eyelid_Up_side_O', faceSdkHandle)
        self.sdd_setDrivenKeyframe(FR['L_eyelid_UpIn'] + _root + _sdk, 'rx', 15, faceSdkHandle, cdAttr, 1, mircdAttr)
        self.sdd_setDrivenKeyframe(FR['L_eyelid_Up'] + _sdk, 'rz', 15, faceSdkHandle, cdAttr, 1, mircdAttr)
        self.sdd_setDrivenKeyframe(FR['L_eyelid_UpOut'] + _root + _sdk, 'rx', -15, faceSdkHandle, cdAttr, 1, mircdAttr)

        cdAttr, mircdAttr = sdd_addAttrToHandle('L_eyelid_Up_side_I', 'R_eyelid_Up_side_I', faceSdkHandle)
        self.sdd_setDrivenKeyframe(FR['L_eyelid_UpIn'] + _root + _sdk, 'rx', -15, faceSdkHandle, cdAttr, 1, mircdAttr)
        self.sdd_setDrivenKeyframe(FR['L_eyelid_Up'] + _sdk, 'rz', -15, faceSdkHandle, cdAttr, 1, mircdAttr)
        self.sdd_setDrivenKeyframe(FR['L_eyelid_UpOut'] + _root + _sdk, 'rx', 15, faceSdkHandle, cdAttr, 1, mircdAttr)

        cdAttr, mircdAttr = sdd_addAttrToHandle('L_eyelid_Dn_side_O', 'R_eyelid_Dn_side_O', faceSdkHandle)
        self.sdd_setDrivenKeyframe(FR['L_eyelid_DnIn'] + _root + _sdk, 'rx', -15, faceSdkHandle, cdAttr, 1, mircdAttr)
        self.sdd_setDrivenKeyframe(FR['L_eyelid_Dn'] + _sdk, 'rz', -15, faceSdkHandle, cdAttr, 1, mircdAttr)
        self.sdd_setDrivenKeyframe(FR['L_eyelid_DnOut'] + _root + _sdk, 'rx', 15, faceSdkHandle, cdAttr, 1, mircdAttr)

        cdAttr, mircdAttr = sdd_addAttrToHandle('L_eyelid_Dn_side_I', 'R_eyelid_Dn_side_I', faceSdkHandle)
        self.sdd_setDrivenKeyframe(FR['L_eyelid_DnIn'] + _root + _sdk, 'rx', 15, faceSdkHandle, cdAttr, 1, mircdAttr)
        self.sdd_setDrivenKeyframe(FR['L_eyelid_Dn'] + _sdk, 'rz', 15, faceSdkHandle, cdAttr, 1, mircdAttr)
        self.sdd_setDrivenKeyframe(FR['L_eyelid_DnOut'] + _root + _sdk, 'rx', -15, faceSdkHandle, cdAttr, 1, mircdAttr)

        cdAttr, mircdAttr = sdd_addAttrToHandle('L_eyelid_close', 'R_eyelid_close', faceSdkHandle)
        self.sdd_setDrivenKeyframe(FR['L_eyelid_Up'] + _root + _sdk, 'rx', (arcMid + 2) * 0.7, faceSdkHandle, cdAttr, 1,
                                   mircdAttr)
        self.sdd_setDrivenKeyframe(FR['L_eyelid_Dn'] + _root + _sdk, 'rx', (-arcMid - 2) * 0.3, faceSdkHandle, cdAttr,
                                   1,
                                   mircdAttr)

        cdAttr, mircdAttr = sdd_addAttrToHandle('L_eyelid_Squint', 'R_eyelid_Squint', faceSdkHandle)
        self.sdd_setDrivenKeyframe(FR['L_eyelid_Up'] + _root + _sdk, 'rx', (arcMid + 2) * 0.7, faceSdkHandle, cdAttr, 1,
                                   mircdAttr)
        self.sdd_setDrivenKeyframe(FR['L_eyelid_Dn'] + _root + _sdk, 'rx', (-arcMid - 2) * 0.3, faceSdkHandle, cdAttr,
                                   1,
                                   mircdAttr)
        dis = sdd_getDistanceTwoPoint([FR['M_brow'] + _cnt], FR['L_brow_a'] + _cnt)
        self.sdd_setDrivenKeyframe(FR['L_brow_a'] + _sdk, 'ty', -dis, faceSdkHandle, cdAttr, 1, mircdAttr)
        self.sdd_setDrivenKeyframe(FR['L_brow_b'] + _sdk, 'ty', -dis, faceSdkHandle, cdAttr, 1, mircdAttr)
        self.sdd_setDrivenKeyframe(FR['L_brow_c'] + _sdk, 'ty', -dis, faceSdkHandle, cdAttr, 1, mircdAttr)
        dis = sdd_getDistanceTwoPoint([FR['L_eyeSag_Up'] + _cnt], FR['L_brow_b'] + _cnt)
        self.sdd_setDrivenKeyframe(FR['L_eyeSag_Up'] + _sdk, 'ty', -dis, faceSdkHandle, cdAttr, 1, mircdAttr)
        dis = sdd_getDistanceTwoPoint([FR['L_eyeSag_Dn'] + _cnt], FR['L_cheek_Up'] + _cnt)
        self.sdd_setDrivenKeyframe(FR['L_eyeSag_Dn'] + _sdk, 'ty', dis * 0.5, faceSdkHandle, cdAttr, 1, mircdAttr)
        self.sdd_setDrivenKeyframe(FR['L_cheek_Up'] + _sdk, 'ty', dis * 0.7, faceSdkHandle, cdAttr, 1, mircdAttr)
        self.sdd_setDrivenKeyframe(FR['L_cheek_Out'] + _sdk, 'ty', dis * 0.7, faceSdkHandle, cdAttr, 1, mircdAttr)

    @staticmethod
    def sdd_noseDefultSdk():
        FR, _sdk, _root, _cnt, faceSdkHandle = self.sdd_getDefultSdkName()
        # nose
        mpy.addAttr(faceSdkHandle, ln='______nose________', at='double', min=0, max=0, k=0)
        mpy.setAttr(faceSdkHandle + '.______nose________', cb=1)

        cdAttr = sdd_addAttrToHandle('M_nose_U', None, faceSdkHandle)
        self.sdd_setDrivenKeyframe(FR['M_nose'] + _root + _sdk, 'rx', -30, faceSdkHandle, cdAttr, 1)
        cdAttr = sdd_addAttrToHandle('M_nose_D', None, faceSdkHandle)
        self.sdd_setDrivenKeyframe(FR['M_nose'] + _root + _sdk, 'rx', 15, faceSdkHandle, cdAttr, 1)
        cdAttr = sdd_addAttrToHandle('M_nose_L', None, faceSdkHandle)
        self.sdd_setDrivenKeyframe(FR['M_nose'] + _root + _sdk, 'rz', 30, faceSdkHandle, cdAttr, 1)
        cdAttr = sdd_addAttrToHandle('M_nose_R', None, faceSdkHandle)
        self.sdd_setDrivenKeyframe(FR['M_nose'] + _root + _sdk, 'rz', -30, faceSdkHandle, cdAttr, 1)

        dis = sdd_getDistanceTwoPoint([FR['L_nose'] + _cnt], FR['R_nose'] + _cnt)

        cdAttr, mircdAttr = sdd_addAttrToHandle('L_nose_U', 'R_nose_U', faceSdkHandle)
        self.sdd_setDrivenKeyframe(FR['L_nose'] + _sdk, 'ty', dis * 0.25, faceSdkHandle, cdAttr, 1, mircdAttr)
        cdAttr, mircdAttr = sdd_addAttrToHandle('L_nose_D', 'R_nose_D', faceSdkHandle)
        self.sdd_setDrivenKeyframe(FR['L_nose'] + _sdk, 'ty', -dis * 0.25, faceSdkHandle, cdAttr, 1, mircdAttr)
        cdAttr, mircdAttr = sdd_addAttrToHandle('L_nose_O', 'R_nose_O', faceSdkHandle)
        self.sdd_setDrivenKeyframe(FR['L_nose'] + _sdk, 'tx', dis * 0.25, faceSdkHandle, cdAttr, 1, mircdAttr)
        cdAttr, mircdAttr = sdd_addAttrToHandle('L_nose_I', 'R_nose_I', faceSdkHandle)
        self.sdd_setDrivenKeyframe(FR['L_nose'] + _sdk, 'tx', -dis * 0.25, faceSdkHandle, cdAttr, 1, mircdAttr)

    @staticmethod
    def sdd_cheekDefultSdk():
        FR, _sdk, _root, _cnt, faceSdkHandle = self.sdd_getDefultSdkName()
        # cheek
        mpy.addAttr(faceSdkHandle, ln='______cheek_______', at='double', min=0, max=0, k=0)
        mpy.setAttr(faceSdkHandle + '.______cheek_______', cb=1)

        dis = sdd_getDistanceTwoPoint([FR['L_cheek'] + _cnt], FR['R_cheek'] + _cnt)

        cdAttr, mircdAttr = sdd_addAttrToHandle('L_cheek_U', 'R_cheek_U', faceSdkHandle)
        self.sdd_setDrivenKeyframe(FR['L_cheek'] + _sdk, 'ty', dis * 0.1, faceSdkHandle, cdAttr, 1, mircdAttr)
        # self.sdd_setDrivenKeyframe(FR['L_cheek_Up']+_sdk,'ty',dis*0.05,faceSdkHandle,cdAttr,1,mircdAttr)

        cdAttr, mircdAttr = sdd_addAttrToHandle('L_cheek_O', 'R_cheek_O', faceSdkHandle)
        self.sdd_setDrivenKeyframe(FR['L_cheek'] + _sdk, 'tx', dis * 0.1, faceSdkHandle, cdAttr, 1, mircdAttr)

        cdAttr, mircdAttr = sdd_addAttrToHandle('L_cheek_I', 'R_cheek_I', faceSdkHandle)
        self.sdd_setDrivenKeyframe(FR['L_cheek'] + _sdk, 'tx', -dis * 0.1, faceSdkHandle, cdAttr, 1, mircdAttr)

        cdAttr, mircdAttr = sdd_addAttrToHandle('L_pump_O', 'R_pump_O', faceSdkHandle)
        self.sdd_setDrivenKeyframe(FR['L_cheek'] + _sdk, 'tx', dis * 0.15, faceSdkHandle, cdAttr, 1, mircdAttr)

    @staticmethod
    def sdd_mouthDefultSdk():
        FR, _sdk, _root, _cnt, faceSdkHandle = self.sdd_getDefultSdkName()
        # mouth
        mpy.addAttr(faceSdkHandle, ln='______jaw_________', at='double', min=0, max=0, k=0)
        mpy.setAttr(faceSdkHandle + '.______jaw_________', cb=1)

        dis = sdd_getDistanceTwoPoint([FR['M_mouth_Up'] + _cnt], FR['M_mouth_Dn'] + _cnt)

        cdAttr = sdd_addAttrToHandle('M_jaw_U', None, faceSdkHandle)
        self.sdd_setDrivenKeyframe(FR['jaw'] + _sdk, 'rx', -5, faceSdkHandle, cdAttr, 0.5)
        cdAttr = sdd_addAttrToHandle('M_jaw_D', None, faceSdkHandle)
        self.sdd_setDrivenKeyframe(FR['jaw'] + _sdk, 'rx', 30, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['L_mouth_Corner'] + _sdk, 'tz', -dis * 0.2, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['R_mouth_Corner'] + _sdk, 'tz', -dis * 0.2, faceSdkHandle, cdAttr, 1)

        cdAttr = sdd_addAttrToHandle('M_jaw_L', None, faceSdkHandle)
        self.sdd_setDrivenKeyframe(FR['jaw'] + _sdk, 'ry', 20, faceSdkHandle, cdAttr, 1)
        cdAttr = sdd_addAttrToHandle('M_jaw_R', None, faceSdkHandle)
        self.sdd_setDrivenKeyframe(FR['jaw'] + _sdk, 'ry', -20, faceSdkHandle, cdAttr, 1)

        dis = sdd_getDistanceTwoPoint([FR['M_mouth_Dn'] + _cnt], FR['M_mouth_Up'] + _cnt)

        cdAttr = sdd_addAttrToHandle('M_jaw_all_U', None, faceSdkHandle)
        self.sdd_setDrivenKeyframe(FR['jaw'] + _root + _sdk, 'ty', dis * 0.5, faceSdkHandle, cdAttr, 1)
        cdAttr = sdd_addAttrToHandle('M_jaw_all_D', None, faceSdkHandle)
        self.sdd_setDrivenKeyframe(FR['jaw'] + _root + _sdk, 'ty', -dis * 0.5, faceSdkHandle, cdAttr, 1)
        cdAttr = sdd_addAttrToHandle('M_jaw_all_L', None, faceSdkHandle)
        self.sdd_setDrivenKeyframe(FR['jaw'] + _root + _sdk, 'tx', dis * 0.5, faceSdkHandle, cdAttr, 1)
        cdAttr = sdd_addAttrToHandle('M_jaw_all_R', None, faceSdkHandle)
        self.sdd_setDrivenKeyframe(FR['jaw'] + _root + _sdk, 'tx', -dis * 0.5, faceSdkHandle, cdAttr, 1)

        mpy.addAttr(faceSdkHandle, ln='______mouth_______', at='double', min=0, max=0, k=0)
        mpy.setAttr(faceSdkHandle + '.______mouth_______', cb=1)

        dis = sdd_getDistanceTwoPoint([FR['M_mouth_Up'] + _cnt, FR['M_mouth_Dn'] + _cnt], FR['L_mouth_Corner'] + _cnt)
        dis = dis / 2.0

        cdAttr, mircdAttr = sdd_addAttrToHandle('L_mouth_corner_O', 'R_mouth_corner_O', faceSdkHandle)
        self.sdd_setDrivenKeyframe(FR['L_mouth_Corner'] + _sdk, 'tx', dis, faceSdkHandle, cdAttr, 1, mircdAttr)
        self.sdd_setDrivenKeyframe(FR['L_mouth_Up'] + _sdk, 'tx', dis * 0.5, faceSdkHandle, cdAttr, 1, mircdAttr)
        self.sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'tx', dis * 0.5, faceSdkHandle, cdAttr, 1, mircdAttr)
        self.sdd_setDrivenKeyframe(FR['L_cheek'] + _sdk, 'tx', dis * 0.5, faceSdkHandle, cdAttr, 1, mircdAttr)
        self.sdd_setDrivenKeyframe(FR['L_cheek'] + _sdk, 'tz', dis * 0.5, faceSdkHandle, cdAttr, 1, mircdAttr)
        self.sdd_setDrivenKeyframe(FR['L_noseFold'] + _sdk, 'tx', dis * 0.125, faceSdkHandle, cdAttr, 1, mircdAttr)

        cdAttr, mircdAttr = sdd_addAttrToHandle('L_mouth_corner_I', 'R_mouth_corner_I', faceSdkHandle)
        self.sdd_setDrivenKeyframe(FR['L_mouth_Corner'] + _sdk, 'tx', -dis * 1.25, faceSdkHandle, cdAttr, 1, mircdAttr)
        self.sdd_setDrivenKeyframe(FR['L_mouth_Up'] + _sdk, 'tx', -dis * 0.625, faceSdkHandle, cdAttr, 1, mircdAttr)
        self.sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'tx', -dis * 0.625, faceSdkHandle, cdAttr, 1, mircdAttr)
        self.sdd_setDrivenKeyframe(FR['M_mouth_Up'] + _sdk, 'tz', dis * 0.03, faceSdkHandle, cdAttr, 1, mircdAttr)
        self.sdd_setDrivenKeyframe(FR['M_mouth_Dn'] + _sdk, 'tz', dis * 0.03, faceSdkHandle, cdAttr, 1, mircdAttr)
        self.sdd_setDrivenKeyframe(FR['L_cheek'] + _sdk, 'tx', -dis * 0.5, faceSdkHandle, cdAttr, 1, mircdAttr)
        self.sdd_setDrivenKeyframe(FR['L_noseFold'] + _sdk, 'tx', -dis * 0.125, faceSdkHandle, cdAttr, 1, mircdAttr)

        dis = sdd_getDistanceTwoPoint([FR['L_nose'] + _cnt, FR['R_nose'] + _cnt], FR['M_mouth_Up'] + _cnt)

        cdAttr, mircdAttr = sdd_addAttrToHandle('L_mouth_corner_U', 'R_mouth_corner_U', faceSdkHandle)
        self.sdd_setDrivenKeyframe(FR['L_mouth_Corner'] + _sdk, 'ty', dis, faceSdkHandle, cdAttr, 1, mircdAttr)
        self.sdd_setDrivenKeyframe(FR['L_mouth_Up'] + _sdk, 'ty', dis * 0.125, faceSdkHandle, cdAttr, 1, mircdAttr)
        self.sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'ty', dis * 0.125, faceSdkHandle, cdAttr, 1, mircdAttr)
        self.sdd_setDrivenKeyframe(FR['L_mouth_Corner'] + _sdk, 'tz', -dis * 0.25, faceSdkHandle, cdAttr, 1, mircdAttr)
        self.sdd_setDrivenKeyframe(FR['L_mouth_Corner'] + _sdk, 'rz', 10, faceSdkHandle, cdAttr, 1, mircdAttr)
        self.sdd_setDrivenKeyframe(FR['L_mouth_Up'] + _sdk, 'rz', 5, faceSdkHandle, cdAttr, 1, mircdAttr)
        self.sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'rz', 5, faceSdkHandle, cdAttr, 1, mircdAttr)
        self.sdd_setDrivenKeyframe(FR['L_cheek'] + _sdk, 'ty', dis * 0.5, faceSdkHandle, cdAttr, 1, mircdAttr)
        self.sdd_setDrivenKeyframe(FR['L_noseFold'] + _sdk, 'ty', dis * 0.125, faceSdkHandle, cdAttr, 1, mircdAttr)

        cdAttr, mircdAttr = sdd_addAttrToHandle('L_mouth_corner_D', 'R_mouth_corner_D', faceSdkHandle)
        self.sdd_setDrivenKeyframe(FR['L_mouth_Corner'] + _sdk, 'ty', -dis * 0.625, faceSdkHandle, cdAttr, 1, mircdAttr)
        self.sdd_setDrivenKeyframe(FR['L_mouth_Up'] + _sdk, 'ty', -dis * 0.125, faceSdkHandle, cdAttr, 1, mircdAttr)
        self.sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'ty', -dis * 0.125, faceSdkHandle, cdAttr, 1, mircdAttr)
        self.sdd_setDrivenKeyframe(FR['L_mouth_Corner'] + _sdk, 'tz', -dis * 0.25, faceSdkHandle, cdAttr, 1, mircdAttr)
        self.sdd_setDrivenKeyframe(FR['L_mouth_Corner'] + _sdk, 'rz', -10, faceSdkHandle, cdAttr, 1, mircdAttr)
        self.sdd_setDrivenKeyframe(FR['L_mouth_Up'] + _sdk, 'rz', -5, faceSdkHandle, cdAttr, 1, mircdAttr)
        self.sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'rz', -5, faceSdkHandle, cdAttr, 1, mircdAttr)
        self.sdd_setDrivenKeyframe(FR['L_cheek'] + _sdk, 'ty', -dis * 0.5, faceSdkHandle, cdAttr, 1, mircdAttr)
        self.sdd_setDrivenKeyframe(FR['L_noseFold'] + _sdk, 'ty', -dis * 0.125, faceSdkHandle, cdAttr, 1, mircdAttr)

        #
        dis = sdd_getDistanceTwoPoint([FR['L_nose'] + _cnt, FR['R_nose'] + _cnt], FR['M_mouth_Up'] + _cnt)

        cdAttr, mircdAttr = sdd_addAttrToHandle('L_mouth_Up_U', 'R_mouth_Up_U', faceSdkHandle)
        self.sdd_setDrivenKeyframe(FR['L_mouth_Up'] + _sdk, 'ty', dis * 0.6, faceSdkHandle, cdAttr, 1, mircdAttr)
        self.sdd_setDrivenKeyframe(FR['M_mouth_Up'] + _sdk, 'ty', dis * 0.25, faceSdkHandle, cdAttr, 1, mircdAttr)
        self.sdd_setDrivenKeyframe(FR['M_mouth_Up'] + _sdk, 'rz', 10, faceSdkHandle, cdAttr, 1, mircdAttr)

        cdAttr, mircdAttr = sdd_addAttrToHandle('L_mouth_Up_D', 'R_mouth_Up_D', faceSdkHandle)
        self.sdd_setDrivenKeyframe(FR['L_mouth_Up'] + _sdk, 'ty', -dis * 0.6, faceSdkHandle, cdAttr, 1, mircdAttr)
        self.sdd_setDrivenKeyframe(FR['M_mouth_Up'] + _sdk, 'ty', -dis * 0.25, faceSdkHandle, cdAttr, 1, mircdAttr)
        self.sdd_setDrivenKeyframe(FR['M_mouth_Up'] + _sdk, 'rz', -10, faceSdkHandle, cdAttr, 1, mircdAttr)

        cdAttr, mircdAttr = sdd_addAttrToHandle('L_mouth_Dn_U', 'R_mouth_Dn_U', faceSdkHandle)
        self.sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'ty', -dis * 0.6, faceSdkHandle, cdAttr, 1, mircdAttr)
        self.sdd_setDrivenKeyframe(FR['M_mouth_Dn'] + _sdk, 'ty', -dis * 0.1, faceSdkHandle, cdAttr, 1, mircdAttr)
        self.sdd_setDrivenKeyframe(FR['M_mouth_Dn'] + _sdk, 'rz', -10, faceSdkHandle, cdAttr, 1, mircdAttr)

        cdAttr, mircdAttr = sdd_addAttrToHandle('L_mouth_Dn_D', 'R_mouth_Dn_D', faceSdkHandle)
        self.sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'ty', dis * 0.6, faceSdkHandle, cdAttr, 1, mircdAttr)
        self.sdd_setDrivenKeyframe(FR['M_mouth_Dn'] + _sdk, 'ty', dis * 0.1, faceSdkHandle, cdAttr, 1, mircdAttr)
        self.sdd_setDrivenKeyframe(FR['M_mouth_Dn'] + _sdk, 'rz', 10, faceSdkHandle, cdAttr, 1, mircdAttr)

        dis = sdd_getDistanceTwoPoint([FR['M_mouth_Dn'] + _cnt], FR['M_mouth_Up'] + _cnt)

        cdAttr = sdd_addAttrToHandle('M_mouth_Up_U', None, faceSdkHandle)
        self.sdd_setDrivenKeyframe(FR['L_mouth_Up'] + _sdk, 'ty', dis * 0.5, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['M_mouth_Up'] + _sdk, 'ty', dis * 0.5, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['R_mouth_Up'] + _sdk, 'ty', dis * 0.5, faceSdkHandle, cdAttr, 1)

        cdAttr = sdd_addAttrToHandle('M_mouth_Dn_U', None, faceSdkHandle)
        self.sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'ty', dis * 0.4, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'tz', dis * 0.2, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['M_mouth_Dn'] + _sdk, 'ty', dis * 0.6, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['M_mouth_Dn'] + _sdk, 'tz', dis * 0.4, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['R_mouth_Dn'] + _sdk, 'ty', dis * 0.4, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['R_mouth_Dn'] + _sdk, 'tz', dis * 0.2, faceSdkHandle, cdAttr, 1)

        cdAttr = sdd_addAttrToHandle('M_mouth_Dn_D', None, faceSdkHandle)
        self.sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'ty', -dis * 0.5, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['M_mouth_Dn'] + _sdk, 'ty', -dis * 0.5, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['R_mouth_Dn'] + _sdk, 'ty', -dis * 0.5, faceSdkHandle, cdAttr, 1)
        #

        cdAttr = sdd_addAttrToHandle('mouth_Up_roll_O', None, faceSdkHandle)
        self.sdd_setDrivenKeyframe(FR['L_mouth_Up'] + _sdk, 'rx', -35, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['M_mouth_Up'] + _sdk, 'rx', -35, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['R_mouth_Up'] + _sdk, 'rx', -35, faceSdkHandle, cdAttr, 1)

        cdAttr = sdd_addAttrToHandle('mouth_Up_roll_I', None, faceSdkHandle)
        self.sdd_setDrivenKeyframe(FR['L_mouth_Up'] + _sdk, 'rx', 35, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['M_mouth_Up'] + _sdk, 'rx', 35, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['R_mouth_Up'] + _sdk, 'rx', 35, faceSdkHandle, cdAttr, 1)

        cdAttr = sdd_addAttrToHandle('mouth_Dn_roll_O', None, faceSdkHandle)
        self.sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'rx', 35, faceSdkHandle, cdAttr, 1, mircdAttr)
        self.sdd_setDrivenKeyframe(FR['M_mouth_Dn'] + _sdk, 'rx', 35, faceSdkHandle, cdAttr, 1, mircdAttr)
        self.sdd_setDrivenKeyframe(FR['R_mouth_Dn'] + _sdk, 'rx', 35, faceSdkHandle, cdAttr, 1, mircdAttr)

        cdAttr = sdd_addAttrToHandle('mouth_Dn_roll_I', None, faceSdkHandle)
        self.sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'rx', -35, faceSdkHandle, cdAttr, 1, mircdAttr)
        self.sdd_setDrivenKeyframe(FR['M_mouth_Dn'] + _sdk, 'rx', -35, faceSdkHandle, cdAttr, 1, mircdAttr)
        self.sdd_setDrivenKeyframe(FR['R_mouth_Dn'] + _sdk, 'rx', -35, faceSdkHandle, cdAttr, 1, mircdAttr)

    @staticmethod
    def sdd_mouthShapeDefultSdk():
        FR, _sdk, _root, _cnt, faceSdkHandle = self.sdd_getDefultSdkName()
        # mouthShape
        mpy.addAttr(faceSdkHandle, ln='______motion______', at='double', min=0, max=0, k=0)
        mpy.setAttr(faceSdkHandle + '.______motion______', cb=1)

        dis = sdd_getDistanceTwoPoint([FR['M_mouth_Up'] + _cnt], FR['M_mouth_Dn'] + _cnt)

        cdAttr = sdd_addAttrToHandle('mouth_A', None, faceSdkHandle)
        self.sdd_setDrivenKeyframe(FR['jaw'] + _sdk, 'ty', -dis * 0.25, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['jaw'] + _sdk, 'rx', 15, faceSdkHandle, cdAttr, 1)

        self.sdd_setDrivenKeyframe(FR['L_mouth_Corner'] + _sdk, 'tx', dis * 0.5, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['L_mouth_Corner'] + _sdk, 'tz', -dis * 0.3, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['L_mouth_Corner'] + _sdk, 'ty', dis * 0.2, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['R_mouth_Corner'] + _sdk, 'tx', -dis * 0.5, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['R_mouth_Corner'] + _sdk, 'tz', -dis * 0.3, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['R_mouth_Corner'] + _sdk, 'ty', dis * 0.2, faceSdkHandle, cdAttr, 1)

        self.sdd_setDrivenKeyframe(FR['L_mouth_Up'] + _sdk, 'tx', dis * 0.3, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['R_mouth_Up'] + _sdk, 'tx', -dis * 0.3, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'tx', dis * 0.3, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['R_mouth_Dn'] + _sdk, 'tx', -dis * 0.3, faceSdkHandle, cdAttr, 1)

        self.sdd_setDrivenKeyframe(FR['L_cheek_Up'] + _sdk, 'tx', dis * 0.1, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['R_cheek_Up'] + _sdk, 'tx', -dis * 0.1, faceSdkHandle, cdAttr, 1)

        self.sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'ry', 8, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['R_mouth_Dn'] + _sdk, 'ry', -8, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'rx', -10, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['R_mouth_Dn'] + _sdk, 'rx', -10, faceSdkHandle, cdAttr, 1)

        self.sdd_setDrivenKeyframe(FR['L_mouth_Up'] + _sdk, 'ry', 8, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['R_mouth_Up'] + _sdk, 'ry', -8, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['L_mouth_Up'] + _sdk, 'rx', 5, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['R_mouth_Up'] + _sdk, 'rx', 5, faceSdkHandle, cdAttr, 1)

        cdAttr = sdd_addAttrToHandle('mouth_E', None, faceSdkHandle)
        self.sdd_setDrivenKeyframe(FR['jaw'] + _sdk, 'rx', 3, faceSdkHandle, cdAttr, 1)

        self.sdd_setDrivenKeyframe(FR['L_mouth_Corner'] + _sdk, 'tx', dis * 0.5, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['L_mouth_Corner'] + _sdk, 'tz', -dis * 0.3, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['L_mouth_Corner'] + _sdk, 'ty', dis * 0.2, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['R_mouth_Corner'] + _sdk, 'tx', -dis * 0.5, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['R_mouth_Corner'] + _sdk, 'tz', -dis * 0.3, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['R_mouth_Corner'] + _sdk, 'ty', dis * 0.2, faceSdkHandle, cdAttr, 1)

        self.sdd_setDrivenKeyframe(FR['L_mouth_Up'] + _sdk, 'tx', dis * 0.1, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['R_mouth_Up'] + _sdk, 'tx', -dis * 0.1, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'tx', dis * 0.1, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['R_mouth_Dn'] + _sdk, 'tx', -dis * 0.1, faceSdkHandle, cdAttr, 1)

        self.sdd_setDrivenKeyframe(FR['L_cheek'] + _sdk, 'tz', dis * 0.1, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['R_cheek'] + _sdk, 'tz', dis * 0.1, faceSdkHandle, cdAttr, 1)

        self.sdd_setDrivenKeyframe(FR['L_cheek_Up'] + _sdk, 'tx', dis * 0.05, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['R_cheek_Up'] + _sdk, 'tx', -dis * 0.05, faceSdkHandle, cdAttr, 1)

        self.sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'ty', -dis * 0.15, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['R_mouth_Dn'] + _sdk, 'ty', -dis * 0.15, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['M_mouth_Dn'] + _sdk, 'ty', -dis * 0.2, faceSdkHandle, cdAttr, 1)

        self.sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'tz', -dis * 0.1, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['R_mouth_Dn'] + _sdk, 'tz', -dis * 0.1, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['M_mouth_Dn'] + _sdk, 'tz', -dis * 0.1, faceSdkHandle, cdAttr, 1)

        self.sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'rx', 10, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['R_mouth_Dn'] + _sdk, 'rx', 10, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['M_mouth_Dn'] + _sdk, 'rx', 15, faceSdkHandle, cdAttr, 1)

        self.sdd_setDrivenKeyframe(FR['L_mouth_Up'] + _sdk, 'ty', dis * 0.2, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['R_mouth_Up'] + _sdk, 'ty', dis * 0.2, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['M_mouth_Up'] + _sdk, 'ty', dis * 0.2, faceSdkHandle, cdAttr, 1)

        cdAttr = sdd_addAttrToHandle('mouth_F', None, faceSdkHandle)
        self.sdd_setDrivenKeyframe(FR['jaw'] + _root + _sdk, 'ty', dis * 0.2, faceSdkHandle, cdAttr, 1)

        self.sdd_setDrivenKeyframe(FR['L_mouth_Corner'] + _sdk, 'tx', dis * 0.5, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['L_mouth_Corner'] + _sdk, 'tz', -dis * 0.3, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['L_mouth_Corner'] + _sdk, 'ty', dis * 0.4, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['R_mouth_Corner'] + _sdk, 'tx', -dis * 0.5, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['R_mouth_Corner'] + _sdk, 'tz', -dis * 0.3, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['R_mouth_Corner'] + _sdk, 'ty', dis * 0.4, faceSdkHandle, cdAttr, 1)

        self.sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'tx', dis * 0.25, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['R_mouth_Dn'] + _sdk, 'tx', -dis * 0.25, faceSdkHandle, cdAttr, 1)

        self.sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'ty', dis * 0.2, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['R_mouth_Dn'] + _sdk, 'ty', dis * 0.2, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['M_mouth_Dn'] + _sdk, 'ty', dis * 0.2, faceSdkHandle, cdAttr, 1)

        self.sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'tz', -dis * 0.15, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['R_mouth_Dn'] + _sdk, 'tz', -dis * 0.15, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['M_mouth_Dn'] + _sdk, 'tz', -dis * 0.2, faceSdkHandle, cdAttr, 1)

        self.sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'rx', -20, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['R_mouth_Dn'] + _sdk, 'rx', -20, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['M_mouth_Dn'] + _sdk, 'rx', -15, faceSdkHandle, cdAttr, 1)

        self.sdd_setDrivenKeyframe(FR['L_mouth_Up'] + _sdk, 'ty', dis * 0.3, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['R_mouth_Up'] + _sdk, 'ty', dis * 0.3, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['M_mouth_Up'] + _sdk, 'ty', dis * 0.4, faceSdkHandle, cdAttr, 1)

        self.sdd_setDrivenKeyframe(FR['L_mouth_Up'] + _sdk, 'tx', dis * 0.5, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['R_mouth_Up'] + _sdk, 'tx', -dis * 0.5, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['M_mouth_Up'] + _sdk, 'tz', dis * 0.2, faceSdkHandle, cdAttr, 1)

        self.sdd_setDrivenKeyframe(FR['jaw'] + _sdk, 'rx', 2, faceSdkHandle, cdAttr, 1)

        self.sdd_setDrivenKeyframe(FR['L_mouth_Up'] + _sdk, 'rz', -15, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['R_mouth_Up'] + _sdk, 'rz', 15, faceSdkHandle, cdAttr, 1)

        self.sdd_setDrivenKeyframe(FR['L_cheek'] + _sdk, 'ty', dis * 0.4, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['R_cheek'] + _sdk, 'ty', dis * 0.4, faceSdkHandle, cdAttr, 1)

        self.sdd_setDrivenKeyframe(FR['L_cheek_Up'] + _sdk, 'ty', dis * 0.1, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['R_cheek_Up'] + _sdk, 'ty', dis * 0.1, faceSdkHandle, cdAttr, 1)

        self.sdd_setDrivenKeyframe(FR['L_cheek_Up'] + _sdk, 'tz', dis * 0.05, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['R_cheek_Up'] + _sdk, 'tz', dis * 0.05, faceSdkHandle, cdAttr, 1)

        cdAttr = sdd_addAttrToHandle('mouth_H', None, faceSdkHandle)
        self.sdd_setDrivenKeyframe(FR['jaw'] + _sdk, 'rx', 1, faceSdkHandle, cdAttr, 1)

        self.sdd_setDrivenKeyframe(FR['L_mouth_Corner'] + _sdk, 'tx', -dis * 0.5, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['R_mouth_Corner'] + _sdk, 'tx', dis * 0.5, faceSdkHandle, cdAttr, 1)

        self.sdd_setDrivenKeyframe(FR['L_mouth_Up'] + _sdk, 'ty', dis * 0.2, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['R_mouth_Up'] + _sdk, 'ty', dis * 0.2, faceSdkHandle, cdAttr, 1)

        self.sdd_setDrivenKeyframe(FR['L_mouth_Up'] + _sdk, 'ry', 15, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['R_mouth_Up'] + _sdk, 'ry', -15, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['L_mouth_Up'] + _sdk, 'rz', -30, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['R_mouth_Up'] + _sdk, 'rz', 30, faceSdkHandle, cdAttr, 1)

        self.sdd_setDrivenKeyframe(FR['M_mouth_Up'] + _sdk, 'ty', dis * 0.5, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['M_mouth_Up'] + _sdk, 'rx', -30, faceSdkHandle, cdAttr, 1)

        self.sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'ry', 10, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['R_mouth_Dn'] + _sdk, 'ry', -10, faceSdkHandle, cdAttr, 1)

        self.sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'rz', 30, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['R_mouth_Dn'] + _sdk, 'rz', -30, faceSdkHandle, cdAttr, 1)

        self.sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'tz', dis * 0.1, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['R_mouth_Dn'] + _sdk, 'tz', dis * 0.1, faceSdkHandle, cdAttr, 1)

        self.sdd_setDrivenKeyframe(FR['M_mouth_Dn'] + _sdk, 'ty', -dis * 0.4, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['M_mouth_Dn'] + _sdk, 'tz', dis * 0.2, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['M_mouth_Dn'] + _sdk, 'rx', 30, faceSdkHandle, cdAttr, 1)

        self.sdd_setDrivenKeyframe(FR['L_cheek'] + _sdk, 'tx', -dis * 0.4, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['R_cheek'] + _sdk, 'tx', dis * 0.4, faceSdkHandle, cdAttr, 1)

        cdAttr = sdd_addAttrToHandle('mouth_M', None, faceSdkHandle)
        self.sdd_setDrivenKeyframe(FR['jaw'] + _sdk, 'rx', 3, faceSdkHandle, cdAttr, 1)

        self.sdd_setDrivenKeyframe(FR['L_mouth_Up'] + _sdk, 'rx', 35, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['R_mouth_Up'] + _sdk, 'rx', 35, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['M_mouth_Up'] + _sdk, 'rx', 35, faceSdkHandle, cdAttr, 1)

        self.sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'rx', -15, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['R_mouth_Dn'] + _sdk, 'rx', -15, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['M_mouth_Dn'] + _sdk, 'rx', -15, faceSdkHandle, cdAttr, 1)

        self.sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'ty', dis * 0.1, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['R_mouth_Dn'] + _sdk, 'ty', dis * 0.1, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['M_mouth_Dn'] + _sdk, 'ty', dis * 0.1, faceSdkHandle, cdAttr, 1)

        self.sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'tz', dis * 0.1, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['R_mouth_Dn'] + _sdk, 'tz', dis * 0.1, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['M_mouth_Dn'] + _sdk, 'tz', dis * 0.1, faceSdkHandle, cdAttr, 1)

        self.sdd_setDrivenKeyframe(FR['L_mouth_Up'] + _sdk, 'ty', -dis * 0.2, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['R_mouth_Up'] + _sdk, 'ty', -dis * 0.2, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['M_mouth_Up'] + _sdk, 'ty', -dis * 0.2, faceSdkHandle, cdAttr, 1)

        self.sdd_setDrivenKeyframe(FR['L_mouth_Up'] + _sdk, 'tz', -dis * 0.1, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['R_mouth_Up'] + _sdk, 'tz', -dis * 0.1, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['M_mouth_Up'] + _sdk, 'tz', -dis * 0.1, faceSdkHandle, cdAttr, 1)

        cdAttr = sdd_addAttrToHandle('mouth_O', None, faceSdkHandle)
        self.sdd_setDrivenKeyframe(FR['jaw'] + _sdk, 'rx', 3, faceSdkHandle, cdAttr, 1)

        self.sdd_setDrivenKeyframe(FR['L_mouth_Corner'] + _sdk, 'tx', -dis, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['R_mouth_Corner'] + _sdk, 'tx', dis, faceSdkHandle, cdAttr, 1)

        self.sdd_setDrivenKeyframe(FR['L_mouth_Corner'] + _sdk, 'tz', dis * 0.1, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['R_mouth_Corner'] + _sdk, 'tz', dis * 0.1, faceSdkHandle, cdAttr, 1)

        self.sdd_setDrivenKeyframe(FR['L_mouth_Up'] + _sdk, 'tx', -dis * 0.2, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['R_mouth_Up'] + _sdk, 'tx', dis * 0.2, faceSdkHandle, cdAttr, 1)

        self.sdd_setDrivenKeyframe(FR['L_mouth_Up'] + _sdk, 'ry', 15, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['R_mouth_Up'] + _sdk, 'ry', -15, faceSdkHandle, cdAttr, 1)

        self.sdd_setDrivenKeyframe(FR['L_mouth_Up'] + _sdk, 'rz', -15, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['R_mouth_Up'] + _sdk, 'rz', 15, faceSdkHandle, cdAttr, 1)

        self.sdd_setDrivenKeyframe(FR['M_mouth_Up'] + _sdk, 'ty', dis * 0.3, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['M_mouth_Up'] + _sdk, 'tz', dis * 0.2, faceSdkHandle, cdAttr, 1)

        self.sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'tx', -dis * 0.3, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['R_mouth_Dn'] + _sdk, 'tx', dis * 0.3, faceSdkHandle, cdAttr, 1)

        self.sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'tz', dis * 0.1, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['R_mouth_Dn'] + _sdk, 'tz', dis * 0.1, faceSdkHandle, cdAttr, 1)

        self.sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'ry', 10, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['R_mouth_Dn'] + _sdk, 'ry', -10, faceSdkHandle, cdAttr, 1)

        self.sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'rz', 10, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['R_mouth_Dn'] + _sdk, 'rz', -10, faceSdkHandle, cdAttr, 1)

        self.sdd_setDrivenKeyframe(FR['M_mouth_Dn'] + _sdk, 'ty', -dis * 0.4, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['M_mouth_Dn'] + _sdk, 'tz', dis * 0.2, faceSdkHandle, cdAttr, 1)

        self.sdd_setDrivenKeyframe(FR['L_cheek'] + _sdk, 'tx', -dis * 0.4, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['R_cheek'] + _sdk, 'tx', dis * 0.4, faceSdkHandle, cdAttr, 1)

        self.sdd_setDrivenKeyframe(FR['L_cheek'] + _sdk, 'tz', -dis * 0.2, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['R_cheek'] + _sdk, 'tz', -dis * 0.2, faceSdkHandle, cdAttr, 1)

        cdAttr = sdd_addAttrToHandle('mouth_U', None, faceSdkHandle)
        self.sdd_setDrivenKeyframe(FR['jaw'] + _sdk, 'rx', 3, faceSdkHandle, cdAttr, 1)

        self.sdd_setDrivenKeyframe(FR['L_mouth_Corner'] + _sdk, 'tx', -dis, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['R_mouth_Corner'] + _sdk, 'tx', dis, faceSdkHandle, cdAttr, 1)

        self.sdd_setDrivenKeyframe(FR['L_mouth_Corner'] + _sdk, 'tz', dis * 0.1, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['R_mouth_Corner'] + _sdk, 'tz', dis * 0.1, faceSdkHandle, cdAttr, 1)

        self.sdd_setDrivenKeyframe(FR['L_mouth_Up'] + _sdk, 'tx', -dis * 0.2, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['R_mouth_Up'] + _sdk, 'tx', dis * 0.2, faceSdkHandle, cdAttr, 1)

        self.sdd_setDrivenKeyframe(FR['L_mouth_Up'] + _sdk, 'ty', -dis * 0.1, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['R_mouth_Up'] + _sdk, 'ty', -dis * 0.1, faceSdkHandle, cdAttr, 1)

        self.sdd_setDrivenKeyframe(FR['L_mouth_Up'] + _sdk, 'ry', 15, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['R_mouth_Up'] + _sdk, 'ry', -15, faceSdkHandle, cdAttr, 1)

        self.sdd_setDrivenKeyframe(FR['L_mouth_Up'] + _sdk, 'rz', -20, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['R_mouth_Up'] + _sdk, 'rz', 20, faceSdkHandle, cdAttr, 1)

        self.sdd_setDrivenKeyframe(FR['M_mouth_Up'] + _sdk, 'ty', dis * 0.3, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['M_mouth_Up'] + _sdk, 'tz', dis * 0.2, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['M_mouth_Up'] + _sdk, 'rx', -30, faceSdkHandle, cdAttr, 1)

        self.sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'tx', -dis * 0.3, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['R_mouth_Dn'] + _sdk, 'tx', dis * 0.3, faceSdkHandle, cdAttr, 1)

        self.sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'ty', dis * 0.3, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['R_mouth_Dn'] + _sdk, 'ty', dis * 0.3, faceSdkHandle, cdAttr, 1)

        self.sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'tz', dis * 0.1, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['R_mouth_Dn'] + _sdk, 'tz', dis * 0.1, faceSdkHandle, cdAttr, 1)

        self.sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'ry', 10, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['R_mouth_Dn'] + _sdk, 'ry', -10, faceSdkHandle, cdAttr, 1)

        self.sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'rz', 20, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['R_mouth_Dn'] + _sdk, 'rz', -20, faceSdkHandle, cdAttr, 1)

        self.sdd_setDrivenKeyframe(FR['M_mouth_Dn'] + _sdk, 'rx', 30, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['M_mouth_Dn'] + _sdk, 'ty', -dis * 0.1, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['M_mouth_Dn'] + _sdk, 'tz', dis * 0.3, faceSdkHandle, cdAttr, 1)

        self.sdd_setDrivenKeyframe(FR['L_cheek'] + _sdk, 'tx', -dis * 0.4, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['R_cheek'] + _sdk, 'tx', dis * 0.4, faceSdkHandle, cdAttr, 1)

        self.sdd_setDrivenKeyframe(FR['L_cheek'] + _sdk, 'tz', -dis * 0.2, faceSdkHandle, cdAttr, 1)
        self.sdd_setDrivenKeyframe(FR['R_cheek'] + _sdk, 'tz', -dis * 0.2, faceSdkHandle, cdAttr, 1)

    @staticmethod
    def sdd_getDefultSdkName():
        T = self.returnTempNameDirc()
        FR, FRJntPos, FRUIPos = self.frTNameDirc()
        _sdk = T['_sdk']
        _root = T['_root']
        _cnt = T['_cnt']
        faceSdkHandle = 'face_sdk_handle'
        return FR, _sdk, _root, _cnt, faceSdkHandle

    @staticmethod
    def sdd_returnTempNameDirc():
        TName = {'_fol': '_fol', '_loc': '_loc', '_final': '_final', '_target': '_target', 'face': 'face',
                 '_base': '_base', '_bsNode': '_bsNode', '_bs': '_bs', '_skin': '_skin', 'M_': 'M_', 'L_': 'L_',
                 'R_': 'R_', '_ctrl': '_ctrl', '_rig': '_rig', '_jnt': '_jnt', '_root': '_root', '_rot': '_rot',
                 '_cur': '_cur', '_cnt': '_cnt', '_sdk': '_sdk', '_grp': '_grp', '_anim': '_anim'}
        return TName

    @staticmethod
    def sdd_setDrivenKeyframe(c, cAttr, v, cd, cdAttr, dv, mircdAttr=None):
        mpy.setDrivenKeyframe(c + '.' + cAttr, cd=cd + '.' + cdAttr, v=0, dv=0, itt='linear', ott='linear')
        mpy.setDrivenKeyframe(c + '.' + cAttr, cd=cd + '.' + cdAttr, v=v, dv=dv, itt='linear', ott='linear')
        if (mircdAttr != None):
            attrList = ['tx', 'ty', 'tz', 'rx', 'ry', 'rz', 'sx', 'sy', 'sz']
            valList = [-1, 1, 1, 1, -1, -1, 1, 1, 1]
            mirc = sdd_getMirrorName(c)
            v = v * valList[attrList.index(cAttr)]
            mpy.setDrivenKeyframe(mirc + '.' + cAttr, cd=cd + '.' + mircdAttr, v=0, dv=0, itt='linear', ott='linear')
            mpy.setDrivenKeyframe(mirc + '.' + cAttr, cd=cd + '.' + mircdAttr, v=v, dv=dv, itt='linear', ott='linear')
