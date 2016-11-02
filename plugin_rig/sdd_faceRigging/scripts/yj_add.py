# -*- coding: utf-8 -*-
#
# author YangJie
# mail wowodeacha@gmail.com
#
#
import maya.OpenMaya as OpenMaya
import maya.cmds as cmds

customDir = {"HardCtrl": "HardCtrl", "Head_cntr": "Head_cntr",
             "BrowOut_R_cntr": "BrowOut_R_cntr", "BrowIn_R_cntr": "BrowIn_R_cntr",
             "Brow_cntr": "Brow_cntr",
             "BrowOut_L_cntr": "BrowOut_L_cntr", "BrowIn_L_cntr": "BrowIn_L_cntr",
             "UprLid_R_cntr": "UprLid_R_cntr", "LwrLid_R_cntr": "LwrLid_R_cntr",
             "UprLid_L_cntr": "UprLid_L_cntr", "LwrLid_L_cntr": "LwrLid_L_cntr",
             "EyeSqz_R_cntr": "EyeSqz_R_cntr",
             "EyeSqz_L_cntr": "EyeSqz_L_cntr",
             "Cheek_R_2_cntr": "Cheek_R_2_cntr",
             "Cheek_L_2_cntr": "Cheek_L_2_cntr",
             "Cheek_R_cntr": "Cheek_R_cntr",
             "Cheek_L_cntr": "Cheek_L_cntr",
             "Nose_R_cntr": "Nose_R_cntr",
             "Nose_cntr": "Nose_cntr",
             "Nose_L_cntr": "Nose_L_cntr",
             "UprLip_R_2_cntr": "UprLip_R_2_cntr", "UprLip_2_cntr": "UprLip_2_cntr",
             "UprLip_L_2_cntr": "UprLip_L_2_cntr",
             "Crnr_R_2_cntr": "Crnr_R_2_cntr", "Crnr_R_cntr": "Crnr_R_cntr", "UprLip_R_cntr": "UprLip_R_cntr",
             "LwrLip_R_cntr": "LwrLip_R_cntr",
             "Crnr_L_2_cntr": "Crnr_L_2_cntr", "Crnr_L_cntr": "Crnr_L_cntr", "UprLip_L_cntr": "UprLip_L_cntr",
             "LwrLip_L_cntr": "LwrLip_L_cntr",
             "UprLip_cntr": "UprLip_cntr", "Mouth_cntr": "Mouth_cntr", "LwrLip_cntr": "LwrLip_cntr",
             "Chin_R_cntr": "Chin_R_cntr", "Chin_cntr": "Chin_cntr", "Chin_L_cntr": "Chin_L_cntr",
             "Jaw_cntr": "Jaw_cntr",
             "Neck_cntr": "Neck_cntr"
             }

jntCtrlDir = {"BrowOut_R_cntr": "R_brow_c_skin", "BrowIn_R_cntr": "R_brow_a_skin",
              "Brow_cntr": "M_brow_skin",
              "BrowOut_L_cntr": "L_brow_c_skin", "BrowIn_L_cntr": "L_brow_a_skin",
              "UprLid_R_cntr": "R_eyelid_Up_skin", "LwrLid_R_cntr": "R_eyelid_Dn_skin",
              "UprLid_L_cntr": "L_eyelid_Up_skin", "LwrLid_L_cntr": "L_eyelid_Dn_skin",
              "EyeSqz_R_cntr": "R_eyelid_Out_skin",
              "EyeSqz_L_cntr": "L_eyelid_Out_skin",
              "Cheek_R_2_cntr": "R_cheek_skin",
              "Cheek_L_2_cntr": "L_cheek_skin",
              "Cheek_R_cntr": "R_cheek_Up_skin",
              "Cheek_L_cntr": "L_cheek_Up_skin",
              "Nose_R_cntr": "R_nose_skin",
              "Nose_cntr": "M_nose_skin",
              "Nose_L_cntr": "L_nose_skin",
              "Crnr_R_cntr": "R_mouth_Corner_skin", "UprLip_R_cntr": "R_mouth_Up_skin",
              "Crnr_L_cntr": "L_mouth_Corner_skin", "UprLip_L_cntr": "L_mouth_Up_skin",
              "LwrLip_L_cntr": "L_mouth_Dn_skin",
              "UprLip_cntr": "M_mouth_Up_skin", "LwrLip_cntr": "M_mouth_Dn_skin",
              "Jaw_cntr": "chin_skin",

              }
CtrlToCtrlDir = {"Head_cntr": "Head_cntr", "UprLip_R_2_cntr": "UprLip_R_2_cntr", "UprLip_2_cntr": "UprLip_2_cntr",
                 "UprLip_L_2_cntr": "UprLip_L_2_cntr",
                 "Crnr_R_2_cntr": "Crnr_R_2_cntr",
                 "LwrLip_R_cntr": "R_mouth_Dn_skin",
                 "Crnr_L_2_cntr": "Crnr_L_2_cntr",
                 "Mouth_cntr": "Mouth_cntr",
                 "Chin_R_cntr": "Chin_R_cntr", "Chin_cntr": "Chin_cntr", "Chin_L_cntr": "Chin_L_cntr",
                 "Neck_cntr": "Neck_cntr"
                 }


