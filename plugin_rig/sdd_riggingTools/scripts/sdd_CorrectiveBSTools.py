##

from maya import cmds
import maya.mel as mm
import maya.OpenMayaAnim as OpenMayaAnim
import maya.OpenMaya as OpenMaya

def sdd_CorrectiveBSTools():
    if(cmds.window('sdd_CorrectiveBSToolsWin',q=1,ex=1)):
        cmds.deleteUI('sdd_CorrectiveBSToolsWin',window=1)
    cmds.window('sdd_CorrectiveBSToolsWin',rtf=1,menuBar=1,s=1,t='sdd_CorrectiveBSToolsWin')
    cmds.columnLayout('cbsMainCL',adj=1,w=250)
    cmds.button(l='Load Skin Mesh',h=35,c='sdd_loadCbsSkinMesh()')
    cmds.text(l='',h=3)
    cmds.textField('cbsSkinMesh',tx='',ed=0)
    cmds.text(l='',h=5)
    cmds.separator(p='cbsMainCL')
    cmds.text(p='cbsMainCL',l='',h=3)

    cmds.radioCollection(p='cbsMainCL')
    cmds.rowLayout(nc=3,cw3=[100,70,70])
    cmds.text(l='Calc BlendShape:')
    cmds.radioButton('cbsCalcTypeAddRB',l='Addition',sl=1)
    cmds.radioButton('cbsCalcTypeOveRB',l='Absolute')

    cmds.separator(p='cbsMainCL')
    cmds.text(p='cbsMainCL',l='',h=8)
    cmds.textField('cbsfinalMesh',p='cbsMainCL',tx='',ed=0)
    cmds.text(p='cbsMainCL',l='',h=8)
    cmds.button('cbsCorrectB',p='cbsMainCL',l='Corrective BlendShape',h=35,c='sdd_CorrectiveBlendShapeBProc()',bgc=[0,1,0])
    cmds.text(p='cbsMainCL',l='',h=3)
    cmds.showWindow('sdd_CorrectiveBSToolsWin')

def sdd_CorrectiveBlendShapeBProc():
    if(cmds.button('cbsCorrectB',q=1,l=1)=='Corrective BlendShape'):
        cmds.button('cbsCorrectB',e=1,l='Complete',bgc=[1,0,0])
        skinMesh=cmds.textField('cbsSkinMesh',q=1,tx=1)
        resMeshName=cmds.duplicate(skinMesh,n=skinMesh+'_Final')[0]
        cmds.select(resMeshName)
        cmds.textField('cbsfinalMesh',e=1,tx=resMeshName)
        try:
            attr=['tx','ty','tz','rx','ry','rz','sx','sy','sz']
            for i in attr:
                cmds.setAttr(resMeshName+'.'+i,l=0)
            cmds.setAttr(skinMesh+'.v',0)
        except:
            pass
    else:
        cmds.button('cbsCorrectB',e=1,l='Corrective BlendShape',bgc=[0,1,0])
        skinMesh=cmds.textField('cbsSkinMesh',q=1,tx=1)
        resMeshName=cmds.textField('cbsfinalMesh',q=1,tx=1)
        skinNodeName=mm.eval('findRelatedSkinCluster("%s")'%skinMesh)
        isAdd=cmds.radioButton('cbsCalcTypeAddRB',q=1,sl=1)
        sdd_inverseCaclBlendShape(resMeshName,skinMesh,resMeshName,skinNodeName,isAdd)
        cmds.select(resMeshName)
        try:
            cmds.setAttr(skinMesh+'.v',1)
        except:
            pass


def sdd_loadCbsSkinMesh():
    sel=cmds.ls(sl=1)
    if(len(sel)==0):
        return
    selS=cmds.listRelatives(sel[0],s=1,f=1)
    if(selS==None):
        return
    if(cmds.objectType(selS[0])!='mesh'):
        return
    skinNode=mm.eval('findRelatedSkinCluster("%s")'%sel[0])
    if(skinNode==''):
        mm.eval('warning "%s ,no skin!"'%sel[0])
        return
    cmds.textField('cbsSkinMesh',e=1,tx=sel[0])


