# -*- coding: utf-8 -*-
#
# author     YangJie
# mail      wowodeacha@gmail.com
# created   2016.07.20
# Nothing Impossible
#
#

import maya.cmds as mpy
import maya.OpenMaya as OpenMaya


class FaceRigPubFuc():
    def __init__(self, author='YJ'):
        self.author = author

    @staticmethod
    # 获取目标的父层级
    def set_object_own_parent(in_object):
        '''check attrubute then set parent'''

    # 根据骨骼生成曲线
    def create_cv_by_jnt(self, cv_name, in_list):

        jnt_dir = self.getObjListPivDir(in_list)
        jnt_piv_list = jnt_dir.values()
        mpy.curve(n=cv_name, ep=jnt_piv_list)
        return

    # 2给骨骼添加标签

    def add_label_to_jnt(self, in_jnt_list, in_label):
        for i in in_jnt_list:
            mpy.setAttr(i + '.type', 18)
            mpy.setAttr(i + '.otherType', in_label, type='string')
            mpy.setAttr(i + '.drawLabel', 1)
        return

    ##获取所选骨骼列表
    def getSelectedJntList(self):
        jntList = mpy.ls(sl=1)
        return jntList

    # 2获取骨骼列表的坐标列表
    def getObjListPivDir(self, inList):
        outPivDir = {}
        for i in inList:
            iPiv = mpy.xform(i, t=1, ws=1, q=1)
            outPivDir[i] = iPiv
        return outPivDir

    # ***吸附模型到指定模型
    def wrapMeshFun(self, TarMeshList, wapMesh):
        global wpOrigArray
        pcyFnMesh = self.getMfnMeshByName(wapMesh)
        pcyItMesh = self.getMItMeshVertexByName(wapMesh)

        unitl = OpenMaya.MScriptUtil()
        unitl.createFromInt(0)
        preInt = unitl.asIntPtr()

        normalArray = OpenMaya.MFloatVectorArray()
        pcyFnMesh.getNormals(normalArray, OpenMaya.MSpace.kTransform)

        vtxList = mpy.ls(wapMesh + '.vtx[*]', fl=1)
        pos1 = mpy.xform(vtxList[-1], q=1, ws=1, t=1)
        pos2 = mpy.xform(vtxList[-2], q=1, ws=1, t=1)
        point1 = OpenMaya.MPoint(pos1[0], pos1[1], pos1[2])
        point2 = OpenMaya.MPoint(pos2[0], pos2[1], pos2[2])
        normalVector = point1 - point2
        normalVector = normalVector.normal()
        rootPoint = mpy.xform(wapMesh, q=1, ws=1, t=1)
        rootPoint = OpenMaya.MPoint(rootPoint[0], rootPoint[1], rootPoint[2])

        pointArray = OpenMaya.MPointArray()
        pcyFnMesh.getPoints(pointArray, OpenMaya.MSpace.kWorld)

        localPointArray = OpenMaya.MPointArray()
        pcyFnMesh.getPoints(localPointArray)
        wpOrigArray = localPointArray

        averageLen = 0
        for i in range(localPointArray.length()):
            averageLen += localPointArray[i].y
        averageLen /= localPointArray.length()

        lenList = []
        for i in range(localPointArray.length()):
            lenList.append(localPointArray[i].y - averageLen)
            print localPointArray[i].y
        meshFnList = []
        for mesh in TarMeshList:
            meshFnFace = self.getMfnMeshByName(mesh)
            meshFnList.append(meshFnFace)

        try:
            for i in range(pcyItMesh.count()):

                pcyItMesh.setIndex(i, preInt)
                arrawPoint = rootPoint + normalVector * lenList[i]
                normal = arrawPoint - pointArray[i]
                # mpy.spaceLocator(p=[arrawPoint.x,arrawPoint.y,arrawPoint.z])
                normal = normal.normal()
                allPoints = OpenMaya.MPointArray()
                for meshfn in meshFnList:
                    points = OpenMaya.MPointArray()
                    ret = meshfn.intersect(pointArray[i], normal, points, 0.0001, OpenMaya.MSpace.kWorld)
                    if (ret):
                        for p in range(points.length()):
                            allPoints.append(points[p])
                if (allPoints.length() > 0):
                    minDis = None
                    midIdx = 0
                    for p in range(allPoints.length()):
                        dis = pointArray[i].distanceTo(allPoints[p])
                        if (minDis == None or minDis > dis):
                            minDis = dis
                            midIdx = p
                    retPoint = OpenMaya.MPoint(allPoints[midIdx].x, allPoints[midIdx].y, allPoints[midIdx].z)
                else:
                    retPoint = arrawPoint
                pcyItMesh.setPosition(retPoint, OpenMaya.MSpace.kWorld)

        finally:
            print ('Done')

    def getMItMeshVertexByName(self, name):
        sList = OpenMaya.MSelectionList()
        sList.add(name)
        dagPath = OpenMaya.MDagPath()
        sList.getDagPath(0, dagPath)
        mItMesh = OpenMaya.MItMeshVertex(dagPath)
        return mItMesh

    def getMfnMeshByName(self, name):
        sList = OpenMaya.MSelectionList()
        sList.add(name)
        dagPath = OpenMaya.MDagPath()
        sList.getDagPath(0, dagPath)
        meshPolygon = OpenMaya.MFnMesh(dagPath)
        return meshPolygon

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
            pos = mpy.xform(secLoc, q=1, ws=1, t=1)
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
            mpy.xform(secLoc, ws=1, t=[vtxPointList[retIdx].x, vtxPointList[retIdx].y, vtxPointList[retIdx].z])

    @staticmethod
    def create_curve_cnt(ctrl_name, typ, r):
        if (typ == 'Sphere'):
            ctrl_name = mpy.curve(n=ctrl_name, d=1,
                                  p=[(0.504214, 0, 0), (0.491572, 0.112198, 0), (0.454281, 0.21877, 0),
                                     (0.394211, 0.314372, 0), (0.314372, 0.394211, 0),
                                     (0.21877, 0.454281, 0), (0.112198, 0.491572, 0), (0, 0.504214, 0),
                                     (-0.112198, 0.491572, 0), (-0.21877, 0.454281, 0),
                                     (-0.314372, 0.394211, 0), (-0.394211, 0.314372, 0),
                                     (-0.454281, 0.21877, 0), (-0.491572, 0.112198, 0), (-0.504214, 0, 0),
                                     (-0.491572, -0.112198, 0), (-0.454281, -0.21877, 0),
                                     (-0.394211, -0.314372, 0), (-0.314372, -0.394211, 0),
                                     (-0.21877, -0.454281, 0), (-0.112198, -0.491572, 0), (0, -0.504214, 0),
                                     (0.112198, -0.491572, 0), (0.21877, -0.454281, 0),
                                     (0.314372, -0.394211, 0), (0.394211, -0.314372, 0),
                                     (0.454281, -0.21877, 0), (0.491572, -0.112198, 0), (0.504214, 0, 0),
                                     (0.491572, 0, -0.112198), (0.454281, 0, -0.21877),
                                     (0.394211, 0, -0.314372), (0.314372, 0, -0.394211),
                                     (0.21877, 0, -0.454281), (0.112198, 0, -0.491572), (0, 0, -0.504214),
                                     (-0.112198, 0, -0.491572), (-0.21877, 0, -0.454281),
                                     (-0.314372, 0, -0.394211), (-0.394211, 0, -0.314372),
                                     (-0.454281, 0, -0.21877), (-0.491572, 0, -0.112198), (-0.504214, 0, 0),
                                     (-0.491572, 0, 0.112198), (-0.454281, 0, 0.21877),
                                     (-0.394211, 0, 0.314372), (-0.314372, 0, 0.394211),
                                     (-0.21877, 0, 0.454281), (-0.112198, 0, 0.491572), (0, 0, 0.504214),
                                     (0, 0.112198, 0.491572), (0, 0.21877, 0.454281),
                                     (0, 0.314372, 0.394211), (0, 0.394211, 0.314372),
                                     (0, 0.454281, 0.21877), (0, 0.491572, 0.112198), (0, 0.504214, 0),
                                     (0, 0.491572, -0.112198), (0, 0.454281, -0.21877),
                                     (0, 0.394211, -0.314372), (0, 0.314372, -0.394211),
                                     (0, 0.21877, -0.454281), (0, 0.112198, -0.491572), (0, 0, -0.504214),
                                     (0, -0.112198, -0.491572), (0, -0.21877, -0.454281),
                                     (0, -0.314372, -0.394211), (0, -0.394211, -0.314372),
                                     (0, -0.454281, -0.21877), (0, -0.491572, -0.112198), (0, -0.504214, 0),
                                     (0, -0.491572, 0.112198), (0, -0.454281, 0.21877),
                                     (0, -0.394211, 0.314372), (0, -0.314372, 0.394211),
                                     (0, -0.21877, 0.454281), (0, -0.112198, 0.491572), (0, 0, 0.504214),
                                     (0.112198, 0, 0.491572), (0.21877, 0, 0.454281),
                                     (0.314372, 0, 0.394211), (0.394211, 0, 0.314372),
                                     (0.454281, 0, 0.21877), (0.491572, 0, 0.112198), (0.504214, 0, 0)])
        if (typ == 'Triangle'):
            cName = mpy.curve(d=1, n=ctrl_name, p=[[0, 0, 0.25], [0, 0.05, 0.1], [0, -0.05, 0.1], [0, 0, 0.25]])
        if (typ == 'Cube'):
            cName = mpy.curve(d=1, n=cName, p=[[0.1, 0.1, -0.1], [-0.1, 0.1, -0.1], [-0.1, 0.1, 0.1], [0.1, 0.1, 0.1],
                                               [0.1, 0.1, -0.1], [0.1, -0.1, -0.1], [0.1, -0.1, 0.1], [0.1, 0.1, 0.1],
                                               [-0.1, 0.1, 0.1], [-0.1, -0.1, 0.1], [0.1, -0.1, 0.1],
                                               [0.1, -0.1, -0.1], [-0.1, -0.1, -0.1], [-0.1, -0.1, 0.1],
                                               [-0.1, 0.1, 0.1], [-0.1, 0.1, -0.1], [-0.1, -0.1, -0.1]])
            mpy.scale(r, r, r, mpy.ls(cName + '.cv[*]'), r=1, ocp=1)
        return cName

    @staticmethod
    def try_parent(obj_a, obj_b):
        obj_p = mpy.listRelatives(obj_b, p=1)
        if (obj_p != None and obj_p[0] != obj_b):
            mpy.parent(obj_a, obj_b)


if __name__ == '__main__':
    print "get"
