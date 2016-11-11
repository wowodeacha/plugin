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