class NewCtrlFun(object):
    def __init__(self):
        self.author = "YJ"

    def create_snap_ctrl_step(self, ctrl_name, fin_mesh):
        CtrlGrp_OP = cmds.group(n=ctrl_name + "_op", em=1)
        CtrlGrp_Zero = cmds.group(n=ctrl_name + "_zerp", em=1)
        cmds.delete(cmds.parentConstraint(ctrl_name, CtrlGrp_OP))
        cmds.delete(cmds.parentConstraint(ctrl_name, CtrlGrp_Zero))
        cmds.parent(ctrl_name, CtrlGrp_OP)
        cmds.parent(CtrlGrp_OP, CtrlGrp_Zero)

        follice_t = self.create_closest_follicle(ctrl_name, fin_mesh)
        cmds.parent(CtrlGrp_Zero,follice_t)

        # cmds.file(frRootPath + 'files/hard_ctrl.ma', i=1, type="mayaAscii")

    # 创建距离模型最近的毛囊
    def create_closest_follicle(self, ctrl_name, fin_mesh):

        follicle_name_s = ctrl_name + "_fol_shape"
        follicle_name_s = cmds.createNode('follicle', n=follicle_name_s)
        follicle_name_t_orig = cmds.listRelatives(follicle_name_s, p=1)[0]
        follicle_name_t = ctrl_name + "_fol"
        cmds.rename(follicle_name_t_orig, follicle_name_t)
        cmds.connectAttr(follicle_name_s + '.ot', follicle_name_t + '.t')
        cmds.connectAttr(follicle_name_s + '.or', follicle_name_t + '.r')

        fin_mesh_shape = cmds.listRelatives(fin_mesh, s=1, f=1)[0]
        cmds.connectAttr(fin_mesh_shape + '.worldMatrix[0]', follicle_name_s + '.inputWorldMatrix')
        cmds.connectAttr(fin_mesh_shape + '.outMesh', follicle_name_s + '.inputMesh')

        # 获取最近的UV

        pos = cmds.xform(ctrl_name, q=1, ws=1, t=1)
        curPos = OpenMaya.MPoint(pos[0], pos[1], pos[2])

        secMFnMesh = self.getMfnMeshByName(fin_mesh)
        vtxPointList = OpenMaya.MPointArray()
        secMFnMesh.getPoints(vtxPointList, OpenMaya.MSpace.kWorld)
        clostP = OpenMaya.MPoint()

        util = OpenMaya.MScriptUtil()
        util.createFromInt(0)
        idPointer = util.asIntPtr()

        secMFnMesh.getClosestPoint(curPos, clostP, OpenMaya.MSpace.kWorld, idPointer)
        idx = OpenMaya.MScriptUtil(idPointer).asInt()
        nearestList = OpenMaya.MIntArray()
        secMFnMesh.getPolygonVertices(idx, nearestList)
        tmpdis = None
        retIdx = None
        for d in nearestList:
            dis = vtxPointList[d].distanceTo(curPos)
            if (tmpdis == None or dis < tmpdis):
                tmpdis = dis
                retIdx = d
        uvVtx = cmds.polyListComponentConversion(fin_mesh + '.vtx[%s]' % retIdx, fv=1, tuv=1)
        uvPos = cmds.polyEditUV(uvVtx[0], q=1, u=1)

        cmds.setAttr(follicle_name_s + '.pu', uvPos[0])
        cmds.setAttr(follicle_name_s + '.pv', uvPos[1])
        if not(cmds.objExists("head_face_ctrlFol_grp")):
            follicle_Grp = cmds.group(n="head_face_ctrlFol_grp",em=1)
        cmds.parent(follicle_name_t,follicle_Grp)
        return follicle_name_t

    # 吸附目标到指定模型最近点
    def matchObjToCloset(self, tarMesh, objList):
        # tarMesh 目标模型  objList吸附列表
        tarMesh = self.getMfnMeshByName(tarMesh)
        clostP = OpenMaya.MPoint()
        util = OpenMaya.MScriptUtil()
        util.createFromInt(0)
        idPointer = util.asIntPtr()
        vtxPointList = OpenMaya.MPointArray()
        tarMesh.getPoints(vtxPointList, OpenMaya.MSpace.kWorld)
        locList = objList
        for i in locList:
            secLoc = i
            pos = cmds.xform(secLoc, q=1, ws=1, t=1)
            curPos = OpenMaya.MPoint(pos[0], pos[1], pos[2])
            tarMesh.getClosestPoint(curPos, clostP, OpenMaya.MSpace.kWorld, idPointer)
            idx = OpenMaya.MScriptUtil(idPointer).asInt()
            nearestList = OpenMaya.MIntArray()
            tarMesh.getPolygonVertices(idx, nearestList)
            tmpdis = None
            retIdx = None
            for d in nearestList:
                dis = vtxPointList[d].distanceTo(curPos)
                if (tmpdis == None or dis < tmpdis):
                    tmpdis = dis
                    retIdx = d
            cmds.xform(secLoc, ws=1, t=[vtxPointList[retIdx].x, vtxPointList[retIdx].y, vtxPointList[retIdx].z])

    def getMfnMeshByName(self, name):
        sList = OpenMaya.MSelectionList()
        sList.add(name)
        dagPath = OpenMaya.MDagPath()
        sList.getDagPath(0, dagPath)
        meshPolygon = OpenMaya.MFnMesh(dagPath)
        return meshPolygon


if __name__ == "__main__":
    NCF = NewCtrlFun()
    # NCF.create_snap_ctrl("new")
    # NCF.matchObjToCloset("pSphere1", ["new"])
    NCF.create_snap_ctrl_step("BrowOut_L_cntr", "pSphere1")
