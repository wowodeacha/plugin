##

from maya import cmds
import maya.mel as mm
import maya.OpenMayaAnim as OpenMayaAnim
import maya.OpenMaya as OpenMaya

def sdd_blendShapeTools():
    if(cmds.window('sdd_BlendShapeToolsWin',q=1,ex=1)):
        cmds.deleteUI('sdd_BlendShapeToolsWin',window=1)
    cmds.window('sdd_BlendShapeToolsWin',rtf=1,menuBar=1,s=1,t='sdd_BlendShapeToolsWin')
    cmds.columnLayout('mbsMainCL',adj=1,w=243)
    cmds.button(l='Load Base Mesh',c='sdd_loadBaseMesh()')
    cmds.text(l='',h=3)
    cmds.textField('mbsBaseMesh',tx='',ed=0)
    cmds.popupMenu()
    cmds.radioMenuItemCollection()
    cmds.menuItem('mbsRemeberMI',l='Remember',c='sdd_rememberBaseName()')
    cmds.menuItem('mbsResetMI',l='',c='sdd_resetBaseName()')
    cmds.text(l='',h=5)
    cmds.separator(p='mbsMainCL')
    cmds.text(p='mbsMainCL',l='',h=3)

    cmds.radioCollection(p='mbsMainCL')
    cmds.rowLayout(nc=3,cw3=[60,60,60])
    cmds.radioButton('mbsMirX',l='X',sl=1)
    cmds.radioButton('mbsMirY',l='Y')
    cmds.radioButton('mbsMirZ',l='Z')

    cmds.text(p='mbsMainCL',l='',h=3)
    cmds.separator(p='mbsMainCL')
    cmds.text(p='mbsMainCL',l='',h=3)

    cmds.rowLayout(p='mbsMainCL',nc=3,cw2=[35,120])
    cmds.text(l='MinDis:')
    cmds.floatField('mbsMindisFF',v=0.0001,pre=4,w=120)

    cmds.separator(p='mbsMainCL')
    cmds.text(p='mbsMainCL',l='',h=5)
    cmds.progressBar('mbsMainPB',p='mbsMainCL',max=1,pr=0,h=15,vis=0)
    cmds.text(p='mbsMainCL',l='',h=5)
    cmds.button(p='mbsMainCL',l='Revert To Base',c='sdd_revertVtxToBase()')
    cmds.text(p='mbsMainCL',l='',h=5)
    cmds.button(p='mbsMainCL',l='Mirror',c='sdd_mirrorOrFilpBS("")')
    cmds.text(p='mbsMainCL',l='',h=5)
    cmds.button(p='mbsMainCL',l='Flip',c='sdd_mirrorOrFilpBS("Flip")')
    cmds.text(p='mbsMainCL',l='',h=5)

    cmds.separator(p='mbsMainCL')

    cmds.text(p='mbsMainCL',l='',h=8)
    cmds.rowLayout('mbsSubBtnRL',p='mbsMainCL',nc=10,cw3=[120,10,120])
    cmds.button(p='mbsSubBtnRL',l='Load Final Mesh',c='sdd_loadfinalMesh()',w=115)
    cmds.text(p='mbsSubBtnRL',l='',h=8)
    cmds.button(p='mbsSubBtnRL',l='Load Sub Mesh',c='sdd_loadSubMesh()',w=115)

    cmds.rowLayout('mbsSubTXRL',p='mbsMainCL',nc=10,cw3=[120,10,120])
    cmds.textField('mbsfinalMesh',p='mbsSubTXRL',tx='',ed=0,w=115)
    cmds.text(p='mbsSubTXRL',l='-',h=8)
    cmds.textField('mbsSubMesh',p='mbsSubTXRL',tx='',ed=0,w=115)

    cmds.button(p='mbsMainCL',l='Subtraction',c='sdd_SubBlenshape()')
    cmds.text(p='mbsMainCL',l='',h=3)
    cmds.showWindow('sdd_BlendShapeToolsWin')

def sdd_loadSubMesh():
    cmds.textField('mbsSubMesh',e=1,tx='')
    sel=sdd_returnSelectMesh()
    if(sel!=None or len(sel)<1):
        cmds.textField('mbsSubMesh',e=1,tx=sel[0])

def sdd_loadfinalMesh():
    cmds.textField('mbsfinalMesh',e=1,tx='')
    sel=sdd_returnSelectMesh()
    if(sel!=None or len(sel)<1):
        cmds.textField('mbsfinalMesh',e=1,tx=sel[0])

