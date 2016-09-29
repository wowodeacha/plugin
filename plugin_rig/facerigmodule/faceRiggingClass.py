# -*- coding: utf-8 -*-
#
# author YangJie
# mail wowodeacha@gmail.com
#
#
import maya.cmds as mpy


class FaceRiggingClass(object):
    def sdd_createSdkJointRigging():
        faceSdkSkinGrp = 'face_sdk_skin_grp'
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

        faceMesh = mpy.textField('frFaceMeshTF', q=1, tx=1)
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

        meshList = mpy.textScrollList('frFaceMeshTSL', q=1, ai=1)
        for i in meshList:
            sdd_tryParent(i, faceSkinMeshGrp)

        bbox = sdd_getBoundingBox(faceSkinMeshGrp)
        mpy.setAttr(faceSkinMeshGrp + '.boxWidthF', bbox[0])
        mpy.setAttr(faceSkinMeshGrp + '.boxWidthS', bbox[1])

        faceOrigMeshGrp = 'face_orig_mesh_grp'
        if mpy.objExists(faceOrigMeshGrp):
            mpy.delete(faceOrigMeshGrp)
        faceOrigMeshGrp = mpy.group(em=1, n=faceOrigMeshGrp)
        mpy.parent(faceOrigMeshGrp, faceBsGrp)
        mpy.setAttr(faceOrigMeshGrp + '.v', 0)

        sdd_connectAttrForce(faceMesh + '.msg', faceSkinMeshGrp + '.faceMesh')
        allMesh = mpy.textScrollList('frFaceMeshTSL', q=1, ai=1)

        for i in range(len(allMesh)):
            origMeshName = allMesh[i] + '_OrigMesh'
            origMeshName = mpy.duplicate(allMesh[i], n=origMeshName)[0]
            sdd_tryParent(origMeshName, faceOrigMeshGrp)
            iOrigAttr = sdd_tryAddMessageAttr(allMesh[i], 'origMesh')
            nOrigAttr = sdd_tryAddMessageAttr(origMeshName, 'origMesh')
            sdd_connectAttrForce(nOrigAttr, iOrigAttr)

            ctrGrp = chr(65 + i) + '_CorrectiveGrp'
            nCtrAttr = sdd_tryAddMessageAttr(origMeshName, 'ctrGrp')
            mpy.setAttr(nCtrAttr, ctrGrp, typ='string')

        sdd_createSdkJntRig()
        sdd_createDefultSdk()

        faceJntList = mpy.listRelatives(faceSdkSkinGrp, c=1, ad=1, typ='joint')
        for i in allMesh:
            mpy.skinCluster(faceJntList, i, mi=1, nw=1, tsb=1)
        mpy.textField('frCurrentMeshTF', e=1, tx='')

        sdd_importAndConnectPanel()
        if (mpy.objExists('Face_Panel_grp')):
            mpy.parent('Face_Panel_grp', faceAnimCtrlGrp)

        sdd_reloadFaceMeshInfo()