def sdd_inverseCaclBlendShape(outMeshName,skinMeshName,finalMeshName,skinNodeName,calcType):
    skinItMesh=sdd_getMItMeshVertexByName(skinMeshName)
    skinDagPath=sdd_getMDagPathByName(skinMeshName)
    finalItMesh=sdd_getMItMeshVertexByName(finalMeshName)
    mfnskin,origItMesh=sdd_getMfnSkinclusterByName(skinNodeName)

    preBindPlug=mfnskin.findPlug('bindPreMatrix')
    worldMatrixPlug=mfnskin.findPlug('matrix')

    exIdx=OpenMaya.MIntArray()
    worldMatrixPlug.getExistingArrayAttributeIndices(exIdx)
    mulMatrixList=[]
    for i in exIdx:
        curPBPlug=preBindPlug.elementByLogicalIndex(i)
        curWDPlug=worldMatrixPlug.elementByLogicalIndex(i)
        if curWDPlug.isConnected() :
            preBindMatrix=OpenMaya.MMatrix(OpenMaya.MFnMatrixData(curPBPlug.asMObject()).matrix())
            worldMatrix=OpenMaya.MMatrix(OpenMaya.MFnMatrixData(curWDPlug.asMObject()).matrix())
            mulMatrixList.append(preBindMatrix*worldMatrix)

    unitl=OpenMaya.MScriptUtil()
    unitl.createFromInt(0)
    countPtr=unitl.asUintPtr()
    outPointArray=OpenMaya.MPointArray()

    # origItMesh.reset()
    for i in range(skinItMesh.count()):
        #after matrix
        finalPoint=finalItMesh.position(OpenMaya.MSpace.kObject)
        skinPoint=skinItMesh.position(OpenMaya.MSpace.kObject)
        origPoint=origItMesh.position(OpenMaya.MSpace.kObject)
        outPoint=origPoint
        if(finalPoint!=skinPoint or calcType==False):
            afterMatrix=sdd_convertPointToMatrix(finalPoint)
            skinMatrix=sdd_convertPointToMatrix(skinPoint)
            #weight
            wt=OpenMaya.MFloatArray()
            mfnskin.getWeights(skinDagPath,skinItMesh.currentItem(),wt,countPtr)
            #unit matrix
            unitMatrix=sdd_createZeroMatrix()
            for a in range(len(mulMatrixList)):
                if(wt[a]!=0):
                    unitMatrix+=mulMatrixList[a]*wt[a]
            #inverse cacl
            inverseMatrix=unitMatrix.inverse()
            finalbeforeMatrix=afterMatrix*inverseMatrix
            skinBeforeMatrix=skinMatrix*inverseMatrix
            finalBeforePoint=sdd_convertMatrixToPoint(finalbeforeMatrix)
            skinBeforePoint=sdd_convertMatrixToPoint(skinBeforeMatrix)

            if(calcType):
                if(finalBeforePoint!=finalPoint):
                    outPoint=origPoint+(finalBeforePoint-skinBeforePoint)
            else:
                outPoint=finalBeforePoint
            
        outPointArray.append(outPoint)

        finalItMesh.next()
        skinItMesh.next()
        origItMesh.next()

    meshPolygon=sdd_getMfnMeshByName(outMeshName)
    meshPolygon.setPoints(outPointArray,OpenMaya.MSpace.kObject)

def sdd_convertMatrixToPoint(mMatrix):
    x=OpenMaya.MScriptUtil.getDoubleArrayItem(mMatrix[3],0)
    y=OpenMaya.MScriptUtil.getDoubleArrayItem(mMatrix[3],1)
    z=OpenMaya.MScriptUtil.getDoubleArrayItem(mMatrix[3],2)
    newPoint=OpenMaya.MPoint(x,y,z)
    return newPoint

def sdd_convertPointToMatrix(mpoint):
    mMatrix=OpenMaya.MMatrix()
    tmpList=[1,0,0,0 ,0,1,0,0 ,0,0,1,0 ,mpoint.x,mpoint.y,mpoint.z,1]
    OpenMaya.MScriptUtil.createMatrixFromList(tmpList,mMatrix)
    return mMatrix

def sdd_createZeroMatrix():
    mMatrix=OpenMaya.MMatrix()
    tmpList=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    OpenMaya.MScriptUtil.createMatrixFromList(tmpList,mMatrix)
    return mMatrix


def sdd_getMDagPathByName(name):
    sList = OpenMaya.MSelectionList()
    sList.add(name)
    dagPath = OpenMaya.MDagPath()
    sList.getDagPath(0, dagPath)
    return dagPath

def sdd_getMfnMeshByName(name):
    sList = OpenMaya.MSelectionList()
    sList.add(name)
    dagPath = OpenMaya.MDagPath()
    sList.getDagPath(0, dagPath)
    meshPolygon = OpenMaya.MFnMesh(dagPath)
    return meshPolygon

def sdd_getMItMeshVertexByName(name):
    sList = OpenMaya.MSelectionList()
    sList.add(name)
    dagPath = OpenMaya.MDagPath()
    sList.getDagPath(0, dagPath)
    mItMesh = OpenMaya.MItMeshVertex(dagPath)
    return mItMesh

def sdd_getMfnSkinclusterByName(name):
    sList = OpenMaya.MSelectionList()
    sList.add(name)
    mObj = OpenMaya.MObject()
    sList.getDependNode(0, mObj)
    mFnSkinCluster=OpenMayaAnim.MFnSkinCluster(mObj)
    inpuObjArray=OpenMaya.MObjectArray()
    mFnSkinCluster.getInputGeometry(inpuObjArray)
    meshItPolygon=OpenMaya.MItMeshVertex(inpuObjArray[0])
    return mFnSkinCluster,meshItPolygon


if __name__ == '__main__':
    sdd_CorrectiveBSTools()