def sdd_rememberBaseName():
    baseName=cmds.textField('mbsBaseMesh',q=1,tx=1)
    cmds.menuItem('mbsResetMI',e=1,l=baseName)
def sdd_resetBaseName():
    baseName=cmds.menuItem('mbsResetMI',q=1,l=1)
    cmds.textField('mbsBaseMesh',e=1,tx=baseName)

def sdd_loadBaseMesh():
    cmds.textField('mbsBaseMesh',e=1,tx='')
    sel=sdd_returnSelectMesh()
    if(sel!=None or len(sel)<1):
        cmds.textField('mbsBaseMesh',e=1,tx=sel[0])

def sdd_returnSelectMesh():
    sel=cmds.ls(sl=1)
    if(len(sel)==0):
        return
    meshVtx=cmds.filterExpand(sel,sm=[31])
    if(meshVtx!=None):
        return meshVtx
    selS=cmds.listRelatives(sel[0],s=1,f=1)
    if(selS==None):
        return
    if(cmds.objectType(selS[0])!='mesh'):
        return
    return sel[0:]


def sdd_getNodeDagPath(name):
    nodeDagPath = OpenMaya.MObject()
    selectionList = OpenMaya.MSelectionList()
    selectionList.add(name)
    nodeDagPath = OpenMaya.MDagPath()
    selectionList.getDagPath(0, nodeDagPath)
    mesh = OpenMaya.MFnMesh(nodeDagPath)
    return mesh

def sdd_mirrorOrFilpBS(typ):
    mirX,mirY,mirZ=1,1,1
    if(cmds.radioButton('mbsMirX',q=1,sl=1)):
        mirX=-1
    if(cmds.radioButton('mbsMirY',q=1,sl=1)):
        mirY=-1
    if(cmds.radioButton('mbsMirZ',q=1,sl=1)):
        mirZ=-1
    mindis=cmds.floatField('mbsMindisFF',q=1,v=1)

    baseName=cmds.textField('mbsBaseMesh',q=1,tx=1)
    if(baseName==''):
    	return
    baseMesh=sdd_getNodeDagPath(baseName)

    sel=sdd_returnSelectMesh()
    if(sel==None):
        return

    selObj=sel[0]
    if(len(sel)>1):
        selObj=sel[0].split('.')[0]
    else:
        sel=cmds.ls(selObj+'.vtx[*]',fl=1)

    selMesh=sdd_getNodeDagPath(selObj)

    basePList=OpenMaya.MPointArray()
    selPList=OpenMaya.MPointArray()
    clostP=OpenMaya.MPoint()
    mirP=OpenMaya.MPoint()
    space = OpenMaya.MSpace.kObject
    util = OpenMaya.MScriptUtil()
    util.createFromInt(0)
    idPointer = util.asIntPtr()

    baseMesh.getPoints(basePList)
    selMesh.getPoints(selPList)
    if(basePList.length()!=selPList.length()):
        cmds.confirmDialog(t='Error',m='Don\'t Match ',b='OK')
        return

    #get cmds.move index list
    movIdxList=[]
    mirIdxList=[]
    try:
        cmds.progressBar('mbsMainPB',e=1,vis=1,max=len(sel))
        sdd_resetMBSWindow('+')
        for i in range(len(sel)):
            vtxIdx=int(sel[i].split('[')[1][:-1])
            cmds.progressBar('mbsMainPB',e=1,pr=i)
            baseP=basePList[vtxIdx]
            selP=selPList[vtxIdx]
            if(baseP.distanceTo(selP)<mindis):
                continue
            movIdxList.append(vtxIdx)

            #get mirror index list
            mirP.x=basePList[vtxIdx][0]*mirX
            mirP.y=basePList[vtxIdx][1]*mirY
            mirP.z=basePList[vtxIdx][2]*mirZ
            
            baseMesh.getClosestPoint(mirP,clostP,space,idPointer)
            idx = OpenMaya.MScriptUtil(idPointer).asInt()
            nearestList=OpenMaya.MIntArray()
            baseMesh.getPolygonVertices(idx,nearestList)
            tmpdis=None
            retIdx=None
            for d in nearestList:
                dis=basePList[d].distanceTo(mirP)
                if(tmpdis==None or dis<tmpdis):
                    tmpdis=dis
                    retIdx=d

            if(mindis*100>=tmpdis):
                mirIdxList.append(retIdx)
            else:
                mirIdxList.append(None)
    finally:
        cmds.progressBar('mbsMainPB',e=1,pr=0,vis=0)
        sdd_resetMBSWindow('-')

    if(len(movIdxList)==0):
        return

    #move vertex
    if(typ=='Flip'):
        sdd_revertVtxToBase()

    try:
        cmds.progressBar('mbsMainPB',e=1,vis=1,max=len(mirIdxList))
        sdd_resetMBSWindow('+')
        for i in range(len(mirIdxList)):
            cmds.progressBar('mbsMainPB',e=1,pr=i)
            if(mirIdxList[i]==None):
                continue
            movIdx=movIdxList[i]
            mirIdx=mirIdxList[i]
            mirPos=selPList[movIdx]
            movP=[mirPos.x*mirX,mirPos.y*mirY,mirPos.z*mirZ]
            cmds.xform(selObj+'.vtx[%d]'%mirIdx,os=1,t=movP)
    finally:
        cmds.progressBar('mbsMainPB',e=1,vis=0,pr=0)
        sdd_resetMBSWindow('-')


