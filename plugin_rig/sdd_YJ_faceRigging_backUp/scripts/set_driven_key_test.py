class YJDefultSDK(object):
    def __init__(self):
        self.author = "YJ"

    def yj_browDefultSdk():
        FR, _sdk, _root, _cnt, faceSdkHandle, faceCur = sdd_getDefultSdkName()

        # brow
        cmds.addAttr(faceSdkHandle, ln='______brow________', at='double', min=0, max=0, k=0)
        cmds.setAttr(faceSdkHandle + '.' + '______brow________', cb=1)

        dis = cmds.getAttr(faceCur + '.eyeBrow_factor')

        cdAttr = sdd_addAttrToHandle('M_Brow_snap_U', None, faceSdkHandle)
        sdd_setDrivenKeyframe(FR['M_brow'] + _sdk, 'ty', dis, faceSdkHandle, cdAttr, 1)
        cdAttr = sdd_addAttrToHandle('M_Brow_snap_D', None, faceSdkHandle)
        sdd_setDrivenKeyframe(FR['M_brow'] + _sdk, 'ty', -dis, faceSdkHandle, cdAttr, 1)

        cdAttr = sdd_addAttrToHandle('M_Brow_snap_I', None, faceSdkHandle)
        # sdd_setDrivenKeyframe(FR['M_brow'] + _sdk, 'ty', -dis, faceSdkHandle, cdAttr, 1)

        cdAttr, mircdAttr = sdd_addAttrToHandle('L_snap_BrowIn_U', 'R_snap_BrowIn_U', faceSdkHandle)
        sdd_setDrivenKeyframe(FR['L_brow_a'] + _sdk, 'ty', dis, faceSdkHandle, cdAttr, 1, mircdAttr)
        sdd_setDrivenKeyframe(FR['L_brow_b'] + _sdk, 'ty', dis * 0.5, faceSdkHandle, cdAttr, 1, mircdAttr)
        #
        cdAttr, mircdAttr = sdd_addAttrToHandle('L_snap_BrowIn_D', 'R_snap_BrowIn_D', faceSdkHandle)
        sdd_setDrivenKeyframe(FR['L_brow_a'] + _sdk, 'ty', -dis, faceSdkHandle, cdAttr, 1, mircdAttr)
        sdd_setDrivenKeyframe(FR['L_brow_b'] + _sdk, 'ty', -dis * 0.5, faceSdkHandle, cdAttr, 1, mircdAttr)
        #
        cdAttr, mircdAttr = sdd_addAttrToHandle('L_snap_BrowOut_U', 'R_snap_BrowOut_U', faceSdkHandle)
        sdd_setDrivenKeyframe(FR['L_brow_c'] + _sdk, 'ty', dis, faceSdkHandle, cdAttr, 1, mircdAttr)
        sdd_setDrivenKeyframe(FR['L_brow_b'] + _sdk, 'ty', dis * 0.5, faceSdkHandle, cdAttr, 1, mircdAttr)

        cdAttr, mircdAttr = sdd_addAttrToHandle('L_snap_BrowOut_D', 'R_snap_BrowOut_D', faceSdkHandle)
        sdd_setDrivenKeyframe(FR['L_brow_c'] + _sdk, 'ty', -dis, faceSdkHandle, cdAttr, 1, mircdAttr)
        sdd_setDrivenKeyframe(FR['L_brow_b'] + _sdk, 'ty', -dis * 0.5, faceSdkHandle, cdAttr, 1, mircdAttr)
        #
        # cdAttr, mircdAttr = sdd_addAttrToHandle('L_brow_Mid_U', 'R_brow_Mid_U', faceSdkHandle)
        # sdd_setDrivenKeyframe(FR['L_brow_b'] + _sdk, 'ty', dis * 0.5, faceSdkHandle, cdAttr, 1, mircdAttr)
        #
        # cdAttr, mircdAttr = sdd_addAttrToHandle('L_brow_Mid_D', 'R_brow_Mid_D', faceSdkHandle)
        # sdd_setDrivenKeyframe(FR['L_brow_b'] + _sdk, 'ty', -dis * 0.5, faceSdkHandle, cdAttr, 1, mircdAttr)
        #
        # cdAttr, mircdAttr = sdd_addAttrToHandle('L_brow_In_In', 'R_brow_In_In', faceSdkHandle)
        # sdd_setDrivenKeyframe(FR['L_brow_a'] + _sdk, 'tx', -dis * 0.5, faceSdkHandle, cdAttr, 1, mircdAttr)

    def yj_eyelidDefultSdk():
        FR, _sdk, _root, _cnt, faceSdkHandle, faceCur = sdd_getDefultSdkName()
        # eyelid
        cmds.addAttr(faceSdkHandle, ln='______eyelid______', at='double', min=0, max=0, k=0)
        cmds.setAttr(faceSdkHandle + '.______eyelid______', cb=1)

        arcMid = cmds.getAttr(faceCur + '.eyeAngle_factor')

        cdAttr, mircdAttr = sdd_addAttrToHandle('L_snap_UprLid_U', 'R_snap_UprLid_U', faceSdkHandle)
        sdd_setDrivenKeyframe(FR['L_eyelid_Up'] + _root + _sdk, 'rx', -5, faceSdkHandle, cdAttr, 1, mircdAttr)

        cdAttr, mircdAttr = sdd_addAttrToHandle('L_snap_UprLid_D', 'R_snap_UprLid_D', faceSdkHandle)
        sdd_setDrivenKeyframe(FR['L_eyelid_Up'] + _root + _sdk, 'rx', arcMid + 2, faceSdkHandle, cdAttr, 1, mircdAttr)
        #
        cdAttr, mircdAttr = sdd_addAttrToHandle('L_snap_LwrLid_U', 'R_snap_LwrLid_U', faceSdkHandle)
        sdd_setDrivenKeyframe(FR['L_eyelid_Dn'] + _root + _sdk, 'rx', -arcMid - 2, faceSdkHandle, cdAttr, 1, mircdAttr)
        #
        cdAttr, mircdAttr = sdd_addAttrToHandle('L_snap_LwrLid_D', 'R_snap_LwrLid_D', faceSdkHandle)
        sdd_setDrivenKeyframe(FR['L_eyelid_Dn'] + _root + _sdk, 'rx', 5, faceSdkHandle, cdAttr, 1, mircdAttr)
        #
        cdAttr, mircdAttr = sdd_addAttrToHandle('L_snap_EyeSqz_U', 'R_snap_EyeSqz_U', faceSdkHandle)
        #
        cdAttr, mircdAttr = sdd_addAttrToHandle('L_snap_EyeSqz_D', 'R_snap_EyeSqz_D', faceSdkHandle)
        #
        cdAttr, mircdAttr = sdd_addAttrToHandle('L_snap_EyeSqz_I', 'R_snap_EyeSqz_I', faceSdkHandle)
        #
        cdAttr, mircdAttr = sdd_addAttrToHandle('L_snap_EyeSqz_O', 'R_snap_EyeSqz_O', faceSdkHandle)
        #
        # cdAttr, mircdAttr = sdd_addAttrToHandle('L_eyelid_Up_side_O', 'R_eyelid_Up_side_O', faceSdkHandle)
        # sdd_setDrivenKeyframe(FR['L_eyelid_UpIn'] + _root + _sdk, 'rx', 15, faceSdkHandle, cdAttr, 1, mircdAttr)
        # sdd_setDrivenKeyframe(FR['L_eyelid_Up'] + _sdk, 'rz', 15, faceSdkHandle, cdAttr, 1, mircdAttr)
        # sdd_setDrivenKeyframe(FR['L_eyelid_UpOut'] + _root + _sdk, 'rx', -15, faceSdkHandle, cdAttr, 1, mircdAttr)
        #
        # cdAttr, mircdAttr = sdd_addAttrToHandle('L_eyelid_Up_side_I', 'R_eyelid_Up_side_I', faceSdkHandle)
        # sdd_setDrivenKeyframe(FR['L_eyelid_UpIn'] + _root + _sdk, 'rx', -15, faceSdkHandle, cdAttr, 1, mircdAttr)
        # sdd_setDrivenKeyframe(FR['L_eyelid_Up'] + _sdk, 'rz', -15, faceSdkHandle, cdAttr, 1, mircdAttr)
        # sdd_setDrivenKeyframe(FR['L_eyelid_UpOut'] + _root + _sdk, 'rx', 15, faceSdkHandle, cdAttr, 1, mircdAttr)
        #
        # cdAttr, mircdAttr = sdd_addAttrToHandle('L_eyelid_Dn_side_O', 'R_eyelid_Dn_side_O', faceSdkHandle)
        # sdd_setDrivenKeyframe(FR['L_eyelid_DnIn'] + _root + _sdk, 'rx', -15, faceSdkHandle, cdAttr, 1, mircdAttr)
        # sdd_setDrivenKeyframe(FR['L_eyelid_Dn'] + _sdk, 'rz', -15, faceSdkHandle, cdAttr, 1, mircdAttr)
        # sdd_setDrivenKeyframe(FR['L_eyelid_DnOut'] + _root + _sdk, 'rx', 15, faceSdkHandle, cdAttr, 1, mircdAttr)
        #
        # cdAttr, mircdAttr = sdd_addAttrToHandle('L_eyelid_Dn_side_I', 'R_eyelid_Dn_side_I', faceSdkHandle)
        # sdd_setDrivenKeyframe(FR['L_eyelid_DnIn'] + _root + _sdk, 'rx', 15, faceSdkHandle, cdAttr, 1, mircdAttr)
        # sdd_setDrivenKeyframe(FR['L_eyelid_Dn'] + _sdk, 'rz', 15, faceSdkHandle, cdAttr, 1, mircdAttr)
        # sdd_setDrivenKeyframe(FR['L_eyelid_DnOut'] + _root + _sdk, 'rx', -15, faceSdkHandle, cdAttr, 1, mircdAttr)
        #
        # cdAttr, mircdAttr = sdd_addAttrToHandle('L_eyelid_close', 'R_eyelid_close', faceSdkHandle)
        # sdd_setDrivenKeyframe(FR['L_eyelid_Up'] + _root + _sdk, 'rx', (arcMid + 2) * 0.7, faceSdkHandle, cdAttr, 1,
        #                       mircdAttr)
        # sdd_setDrivenKeyframe(FR['L_eyelid_Dn'] + _root + _sdk, 'rx', (-arcMid - 2) * 0.3, faceSdkHandle, cdAttr, 1,
        #                       mircdAttr)
        #
        # cdAttr, mircdAttr = sdd_addAttrToHandle('L_eyelid_Squint', 'R_eyelid_Squint', faceSdkHandle)
        # sdd_setDrivenKeyframe(FR['L_eyelid_Up'] + _root + _sdk, 'rx', (arcMid + 2) * 0.7, faceSdkHandle, cdAttr, 1,
        #                       mircdAttr)
        # sdd_setDrivenKeyframe(FR['L_eyelid_Dn'] + _root + _sdk, 'rx', (-arcMid - 2) * 0.3, faceSdkHandle, cdAttr, 1,
        #                       mircdAttr)
        # dis = cmds.getAttr(faceCur + '.eyeBrow_factor')
        #
        # sdd_setDrivenKeyframe(FR['L_brow_a'] + _sdk, 'ty', -dis * 0.8, faceSdkHandle, cdAttr, 1, mircdAttr)
        # sdd_setDrivenKeyframe(FR['L_brow_b'] + _sdk, 'ty', -dis * 0.8, faceSdkHandle, cdAttr, 1, mircdAttr)
        # sdd_setDrivenKeyframe(FR['L_brow_c'] + _sdk, 'ty', -dis * 0.8, faceSdkHandle, cdAttr, 1, mircdAttr)
        #
        # sdd_setDrivenKeyframe(FR['L_eyeSag_Up'] + _sdk, 'ty', -dis * 0.4, faceSdkHandle, cdAttr, 1, mircdAttr)
        #
        # sdd_setDrivenKeyframe(FR['L_eyeSag_Dn'] + _sdk, 'ty', dis * 0.25, faceSdkHandle, cdAttr, 1, mircdAttr)
        # sdd_setDrivenKeyframe(FR['L_cheek_In'] + _sdk, 'ty', dis * 0.4, faceSdkHandle, cdAttr, 1, mircdAttr)
        # sdd_setDrivenKeyframe(FR['L_cheek_Up'] + _sdk, 'ty', dis * 0.6, faceSdkHandle, cdAttr, 1, mircdAttr)
        # sdd_setDrivenKeyframe(FR['L_cheek_Out'] + _sdk, 'ty', dis * 0.9, faceSdkHandle, cdAttr, 1, mircdAttr)

    def yj_cheekDefultSdk():
        FR, _sdk, _root, _cnt, faceSdkHandle, faceCur = sdd_getDefultSdkName()
        # cheek
        cmds.addAttr(faceSdkHandle, ln='______cheek_______', at='double', min=0, max=0, k=0)
        cmds.setAttr(faceSdkHandle + '.______cheek_______', cb=1)

        dis = cmds.getAttr(faceCur + '.cheek_factor')

        cdAttr, mircdAttr = sdd_addAttrToHandle('L_snap_Cheek_U', 'R_snap_Cheek_U', faceSdkHandle)

        #
        cdAttr, mircdAttr = sdd_addAttrToHandle('L_snap_Cheek_2_U', 'R_snap_Cheek_2_U', faceSdkHandle)
        sdd_setDrivenKeyframe(FR['L_cheek'] + _sdk, 'ty', dis * 0.8, faceSdkHandle, cdAttr, 1, mircdAttr)
        sdd_setDrivenKeyframe(FR['L_cheek_Up'] + _sdk, 'ty', dis * 0.05, faceSdkHandle, cdAttr, 1, mircdAttr)

        cdAttr, mircdAttr = sdd_addAttrToHandle('L_snap_Cheek_2_O', 'R_snap_Cheek_2_O', faceSdkHandle)
        sdd_setDrivenKeyframe(FR['L_cheek'] + _sdk, 'tx', dis * 0.8, faceSdkHandle, cdAttr, 1, mircdAttr)
        #
        cdAttr, mircdAttr = sdd_addAttrToHandle('L_snap_Cheek_2_I', 'R_snap_Cheek_2_I', faceSdkHandle)
        sdd_setDrivenKeyframe(FR['L_cheek'] + _sdk, 'tx', -dis * 0.8, faceSdkHandle, cdAttr, 1, mircdAttr)
        #
        # cdAttr, mircdAttr = sdd_addAttrToHandle('L_pump_O', 'R_pump_O', faceSdkHandle)
        # sdd_setDrivenKeyframe(FR['L_cheek'] + _sdk, 'tx', dis, faceSdkHandle, cdAttr, 1, mircdAttr)

    def yj_noseDefultSdk():
        FR, _sdk, _root, _cnt, faceSdkHandle, faceCur = sdd_getDefultSdkName()
        # nose
        cmds.addAttr(faceSdkHandle, ln='______nose________', at='double', min=0, max=0, k=0)
        cmds.setAttr(faceSdkHandle + '.______nose________', cb=1)

        cdAttr = sdd_addAttrToHandle('M_snap_Nose_I', None, faceSdkHandle)
        #
        cdAttr = sdd_addAttrToHandle('M_snap_Nose_O', None, faceSdkHandle)
        #
        cdAttr = sdd_addAttrToHandle('L_snap_Nose_U', "R_snap_Nose_U", faceSdkHandle)
        #
        #
        #
        # cdAttr = sdd_addAttrToHandle('M_nose_U', None, faceSdkHandle)
        # sdd_setDrivenKeyframe(FR['M_nose'] + _root + _sdk, 'rx', -30, faceSdkHandle, cdAttr, 1)
        # cdAttr = sdd_addAttrToHandle('M_nose_D', None, faceSdkHandle)
        # sdd_setDrivenKeyframe(FR['M_nose'] + _root + _sdk, 'rx', 15, faceSdkHandle, cdAttr, 1)
        # cdAttr = sdd_addAttrToHandle('M_nose_L', None, faceSdkHandle)
        # sdd_setDrivenKeyframe(FR['M_nose'] + _root + _sdk, 'rz', 30, faceSdkHandle, cdAttr, 1)
        # cdAttr = sdd_addAttrToHandle('M_nose_R', None, faceSdkHandle)
        # sdd_setDrivenKeyframe(FR['M_nose'] + _root + _sdk, 'rz', -30, faceSdkHandle, cdAttr, 1)
        #
        # dis = cmds.getAttr(faceCur + '.nose_factor')
        #
        # cdAttr, mircdAttr = sdd_addAttrToHandle('L_nose_U', 'R_nose_U', faceSdkHandle)
        # sdd_setDrivenKeyframe(FR['L_nose'] + _sdk, 'ty', dis * 0.25, faceSdkHandle, cdAttr, 1, mircdAttr)
        # cdAttr, mircdAttr = sdd_addAttrToHandle('L_nose_D', 'R_nose_D', faceSdkHandle)
        # sdd_setDrivenKeyframe(FR['L_nose'] + _sdk, 'ty', -dis * 0.25, faceSdkHandle, cdAttr, 1, mircdAttr)
        # cdAttr, mircdAttr = sdd_addAttrToHandle('L_nose_O', 'R_nose_O', faceSdkHandle)
        # sdd_setDrivenKeyframe(FR['L_nose'] + _sdk, 'tx', dis * 0.25, faceSdkHandle, cdAttr, 1, mircdAttr)
        # cdAttr, mircdAttr = sdd_addAttrToHandle('L_nose_I', 'R_nose_I', faceSdkHandle)
        # sdd_setDrivenKeyframe(FR['L_nose'] + _sdk, 'tx', -dis * 0.25, faceSdkHandle, cdAttr, 1, mircdAttr)

    def yj_mouthDefultSdk():
        FR, _sdk, _root, _cnt, faceSdkHandle, faceCur = sdd_getDefultSdkName()
        # mouth
        cmds.addAttr(faceSdkHandle, ln='______jaw_________', at='double', min=0, max=0, k=0)
        cmds.setAttr(faceSdkHandle + '.______jaw_________', cb=1)

        dis = cmds.getAttr(faceCur + '.mouth_factor')

        cdAttr = sdd_addAttrToHandle('M_snap_UprLip_2_D', None, faceSdkHandle)
        #
        cdAttr = sdd_addAttrToHandle('M_snap_UprLip_2_I', None, faceSdkHandle)
        #
        cdAttr = sdd_addAttrToHandle('M_snap_UprLip_2_O', None, faceSdkHandle)
        #

        cdAttr = sdd_addAttrToHandle('M_snap_UprLip_U', None, faceSdkHandle)
        #
        cdAttr = sdd_addAttrToHandle('M_snap_UprLip_I', None, faceSdkHandle)
        #
        cdAttr = sdd_addAttrToHandle('M_snap_UprLip_O', None, faceSdkHandle)
        #
        cdAttr = sdd_addAttrToHandle('M_snap_UprLip_S', None, faceSdkHandle)

        #
        cdAttr, mircdAttr = sdd_addAttrToHandle('L_snap_UprLip_2_U', 'R_snap_UprLip_2_U', faceSdkHandle)
        #
        cdAttr, mircdAttr = sdd_addAttrToHandle('L_snap_UprLip_2_O', 'R_snap_UprLip_2_O', faceSdkHandle)
        #
        cdAttr, mircdAttr = sdd_addAttrToHandle('L_snap_Crnr_2_D', 'R_snap_Crnr_2_D', faceSdkHandle)
        #
        cdAttr, mircdAttr = sdd_addAttrToHandle('L_snap_Crnr_2_B', 'R_snap_Crnr_2_B', faceSdkHandle)
        #
        cdAttr, mircdAttr = sdd_addAttrToHandle('L_snap_Crnr_2_O', 'R_snap_Crnr_2_O', faceSdkHandle)

        #

        #
        cdAttr, mircdAttr = sdd_addAttrToHandle('L_snap_UprLip_U', 'R_snap_UprLip_U', faceSdkHandle)
        #
        cdAttr, mircdAttr = sdd_addAttrToHandle('L_snap_UprLip_D', 'R_snap_UprLip_D', faceSdkHandle)
        #
        cdAttr, mircdAttr = sdd_addAttrToHandle('L_snap_UprLip_I', 'R_snap_UprLip_I', faceSdkHandle)
        #
        cdAttr, mircdAttr = sdd_addAttrToHandle('L_snap_UprLip_O', 'R_snap_UprLip_O', faceSdkHandle)

        #

        cdAttr = sdd_addAttrToHandle('M_snap_Mouth_U', None, faceSdkHandle)
        #
        cdAttr = sdd_addAttrToHandle('M_snap_Mouth_I', None, faceSdkHandle)
        #
        cdAttr = sdd_addAttrToHandle('M_snap_Mouth_O', None, faceSdkHandle)
        #
        cdAttr, mircdAttr = sdd_addAttrToHandle('L_M_snap_Mouth', 'R_M_snap_Mouth', faceSdkHandle)
        #

        #
        cdAttr = sdd_addAttrToHandle('M_snap_LwrLip_U', None, faceSdkHandle)
        #
        cdAttr = sdd_addAttrToHandle('M_snap_LwrLip_D', None, faceSdkHandle)
        #
        cdAttr = sdd_addAttrToHandle('M_snap_LwrLip_L', None, faceSdkHandle)
        #
        cdAttr = sdd_addAttrToHandle('M_snap_LwrLip_R', None, faceSdkHandle)
        #
        cdAttr = sdd_addAttrToHandle('M_snap_LwrLip_I', None, faceSdkHandle)
        #
        cdAttr = sdd_addAttrToHandle('M_snap_LwrLip_O', None, faceSdkHandle)

        #
        cdAttr, mircdAttr = sdd_addAttrToHandle('L_snap_LwrLip_U', 'R_snap_LwrLip_U', faceSdkHandle)
        #
        cdAttr, mircdAttr = sdd_addAttrToHandle('L_snap_LwrLip_D', 'R_snap_LwrLip_D', faceSdkHandle)
        #
        cdAttr, mircdAttr = sdd_addAttrToHandle('L_snap_LwrLip_L', 'R_snap_LwrLip_L', faceSdkHandle)
        #
        cdAttr, mircdAttr = sdd_addAttrToHandle('L_snap_LwrLip_I', 'R_snap_LwrLip_I', faceSdkHandle)
        #

        #
        cdAttr = sdd_addAttrToHandle('M_snap_Chin_U', None, faceSdkHandle)
        #
        cdAttr = sdd_addAttrToHandle('M_snap_Chin_D', None, faceSdkHandle)
        #
        cdAttr = sdd_addAttrToHandle('M_snap_Chin_I', None, faceSdkHandle)
        #
        cdAttr = sdd_addAttrToHandle('M_snap_Chin_O', None, faceSdkHandle)
        #
        # cdAttr, mircdAttr = sdd_addAttrToHandle('L_M_snap_Chin', 'R_M_snap_Chin', faceSdkHandle)
        #
        #
        cdAttr, mircdAttr = sdd_addAttrToHandle('L_snap_Chin_D', 'R_snap_Chin_D', faceSdkHandle)
        #
        cdAttr, mircdAttr = sdd_addAttrToHandle('L_snap_Chin_O', 'R_snap_Chin_O', faceSdkHandle)
        #

        #
        cdAttr = sdd_addAttrToHandle('M_snap_Jaw_U', None, faceSdkHandle)
        #
        cdAttr = sdd_addAttrToHandle('M_snap_Jaw_D', None, faceSdkHandle)
        #
        cdAttr = sdd_addAttrToHandle('M_snap_Jaw_L', None, faceSdkHandle)
        #
        cdAttr = sdd_addAttrToHandle('M_snap_Jaw_R', None, faceSdkHandle)
        #
        cdAttr = sdd_addAttrToHandle('M_snap_Jaw_I', None, faceSdkHandle)
        #
        cdAttr = sdd_addAttrToHandle('M_snap_Jaw_O', None, faceSdkHandle)

        #
        cdAttr = sdd_addAttrToHandle('M_snap_Neck_U', None, faceSdkHandle)

        # cdAttr = sdd_addAttrToHandle('M_jaw_U', None, faceSdkHandle)
        # cdAttr = sdd_addAttrToHandle('M_jaw_U', None, faceSdkHandle)
        # sdd_setDrivenKeyframe(FR['jaw'] + _sdk, 'rx', -5, faceSdkHandle, cdAttr, 0.5)
        # cdAttr = sdd_addAttrToHandle('M_jaw_D', None, faceSdkHandle)
        # sdd_setDrivenKeyframe(FR['jaw'] + _sdk, 'rx', 30, faceSdkHandle, cdAttr, 1)
        # sdd_setDrivenKeyframe(FR['L_mouth_Corner'] + _sdk, 'tz', -dis * 0.2, faceSdkHandle, cdAttr, 1)
        # sdd_setDrivenKeyframe(FR['R_mouth_Corner'] + _sdk, 'tz', -dis * 0.2, faceSdkHandle, cdAttr, 1)
        #
        # cdAttr = sdd_addAttrToHandle('M_jaw_L', None, faceSdkHandle)
        # sdd_setDrivenKeyframe(FR['jaw'] + _sdk, 'ry', 20, faceSdkHandle, cdAttr, 1)
        # cdAttr = sdd_addAttrToHandle('M_jaw_R', None, faceSdkHandle)
        # sdd_setDrivenKeyframe(FR['jaw'] + _sdk, 'ry', -20, faceSdkHandle, cdAttr, 1)
        #
        # cdAttr = sdd_addAttrToHandle('M_jaw_all_U', None, faceSdkHandle)
        # sdd_setDrivenKeyframe(FR['jaw'] + _root + _sdk, 'ty', dis * 0.5, faceSdkHandle, cdAttr, 1)
        # cdAttr = sdd_addAttrToHandle('M_jaw_all_D', None, faceSdkHandle)
        # sdd_setDrivenKeyframe(FR['jaw'] + _root + _sdk, 'ty', -dis * 0.5, faceSdkHandle, cdAttr, 1)
        # cdAttr = sdd_addAttrToHandle('M_jaw_all_L', None, faceSdkHandle)
        # sdd_setDrivenKeyframe(FR['jaw'] + _root + _sdk, 'tx', dis * 0.5, faceSdkHandle, cdAttr, 1)
        # cdAttr = sdd_addAttrToHandle('M_jaw_all_R', None, faceSdkHandle)
        # sdd_setDrivenKeyframe(FR['jaw'] + _root + _sdk, 'tx', -dis * 0.5, faceSdkHandle, cdAttr, 1)
        #
        # cmds.addAttr(faceSdkHandle, ln='______mouth_______', at='double', min=0, max=0, k=0)
        # cmds.setAttr(faceSdkHandle + '.______mouth_______', cb=1)
        #
        # cdAttr, mircdAttr = sdd_addAttrToHandle('L_mouth_corner_O', 'R_mouth_corner_O', faceSdkHandle)
        # sdd_setDrivenKeyframe(FR['L_mouth_Corner'] + _sdk, 'tx', dis, faceSdkHandle, cdAttr, 1, mircdAttr)
        # sdd_setDrivenKeyframe(FR['L_mouth_Up'] + _sdk, 'tx', dis * 0.5, faceSdkHandle, cdAttr, 1, mircdAttr)
        # sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'tx', dis * 0.5, faceSdkHandle, cdAttr, 1, mircdAttr)
        # sdd_setDrivenKeyframe(FR['L_cheek'] + _sdk, 'tx', dis * 0.5, faceSdkHandle, cdAttr, 1, mircdAttr)
        # sdd_setDrivenKeyframe(FR['L_cheek'] + _sdk, 'tz', dis * 0.5, faceSdkHandle, cdAttr, 1, mircdAttr)
        # sdd_setDrivenKeyframe(FR['L_noseFold'] + _sdk, 'tx', dis * 0.125, faceSdkHandle, cdAttr, 1, mircdAttr)
        #
        # cdAttr, mircdAttr = sdd_addAttrToHandle('L_mouth_corner_I', 'R_mouth_corner_I', faceSdkHandle)
        # sdd_setDrivenKeyframe(FR['L_mouth_Corner'] + _sdk, 'tx', -dis * 1.25, faceSdkHandle, cdAttr, 1, mircdAttr)
        # sdd_setDrivenKeyframe(FR['L_mouth_Up'] + _sdk, 'tx', -dis * 0.625, faceSdkHandle, cdAttr, 1, mircdAttr)
        # sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'tx', -dis * 0.625, faceSdkHandle, cdAttr, 1, mircdAttr)
        # sdd_setDrivenKeyframe(FR['M_mouth_Up'] + _sdk, 'tz', dis * 0.03, faceSdkHandle, cdAttr, 1, mircdAttr)
        # sdd_setDrivenKeyframe(FR['M_mouth_Dn'] + _sdk, 'tz', dis * 0.03, faceSdkHandle, cdAttr, 1, mircdAttr)
        # sdd_setDrivenKeyframe(FR['L_cheek'] + _sdk, 'tx', -dis * 0.5, faceSdkHandle, cdAttr, 1, mircdAttr)
        # sdd_setDrivenKeyframe(FR['L_noseFold'] + _sdk, 'tx', -dis * 0.125, faceSdkHandle, cdAttr, 1, mircdAttr)
        #
        # cdAttr, mircdAttr = sdd_addAttrToHandle('L_mouth_corner_U', 'R_mouth_corner_U', faceSdkHandle)
        # sdd_setDrivenKeyframe(FR['L_mouth_Corner'] + _sdk, 'ty', dis, faceSdkHandle, cdAttr, 1, mircdAttr)
        # sdd_setDrivenKeyframe(FR['L_mouth_Up'] + _sdk, 'ty', dis * 0.25, faceSdkHandle, cdAttr, 1, mircdAttr)
        # sdd_setDrivenKeyframe(FR['L_mouth_Up'] + _sdk, 'rz', 5, faceSdkHandle, cdAttr, 1, mircdAttr)
        # sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'ty', dis * 0.25, faceSdkHandle, cdAttr, 1, mircdAttr)
        # sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'rz', 5, faceSdkHandle, cdAttr, 1, mircdAttr)
        # sdd_setDrivenKeyframe(FR['L_mouth_Corner'] + _sdk, 'tz', -dis * 0.25, faceSdkHandle, cdAttr, 1, mircdAttr)
        # sdd_setDrivenKeyframe(FR['L_mouth_Corner'] + _sdk, 'rz', 10, faceSdkHandle, cdAttr, 1, mircdAttr)
        # sdd_setDrivenKeyframe(FR['L_mouth_Up'] + _sdk, 'rz', 5, faceSdkHandle, cdAttr, 1, mircdAttr)
        # sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'rz', 5, faceSdkHandle, cdAttr, 1, mircdAttr)
        # sdd_setDrivenKeyframe(FR['L_cheek'] + _sdk, 'ty', dis * 0.5, faceSdkHandle, cdAttr, 1, mircdAttr)
        # sdd_setDrivenKeyframe(FR['L_noseFold'] + _sdk, 'ty', dis * 0.125, faceSdkHandle, cdAttr, 1, mircdAttr)
        #
        # cdAttr, mircdAttr = sdd_addAttrToHandle('L_mouth_corner_D', 'R_mouth_corner_D', faceSdkHandle)
        # sdd_setDrivenKeyframe(FR['L_mouth_Corner'] + _sdk, 'ty', -dis * 0.625, faceSdkHandle, cdAttr, 1, mircdAttr)
        # sdd_setDrivenKeyframe(FR['L_mouth_Up'] + _sdk, 'ty', -dis * 0.25, faceSdkHandle, cdAttr, 1, mircdAttr)
        # sdd_setDrivenKeyframe(FR['L_mouth_Up'] + _sdk, 'rz', -5, faceSdkHandle, cdAttr, 1, mircdAttr)
        # sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'ty', -dis * 0.25, faceSdkHandle, cdAttr, 1, mircdAttr)
        # sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'rz', -5, faceSdkHandle, cdAttr, 1, mircdAttr)
        # sdd_setDrivenKeyframe(FR['L_mouth_Corner'] + _sdk, 'tz', -dis * 0.25, faceSdkHandle, cdAttr, 1, mircdAttr)
        # sdd_setDrivenKeyframe(FR['L_mouth_Corner'] + _sdk, 'rz', -10, faceSdkHandle, cdAttr, 1, mircdAttr)
        # sdd_setDrivenKeyframe(FR['L_mouth_Up'] + _sdk, 'rz', -5, faceSdkHandle, cdAttr, 1, mircdAttr)
        # sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'rz', -5, faceSdkHandle, cdAttr, 1, mircdAttr)
        # sdd_setDrivenKeyframe(FR['L_cheek'] + _sdk, 'ty', -dis * 0.5, faceSdkHandle, cdAttr, 1, mircdAttr)
        # sdd_setDrivenKeyframe(FR['L_noseFold'] + _sdk, 'ty', -dis * 0.125, faceSdkHandle, cdAttr, 1, mircdAttr)
        #
        # #
        # cdAttr, mircdAttr = sdd_addAttrToHandle('L_mouth_Up_U', 'R_mouth_Up_U', faceSdkHandle)
        # sdd_setDrivenKeyframe(FR['L_mouth_Up'] + _sdk, 'ty', dis * 0.6, faceSdkHandle, cdAttr, 1, mircdAttr)
        # sdd_setDrivenKeyframe(FR['M_mouth_Up'] + _sdk, 'ty', dis * 0.25, faceSdkHandle, cdAttr, 1, mircdAttr)
        # sdd_setDrivenKeyframe(FR['M_mouth_Up'] + _sdk, 'rz', 10, faceSdkHandle, cdAttr, 1, mircdAttr)
        #
        # cdAttr, mircdAttr = sdd_addAttrToHandle('L_mouth_Up_D', 'R_mouth_Up_D', faceSdkHandle)
        # sdd_setDrivenKeyframe(FR['L_mouth_Up'] + _sdk, 'ty', -dis * 0.6, faceSdkHandle, cdAttr, 1, mircdAttr)
        # sdd_setDrivenKeyframe(FR['M_mouth_Up'] + _sdk, 'ty', -dis * 0.25, faceSdkHandle, cdAttr, 1, mircdAttr)
        # sdd_setDrivenKeyframe(FR['M_mouth_Up'] + _sdk, 'rz', -10, faceSdkHandle, cdAttr, 1, mircdAttr)
        #
        # cdAttr, mircdAttr = sdd_addAttrToHandle('L_mouth_Dn_U', 'R_mouth_Dn_U', faceSdkHandle)
        # sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'ty', -dis * 0.6, faceSdkHandle, cdAttr, 1, mircdAttr)
        # sdd_setDrivenKeyframe(FR['M_mouth_Dn'] + _sdk, 'ty', -dis * 0.1, faceSdkHandle, cdAttr, 1, mircdAttr)
        # sdd_setDrivenKeyframe(FR['M_mouth_Dn'] + _sdk, 'rz', -10, faceSdkHandle, cdAttr, 1, mircdAttr)
        #
        # cdAttr, mircdAttr = sdd_addAttrToHandle('L_mouth_Dn_D', 'R_mouth_Dn_D', faceSdkHandle)
        # sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'ty', dis * 0.6, faceSdkHandle, cdAttr, 1, mircdAttr)
        # sdd_setDrivenKeyframe(FR['M_mouth_Dn'] + _sdk, 'ty', dis * 0.1, faceSdkHandle, cdAttr, 1, mircdAttr)
        # sdd_setDrivenKeyframe(FR['M_mouth_Dn'] + _sdk, 'rz', 10, faceSdkHandle, cdAttr, 1, mircdAttr)
        #
        # cdAttr = sdd_addAttrToHandle('M_mouth_Up_U', None, faceSdkHandle)
        # sdd_setDrivenKeyframe(FR['L_mouth_Up'] + _sdk, 'ty', dis * 0.5, faceSdkHandle, cdAttr, 1)
        # sdd_setDrivenKeyframe(FR['M_mouth_Up'] + _sdk, 'ty', dis * 0.5, faceSdkHandle, cdAttr, 1)
        # sdd_setDrivenKeyframe(FR['R_mouth_Up'] + _sdk, 'ty', dis * 0.5, faceSdkHandle, cdAttr, 1)
        #
        # cdAttr = sdd_addAttrToHandle('M_mouth_Dn_U', None, faceSdkHandle)
        # sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'ty', dis * 0.4, faceSdkHandle, cdAttr, 1)
        # sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'tz', dis * 0.2, faceSdkHandle, cdAttr, 1)
        # sdd_setDrivenKeyframe(FR['M_mouth_Dn'] + _sdk, 'ty', dis * 0.6, faceSdkHandle, cdAttr, 1)
        # sdd_setDrivenKeyframe(FR['M_mouth_Dn'] + _sdk, 'tz', dis * 0.4, faceSdkHandle, cdAttr, 1)
        # sdd_setDrivenKeyframe(FR['R_mouth_Dn'] + _sdk, 'ty', dis * 0.4, faceSdkHandle, cdAttr, 1)
        # sdd_setDrivenKeyframe(FR['R_mouth_Dn'] + _sdk, 'tz', dis * 0.2, faceSdkHandle, cdAttr, 1)
        #
        # cdAttr = sdd_addAttrToHandle('M_mouth_Dn_D', None, faceSdkHandle)
        # sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'ty', -dis * 0.5, faceSdkHandle, cdAttr, 1)
        # sdd_setDrivenKeyframe(FR['M_mouth_Dn'] + _sdk, 'ty', -dis * 0.5, faceSdkHandle, cdAttr, 1)
        # sdd_setDrivenKeyframe(FR['R_mouth_Dn'] + _sdk, 'ty', -dis * 0.5, faceSdkHandle, cdAttr, 1)
        # #
        #
        # cdAttr = sdd_addAttrToHandle('mouth_Up_roll_O', None, faceSdkHandle)
        # sdd_setDrivenKeyframe(FR['L_mouth_Up'] + _sdk, 'rx', -35, faceSdkHandle, cdAttr, 1)
        # sdd_setDrivenKeyframe(FR['M_mouth_Up'] + _sdk, 'rx', -35, faceSdkHandle, cdAttr, 1)
        # sdd_setDrivenKeyframe(FR['R_mouth_Up'] + _sdk, 'rx', -35, faceSdkHandle, cdAttr, 1)
        #
        # cdAttr = sdd_addAttrToHandle('mouth_Up_roll_I', None, faceSdkHandle)
        # sdd_setDrivenKeyframe(FR['L_mouth_Up'] + _sdk, 'rx', 35, faceSdkHandle, cdAttr, 1)
        # sdd_setDrivenKeyframe(FR['M_mouth_Up'] + _sdk, 'rx', 35, faceSdkHandle, cdAttr, 1)
        # sdd_setDrivenKeyframe(FR['R_mouth_Up'] + _sdk, 'rx', 35, faceSdkHandle, cdAttr, 1)
        #
        # cdAttr = sdd_addAttrToHandle('mouth_Dn_roll_O', None, faceSdkHandle)
        # sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'rx', 35, faceSdkHandle, cdAttr, 1, mircdAttr)
        # sdd_setDrivenKeyframe(FR['M_mouth_Dn'] + _sdk, 'rx', 35, faceSdkHandle, cdAttr, 1, mircdAttr)
        # sdd_setDrivenKeyframe(FR['R_mouth_Dn'] + _sdk, 'rx', 35, faceSdkHandle, cdAttr, 1, mircdAttr)
        #
        # cdAttr = sdd_addAttrToHandle('mouth_Dn_roll_I', None, faceSdkHandle)
        # sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'rx', -35, faceSdkHandle, cdAttr, 1, mircdAttr)
        # sdd_setDrivenKeyframe(FR['M_mouth_Dn'] + _sdk, 'rx', -35, faceSdkHandle, cdAttr, 1, mircdAttr)
        # sdd_setDrivenKeyframe(FR['R_mouth_Dn'] + _sdk, 'rx', -35, faceSdkHandle, cdAttr, 1, mircdAttr)

    def yj_importAndConnectPanel():
        T = sdd_returnTempNameDirc()
        FR, FRJntPos, FRUIPos = sdd_frTNameDirc()
        _root = T['_root']
        _sdk = T['_sdk']
        _cnt = T['_cnt']
        _grp = T['_grp']
        faceCur = 'faceMoveCur'
        panelGrp = 'Face_Panel_grp'
        cmds.delete(cmds.parentConstraint(faceCur, panelGrp))
        bbox = sdd_getBoundingBox(faceCur)
        cmds.setAttr(panelGrp + '.tx', bbox[0])

        sdd_connectPanelAttr('M_Brow_snap_U', 'Brow_cntr.ty', 1)
        sdd_connectPanelAttr('M_Brow_snap_D', 'Brow_cntr.ty', -1)
        sdd_connectPanelAttr('M_Brow_snap_I', 'Brow_cntr.tx', -1)
        sdd_connectPanelAttr('L_snap_BrowIn_U', 'BrowIn_L_cntr.ty', 1)
        sdd_connectPanelAttr('L_snap_BrowIn_D', 'BrowIn_L_cntr.ty', -1)
        sdd_connectPanelAttr('L_snap_BrowOut_U', 'BrowOut_L_cntr.ty', 1)
        sdd_connectPanelAttr('L_snap_BrowOut_D', 'BrowOut_L_cntr.ty', -1)

        sdd_connectPanelAttr('R_snap_BrowIn_U', 'BrowIn_R_cntr.ty', 1)
        sdd_connectPanelAttr('R_snap_BrowIn_D', 'BrowIn_R_cntr.ty', -1)
        sdd_connectPanelAttr('R_snap_BrowOut_U', 'R_snap_BrowOut_U.ty', 1)
        sdd_connectPanelAttr('R_snap_BrowOut_D', 'R_snap_BrowOut_D.ty', -1)
        # sdd_connectPanelAttr('R_brow_Out_D', 'Face_R_brow_b_anim.ty', -1)

        # sdd_connectPanelAttr('L_brow_Mid_U', 'Face_L_brow_b_anim.rz', -15)
        # sdd_connectPanelAttr('L_brow_Mid_D', 'Face_L_brow_b_anim.rz', 15)

        # sdd_connectPanelAttr('R_brow_Mid_U', 'Face_R_brow_b_anim.rz', 15)
        # sdd_connectPanelAttr('R_brow_Mid_D', 'Face_R_brow_b_anim.rz', -15)

        sdd_connectPanelAttr('L_snap_UprLid_U', 'UprLid_L_cntr.ty', 1)
        sdd_connectPanelAttr('L_snap_UprLid_D', 'UprLid_L_cntr.ty', -1)
        sdd_connectPanelAttr('L_snap_LwrLid_U', 'LwrLid_L_cntr.ty', 1)
        sdd_connectPanelAttr('L_snap_LwrLid_D', 'LwrLid_L_cntr.ty', -1)

        sdd_connectPanelAttr('R_snap_UprLid_U', 'UprLid_R_cntr.ty', 1)
        sdd_connectPanelAttr('R_snap_UprLid_D', 'UprLid_R_cntr.ty', -1)
        sdd_connectPanelAttr('R_snap_LwrLid_U', 'LwrLid_R_cntr.ty', 1)
        sdd_connectPanelAttr('R_snap_LwrLid_D', 'LwrLid_R_cntr.ty', -1)

        # sdd_connectPanelAttr('L_eyelid_close', 'Face_L_eyelid_close_anim.ty', -1)
        # sdd_connectPanelAttr('R_eyelid_close', 'Face_R_eyelid_close_anim.ty', -1)
        #
        sdd_connectPanelAttr('L_snap_EyeSqz_U', 'EyeSqz_L_cntr.ty', 1)
        sdd_connectPanelAttr('L_snap_EyeSqz_D', 'EyeSqz_L_cntr.ty', -1)
        sdd_connectPanelAttr('R_snap_EyeSqz_I', 'EyeSqz_R_cntr.tx', -1)
        sdd_connectPanelAttr('R_snap_EyeSqz_O', 'EyeSqz_R_cntr.tx', 1)
        sdd_connectPanelAttr('R_snap_EyeSqz_U', 'EyeSqz_R_cntr.ty', 1)
        sdd_connectPanelAttr('R_snap_EyeSqz_D', 'EyeSqz_R_cntr.ty', -1)
        sdd_connectPanelAttr('R_snap_EyeSqz_I', 'EyeSqz_R_cntr.tx', -1)
        sdd_connectPanelAttr('R_snap_EyeSqz_O', 'EyeSqz_R_cntr.tx', 1)
        #
        # sdd_connectPanelAttr('L_eyelid_Up_side_O', 'Face_L_eyelid_Up_anim.tx', 1)
        # sdd_connectPanelAttr('L_eyelid_Up_side_I', 'Face_L_eyelid_Up_anim.tx', -1)
        # sdd_connectPanelAttr('L_eyelid_Dn_side_I', 'Face_L_eyelid_Dn_anim.tx', -1)
        # sdd_connectPanelAttr('L_eyelid_Dn_side_O', 'Face_L_eyelid_Dn_anim.tx', 1)
        #
        # sdd_connectPanelAttr('R_eyelid_Up_side_O', 'Face_R_eyelid_Up_anim.tx', 1)
        # sdd_connectPanelAttr('R_eyelid_Up_side_I', 'Face_R_eyelid_Up_anim.tx', -1)
        # sdd_connectPanelAttr('R_eyelid_Dn_side_I', 'Face_R_eyelid_Dn_anim.tx', -1)
        # sdd_connectPanelAttr('R_eyelid_Dn_side_O', 'Face_R_eyelid_Dn_anim.tx', 1)
        #
        sdd_connectPanelAttr('L_snap_Cheek_U', 'Cheek_L_cntr.ty', 1)
        sdd_connectPanelAttr('R_snap_Cheek_U', 'Cheek_R_cntr.ty', 1)
        #
        sdd_connectPanelAttr('L_snap_Cheek_2_U', 'Cheek_L_2_cntr.ty', 1)
        sdd_connectPanelAttr('L_snap_Cheek_2_O', 'Cheek_L_2_cntr.tx', 1)
        sdd_connectPanelAttr('L_snap_Cheek_2_I', 'LwrLid_L_cntr.tx', -1)
        sdd_connectPanelAttr('L_snap_Cheek_2_U', 'LwrLid_L_cntr.ty', 1)
        sdd_connectPanelAttr('L_snap_Cheek_2_O', 'LwrLid_L_cntr.tx', 1)
        sdd_connectPanelAttr('L_snap_Cheek_2_I', 'LwrLid_L_cntr.tx', -1)
        #
        sdd_connectPanelAttr('M_snap_Nose_I', 'Nose_cntr.tx', 1)
        sdd_connectPanelAttr('M_snap_Nose_I', 'Nose_cntr.tx', -1)
        sdd_connectPanelAttr('L_snap_Nose_U', 'Nose_L_cntr.ty', 1)
        sdd_connectPanelAttr('R_snap_Nose_U', 'Nose_L_cntr.ty', 1)

        sdd_connectPanelAttr('M_snap_UprLip_2_D', 'UprLip_2_cntr.ty', -1)
        sdd_connectPanelAttr('M_snap_UprLip_2_I', 'UprLip_2_cntr.tx', -1)
        sdd_connectPanelAttr('M_snap_UprLip_2_O', 'UprLip_2_cntr.tx', 1)
        '''
        sdd_connectPanelAttr('L_mouth_corner_O', 'Crnr_L_2_cntr.txLink', 1)#here
        sdd_connectPanelAttr('L_mouth_corner_I', 'Crnr_L_2_cntr.txLink', -1)#here
        sdd_connectPanelAttr('L_mouth_corner_U', 'Crnr_L_2_cntr.tyLink', 1)#here
        sdd_connectPanelAttr('L_mouth_corner_D', 'Crnr_L_2_cntr.tyLink', -1)#here

        sdd_connectPanelAttr('R_mouth_corner_O', 'Crnr_R_2_cntr.txLink', 1)#here
        sdd_connectPanelAttr('R_mouth_corner_I', 'Crnr_R_2_cntr.txLink', -1)#here
        sdd_connectPanelAttr('R_mouth_corner_U', 'Crnr_R_2_cntr.tyLink', 1)#here
        sdd_connectPanelAttr('R_mouth_corner_D', 'Crnr_R_2_cntr.tyLink', -1)#here
        '''

        sdd_connectPanelAttr('M_snap_UprLip_U', 'UprLip_cntr.ty', 1)
        sdd_connectPanelAttr('M_snap_UprLip_I', 'UprLip_cntr.tz', -1)
        sdd_connectPanelAttr('M_snap_UprLip_O', 'UprLip_cntr.tz', 1)
        sdd_connectPanelAttr('M_snap_UprLip_S', 'UprLip_cntr.tx', 1)

        sdd_connectPanelAttr('L_snap_UprLip_2_U', 'UprLip_L_2_cntr.ty', 1)
        sdd_connectPanelAttr('L_snap_UprLip_2_O', 'UprLip_L_2_cntr.tx', 1)

        # sdd_connectPanelAttr('L_mouth_Up_U', 'Face_L_lip_side_Up_anim.ty', 1)
        # sdd_connectPanelAttr('L_mouth_Up_D', 'Face_L_lip_side_Up_anim.ty', -1)
        # sdd_connectPanelAttr('L_mouth_Dn_U', 'Face_L_lip_side_Dn_anim.ty', 1)
        # sdd_connectPanelAttr('L_mouth_Dn_D', 'Face_L_lip_side_Dn_anim.ty', -1)

        sdd_connectPanelAttr('L_snap_Crnr_2_D', 'Crnr_L_2_cntr.ty', -1)
        sdd_connectPanelAttr('L_snap_Crnr_2_B', 'Crnr_L_2_cntr.tz', -1)
        sdd_connectPanelAttr('L_snap_Crnr_2_O', 'Crnr_L_2_cntr.tx', 1)
        sdd_connectPanelAttr('R_snap_Crnr_2_D', 'Crnr_R_2_cntr.ty', -1)
        sdd_connectPanelAttr('R_snap_Crnr_2_B', 'Crnr_R_2_cntr.tz', -1)
        sdd_connectPanelAttr('R_snap_Crnr_2_O', 'Crnr_R_2_cntr.tx', 1)
        # sdd_connectPanelAttr('R_mouth_Dn_D', 'Face_R_lip_side_Dn_anim.ty', -1)

        sdd_connectPanelAttr('L_snap_UprLip_U', 'UprLip_L_cntr.ty', 1)
        sdd_connectPanelAttr('L_snap_UprLip_D', 'UprLip_L_cntr.ty', -1)
        sdd_connectPanelAttr('L_snap_UprLip_I', 'UprLip_L_cntr.tx', -1)
        sdd_connectPanelAttr('L_snap_UprLip_O', 'UprLip_L_cntr.tx', 1)
        sdd_connectPanelAttr('R_snap_UprLip_U', 'UprLip_R_cntr.ty', 1)
        sdd_connectPanelAttr('R_snap_UprLip_D', 'UprLip_R_cntr.ty', -1)
        sdd_connectPanelAttr('R_snap_UprLip_I', 'UprLip_R_cntr.tx', -1)
        sdd_connectPanelAttr('R_snap_UprLip_O', 'UprLip_R_cntr.tx', 1)

        sdd_connectPanelAttr('M_snap_Mouth_U', 'UprLip_cntr.ty', 1)
        sdd_connectPanelAttr('M_snap_Mouth_I', 'UprLip_cntr.tx', -1)
        sdd_connectPanelAttr('M_snap_Mouth_O', 'UprLip_cntr.tx', 1)
        sdd_connectPanelAttr('L_M_snap_Mouth', 'Mouth_cntr.tx', 1)
        sdd_connectPanelAttr('R_M_snap_Mouth', 'Mouth_cntr.tx', -1)
        # sdd_connectPanelAttr('mouth_O', 'Face_L_mouth_O_anim.tx', 1)
        # sdd_connectPanelAttr('mouth_U', 'Face_L_mouth_U_anim.tx', 1)

        # sdd_connectPanelAttr('L_eyeBall_U', 'Face_L_eye_anim.ty', 1)
        # sdd_connectPanelAttr('L_eyeBall_D', 'Face_L_eye_anim.ty', -1)
        # sdd_connectPanelAttr('L_eyeBall_O', 'Face_L_eye_anim.tx', 1)
        # sdd_connectPanelAttr('L_eyeBall_I', 'Face_L_eye_anim.tx', -1)
        #
        # sdd_connectPanelAttr('R_eyeBall_U', 'Face_R_eye_anim.ty', 1)
        # sdd_connectPanelAttr('R_eyeBall_D', 'Face_R_eye_anim.ty', -1)
        # sdd_connectPanelAttr('R_eyeBall_I', 'Face_R_eye_anim.tx', 1)
        # sdd_connectPanelAttr('R_eyeBall_O', 'Face_R_eye_anim.tx', -1)
        #
        # sdd_connectPanelAttr('L_eyeAll_U', 'Face_L_eye_all_anim.ty', 1)
        # sdd_connectPanelAttr('L_eyeAll_D', 'Face_L_eye_all_anim.ty', -1)
        # sdd_connectPanelAttr('L_eyeAll_O', 'Face_L_eye_all_anim.tx', 1)
        # sdd_connectPanelAttr('L_eyeAll_I', 'Face_L_eye_all_anim.tx', -1)

        # cmds.connectAttr('Face_L_eye_all_anim.sx', FR['L_eye_root'] + _sdk + '.sx')
        # cmds.connectAttr('Face_L_eye_all_anim.sy', FR['L_eye_root'] + _sdk + '.sy')



        sdd_connectPanelAttr('M_snap_LwrLip_U', 'LwrLip_cntr.ty', 1)
        sdd_connectPanelAttr('M_snap_LwrLip_D', 'LwrLip_cntr.ty', -1)
        sdd_connectPanelAttr('M_snap_LwrLip_L', 'LwrLip_cntr.tx', 1)
        sdd_connectPanelAttr('M_snap_LwrLip_R', 'LwrLip_cntr.tx', -1)
        sdd_connectPanelAttr('M_snap_LwrLip_I', 'LwrLip_cntr.tz', -1)
        sdd_connectPanelAttr('M_snap_LwrLip_O', 'LwrLip_cntr.tz', 1)

        # cdAttr, mircdAttr = sdd_addAttrToHandle('L_snap_LwrLip_U', 'R_snap_LwrLip_U', faceSdkHandle)
        # #
        # cdAttr, mircdAttr = sdd_addAttrToHandle('L_snap_LwrLip_D', 'R_snap_LwrLip_D', faceSdkHandle)
        # #
        # cdAttr, mircdAttr = sdd_addAttrToHandle('L_snap_LwrLip_L', 'R_snap_LwrLip_L', faceSdkHandle)
        # #
        # cdAttr, mircdAttr = sdd_addAttrToHandle('L_snap_LwrLip_I', 'R_snap_LwrLip_I', faceSdkHandle)

        sdd_connectPanelAttr('L_snap_LwrLip_U', 'LwrLip_L_cntr.ty', 1)
        sdd_connectPanelAttr('L_snap_LwrLip_D', 'LwrLip_L_cntr.ty', -1)
        sdd_connectPanelAttr('L_snap_LwrLip_L', 'LwrLip_L_cntr.tx', 1)
        sdd_connectPanelAttr('L_snap_LwrLip_I', 'LwrLip_L_cntr.tz', -1)
        sdd_connectPanelAttr('R_snap_LwrLip_U', 'LwrLip_R_cntr.ty', 1)
        sdd_connectPanelAttr('R_snap_LwrLip_D', 'LwrLip_R_cntr.ty', -1)
        sdd_connectPanelAttr('R_snap_LwrLip_L', 'LwrLip_R_cntr.tx', 1)
        sdd_connectPanelAttr('R_snap_LwrLip_I', 'LwrLip_R_cntr.tz', -1)

        # cdAttr = sdd_addAttrToHandle('M_snap_Chin_U', None, faceSdkHandle)
        # #
        # cdAttr = sdd_addAttrToHandle('M_snap_Chin_D', None, faceSdkHandle)
        # #
        # cdAttr = sdd_addAttrToHandle('M_snap_Chin_I', None, faceSdkHandle)
        # #
        # cdAttr = sdd_addAttrToHandle('M_snap_Chin_O', None, faceSdkHandle)

        sdd_connectPanelAttr('M_snap_Chin_D', 'Chin_cntr.ty', -1)
        sdd_connectPanelAttr('M_snap_Chin_B', 'Chin_cntr.tz', -1)
        sdd_connectPanelAttr('M_snap_Chin_O', 'Chin_cntr.tz', 1)

        # cdAttr, mircdAttr = sdd_addAttrToHandle('L_snap_Chin_D', 'R_snap_Chin_D', faceSdkHandle)
        # #
        # cdAttr, mircdAttr = sdd_addAttrToHandle('L_snap_Chin_O', 'R_snap_Chin_O', faceSdkHandle)
        sdd_connectPanelAttr('L_snap_Chin_D', 'Chin_L_cntr.ty', -1)
        sdd_connectPanelAttr('L_snap_Chin_O', 'Chin_L_cntr.tx', 1)
        sdd_connectPanelAttr('R_snap_Chin_D', 'Chin_R_cntr.ty', -1)
        sdd_connectPanelAttr('R_snap_Chin_O', 'Chin_R_cntr.tx', 1)
        # cmds.connectAttr('Face_R_eye_all_anim.sx', FR['R_eye_root'] + _sdk + '.sx')
        # cmds.connectAttr('Face_R_eye_all_anim.sy', FR['R_eye_root'] + _sdk + '.sy')
        #
        # cmds.connectAttr('Face_mouth_all_anim.sx', FR['jaw'] + _root + _sdk + '.sx')
        # cmds.connectAttr('Face_mouth_all_anim.sy', FR['jaw'] + _root + _sdk + '.sy')

        #
        # cdAttr = sdd_addAttrToHandle('M_snap_Jaw_U', None, faceSdkHandle)
        # #
        # cdAttr = sdd_addAttrToHandle('M_snap_Jaw_D', None, faceSdkHandle)
        # #
        # cdAttr = sdd_addAttrToHandle('M_snap_Jaw_L', None, faceSdkHandle)
        # #
        # cdAttr = sdd_addAttrToHandle('M_snap_Jaw_R', None, faceSdkHandle)
        # #
        # cdAttr = sdd_addAttrToHandle('M_snap_Jaw_I', None, faceSdkHandle)
        # #
        # cdAttr = sdd_addAttrToHandle('M_snap_Jaw_O', None, faceSdkHandle)
        sdd_connectPanelAttr('M_snap_Jaw_U', 'Jaw_cntr.ty', 1)
        sdd_connectPanelAttr('M_snap_Jaw_D', 'Jaw_cntr.ty', -1)
        sdd_connectPanelAttr('M_snap_Jaw_L', 'Jaw_cntr.tx', 1)
        sdd_connectPanelAttr('M_snap_Jaw_R', 'Jaw_cntr.tx', -1)
        sdd_connectPanelAttr('M_snap_Jaw_I', 'Jaw_cntr.tz', -1)
        sdd_connectPanelAttr('M_snap_Jaw_O', 'Jaw_cntr.tz', 1)
        '''
        cmds.connectAttr('Face_jaw_anim.jawTranslateX', FR['jaw'] + _grp + '.tx')
        cmds.connectAttr('Face_jaw_anim.jawTranslateY', FR['jaw'] + _grp + '.ty')
        cmds.connectAttr('Face_jaw_anim.jawTranslateZ', FR['jaw'] + _grp + '.tz')
        '''


        # sdd_connectPanelAttr('M_nose_U', 'Face_nose_anim.ty', 1)
        # sdd_connectPanelAttr('M_nose_D', 'Face_nose_anim.ty', -1)
        # sdd_connectPanelAttr('M_nose_L', 'Face_nose_anim.tx', 1)
        # sdd_connectPanelAttr('M_nose_R', 'Face_nose_anim.tx', -1)
        #
        # sdd_connectPanelAttr('L_nose_U', 'Face_L_nose_anim.ty', 1)
        # sdd_connectPanelAttr('L_nose_D', 'Face_L_nose_anim.ty', -1)
        # sdd_connectPanelAttr('L_nose_O', 'Face_L_nose_anim.tx', 1)
        # sdd_connectPanelAttr('L_nose_I', 'Face_L_nose_anim.tx', -1)
        #
        # sdd_connectPanelAttr('R_nose_U', 'Face_R_nose_anim.ty', 1)
        # sdd_connectPanelAttr('R_nose_D', 'Face_R_nose_anim.ty', -1)
        # sdd_connectPanelAttr('R_nose_O', 'Face_R_nose_anim.tx', 1)
        # sdd_connectPanelAttr('R_nose_I', 'Face_R_nose_anim.tx', -1)
        #
        # sdd_connectPanelAttr('L_cheek_U', 'Face_L_cheek_anim.ty', 1)
        # sdd_connectPanelAttr('L_cheek_O', 'Face_L_cheek_anim.tx', 1)
        # sdd_connectPanelAttr('L_cheek_I', 'Face_L_cheek_anim.tx', -1)
        #
        # sdd_connectPanelAttr('R_cheek_U', 'Face_R_cheek_anim.ty', 1)
        # sdd_connectPanelAttr('R_cheek_O', 'Face_R_cheek_anim.tx', 1)
        # sdd_connectPanelAttr('R_cheek_I', 'Face_R_cheek_anim.tx', -1)
        #
        # cmds.connectAttr('Face_mouth_sticky_anim.ty', FR['jaw'] + _cnt + '.Lip_Sticky_P')
        # cmds.connectAttr('Face_L_lip_corner_anim.ty', FR['jaw'] + _cnt + '.L_Lip_Corner_P')
        # cmds.connectAttr('Face_R_lip_corner_anim.ty', FR['jaw'] + _cnt + '.R_Lip_Corner_P')
        #
        # sdd_connectPanelAttr('M_jaw_U', 'Face_jaw_anim.ty', 0.5)
        # sdd_connectPanelAttr('M_jaw_D', 'Face_jaw_anim.ty', -1)
        # sdd_connectPanelAttr('M_jaw_L', 'Face_jaw_anim.tx', 1)
        # sdd_connectPanelAttr('M_jaw_R', 'Face_jaw_anim.tx', -1)
        #
        # sdd_connectPanelAttr('M_jaw_all_U', 'Face_mouth_all_anim.ty', 1)
        # sdd_connectPanelAttr('M_jaw_all_D', 'Face_mouth_all_anim.ty', -1)
        # sdd_connectPanelAttr('M_jaw_all_L', 'Face_mouth_all_anim.tx', 1)
        # sdd_connectPanelAttr('M_jaw_all_R', 'Face_mouth_all_anim.tx', -1)
        #
        # sdd_connectPanelAttr('M_mouth_Up_U', 'Face_lip_open_Up_anim.ty', 1)
        # sdd_connectPanelAttr('M_mouth_Dn_U', 'Face_lip_open_Dn_anim.ty', 1)
        # sdd_connectPanelAttr('M_mouth_Dn_D', 'Face_lip_open_Dn_anim.ty', -1)
        #
        # sdd_connectPanelAttr('L_pump_O', 'Face_L_Pump_anim.tx', 1)
        # sdd_connectPanelAttr('R_pump_O', 'Face_R_Pump_anim.tx', 1)