def sdd_resetMBSWindow(typ):
    h=cmds.window('sdd_BlendShapeToolsWin',q=1,h=1)
    if(typ=='+'):
        cmds.window('sdd_BlendShapeToolsWin',e=1,h=h+15)
    else:
        cmds.window('sdd_BlendShapeToolsWin',e=1,h=h-15)


    #dd=sdd_getMirrorPointIdxList(ls(sl=1)[0])
def sdd_revertVtxToBase():
    mindis=cmds.floatField('mbsMindisFF',q=1,v=1)

    sel=sdd_returnSelectMesh()
    if(sel==None):
        return

    vtx=cmds.filterExpand(sel,sm=[31])
    baseName=cmds.textField('mbsBaseMesh',q=1,tx=1)
    if(vtx==None and len(sel)==2):
        baseName=sel[0]
        selObj=sel[1]
        sel=cmds.ls(selObj+'.vtx[*]',fl=1)
    else:
        selObj=sel[0]
        if(len(sel)>1):
            selObj=sel[0].split('.')[0]
        else:
            sel=cmds.ls(selObj+'.vtx[*]',fl=1)

    baseMesh=sdd_getNodeDagPath(baseName)

    selMesh=sdd_getNodeDagPath(selObj)

    basePList=OpenMaya.MPointArray()
    selPList=OpenMaya.MPointArray()

    baseMesh.getPoints(basePList)
    selMesh.getPoints(selPList)
    if(basePList.length()!=selPList.length()):
        cmds.confirmDialog(t='Error',m='Don\'t Match ',b='OK')
        return
    try:
        cmds.progressBar('mbsMainPB',e=1,vis=1,max=len(sel))
        sdd_resetMBSWindow('+')
        for i in range(len(sel)):
            vtxIdx=int(sel[i].split('[')[1][:-1])  
            cmds.progressBar('mbsMainPB',e=1,pr=i)
            baseP=basePList[vtxIdx]
            selP=selPList[vtxIdx]
            if(baseP.distanceTo(selP)>mindis):
                movP=[baseP.x,baseP.y,baseP.z]
                cmds.xform(selObj+'.vtx[%d]'%vtxIdx,os=1,t=movP)
    finally:
        cmds.progressBar('mbsMainPB',e=1,vis=0,pr=0)
        sdd_resetMBSWindow('-')


#Init SkinCluster Info
def sdd_SubBlenshape():
    #getSkinClusterInfo
    basMeshName=cmds.textField('mbsBaseMesh',q=1,tx=1)
    finalMeshName=cmds.textField('mbsfinalMesh',q=1,tx=1)
    subMeshName=cmds.textField('mbsSubMesh',q=1,tx=1)
    if(basMeshName=='' or finalMeshName=='' or subMeshName==''):
        mm.eval('warning "please load base mesh and Target mesh"')
        return
    
    vtxNum=cmds.polyEvaluate(basMeshName,v=1)
    if(vtxNum!=cmds.polyEvaluate(finalMeshName,v=1) and vtxNum!=cmds.polyEvaluate(subMeshName,v=1) ):
        mm.eval('warning "not match!"')
        return

    #get Move Vertex List
    
    finalMeshArray=sdd_getMeshVertexInfo(finalMeshName,OpenMaya.MSpace.kObject)
    selMeshArray=sdd_getMeshVertexInfo(subMeshName,OpenMaya.MSpace.kObject)
    basMeshArray=sdd_getMeshVertexInfo(basMeshName,OpenMaya.MSpace.kObject)

    resMeshName=cmds.duplicate(subMeshName)[0]
    attr=['tx','ty','tz','rx','ry','rz','sx','sy','sz']
    sdd_mbsUnlockAttrList(resMeshName,attr)
    cmds.select(resMeshName)

    outPointArray=OpenMaya.MPointArray()
    for i in range(basMeshArray.length()):
        finalPoint=basMeshArray[i]+(finalMeshArray[i]-selMeshArray[i])

        outPointArray.append(finalPoint)
    dagPath=sdd_returnMDagPath(resMeshName)
    meshPolygon = OpenMaya.MFnMesh(dagPath)
    meshPolygon.setPoints(outPointArray,OpenMaya.MSpace.kObject)


def sdd_mbsUnlockAttrList(obj,attr):
    try:
        for i in attr:
            cmds.setAttr(obj+'.'+i,l=0)
    except:
        pass

def sdd_getMeshVertexInfo(obj,space):
    dagPath=sdd_returnMDagPath(obj)
    meshPolygon = OpenMaya.MFnMesh(dagPath)
    tmpPointArray = OpenMaya.MPointArray()
    meshPolygon.getPoints(tmpPointArray,space)
    return tmpPointArray


def sdd_getBaseMeshVertexInfo(objName,space):
    skinNode=mm.eval('findRelatedSkinCluster("%s")'%objName)
    if(skinNode==''):
        tmpPointArray=sdd_getMeshVertexInfo(objName,space)
        return skinNode,None,tmpPointArray
    mObj=sdd_returnMObject(skinNode)
    mFnSkinCluster=OpenMayaAnim.MFnSkinCluster(mObj)
    inpuObjArray=OpenMaya.MObjectArray()
    mFnSkinCluster.getInputGeometry(inpuObjArray)
    if(inpuObjArray.length()>0):
        meshPolygon=OpenMaya.MFnMesh(inpuObjArray[0])
        tmpPointArray = OpenMaya.MPointArray()
        meshPolygon.getPoints(tmpPointArray,space)
    return skinNode,mFnSkinCluster,tmpPointArray

def sdd_createMatrixFromList(mList):
    matrix=OpenMaya.MMatrix()
    OpenMaya.MScriptUtil.createMatrixFromList(mList,matrix)
    return matrix

def returnListByMMatrix(inputMatrix):
    returnList = []
    for row in range(0,4):
        for col in range(0,4):
            matrixValue = 0.0
            matrixValue = OpenMaya.MScriptUtil.getDoubleArrayItem(inputMatrix[row] , col)
            returnList.append( matrixValue )
    return returnList


def sdd_getSkinClusterDIF(helpList,outList):
    global jointNum,skinNode
    matList=[]
    for i in range(jointNum):
        tmp=cmds.getAttr(skinNode+'.matrix[%s]'%i)
        matList.append(sdd_createMatrixFromList(tmp))

    x1=sdd_getPosBeforSkinDeform(matList,helpList)
    x2=sdd_getPosBeforSkinDeform(matList,outList)
    retList=[]
    for i in range(len(x1)):
        p1=x1[i][1]
        p2=x2[i][1]
        tmp=[p1[0]-p2[0],p1[1]-p2[1],p1[2]-p2[2]]
        retList.append([x1[i][0],tmp])
    return retList

def sdd_getPosBeforSkinDeform(matList,idxList):
    retList=[]
    for j in idxList:
        vtxId=j[0]
        vtxPos=j[1]
        oldMatrix=sdd_createMatrixFromList([1,0,0,0 ,0,1,0,0 ,0,0,1,0 ,vtxPos[0],vtxPos[1],vtxPos[2],1])
        unitMatrix=sdd_returnUnitMatrix(matList,vtxId)
        resultMatrix=oldMatrix*unitMatrix.inverse()
        tmp=returnListByMMatrix(resultMatrix)
        retList.append([vtxId,[tmp[12],tmp[13],tmp[14]]])
    return retList



#GetDagPath
def sdd_returnMObject(name):
    sList = OpenMaya.MSelectionList()
    sList.add(name)
    obj = OpenMaya.MObject()
    sList.getDependNode(0, obj)
    return obj

def sdd_returnMDagPath(name):
    sList = OpenMaya.MSelectionList()
    sList.add(name)
    dagPath = OpenMaya.MDagPath()
    sList.getDagPath(0, dagPath)
    return dagPath
if __name__ == '__main__':
    sdd_blendShapeTools()
