from maya import cmds
import maya.mel as mm
import maya.OpenMayaAnim as OpenMayaAnim
import maya.OpenMaya as OpenMaya
import math
import _winreg as _reg
import random
import time
import sys
import os
import yj_add as yj_add

reload(yj_add)
NewCtrlModule = yj_add.NewCtrlModule()


def sdd_FaceRigging(rootPath):
    # if(sdd_checkRegister()==False):
    #     return
    curTime = time.time()
    endTime = time.mktime(time.strptime('2016-12-30', '%Y-%m-%d'))
    if (curTime > endTime):
        cmds.confirmDialog(t='Timeout', m='Please contact sundongdong.\r\nEmail:136941679@qq.com', b=['OK'])
        return

    global frRootPath
    global ctrBsPuffDate
    ctrBsPuffDate = None
    frRootPath = rootPath
    FR, FRJntPos, FRUIPos = sdd_frTNameDirc()
    T = sdd_returnTempNameDirc()
    _skin = T['_skin']

    if (cmds.window('sdd_YJ_FaceRiggingWin', q=1, ex=1)): cmds.deleteUI('sdd_YJ_FaceRiggingWin')
    cmds.window('sdd_YJ_FaceRiggingWin', ret=1, s=0)
    cmds.columnLayout('frMainCL')

    cmds.tabLayout('frMainRigTL', p='frMainCL', sc='sdd_tabLayoutSelectChange()')

    # joint
    cmds.formLayout('frIconBtnFL', p='frMainRigTL', w=450, h=450)
    cmds.image('frIconBgI', i=frRootPath + 'icons/FaceRigBackground.png', w=450, h=450)
    for i in FR.keys():
        item = FR[i]
        pos = FRUIPos[i]
        if (pos != None):
            cmds.iconTextButton(item, c='if(cmds.objExists("%s")):cmds.select("%s")' % (item + _skin, item + _skin),
                                st='textOnly', bgc=[0, 0.8, 0], w=12, h=12, p='frIconBtnFL')
            cmds.formLayout('frIconBtnFL', e=1, ap=[[item, 'left', 0, pos[0]], [item, 'top', 0, pos[1]]])

    cmds.button('frMirrorRToLB', p='frIconBtnFL', l='R << L', w=50, h=25, c='sdd_mirrorJntPos("L>>R")')
    cmds.button('frMirrorLToRB', p='frIconBtnFL', l='R >> L', w=50, h=25, c='sdd_mirrorJntPos("R>>L")')
    cmds.button('frImportBaseB', p='frIconBtnFL', l='Import Base', w=80, h=25, c='sdd_importBaseJnt()')

    cmds.checkBoxGrp('frMirrorOptionToCBG', cw3=[80, 70, 70], ncb=2, l='Mirror Options:', la2=['Transform', 'Rotate'],
                     va2=[1, 1])

    # cmds.formLayout('frIconBtnFL',e=1,ap=[['frIconBgI','left',0,0],['frIconBgI','top',0,0],['frIconBgI','bottom',0,0],['frIconBgI','right',0,0]])
    cmds.formLayout('frIconBtnFL', e=1,
                    ap=[['frMirrorOptionToCBG', 'left', 0, 25], ['frMirrorOptionToCBG', 'top', 0, 95]])

    cmds.formLayout('frIconBtnFL', e=1, ap=[['frMirrorLToRB', 'left', 0, 89], ['frMirrorLToRB', 'top', 0, 90]])
    cmds.formLayout('frIconBtnFL', e=1, ap=[['frMirrorRToLB', 'left', 0, 0], ['frMirrorRToLB', 'top', 0, 90]])
    cmds.formLayout('frIconBtnFL', e=1, ap=[['frImportBaseB', 'left', 0, 0], ['frImportBaseB', 'top', 0, 0]])

    # mesh
    cmds.columnLayout('frRiggingCL', p='frMainRigTL', adj=1)

    cmds.frameLayout('frRiggingFL', p='frRiggingCL', w=290, l="Mesh List", collapsable=1, cl=0)
    cmds.columnLayout('frMeshRiggingCL', adj=1)
    # cmds.floatSliderGrp('frMirDisFSG',l='Mirror Distance:',f=1,w=305,pre=4,v=0.01,min=0,max=1,cw3=[80,50,80],cal=[1,'left'])
    cmds.button('frLoadAllMeshB', l='Load', w=220, c='sdd_loadFaceAllMesh()')
    cmds.textScrollList('frFaceMeshTSL', h=100, w=440, ams=1, sc='sdd_faceMeshSelectChange()')
    cmds.button('frSetFaceMeshB', l='Set Face Mesh', c='sdd_setFaceMesh()', en=0)
    cmds.textField('frFaceMeshTF', ed=0)
    cmds.button('frSdkRiggingB', l='Rigging', c='sdd_createSdkJointRigging()', en=0, h=35)
    cmds.rowLayout('frMoveJointRL', nc=3, cw3=[80, 278, 80], vis=0)
    cmds.button('frMoveMirrorLRoRB', w=80, l='R << L', c='sdd_mirrorJntPos("L>>R")', h=35)
    cmds.button('frMoveJointModeB', w=278, l='Finally', c='sdd_resetJointPosition()', h=35)
    cmds.button('frMoveMirrorRRoLB', w=80, l='R >> L', c='sdd_mirrorJntPos("R>>L")', h=35)

    cmds.frameLayout('frToolsFL', p='frRiggingCL', w=290, l="Tools", collapsable=1, cl=1, en=0)
    cmds.columnLayout('frToolsCL', adj=1, rs=5)
    cmds.rowLayout(p='frToolsCL', nc=4)
    cmds.iconTextButton(l='Create Joint', c='', w=219, h=35, st='textOnly', bgc=[0.35, 0.35, 0.35])
    cmds.iconTextButton(l='Fk Control', c='', w=219, h=35, st='textOnly', bgc=[0.35, 0.35, 0.35])

    cmds.separator(h=10, p='frToolsCL')
    cmds.rowLayout(nc=2, p='frToolsCL')
    cmds.intSliderGrp('frSikCntNumISG', l='Ctrl Number:', f=1, w=220, v=4, cw3=[60, 30, 80], cal=[1, 'left'])
    cmds.checkBoxGrp('frSikTwistCBG', l='Adv Twist:', cw2=[60, 30], v1=1, cal=[1, 'left'])

    cmds.rowLayout(p='frToolsCL', nc=4, cw4=[60, 160, 60, 155])
    cmds.text(w=60, al='left', l='Start Joint:')
    cmds.textField('frSikStartTF', w=155, ed=0)
    cmds.popupMenu(b=1)
    cmds.menuItem(l='Load', c='sdd_loadEyeBallMesh("frREyeMeshTF")')
    cmds.text(w=60, al='left', l='End Joint :')
    cmds.textField('frSikEndTF', w=155, ed=0)
    cmds.popupMenu(b=1)
    cmds.menuItem(l='Load', c='sdd_loadEyeBallMesh("frLEyeMeshTF")')
    cmds.iconTextButton(l='Spline IK', p='frToolsCL', h=35, st='textOnly', bgc=[0.35, 0.35, 0.35])

    # ==================================================================================
    # zzx .........................
    cmds.frameLayout("shapeFL", p="frRiggingCL", l=" Shape", collapsable=True, w=350, cl=True)
    # cmds.separator(p="shapeFL",style="none",h=3)
    cmds.separator(p="shapeFL", style="in", h=3)
    cmds.rowLayout("mirrorShapeRL00", p="shapeFL", nc=2, cw2=(50, 150))
    cmds.text(p='mirrorShapeRL00', l='')
    cmds.button(l="Zero Cnt", h=25, w=120, p='mirrorShapeRL00', bgc=(1.000, 1.000, 1.000), c="zzx_zeroCnt()")

    cmds.rowLayout("mirrorShapeRL", p="shapeFL", nc=3, cw3=(95, 50, 130))
    cmds.button(l="R  -- >  L", h=30, w=70, p='mirrorShapeRL', bgc=(1.000, 0.686, 0.686), c="zzx_mirrorCnt('RtoL')")
    cmds.button(l="", h=50, w=25, p='mirrorShapeRL', en=0)  # bgc=(1.000,1.000,0.000)
    cmds.button(l="R  < --  L", h=30, w=70, p='mirrorShapeRL', bgc=(0.388, 0.863, 1.000), c="zzx_mirrorCnt('LtoR')")

    cmds.rowLayout("mirrorShapeRL02", p="shapeFL", nc=4, cw4=(30, 50, 10, 130))
    cmds.text(p='mirrorShapeRL02', l='')
    cmds.button(l="Export", h=30, w=70, p='mirrorShapeRL02', bgc=(1.000, 0.000, 0.000),
                c="zzx_importExportCnt('export')")
    cmds.text(p='mirrorShapeRL02', l='')
    cmds.button(l="Import", h=30, w=70, p='mirrorShapeRL02', en=1, bgc=(0.000, 0.000, 1.000),
                c="zzx_importExportCnt('import')")

    cmds.separator(p="shapeFL", style="in", h=3)
    # zzx .........................
    # ==================================================================================
    # ==================================================================================
    # cmds.paneLayout('frFaceMashPL',cn='vertical4',p='frRiggingCL',w=440,h=180,ps=[[1,70,0],[2,10,0],[3,10,0],[4,10,0]])

    # cmds.columnLayout(p='frFaceMashPL',adj=1,w=20)
    # cmds.text(l='Mesh List:',al='left')
    # cmds.textScrollList('frMidVtxTSL',h=160,ams=1,sc='sdd_MiddleVtxIdxSelectChange(1)')

    # cmds.columnLayout(p='frFaceMashPL',adj=1,w=20)
    # cmds.text(l='Middle:',al='left')
    # cmds.textScrollList('frMidVtxTSL',h=160,ams=1,sc='sdd_MiddleVtxIdxSelectChange(1)')
    # cmds.popupMenu()

    # cmds.menuItem(l='Select All',c='sdd_MiddleVtxIdxSelectChange(2)')
    # cmds.columnLayout(p='frFaceMashPL',adj=1,w=20)
    # cmds.text(l='Mirror:',al='left')
    # cmds.textScrollList('frMirVtxTSL',h=160,ams=1,sc='sdd_MirrorVtxIdxSelectChange(1)')
    # cmds.popupMenu()

    # cmds.menuItem(l='Select All',c='sdd_MirrorVtxIdxSelectChange(2)')
    # cmds.columnLayout(p='frFaceMashPL',adj=1,w=20)
    # cmds.text(l='Error:',al='left')
    # cmds.textScrollList('frErrVtxTSL',h=160,ams=1,sc='sdd_ErrorVtxIdxSelectChange(1)')
    # cmds.popupMenu()
    # cmds.menuItem(l='Select All',c='sdd_ErrorVtxIdxSelectChange(2)')
    # ==================================================================================

    # sdk
    cmds.columnLayout('frSdkDefineAllCL', p='frMainRigTL', adj=1)

    cmds.columnLayout('frSdkDefineCL', p='frSdkDefineAllCL', adj=1)
    cmds.rowLayout(nc=13)
    cmds.text(l='Filter: ', w=35, al='right')
    cmds.checkBox('frSdkFilterLCB', v=1, w=40, l='L_*', cc='sdd_loadSdkAttrToList()')
    cmds.checkBox('frSdkFilterRCB', w=40, l='R_*', cc='sdd_loadSdkAttrToList()')
    cmds.text(l='Mirror Keys: ', w=80, al='right')
    cmds.checkBox('frSdkMirrorCB', v=1, l='')
    cmds.text(l='Key Value: ', w=80, al='right')
    cmds.iconTextRadioCollection()
    cmds.iconTextRadioButton('frSdkKeyV0IRB', l='0%', w=40, st='textOnly', cc='sdd_setAttrSdkValue()')
    cmds.iconTextRadioButton('frSdkKeyV5IRB', l='50%', w=40, st='textOnly', cc='sdd_setAttrSdkValue()')
    cmds.iconTextRadioButton('frSdkKeyV10IRB', l='100%', w=40, st='textOnly', sl=1, cc='sdd_setAttrSdkValue()')

    cmds.paneLayout('frSdkDefinePL', p='frSdkDefineCL', w=375, cn='vertical2', h=340)
    cmds.columnLayout(p='frSdkDefinePL', adj=1, w=20)
    cmds.text(l='SDK Attribute:', al='left')
    cmds.textScrollList('frSdkAttrTSL', h=300, ams=1, sc='sdd_sdkAttrListSelectChange()')
    cmds.popupMenu()
    cmds.menuItem(l='refresh', c='sdd_loadSdkAttrToList()')
    cmds.menuItem(l='Save SDK', c='sdd_saveSdkToFile()')
    cmds.menuItem(l='Load SDK', c='sdd_loadSdkFromFile()')

    cmds.button(l='New Attribute', c='sdd_newSdkAttr()')
    cmds.columnLayout(p='frSdkDefinePL', adj=1, w=20)
    cmds.text(l='Control List:', al='left')
    cmds.textScrollList('frSdkCntTSL', h=300, ams=1, sc='sdd_sdkCntListSelectChange()')
    cmds.popupMenu()
    cmds.menuItem(l='Delete', c='sdd_deleteMoveSdkObj()')
    cmds.button(l='Check Move', c='sdd_checkMoveCntList()')
    cmds.columnLayout('frSdkDefineEditCL', p='frSdkDefineAllCL', adj=1)

    cmds.columnLayout('frSdkDefineDnCL', p='frSdkDefineEditCL', adj=1)
    cmds.rowLayout('frSDKToolsRL', nc=6, cw6=[65, 83, 72, 65, 80, 65])
    cmds.button(l='L<<R', w=65, h=30, c='sdd_mirrorSdkCntPos("L<<R")')
    cmds.button(l='Reset To Zero', w=83, h=30, c='sdd_mirrorSdkCntPos("Zero")')
    cmds.button(l='L>>R', w=65, h=30, c='sdd_mirrorSdkCntPos("L>>R")')
    cmds.button(l='+', w=65, h=30, c='sdd_scaleSdkKeys("+")')
    cmds.columnLayout()
    cmds.text(l='Scale Keys', w=78, h=15)
    cmds.rowLayout(nc=3, cw3=[15, 40, 15])
    cmds.button(l='<', w=15, h=15, c='sdd_addOrSubScaleValue("<")')
    cmds.intField('frScaleSdkIF', w=40, max=100, min=0, v=80, h=15)
    cmds.button(l='>', w=15, h=15, c='sdd_addOrSubScaleValue(">")')
    cmds.button(p='frSDKToolsRL', l='-', w=65, h=30, c='sdd_scaleSdkKeys("-")')

    cmds.separator(h=5, p='frSdkDefineDnCL')
    cmds.button('frSdkRedefineB', l='Redefine', p='frSdkDefineDnCL', h=35, c='sdd_sdkRedefine()')

    # corrective
    cmds.columnLayout('frCorrectiveAllCL', p='frMainRigTL', adj=1)

    cmds.columnLayout('frCorrectiveCL', p='frCorrectiveAllCL', adj=1)
    cmds.rowLayout(nc=13)
    cmds.text(l='Filter: ', w=35, al='right')
    cmds.checkBox('frCrtSdkFilterLCB', v=1, w=40, l='L_*', cc='sdd_loadBsSdkAttrToList()')
    cmds.checkBox('frCrtSdkFilterRCB', v=1, w=40, l='R_*', cc='sdd_loadBsSdkAttrToList()')
    cmds.text(l='Mirror BS: ', w=60, al='right')
    cmds.checkBox('frCrtMirrorCB', v=0, l='')
    cmds.floatField('frMirDisTF', w=50, pre=4, v=0.01, min=0, max=1, h=16)

    cmds.text(w=60, al='right', l='Refrence:  ')
    cmds.checkBox('frMeshReferenceCB', v=1, l='', cc='sdd_meshReferenceChange(4)')
    cmds.text(w=15, al='right', l='')
    cmds.iconTextCheckBox('frShowAllMeshListITCB', st='textOnly', l='Mesh', w=100, bgc=[0.35, 0.35, 0.35],
                          cc='sdd_allMeshListShow()', v=1)

    cmds.paneLayout('frCorrectivePL', p='frCorrectiveCL', w=375, cn='vertical3', h=340)
    cmds.columnLayout('frCtrMeshListCL', p='frCorrectivePL', adj=1, w=20)
    cmds.textField('frCurrentMeshTF', ed=0, h=20)
    cmds.textScrollList('frCtrAllMeshTSL', h=290, ams=1, sc='sdd_ctrAllMeshListSelectChange()')
    cmds.popupMenu()
    cmds.menuItem(l='ReCheck Mirror', c='sdd_calcMeshMirrorInfor(2)')
    cmds.menuItem(l='Show Mirror Window', c='sdd_faceMeshMirrorInfo()')

    cmds.button('frSetCurMeshB', l='Set', c='sdd_setCurrentCtrMeshProc()')

    cmds.columnLayout(p='frCorrectivePL', adj=1, w=20)
    cmds.text(l='SDK Attribute:', al='left', h=20)
    cmds.textScrollList('frCrtSdkAttrTSL', h=290, ams=1, sc='sdd_bsSdkAttrListSelectChange()')
    cmds.popupMenu()
    cmds.menuItem(l='refresh', c='sdd_loadBsSdkAttrToList()')
    cmds.button(l='New Attribute', c='sdd_newSdkAttr()')

    cmds.columnLayout(p='frCorrectivePL', adj=1, w=20)
    cmds.text(l='Corrective Blendshape List:', al='left', h=20)
    cmds.textScrollList('frCrtBsTSL', h=290, sc='sdd_bsSdkBsListSelectChange()')
    cmds.popupMenu()
    cmds.menuItem(l='Delete', c='sdd_deleteCorrectiveBS()')
    cmds.button('frCrtNewBSB', l='New Blendshape', c='sdd_newCorrectiveBlendShape()', en=0)

    cmds.columnLayout('frCorrectiveEditCL', p='frCorrectiveAllCL', adj=1)

    cmds.columnLayout('frCorrectiveDnCL', p='frCorrectiveEditCL', adj=1)
    cmds.rowLayout('frCtrModifyRL', nc=6, cw6=[65, 83, 72, 65, 80, 65], en=0)
    cmds.button(l='R<<L', w=65, h=30, c='sdd_mirrorAndResetCrtBS("R<<L")')
    cmds.button(l='Reset', w=83, h=30, c='sdd_mirrorAndResetCrtBS("Reset")')
    cmds.button(l='R>>L', w=65, h=30, c='sdd_mirrorAndResetCrtBS("R>>L")')
    cmds.button(l='+', w=65, h=30, c='sdd_caclCtrBsPuff("+")')
    cmds.columnLayout()
    cmds.text(l='Puff', w=78, h=10)
    cmds.floatSlider('frCtrBsPuffFS', w=78, max=1, min=0.01, v=0.2)
    cmds.button(p='frCtrModifyRL', l='-', w=65, h=30, c='sdd_caclCtrBsPuff("-")')

    cmds.separator(h=5, p='frCorrectiveDnCL')
    cmds.button('frCtrBsEditB', l='Edit', p='frCorrectiveDnCL', h=35, c='sdd_ctrBsEdit()', en=0)

    # Advanced
    cmds.columnLayout('frAdvancedCL', p='frMainRigTL', adj=1, rs=5, en=1)
    # cmds.frameLayout('frExtraMeshFL',p='frAdvancedCL',w=290,l="Extra Mesh",collapsable=0,cl=0)
    # cmds.columnLayout('frExtraMeshCL',adj=1,rs=5)
    # cmds.rowLayout(nc=3,rat=[2,'top',0])
    # cmds.textScrollList('frExtraMeshTSL',h=100,w=300,ams=1,sc='sdd_extraMeshSelectChange()')
    # cmds.columnLayout(rs=2)
    # cmds.button(l='Load',w=135,c='sdd_loadExtraMesh()')
    # cmds.button(l='Clear',w=135,c='sdd_clearExtraMeshList()')

    # cmds.text(l='',h=22)
    # cmds.button(l='Create Final BS',w=135,c='sdd_createFinalBS()')

    cmds.frameLayout('frFinalMeshFL', p='frAdvancedCL', w=290, l="Final Mesh", collapsable=1, cl=0)
    cmds.columnLayout('frFinalMeshCL', adj=1)
    cmds.button('frFinalMeshB', p='frFinalMeshCL', l='Create Final Mesh', c='sdd_createFinalMesh()')

    cmds.frameLayout('frHeadScaleFL', p='frAdvancedCL', w=290, l="Head Scale", collapsable=1, cl=0)
    cmds.columnLayout('frHeadScaleCL', adj=1)
    cmds.button('frHeadScaleB', p='frHeadScaleCL', l='Create', c='sdd_headScaleCreate()')
    cmds.rowLayout(p='frHeadScaleCL', nc=4)
    cmds.button('frHeadMeshGrpB', l='', w=223, c='sdd_switchMeshDisplay([0,0,1,0,0,0])')
    cmds.button('frJawMeshGrpB', l='', w=223, c='sdd_switchMeshDisplay([0,0,0,1,0,0])')
    cmds.rowLayout(p='frHeadScaleCL', nc=4)
    cmds.button('frHeadWeightGrpB', l='', w=223, c='sdd_transferWeightToLattice(1)')
    cmds.button('frJawWeightGrpB', l='', w=223, c='sdd_transferWeightToLattice(2)')

    cmds.frameLayout('frSecondCtrlFL', p='frAdvancedCL', w=290, l="Second Control", collapsable=1, cl=0)
    cmds.columnLayout('frSecondCtrlCL', adj=1)
    cmds.rowLayout(p='frSecondCtrlCL', nc=4)
    cmds.button('frSecondCtrlB', w=223, l='Create Space Lacator', c='sdd_createSecLacator()')
    cmds.button('frSecondMatchB', w=223, l='Match To Clost Point', c='sdd_matchSecLocToCloset()')
    cmds.button('frSecondRigB', p='frSecondCtrlCL', l='Rigging', c='sdd_createSecRigging()')

    cmds.frameLayout('frSnapCtrlFL', p='frAdvancedCL', w=290, l="Snap Control", collapsable=1, cl=0)
    cmds.columnLayout('frSnapCtrlCL', adj=1)
    cmds.rowLayout(p='frSnapCtrlCL', nc=4)
    cmds.button('frSnapCtrlB', w=223, l='Create Snap Ctrl', c='')
    cmds.button('frSnapMatchB', w=223, l='Match To Clost Point', c='')
    cmds.rowLayout(p='frSnapCtrlCL', nc=4)
    cmds.button('frSnapCtrlMirB', w=223, l='L>>R Mir', c='')
    cmds.button('frSnapRigB', w=223, l='Set Up To Snap Ctrl', c='')

    cmds.frameLayout('frWrapMeshFL', p='frAdvancedCL', w=290, l="Warp Mesh", collapsable=1, cl=1)
    cmds.columnLayout('frWrapMeshCL', adj=1)
    cmds.button(w=256, l='Load Mesh', c='sdd_loadWrapMeshToList()')
    cmds.textScrollList('frwmMeshTLS', h=80, w=256)
    cmds.button(w=223, l='Create Wrap Cylinder', c='sdd_createWrapCylinder()')
    cmds.textField('frwmCylinderTF', ed=0, w=223)
    cmds.rowLayout(p='frWrapMeshCL', nc=4)
    cmds.button(w=223, l='Match', c='sdd_wrapMeshProc()')
    cmds.button(w=223, l='Restore', c='sdd_wrapMeshRestore()')

    cmds.progressBar('frMainStatePB', p='frMainCL', h=10, w=440, vis=0)

    cmds.tabLayout('frMainRigTL', e=1,
                   tli=[[1, 'Joint Template'], [2, 'Rigging'], [3, 'Sdk Define'], [4, 'Corrective'], [5, 'Advanced']])
    cmds.showWindow('sdd_YJ_FaceRiggingWin')


def sdd_addOrSubScaleValue(typ):
    val = cmds.intField('frScaleSdkIF', q=1, v=1)
    if (typ == '<'):
        val -= 10
    else:
        val += 10
    val = max(0, min(val, 100))
    cmds.intField('frScaleSdkIF', e=1, v=val)


# ==================================================================================
# zzx .........................
def zzx_importExportCnt(_type):
    global _ctrlPosDict
    if _type == "export":
        _ctrlPosDict = {}
        _ctrlList = cmds.ls('*FK') + cmds.ls('*Ctrl') + cmds.ls('*IK') + cmds.ls('*Pole') + cmds.ls('*CC') + cmds.ls(
            '*cnt') + cmds.ls('*Switch')
        for i in range(len(_ctrlList)):
            _ctrlPosList_ele = []
            for j in range(100):
                if cmds.objExists(_ctrlList[i] + ".cv[" + str(j) + "]"):
                    _TXGrp = cmds.xform(_ctrlList[i] + ".cv[" + str(j) + "]", q=1, ws=1, t=1)
                    _ctrlPosList_ele.append(_TXGrp)
                else:
                    break
            _ctrlPosDict[_ctrlList[i]] = _ctrlPosList_ele
    else:
        for _cnt in _ctrlPosDict.keys():
            if cmds.objExists(_cnt):
                _anim = _cnt
                _ctrlPosList_ele = _ctrlPosDict[_cnt]
                for k in range(len(_ctrlPosList_ele)):
                    cmds.xform(_anim + ".cv[" + str(k) + "]", ws=1, t=_ctrlPosList_ele[k])

    if _type == "export":
        sys.stderr.write('Export Cnt ~')
    else:
        sys.stderr.write('Import Cnt ~')


def zzx_mirrorCnt(_type):
    _from_AnimList = cmds.ls('Left*FK') + cmds.ls('Left*IK') + cmds.ls('Left*Pole') + cmds.ls('Left*CC') + cmds.ls(
        'Left*Switch') + cmds.ls('L*cnt')
    _to_AnimList = cmds.ls('Right*FK') + cmds.ls('Right*IK') + cmds.ls('Right*Pole') + cmds.ls('Right*CC') + cmds.ls(
        'Right*Switch') + cmds.ls('R*cnt')
    if _type == 'LtoR':
        zzx_mirrorCntCMD(_from_AnimList, _to_AnimList)
    else:
        zzx_mirrorCntCMD(_to_AnimList, _from_AnimList)


def zzx_mirrorCntCMD(_from_AnimList, _to_AnimList):
    for _num in range(len(_from_AnimList)):
        _LCtrl = _from_AnimList[_num]
        _RCtrl = _to_AnimList[_num]
        for i in range(100):
            if cmds.objExists(_LCtrl + ".cv[" + str(i) + "]"):
                _TXGrp = cmds.xform(_LCtrl + ".cv[" + str(i) + "]", q=1, ws=1, t=1)
                _TXGrp_new = [_TXGrp[0] * (-1), _TXGrp[1], _TXGrp[2]]
                cmds.xform(_RCtrl + ".cv[" + str(i) + "]", ws=1, t=_TXGrp_new)
            else:
                continue


def zzx_zeroCnt():
    _allAnimGrp = cmds.ls('*FK') + cmds.ls('*Ctrl') + cmds.ls('*IK') + cmds.ls('*Pole') + cmds.ls('*CC') + cmds.ls(
        '*cnt')
    _attrLists = ['translateX', 'translateY', 'translateZ', 'rotateX', 'rotateY', 'rotateZ', 'Shut', 'Thumb', 'Index',
                  'Middle', 'Ring', 'Pinky', 'stertch', 'Heel', 'Ball', 'TipToe', 'Side']
    for _anim in _allAnimGrp:
        _attrGrp = cmds.listAttr(_anim, k=1)
        for _attr in _attrGrp:
            if _attr in _attrLists:
                cmds.setAttr(_anim + "." + _attr, 0)


# zzx .........................
# ==================================================================================
def sdd_createSecLacator():
    FR, FRJntPos, FRUIPos = sdd_frTNameDirc()
    T = sdd_returnTempNameDirc()
    _sdk = T['_sdk']
    _cnt = T['_cnt']
    _rig = T['_rig']
    _anim = T['_anim']
    _grp = T['_grp']
    _loc = T['_loc']
    _skin = T['_skin']

    faceCur = 'faceMoveCur'

    faceAdvancedGrp = 'face_advanced_rig_grp'
    if not (cmds.objExists(faceAdvancedGrp)):
        return

    faceSecLocGrp = 'face_second_loctor_grp'
    if not (cmds.objExists(faceSecLocGrp)):
        faceSecLocGrp = cmds.group(em=1, n=faceSecLocGrp)
        cmds.parent(faceSecLocGrp, faceAdvancedGrp)
    _rad = cmds.getAttr(faceCur + '.globalScale')

    baseNameList = sdd_returnAllSdkCntList()
    skipList = [FR['head'], FR['jaw'], FR['L_eye_root'], FR['R_eye_root'], FR['L_eyeBall'], FR['R_eyeBall']]
    for i in baseNameList:
        if (i in skipList):
            continue
        sdkCnt = i + _cnt
        sdkJnt = i + _skin
        if (not (cmds.objExists(sdkCnt)) or not (cmds.objExists(sdkJnt))):
            continue
        secLoc = i + _loc
        if (cmds.objExists(secLoc)):
            continue

        secLoc = sdd_createSpaceLocator(secLoc, _rad * 0.1)
        cmds.delete(cmds.parentConstraint(sdkCnt, secLoc))
        cmds.parent(secLoc, faceSecLocGrp)

    cmds.select(faceSecLocGrp)


def sdd_matchSecLocToCloset():
    faceAdvancedGrp = 'face_advanced_rig_grp'
    if not (cmds.objExists(faceAdvancedGrp)):
        return
    faceSecLocGrp = 'face_second_loctor_grp'
    if not (cmds.objExists(faceSecLocGrp)):
        return

    secMesh = sdd_getSecondMesh()
    secMFnMesh = sdd_getMfnMeshByName(secMesh)

    clostP = OpenMaya.MPoint()
    util = OpenMaya.MScriptUtil()
    util.createFromInt(0)
    idPointer = util.asIntPtr()
    vtxPointList = OpenMaya.MPointArray()
    secMFnMesh.getPoints(vtxPointList, OpenMaya.MSpace.kWorld)
    mirDis = 5
    secMeshShape = cmds.listRelatives(secMesh, s=1, f=1)[0]

    locList = cmds.listRelatives(faceSecLocGrp, c=1)
    for i in locList:
        secLoc = i
        pos = cmds.xform(secLoc, q=1, ws=1, t=1)
        curPos = OpenMaya.MPoint(pos[0], pos[1], pos[2])

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
        cmds.xform(secLoc, ws=1, t=[vtxPointList[retIdx].x, vtxPointList[retIdx].y, vtxPointList[retIdx].z])


def sdd_createSecRigging():
    FR, FRJntPos, FRUIPos = sdd_frTNameDirc()
    T = sdd_returnTempNameDirc()
    _sdk = T['_sdk']
    _cnt = T['_cnt']
    _rig = T['_rig']
    _anim = T['_anim']
    _grp = T['_grp']
    _loc = T['_loc']
    _skin = T['_skin']
    _fol = T['_fol']
    faceCur = 'faceMoveCur'

    faceAdvancedGrp = 'face_advanced_rig_grp'
    if not (cmds.objExists(faceAdvancedGrp)):
        return
    faceSecLocGrp = 'face_second_loctor_grp'
    if not (cmds.objExists(faceSecLocGrp)):
        return

    faceSecFolGrp = 'face_second_follicle_grp'
    if (cmds.objExists(faceSecFolGrp)):
        return
    faceSecFolGrp = cmds.group(em=1, n=faceSecFolGrp)
    cmds.setAttr(faceSecFolGrp + '.it', 0)
    cmds.setAttr(faceSecFolGrp + '.v', 0)
    cmds.parent(faceSecFolGrp, faceAdvancedGrp)

    faceSecAnimGrp = 'face_second_anim_grp'
    if (cmds.objExists(faceSecAnimGrp)):
        return
    faceAnimCtrlGrp = 'face_anim_ctrl_grp'

    faceSecAnimGrp = cmds.group(em=1, n=faceSecAnimGrp)
    cmds.setAttr(faceSecAnimGrp + '.it', 0)
    cmds.parent(faceSecAnimGrp, faceAnimCtrlGrp)

    secMesh = sdd_getSecondMesh()
    secMFnMesh = sdd_getMfnMeshByName(secMesh)

    clostP = OpenMaya.MPoint()
    util = OpenMaya.MScriptUtil()
    util.createFromInt(0)
    idPointer = util.asIntPtr()
    vtxPointList = OpenMaya.MPointArray()
    secMFnMesh.getPoints(vtxPointList, OpenMaya.MSpace.kWorld)
    # mirDis=5
    secMeshShape = cmds.listRelatives(secMesh, s=1, f=1)[0]

    locList = cmds.listRelatives(faceSecLocGrp, c=1)
    faceCur = 'faceMoveCur'
    _rad = cmds.getAttr(faceCur + '.globalScale')

    for i in locList:
        secLoc = i
        baseName = i[:-len(_loc)]
        sdkCnt = baseName + _cnt
        sdkJnt = baseName + _skin
        secFol = baseName + _fol
        secRig = baseName + _rig

        secAnim = sdd_createCurveCnt(baseName + _anim, 'Sphere', _rad * 0.15)
        invGrp = cmds.group(secAnim, n=secAnim + '_inv_grp')
        zeroGrp = cmds.group(invGrp, n=secAnim + '_zero_grp')
        cmds.parent(zeroGrp, faceSecAnimGrp)
        cmds.delete(cmds.parentConstraint(sdkCnt, zeroGrp))

        pos = cmds.xform(secLoc, q=1, ws=1, t=1)
        curPos = OpenMaya.MPoint(pos[0], pos[1], pos[2])

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

        uvVtx = cmds.polyListComponentConversion(secMesh + '.vtx[%s]' % retIdx, fv=1, tuv=1)
        uvPos = cmds.polyEditUV(uvVtx[0], q=1, u=1)

        secFol = cmds.createNode('follicle', n=secFol)
        secFolT = cmds.listRelatives(secFol, p=1)[0]
        cmds.connectAttr(secFol + '.ot', secFolT + '.t')
        cmds.connectAttr(secFol + '.or', secFolT + '.r')

        cmds.connectAttr(secMeshShape + '.worldMatrix[0]', secFol + '.inputWorldMatrix')
        cmds.connectAttr(secMeshShape + '.outMesh', secFol + '.inputMesh')
        cmds.setAttr(secFol + '.pu', uvPos[0])
        cmds.setAttr(secFol + '.pv', uvPos[1])

        cmds.parent(secFolT, faceSecFolGrp)
        cmds.delete(cmds.pointConstraint(secFolT, zeroGrp))
        cmds.pointConstraint(secFolT, zeroGrp, mo=1)

        tmd = cmds.createNode('multiplyDivide', n=secAnim + '_invT_md')
        cmds.setAttr(tmd + '.i2', -1, -1, -1, typ='float3')
        cmds.connectAttr(secAnim + '.t', tmd + '.i1')
        cmds.connectAttr(tmd + '.o', invGrp + '.t')

        cmds.connectAttr(secAnim + '.t', secRig + '.t')
        cmds.connectAttr(secAnim + '.r', secRig + '.r')
        cmds.connectAttr(secAnim + '.s', secRig + '.s')

        skinMesh = sdd_getFaceMeshName()
        skinNode = mm.eval('findRelatedSkinCluster %s' % skinMesh)
        wt = cmds.skinPercent(skinNode, skinMesh + '.vtx[%s]' % retIdx, q=1, t=sdkJnt)
        if (wt == 0):
            wt = 1
        pos = cmds.xform(secAnim, q=1, t=1, ws=1)
        cmds.scale(1 / wt, 1 / wt, 1 / wt, cmds.ls(secAnim + '.cv[*]'), r=1, p=pos)
        cmds.setAttr(zeroGrp + '.s', wt, wt, wt, typ='float3')

    cmds.setAttr(faceSecLocGrp + '.v', 0)
    sdd_secondRigButtonChange()


def sdd_createSecLacator():
    FR, FRJntPos, FRUIPos = sdd_frTNameDirc()
    T = sdd_returnTempNameDirc()
    _sdk = T['_sdk']
    _cnt = T['_cnt']
    _rig = T['_rig']
    _anim = T['_anim']
    _grp = T['_grp']
    _loc = T['_loc']
    _skin = T['_skin']
    faceCur = 'faceMoveCur'

    faceAdvancedGrp = 'face_advanced_rig_grp'
    if not (cmds.objExists(faceAdvancedGrp)):
        return

    faceSecLocGrp = 'face_second_loctor_grp'
    if not (cmds.objExists(faceSecLocGrp)):
        faceSecLocGrp = cmds.group(em=1, n=faceSecLocGrp)
        cmds.setAttr(faceSecLocGrp + '.it', 0)
        cmds.parent(faceSecLocGrp, faceAdvancedGrp)
    _rad = cmds.getAttr(faceCur + '.globalScale')

    secMesh = sdd_getSecondMesh()
    secMFnMesh = sdd_getMfnMeshByName(secMesh)

    clostP = OpenMaya.MPoint()
    util = OpenMaya.MScriptUtil()
    util.createFromInt(0)
    idPointer = util.asIntPtr()
    vtxPointList = OpenMaya.MPointArray()
    secMFnMesh.getPoints(vtxPointList, OpenMaya.MSpace.kWorld)
    # mirDis=5

    baseNameList = sdd_returnAllSdkCntList()
    skipList = [FR['head'], FR['jaw'], FR['L_eye_root'], FR['R_eye_root'], FR['L_eyeBall'], FR['R_eyeBall']]
    for i in baseNameList:
        if (i in skipList):
            continue
        sdkCnt = i + _cnt
        sdkJnt = i + _skin
        if (not (cmds.objExists(sdkCnt)) or not (cmds.objExists(sdkJnt))):
            continue
        secLoc = i + _loc
        if (cmds.objExists(secLoc)):
            continue

        secLoc = sdd_createSpaceLocator(secLoc, _rad * 0.1)
        cmds.delete(cmds.parentConstraint(sdkCnt, secLoc))
        cmds.parent(secLoc, faceSecLocGrp)

        pos = cmds.xform(secLoc, q=1, ws=1, t=1)

        curPos = OpenMaya.MPoint(pos[0], pos[1], pos[2])

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
        # if(vtxPointList[retIdx].distanceTo(curPos)<mirDis):
        cmds.xform(secLoc, ws=1, t=[vtxPointList[retIdx].x, vtxPointList[retIdx].y, vtxPointList[retIdx].z])

    cmds.select(faceSecLocGrp)
    cmds.setAttr(faceSecLocGrp + '.v', 1)


def sdd_secondRigButtonChange():
    faceSecFolGrp = 'face_second_follicle_grp'
    faceSecAnimGrp = 'face_second_anim_grp'
    if (cmds.objExists(faceSecFolGrp) or cmds.objExists(faceSecAnimGrp)):
        cmds.button('frSecondRigB', e=1, l='Delete', c='sdd_deleteSecRigging()')
    else:
        cmds.button('frSecondRigB', e=1, l='Create', c='sdd_createSecRigging()')


def sdd_deleteSecRigging():
    ret = cmds.confirmDialog(t='FinalMesh', m='Delete All FinalMesh Group?', b=['Yes', 'No'], db='No', cb='No', ds='No')
    if (ret == 'Yes'):
        # 'face_second_loctor_grp',
        delList = ['face_second_follicle_grp', 'face_second_anim_grp']
        for i in delList:
            if cmds.objExists(i):
                cmds.delete(i)

        sdd_secondRigButtonChange()


def sdd_getSecondMesh():
    faceSecMeshGrp = 'face_second_mesh_grp'
    secMesh = cmds.listRelatives(faceSecMeshGrp, c=1)
    if (secMesh != None):
        return secMesh[0]


def sdd_createSpaceLocator(locName, rad):
    locName = cmds.spaceLocator(n=locName)[0]
    locShape = cmds.listRelatives(locName, s=1, f=1)[0]
    cmds.setAttr(locShape + '.lsx', rad)
    cmds.setAttr(locShape + '.lsy', rad)
    cmds.setAttr(locShape + '.lsz', rad)
    return locName


def sdd_createFinalMesh():
    faceCur = 'faceMoveCur'
    faceSkinMeshGrp = 'face_skin_mesh_grp'
    if not (cmds.objExists(faceSkinMeshGrp)):
        return
    faceFinalMeshGrp = 'face_final_mesh_grp'
    faceHeadScaleMeshGrp = 'face_headScale_mesh_grp'
    if cmds.objExists(faceFinalMeshGrp) or cmds.objExists(faceHeadScaleMeshGrp):
        return
    faceBaseGrp = 'face_base_rig_grp'
    cmds.setAttr(faceBaseGrp + '.it', 0)

    faceAdvancedGrp = 'face_advanced_rig_grp'
    if not (cmds.objExists(faceAdvancedGrp)):
        faceAdvancedGrp = cmds.group(n=faceAdvancedGrp, em=1)
        cmds.setAttr(faceAdvancedGrp + '.it', 0)
        cmds.parent(faceAdvancedGrp, faceCur)

    faceMeshGrp = 'face_mesh_grp'

    faceFinalMeshGrp = cmds.group(em=1, n=faceFinalMeshGrp)
    cmds.parent(faceFinalMeshGrp, faceMeshGrp)

    faceHeadScaleMeshGrp = cmds.group(em=1, n=faceHeadScaleMeshGrp)
    cmds.setAttr(faceHeadScaleMeshGrp + '.it', 0)
    cmds.parent(faceHeadScaleMeshGrp, faceMeshGrp)

    faceAllList = cmds.listRelatives(faceSkinMeshGrp, c=1)
    finalMeshList = []
    headScaleMeshList = []
    for i in faceAllList:
        dMesh = cmds.duplicate(i, n=i + '_final')[0]
        cmds.parent(dMesh, faceFinalMeshGrp)
        finalMeshList.append(dMesh)
        dMesh = cmds.duplicate(i, n=i + '_headScale')[0]
        cmds.parent(dMesh, faceHeadScaleMeshGrp)
        headScaleMeshList.append(dMesh)

    headScaleBS = 'headScale_BS'
    headScaleBS = cmds.blendShape(faceSkinMeshGrp, faceHeadScaleMeshGrp, n=headScaleBS)
    cmds.setAttr(headScaleBS[0] + '.' + faceSkinMeshGrp, 1)

    finalBS = 'final_BS'
    finalBS = cmds.blendShape(faceHeadScaleMeshGrp, faceFinalMeshGrp, n=finalBS)
    cmds.setAttr(finalBS[0] + '.' + faceHeadScaleMeshGrp, 1)

    cmds.setAttr(faceFinalMeshGrp + '.v', 1)
    cmds.setAttr(faceHeadScaleMeshGrp + '.v', 0)
    sdd_finalMeshButtonChange()

    faceSecMeshGrp = 'face_second_mesh_grp'
    if (cmds.objExists(faceSecMeshGrp)):
        cmds.delete(faceSecMeshGrp)
    faceSecMeshGrp = cmds.group(n=faceSecMeshGrp, em=1)
    cmds.parent(faceSecMeshGrp, faceMeshGrp)
    cmds.setAttr(faceSecMeshGrp + '.v', 0)

    faceMesh = sdd_getFaceMeshName()
    secMesh = cmds.duplicate(faceMesh, n='face_second_control_Mesh')[0]
    cmds.parent(secMesh, faceCur)
    cmds.polyAutoProjection(secMesh, cm=0, l=2, sc=1, o=1, ps=0.2, ws=0, ch=0)
    secondBS = 'second_BS'
    secondBS = cmds.blendShape(faceMesh + '_final', secMesh, n=secondBS)
    cmds.setAttr(secondBS[0] + '.' + faceMesh + '_final', 1)
    cmds.parent(secMesh, faceSecMeshGrp)


def sdd_deleteFinalMesh():
    ret = cmds.confirmDialog(t='FinalMesh', m='Delete All FinalMesh Group?', b=['Yes', 'No'], db='No', cb='No', ds='No')
    if (ret == 'Yes'):
        faceFinalMeshGrp = 'face_final_mesh_grp'
        faceHeadScaleMeshGrp = 'face_headScale_mesh_grp'
        faceSecondMeshGrp = 'face_second_mesh_grp'
        delList = [faceFinalMeshGrp, faceHeadScaleMeshGrp, faceSecondMeshGrp]
        for i in delList:
            if cmds.objExists(i):
                cmds.delete(i)
        sdd_finalMeshButtonChange()


def sdd_finalMeshButtonChange():
    faceFinalMeshGrp = 'face_final_mesh_grp'
    faceHeadScaleMeshGrp = 'face_headScale_mesh_grp'
    faceSecondMeshGrp = 'face_second_mesh_grp'
    if (cmds.objExists(faceFinalMeshGrp) or cmds.objExists(faceHeadScaleMeshGrp) or cmds.objExists(faceSecondMeshGrp)):
        cmds.button('frFinalMeshB', e=1, l='Delete', c='sdd_deleteFinalMesh()')
    else:
        cmds.button('frFinalMeshB', e=1, l='Create', c='sdd_createFinalMesh()')


def sdd_switchMeshDisplay(showList):
    faceBaseGrp = ['face_base_rig_grp']
    faceSkinMeshGrp = ['face_skin_mesh_grp']
    headSRigGrp = ['headScale_rig_grp', 'headScale_mesh_grp']
    jawSRigGrp = ['jawScale_rig_grp', 'jawScale_mesh_grp']
    faceFinalMeshGrp = ['face_final_mesh_grp', 'face_second_anim_grp']
    faceHeadScaleMeshGrp = ['face_headScale_mesh_grp']

    hasShow = True
    allList = [faceBaseGrp, faceSkinMeshGrp, headSRigGrp, jawSRigGrp, faceFinalMeshGrp, faceHeadScaleMeshGrp]
    for i in range(len(allList)):
        for obj in allList[i]:
            if (cmds.objExists(obj)):
                cmds.setAttr(obj + '.v', showList[i])
                #         if(showList[i]==1):
                #             hasShow=False
                # if(not hasShow):
                #     cmds.setAttr(faceSkinMeshGrp+'.v',1)


def sdd_loadHeadMeshGrpToList():
    headSRigGrp = 'headScale_rig_grp'
    jawSRigGrp = 'jawScale_rig_grp'
    if (cmds.objExists(headSRigGrp)):
        grpName = cmds.button('frHeadMeshGrpB', e=1, l='HeadScale Grp')
        cmds.button('frHeadWeightGrpB', e=1, l='Transfer Weights')
    else:
        grpName = cmds.button('frHeadMeshGrpB', e=1, l='')
        cmds.button('frHeadWeightGrpB', e=1, l='')

    if (cmds.objExists(jawSRigGrp)):
        grpName = cmds.button('frJawMeshGrpB', e=1, l='JawScale Grp')
        cmds.button('frJawWeightGrpB', e=1, l='Transfer Weights')
    else:
        grpName = cmds.button('frJawMeshGrpB', e=1, l='')
        cmds.button('frJawWeightGrpB', e=1, l='')

    headScaleGrp = 'face_headScale_grp'
    if (cmds.objExists(headScaleGrp)):
        cmds.button('frHeadScaleB', e=1, l='Delete', c='sdd_deleteHeadScale()')
    else:
        cmds.button('frHeadScaleB', e=1, l='Create', c='sdd_headScaleCreate()')


def sdd_deleteHeadScale():
    ret = cmds.confirmDialog(t='HeadScale', m='Delete All HeadScale Object?', b=['Yes', 'No'], db='No', cb='No',
                             ds='No')
    if (ret == 'Yes'):
        grpList = ['face_headScale_grp', 'headScale_anim_grp', 'jawScale_anim_grp']
        for i in grpList:
            if cmds.objExists(i):
                cmds.delete(i)
        sdd_switchMeshDisplay([0, 0, 0, 0, 1, 0])
    sdd_loadHeadMeshGrpToList()


def sdd_transferWeightToLattice(typ):
    meshGrp = 'headScale_mesh_grp'
    if (typ == 2):
        meshGrp = 'jawScale_mesh_grp'
    if not (cmds.objExists(meshGrp)):
        return
    mesh = cmds.listConnections(meshGrp + '.mesh')
    ltc = cmds.listConnections(meshGrp + '.lattice')
    if (mesh == None or ltc == None):
        return
    meshSkin = mm.eval('findRelatedSkinCluster %s' % mesh[0])
    ltcSkin = mm.eval('findRelatedSkinCluster %s' % ltc[0])
    if (meshSkin == '' or ltcSkin == ''):
        return
    cmds.copySkinWeights(ss=meshSkin, ds=ltcSkin, nm=1, sa='closestPoint', ia=['oneToOne', 'closestJoint'])
    sdd_switchMeshDisplay([0, 0, 0, 0, 1, 0])


def sdd_headScaleCreate():
    FR, FRJntPos, FRUIPos = sdd_frTNameDirc()
    TName = sdd_returnTempNameDirc()
    _skin = TName['_skin']

    faceSdkHandle = 'face_sdk_handle'
    if not (cmds.objExists(faceSdkHandle)):
        return
    headScaleGrp = 'face_headScale_grp'
    if cmds.objExists(headScaleGrp):
        return
    faceAdvancedGrp = 'face_advanced_rig_grp'
    if not (cmds.objExists(faceAdvancedGrp)):
        return

    faceSkinMeshGrp = 'face_skin_mesh_grp'
    faceAllList = cmds.listRelatives(faceSkinMeshGrp, c=1)
    mBox = [None, None, None, None, None, None]
    mObj = ['', '', '', '', '', '']
    for i in faceAllList:
        box = cmds.xform(i, q=1, bbi=1)
        for a in range(3):
            if (mBox[a] == None):
                mBox[a] = box[a]
                mObj[a] = i
            elif (box[a] < mBox[a]):
                mBox[a] = box[a]
                mObj[a] = i
        for a in range(3, 6):
            if (mBox[a] == None):
                mBox[a] = box[a]
                mObj[a] = i
            elif (box[a] > mBox[a]):
                mBox[a] = box[a]
                mObj[a] = i
    dupList = []
    for i in mObj:
        if not (i in dupList):
            dupList.append(i)

    headScaleGrp = cmds.group(em=1, n=headScaleGrp)
    cmds.parent(headScaleGrp, faceAdvancedGrp)

    baseName = 'headScale'
    headMeshGrp = sdd_headScaleMesh(faceSdkHandle, dupList, headScaleGrp, baseName)
    rPos = cmds.xform(FR['head'] + _skin, q=1, ws=1, t=1)
    sPos = cmds.xform(FR['jaw'] + _skin, q=1, ws=1, t=1)
    ePos = [sPos[0], mBox[4], sPos[2]]
    sdd_headScaleJntList(4, rPos, sPos, ePos, headScaleGrp, headMeshGrp, baseName)

    baseName = 'jawScale'
    jawMeshGrp = sdd_headScaleMesh(faceSdkHandle, dupList, headScaleGrp, baseName)
    sPos1 = cmds.xform(FR['L_eyelid_In'] + _skin, q=1, ws=1, t=1)
    sPos2 = cmds.xform(FR['R_eyelid_In'] + _skin, q=1, ws=1, t=1)
    sPos1[0] += sPos2[0]
    sPos1[1] += sPos2[1]
    sPos1[2] += sPos2[2]
    sPos1[0] /= 2
    sPos1[1] /= 2
    sPos1[2] /= 2
    ePos = cmds.xform(FR['chin'] + _skin, q=1, ws=1, t=1)
    sdd_headScaleJntList(4, rPos, sPos1, ePos, headScaleGrp, jawMeshGrp, baseName)
    sdd_loadHeadMeshGrpToList()


def sdd_headScaleMesh(faceSdkHandle, dupList, headScaleGrp, baseName):
    headMeshGrp = '%s_mesh_grp' % baseName
    headMeshGrp = cmds.group(em=1, n=headMeshGrp)
    cmds.parent(headMeshGrp, headScaleGrp)
    cmds.setAttr(headMeshGrp + '.v', 0)

    sdd_resetAllSdkHandleAttr()
    cmds.setAttr(faceSdkHandle + '.L_eyelid_close', 1)
    cmds.setAttr(faceSdkHandle + '.R_eyelid_close', 1)
    newMeshList = []
    for i in dupList:
        dMesh = cmds.duplicate(i, n=i + '_%s' % baseName)[0]
        cmds.parent(dMesh, headMeshGrp)
        newMeshList.append(dMesh)

    if (len(newMeshList) > 1):
        headMesh = cmds.polyUnite(newMeshList, ch=0, n=baseName + '_mesh')
        headMesh = headMesh[0]
        cmds.parent(headMesh, headScaleGrp)
        cmds.delete(cmds.listRelatives(headMeshGrp, c=1))
        cmds.parent(headMesh, headMeshGrp)

    else:
        headMesh = cmds.rename(newMeshList[0], baseName + '_mesh')

    iOrigAttr = sdd_tryAddMessageAttr(headMeshGrp, 'mesh')
    sdd_connectAttrForce(headMesh + '.msg', iOrigAttr)

    cmds.setAttr(faceSdkHandle + '.L_eyelid_close', 0)
    cmds.setAttr(faceSdkHandle + '.R_eyelid_close', 0)
    return headMeshGrp


# num,rPos,sPos,ePos,headScaleGrp,headMeshGrp,baseName=(4,rPos,sPos,ePos,headScaleGrp,headMeshGrp,baseName)

def sdd_headScaleJntList(num, rPos, sPos, ePos, headScaleGrp, headMeshGrp, baseName):
    headRigGrp = '%s_rig_grp' % baseName
    headRigGrp = cmds.group(em=1, n=headRigGrp)
    cmds.setAttr(headRigGrp + '.v', 0)
    # cmds.setDrivenKeyframe(headMeshGrp+'.v',cd=headRigGrp+'.v',v=0,dv=0,itt='linear',ott='linear')
    # cmds.setDrivenKeyframe(headMeshGrp+'.v',cd=headRigGrp+'.v',v=1,dv=1,itt='linear',ott='linear')
    faceAnimCtrlGrp = 'face_anim_ctrl_grp'

    cmds.parent(headRigGrp, headScaleGrp)
    direction = (ePos[1] - sPos[1]) > 0

    TName = sdd_returnTempNameDirc()
    _skin = TName['_skin']
    # _ctrl=TName['_ctrl']
    _anim = TName['_anim']
    _grp = TName['_grp']
    cur = cmds.curve(ep=[sPos, ePos], n=baseName + '_cur')
    cmds.rebuildCurve(cur, ch=0, rpo=1, end=1, kr=0, kcp=1, kt=0)
    cmds.parent(cur, headRigGrp)
    cmds.select(cl=1)

    jntList = []
    jnt = cmds.joint(p=rPos, n=baseName + '_root' + _skin)
    jntList.append(jnt)
    for i in range(num + 1):
        pos = cmds.pointOnCurve(cur, p=1, pr=1.0 / num * i)
        jnt = cmds.joint(p=pos, n=baseName + '_%s' % (i + 1) + _skin)
        jntList.append(jnt)
    cmds.joint(jntList[1], e=1, oj='yxz', sao='xup', ch=1, zso=1)
    jntGrp = cmds.group(em=1, n=jntList[1] + '_zero_grp')
    cmds.delete(cmds.parentConstraint(jntList[1], jntGrp))
    if (direction):
        cmds.move(0, (ePos[1] - sPos[1]) / -num * 0.5, 0, jntGrp, r=1, os=1, wd=1)
    else:
        cmds.move(0, (ePos[1] - sPos[1]) / num * 0.5, 0, jntGrp, r=1, os=1, wd=1)

    cmds.parent(jntList[1], jntGrp)
    cmds.parent(jntGrp, jntList[0])
    cmds.joint(jntList[-1], e=1, oj='none', ch=0, zso=1)
    cmds.parent(jntList[0], headRigGrp)
    cmds.delete(cur)

    cntPos = [0, 0, 0]
    cntPos[0] = ePos[0] + (ePos[0] - sPos[0]) * 0.3
    cntPos[1] = ePos[1] + (ePos[1] - sPos[1]) * 0.3
    cntPos[2] = ePos[2] + (ePos[2] - sPos[2]) * 0.3

    cnt = sdd_createCurveCnt(baseName + _anim, typ='Cube', r=1)
    cntGrp = cmds.group(cnt, n=cnt + _grp)

    cmds.transformLimits(cnt, tx=[-1, 1], etx=[1, 1], ty=[-1, 1], ety=[1, 1], tz=[-1, 1], etz=[1, 1])
    faceCur = 'faceMoveCur'

    cmds.setAttr(cntGrp + '.t', cntPos[0], cntPos[1], cntPos[2], typ='float3')
    _rad = cmds.getAttr(faceCur + '.globalScale')
    cmds.setAttr(cntGrp + '.s', _rad * 3, _rad * 3, _rad * 3, typ='float3')

    attrList = ['rx', 'ry', 'rz', 'sx', 'sy', 'sz', 'v']
    sdd_frLockAndAttr(cnt, attrList)
    cmds.parent(cntGrp, faceAnimCtrlGrp)

    jList = jntList[1:]
    for i in jList[:-1]:
        cdAttr = cnt + '.tx'
        cAttr = i + '.rz'

        cmds.setDrivenKeyframe(cAttr, cd=cdAttr, v=0, dv=0, itt='linear', ott='linear')
        cmds.setDrivenKeyframe(cAttr, cd=cdAttr, v=-10, dv=1, itt='linear', ott='linear')
        cmds.setDrivenKeyframe(cAttr, cd=cdAttr, v=10, dv=-1, itt='linear', ott='linear')

        cdAttr = cnt + '.tz'
        cAttr = i + '.rx'
        cmds.setDrivenKeyframe(cAttr, cd=cdAttr, v=0, dv=0, itt='linear', ott='linear')
        if (direction):
            cmds.setDrivenKeyframe(cAttr, cd=cdAttr, v=10, dv=1, itt='linear', ott='linear')
            cmds.setDrivenKeyframe(cAttr, cd=cdAttr, v=-10, dv=-1, itt='linear', ott='linear')
        else:
            cmds.setDrivenKeyframe(cAttr, cd=cdAttr, v=10, dv=-1, itt='linear', ott='linear')
            cmds.setDrivenKeyframe(cAttr, cd=cdAttr, v=-10, dv=1, itt='linear', ott='linear')

    for i in jList:
        cdAttr = cnt + '.ty'
        cAttr = i + '.ty'
        cv = cmds.getAttr(cAttr)
        cmds.setDrivenKeyframe(cAttr, cd=cdAttr, v=cv, dv=0, itt='linear', ott='linear')
        if (direction):
            cmds.setDrivenKeyframe(cAttr, cd=cdAttr, v=cv * 1.3, dv=1, itt='linear', ott='linear')
            cmds.setDrivenKeyframe(cAttr, cd=cdAttr, v=cv * 0.7, dv=-1, itt='linear', ott='linear')
        else:
            cmds.setDrivenKeyframe(cAttr, cd=cdAttr, v=cv * 1.3, dv=-1, itt='linear', ott='linear')
            cmds.setDrivenKeyframe(cAttr, cd=cdAttr, v=cv * 0.7, dv=1, itt='linear', ott='linear')

    for i in jList:
        cdAttr = cnt + '.ty'
        cAttr = i + '.sx'
        cmds.setDrivenKeyframe(cAttr, cd=cdAttr, v=1, dv=0, itt='linear', ott='linear')
        if (direction):
            cmds.setDrivenKeyframe(cAttr, cd=cdAttr, v=0.8, dv=1, itt='linear', ott='linear')
            cmds.setDrivenKeyframe(cAttr, cd=cdAttr, v=1.2, dv=-1, itt='linear', ott='linear')
        else:
            cmds.setDrivenKeyframe(cAttr, cd=cdAttr, v=0.8, dv=-1, itt='linear', ott='linear')
            cmds.setDrivenKeyframe(cAttr, cd=cdAttr, v=1.2, dv=1, itt='linear', ott='linear')

    for i in jList:
        cdAttr = cnt + '.ty'
        cAttr = i + '.sz'
        cmds.setDrivenKeyframe(cAttr, cd=cdAttr, v=1, dv=0, itt='linear', ott='linear')
        if (direction):
            cmds.setDrivenKeyframe(cAttr, cd=cdAttr, v=0.9, dv=1, itt='linear', ott='linear')
            cmds.setDrivenKeyframe(cAttr, cd=cdAttr, v=1.1, dv=-1, itt='linear', ott='linear')
        else:
            cmds.setDrivenKeyframe(cAttr, cd=cdAttr, v=0.9, dv=-1, itt='linear', ott='linear')
            cmds.setDrivenKeyframe(cAttr, cd=cdAttr, v=1.1, dv=1, itt='linear', ott='linear')

    faceAllList = cmds.listRelatives(headMeshGrp, c=1)
    if (faceAllList != None):
        for i in faceAllList:
            cmds.skinCluster(jntList, i, mi=1, nw=1, tsb=1)

    faceHeadScaleMeshGrp = 'face_headScale_mesh_grp'
    latticeList = cmds.lattice(faceHeadScaleMeshGrp, dv=[20, 40, 20], oc=1, ldv=[2, 2, 2], n=baseName + '_lattice')
    for i in latticeList[1:]:
        sx = cmds.getAttr(i + '.sx')
        cmds.setAttr(i + '.sx', sx * 1.5)
        sy = cmds.getAttr(i + '.sy')
        cmds.setAttr(i + '.sy', sy * 1.5)
        sz = cmds.getAttr(i + '.sz')
        cmds.setAttr(i + '.sz', sz * 1.5)
        cmds.setAttr(i + '.v', 0)
        cmds.parent(i, headRigGrp)
    cmds.skinCluster(jntList, latticeList[1], mi=1, nw=1, tsb=1)

    iOrigAttr = sdd_tryAddMessageAttr(headMeshGrp, 'lattice')
    sdd_connectAttrForce(latticeList[1] + '.msg', iOrigAttr)



    # startCtrl=cmds.duplicate(jntList[1],n=jntList[1]+_ctrl,po=1)[0]
    # endCtrl=cmds.duplicate(jntList[-1],n=jntList[-1]+_ctrl,po=1)[0]
    # cmds.parent(startCtrl,endCtrl,headScaleGrp)

    # skinNode=cmds.skinCluster(startCtrl,endCtrl,cur,mi=1,nw=1,tsb=1)[0]
    # cmds.skinPercent(skinNode,cur+'.cv[0]',tv=[startCtrl,1])
    # cmds.skinPercent(skinNode,cur+'.cv[1]',tv=[startCtrl,1])
    # cmds.skinPercent(skinNode,cur+'.cv[2]',tv=[[startCtrl,0.5],[endCtrl,0.5]])
    # cmds.skinPercent(skinNode,cur+'.cv[3]',tv=[endCtrl,1])

    # ik_H=cmds.ikHandle(sol='ikSplineSolver',pcv=0,ccv=0,sj=jntList[1],ee=jntList[-1],c=cur,n=baseName+'_ikH')[0]
    # cmds.parent(ik_H,headScaleGrp)


def sdd_allMeshListShow():
    if (cmds.iconTextCheckBox('frShowAllMeshListITCB', q=1, v=1)):
        cmds.columnLayout('frCtrMeshListCL', e=1, vis=1)
    else:
        cmds.columnLayout('frCtrMeshListCL', e=1, vis=0)


# def sdd_ctrMeshSelectChange():
#     selI=cmds.textScrollList('frAllMeshTSL',q=1,si=1)
#     if(selI==None):
#         return
#     cmds.select(selI[0])


# def sdd_loadAllMeshToCtrList():
#     curMesh=cmds.textField('frCurrentMeshTF',q=1,tx=1)
#     faceSkinMeshGrp='face_skin_mesh_grp'
#     if not(cmds.objExists(faceSkinMeshGrp)):
#         return
#     faceAllList=cmds.listRelatives(faceSkinMeshGrp,c=1)
#     cmds.textScrollList('frAllMeshTSL',e=1,ra=1)
#     for i in faceAllList:
#         cmds.textScrollList('frAllMeshTSL',e=1,a=i)
#     if(curMesh==''):
#         curMesh=sdd_getCurrentMeshName()
#         cmds.textField('frCurrentMeshTF',e=1,tx=curMesh)



def sdd_faceMeshSelectChange():
    selI = cmds.textScrollList('frFaceMeshTSL', q=1, si=1)
    if (selI == None):
        return
    sel = []
    for i in selI:
        if (cmds.objExists(i)):
            sel.append(i)
    cmds.select(sel)


def sdd_loadFaceAllMesh():
    sel = cmds.ls(sl=1)
    if (len(sel) == 0):
        return

    cmds.textScrollList('frFaceMeshTSL', e=1, ra=1)
    for i in sel:
        shape = cmds.listRelatives(i, s=1, f=1)
        if (shape == None):
            continue
        if (cmds.objectType(shape[0]) != 'mesh'):
            continue
        cmds.textScrollList('frFaceMeshTSL', e=1, a=i)

    cmds.textField('frFaceMeshTF', e=1, tx='')
    cmds.button('frSetFaceMeshB', e=1, en=1)


def sdd_tryParent(obj1, obj2):
    pObj = cmds.listRelatives(obj2, p=1)
    if (pObj != None and pObj[0] != obj2):
        cmds.parent(obj1, obj2)


def sdd_connectAttrForce(attr1, attr2):
    cnn = cmds.listConnections(attr2, p=1)
    if (cnn != None):
        cmds.disconnectAttr(attr2, cnn[0])
    cmds.connectAttr(attr1, attr2, f=1)


# def sdd_createFinalBS():
#     faceSkinMeshGrp='face_skin_mesh_grp'
#     allI=cmds.textScrollList('frExtraMeshTSL',q=1,ai=1)
#     faceMesh=sdd_getCurrentMeshName()
#     if(faceMesh==''):
#         return
#     faceList=[faceMesh]
#     if(allI!=None):
#         for i in allI:
#             faceList.append(i)

#     for i in faceList:
#         fMesh=cmds.duplicate(i,n=i+'_final')[0]
#         cmds.parent(i,faceLinkBsGrp)
#         cmds.blendShape(i,fMesh,n=i+'_bs')


def sdd_faceMeshMirrorInfo():
    if (cmds.window('sdd_frMirrorInfoWin', q=1, ex=1)): cmds.deleteUI('sdd_frMirrorInfoWin')
    cmds.window('sdd_frMirrorInfoWin', ret=1, s=0)
    cmds.columnLayout('frmiMainCL')

    cmds.paneLayout('frFaceMashPL', cn='vertical3', p='frmiMainCL', w=440, h=360)
    cmds.columnLayout(p='frFaceMashPL', adj=1, w=20)
    cmds.text(l='Middle Vertex Index :', al='left')
    cmds.textScrollList('frMidVtxTSL', h=320, ams=1, sc='sdd_MiddleVtxIdxSelectChange(1)')
    cmds.button(l='Select All', c='sdd_MiddleVtxIdxSelectChange(2)')
    cmds.columnLayout(p='frFaceMashPL', adj=1, w=20)
    cmds.text(l='Mirror Vertex Index :', al='left')
    cmds.textScrollList('frMirVtxTSL', h=320, ams=1, sc='sdd_MirrorVtxIdxSelectChange(1)')
    cmds.button(l='Select All', c='sdd_MirrorVtxIdxSelectChange(2)')
    cmds.columnLayout(p='frFaceMashPL', adj=1, w=20)
    cmds.text(l='Error Vertex Index :', al='left')
    cmds.textScrollList('frErrVtxTSL', h=320, ams=1, sc='sdd_ErrorVtxIdxSelectChange(1)')
    cmds.button(l='Select All', c='sdd_ErrorVtxIdxSelectChange(2)')
    cmds.showWindow('sdd_frMirrorInfoWin')
    sdd_loadFRMirrorInfo()


def sdd_loadFRMirrorInfo():
    faceMesh, origMesh, ctrGrp, suf = sdd_getCtrMeshAnGrpInfo()

    attrList = cmds.listAttr(ctrGrp, ud=1)

    cmds.textScrollList('frMidVtxTSL', e=1, ra=1)

    if ('MiddleVtxIdx' in attrList):
        mVtxList = cmds.getAttr(ctrGrp + '.MiddleVtxIdx')
        if (mVtxList != None):
            for i in range(len(mVtxList)):
                cmds.textScrollList('frMidVtxTSL', e=1, a='%s' % (mVtxList[i]))

    cmds.textScrollList('frErrVtxTSL', e=1, ra=1)
    if ('ErrorVtxIdx' in attrList):
        eVtxList = cmds.getAttr(ctrGrp + '.ErrorVtxIdx')
        if (eVtxList != None):
            for i in range(len(eVtxList)):
                cmds.textScrollList('frErrVtxTSL', e=1, a='%s' % (eVtxList[i]))

    cmds.textScrollList('frMirVtxTSL', e=1, ra=1)
    if ('LeftVtxIdx' in attrList):
        lVtxList = cmds.getAttr(ctrGrp + '.LeftVtxIdx')
        rVtxList = cmds.getAttr(ctrGrp + '.RightVtxIdx')
        if (lVtxList != None):
            for i in range(len(lVtxList)):
                cmds.textScrollList('frMirVtxTSL', e=1, a='%s-%s' % (lVtxList[i], rVtxList[i]))

        if (lVtxList == None):
            cmds.checkBox('frCrtMirrorCB', e=1, en=0)
            if (cmds.window('sdd_frMirrorInfoWin', q=1, ex=1)): cmds.deleteUI('sdd_frMirrorInfoWin')
        else:
            cmds.checkBox('frCrtMirrorCB', e=1, en=1)


def sdd_tabLayoutSelectChange():
    if (cmds.rowLayout('frMoveJointRL', q=1, vis=1)):
        cmds.tabLayout('frMainRigTL', e=1, sti=2)
        return
    if (cmds.button('frCtrBsEditB', q=1, l=1) != 'Edit'):
        cmds.tabLayout('frMainRigTL', e=1, sti=4)
        return
    tabIdx = cmds.tabLayout('frMainRigTL', q=1, sti=1)
    if (tabIdx == 2):
        sdd_reloadFaceMeshInfo()
        sdd_switchMeshDisplay([1, 1, 0, 0, 0, 0])
    elif (tabIdx == 3):
        sdd_loadSdkAttrToList()
        sdd_switchMeshDisplay([1, 1, 0, 0, 0, 0])
    elif (tabIdx == 4):
        sdd_switchMeshDisplay([0, 1, 0, 0, 0, 0])
        sdd_loadBsSdkAttrToList()
        sdd_loadBsToList()
        sdd_loadCtrAllMeshToList()
    elif (tabIdx == 5):
        sdd_switchMeshDisplay([0, 0, 0, 0, 1, 0])
        sdd_loadHeadMeshGrpToList()
        sdd_finalMeshButtonChange()
        sdd_secondRigButtonChange()

    sdd_meshReferenceChange(tabIdx)
    sdd_resetAllSdkHandleAttr()


def sdd_resetAllSdkHandleAttr():
    faceSdkHandle = 'face_sdk_handle'
    if not (cmds.objExists(faceSdkHandle)):
        return
    allI = cmds.listAttr(faceSdkHandle, ud=1)
    for i in allI:
        cmds.setAttr(faceSdkHandle + '.' + i, 0)


def sdd_loadCtrAllMeshToList():
    cmds.textScrollList('frCtrAllMeshTSL', e=1, ra=1)
    faceSkinMeshGrp = 'face_skin_mesh_grp'
    if not (cmds.objExists(faceSkinMeshGrp)):
        return
    faceAllList = cmds.listRelatives(faceSkinMeshGrp, c=1)
    for i in faceAllList:
        cmds.textScrollList('frCtrAllMeshTSL', e=1, a=i)
    faceMesh = cmds.textField('frCurrentMeshTF', q=1, tx=1)
    if (faceMesh == ''):
        faceMesh = cmds.textField('frFaceMeshTF', q=1, tx=1)
        if (faceMesh == ''):
            sdd_reloadFaceMeshInfo()
        faceMesh = cmds.textField('frFaceMeshTF', q=1, tx=1)
        sdd_setCurrentCtrMesh(faceMesh)
    cmds.button('frSetCurMeshB', e=1, en=0)


def sdd_setCurrentCtrMeshProc():
    selI = cmds.textScrollList('frCtrAllMeshTSL', q=1, si=1)
    if (selI == None):
        return
    sdd_setCurrentCtrMesh(selI[0])


def sdd_ctrAllMeshListSelectChange():
    selI = cmds.textScrollList('frCtrAllMeshTSL', q=1, si=1)
    if (selI != None):
        cmds.button('frSetCurMeshB', e=1, en=1)
    cmds.select(selI[0])


def sdd_reloadFaceMeshInfo():
    faceSdkRigGrp = 'face_sdk_rig_grp'
    if (cmds.objExists(faceSdkRigGrp)):
        cmds.button('frLoadAllMeshB', e=1, en=0)
        cmds.button('frSdkRiggingB', e=1, en=1, l='Move Joint Mode', c='sdd_resetJointPosition()')

    else:
        cmds.button('frLoadAllMeshB', e=1, en=1)
        cmds.button('frSdkRiggingB', e=1, l='Rigging', c='sdd_createSdkJointRigging()')

    faceBsGrp = 'face_bs_grp'
    if not (cmds.objExists(faceBsGrp)):
        return
    faceSkinMeshGrp = 'face_skin_mesh_grp'
    if not (cmds.objExists(faceSkinMeshGrp)):
        return
    faceAllList = cmds.listRelatives(faceSkinMeshGrp, c=1)
    cmds.textScrollList('frFaceMeshTSL', e=1, ra=1)
    for i in faceAllList:
        cmds.textScrollList('frFaceMeshTSL', e=1, a=i)
    skinMesh = cmds.listConnections(faceSkinMeshGrp + '.faceMesh')[0]
    # origMeshName=cmds.listConnections(skinMesh+'.origMesh')[0]
    # if not(cmds.objExists(origMeshName)):
    #     return
    cmds.textField('frFaceMeshTF', e=1, tx=skinMesh)


def sdd_getFaceMeshName():
    faceMesh = cmds.textField('frFaceMeshTF', q=1, tx=1)
    if (faceMesh == ''):
        sdd_reloadFaceMeshInfo()
    faceMesh = cmds.textField('frFaceMeshTF', q=1, tx=1)
    return faceMesh


def sdd_resetJointPosition():
    FR, FRJntPos, FRUIPos = sdd_frTNameDirc()
    T = sdd_returnTempNameDirc()
    _skin = T['_skin']
    _grp = T['_grp']
    _cnt = T['_cnt']
    faceSdkRigGrp = 'face_sdk_rig_grp'
    faceSdkSkinGrp = 'face_sdk_skin_grp'

    if (not cmds.rowLayout('frMoveJointRL', q=1, vis=1)):
        sdd_setSkinJointMoveMode(1)
        cmds.setAttr(faceSdkRigGrp + '.v', 0)
        cmds.button('frSdkRiggingB', e=1, vis=0)
        cmds.rowLayout('frMoveJointRL', e=1, vis=1)
        allObjList = cmds.listRelatives(faceSdkSkinGrp, c=1, ad=1)
        delObjList = []
        for i in allObjList:
            if (cmds.objectType(i) != 'joint'):
                delObjList.append(i)
        if (len(delObjList) > 0):
            cmds.delete(delObjList)
    else:
        sdd_setSkinJointMoveMode(0)

        allJntList = cmds.listRelatives(faceSdkSkinGrp, c=1, ad=1)
        cmds.button('frSdkRiggingB', e=1, vis=1)
        cmds.rowLayout('frMoveJointRL', e=1, vis=0)
        cmds.setAttr(faceSdkRigGrp + '.v', 1)
        cmds.delete(cmds.parentConstraint(FR['L_eye_root'] + _skin, FR['L_eye_root'] + _grp))
        cmds.delete(cmds.parentConstraint(FR['R_eye_root'] + _skin, FR['R_eye_root'] + _grp))
        cmds.delete(cmds.parentConstraint(FR['jaw'] + _skin, FR['jaw'] + _grp))

        cmds.parentConstraint(FR['L_eye_root'] + _cnt, FR['L_eye_root'] + _skin)
        cmds.parentConstraint(FR['R_eye_root'] + _cnt, FR['R_eye_root'] + _skin)
        cmds.parentConstraint(FR['jaw'] + _cnt, FR['jaw'] + _skin)

        rootList = [FR['L_eye_root'] + _skin, FR['R_eye_root'] + _skin, FR['jaw'] + _skin]
        for i in allJntList:
            if not (i in rootList):
                cmds.delete(cmds.parentConstraint(i, i[:-len(_skin)] + _grp))
                cmds.parentConstraint(i[:-len(_skin)] + _cnt, i)


def sdd_setSkinJointMoveMode(typ):
    faceSkinMeshGrp = 'face_skin_mesh_grp'
    if not (cmds.objExists(faceSkinMeshGrp)):
        return
    allChildList = cmds.listRelatives(faceSkinMeshGrp, c=1)
    if (allChildList == None):
        return
    skinNodeList = []
    for i in allChildList:
        skinNode = mm.eval('findRelatedSkinCluster %s' % i)
        if (skinNode != ''):
            cmds.skinCluster(skinNode, e=1, mjm=typ)


# Corrective BS ____________________________________________________________________________________====

def sdd_bsSdkAttrListSelectChange():
    TName = sdd_returnTempNameDirc()
    _sdk = TName['_sdk']
    _grp = TName['_grp']
    _cnt = TName['_cnt']

    faceSdkHandle = 'face_sdk_handle'
    if not (cmds.objExists(faceSdkHandle)):
        return

    allI = cmds.listAttr(faceSdkHandle, ud=1)
    selI = cmds.textScrollList('frCrtSdkAttrTSL', q=1, si=1)
    if (allI == None):
        return
    if (selI == None):
        return
    for i in allI:
        cmds.setAttr(faceSdkHandle + '.' + i, 0)

    aSel = []
    for i in selI:
        attr = faceSdkHandle + '.' + i
        maxV = cmds.addAttr(attr, q=1, max=1)
        if (maxV > 0):
            cmds.setAttr(attr, 1)
            aSel.append(i)
    cmds.textScrollList('frCrtSdkAttrTSL', e=1, da=1)
    for i in aSel[:2]:
        cmds.textScrollList('frCrtSdkAttrTSL', e=1, si=i)

    selI = cmds.textScrollList('frCrtSdkAttrTSL', q=1, si=1)
    if (selI == None):
        cmds.button('frCrtNewBSB', e=1, en=0)
    else:
        cmds.button('frCrtNewBSB', e=1, en=1)
    cmds.textScrollList('frCrtBsTSL', e=1, da=1)
    cmds.button('frCtrBsEditB', e=1, en=0)


def sdd_loadBsSdkAttrToList():
    TName = sdd_returnTempNameDirc()
    L_ = TName['L_']
    R_ = TName['R_']

    faceSdkHandle = 'face_sdk_handle'
    if not (cmds.objExists(faceSdkHandle)):
        return
    sdkAttrList = cmds.listAttr(faceSdkHandle, ud=1)
    selI = cmds.textScrollList('frCrtSdkAttrTSL', q=1, si=1)
    cmds.textScrollList('frCrtSdkAttrTSL', e=1, ra=1)
    fl = cmds.checkBox('frCrtSdkFilterLCB', q=1, v=1)
    fr = cmds.checkBox('frCrtSdkFilterRCB', q=1, v=1)

    for attr in sdkAttrList:
        if (attr[:len(L_)] == L_):
            if (fl == 1):
                cmds.textScrollList('frCrtSdkAttrTSL', e=1, a=attr)
        elif (attr[:len(R_)] == R_):
            if (fr == 1):
                cmds.textScrollList('frCrtSdkAttrTSL', e=1, a=attr)
        else:
            cmds.textScrollList('frCrtSdkAttrTSL', e=1, a=attr)

    allI = cmds.textScrollList('frCrtSdkAttrTSL', q=1, ai=1)
    if (selI != None):
        for i in selI:
            if (i in allI):
                cmds.textScrollList('frCrtSdkAttrTSL', e=1, si=i)
    sdd_loadBsToList()


def sdd_getCurrentMeshName():
    faceMesh = cmds.textField('frCurrentMeshTF', q=1, tx=1)
    if (faceMesh == ''):
        sdd_loadCtrAllMeshToList()
    faceMesh = cmds.textField('frCurrentMeshTF', q=1, tx=1)
    if (faceMesh == ''):
        return
    return faceMesh


def sdd_getCtrMeshAnGrpInfo():
    skinMesh = sdd_getCurrentMeshName()
    origMesh = cmds.listConnections(skinMesh + '.origMesh')[0]
    ctrGrp = cmds.listConnections(origMesh + '.ctrGrp')
    if (ctrGrp == None):
        ctrGrp = cmds.getAttr(origMesh + '.ctrGrp')
    else:
        ctrGrp = ctrGrp[0]
    suf = ctrGrp.split('_')[0]
    return skinMesh, origMesh, ctrGrp, suf


def sdd_newCorrectiveBlendShape():
    TName = sdd_returnTempNameDirc()
    _grp = TName['_grp']
    _sdk = TName['_sdk']
    _cnt = TName['_cnt']
    _bs = TName['_bs']
    _bsNode = TName['_bsNode']

    faceBaseGrp = 'face_base_rig_grp'
    faceSdkRigGrp = 'face_sdk_rig_grp'
    if (not cmds.objExists(faceBaseGrp) or not cmds.objExists(faceSdkRigGrp)):
        return
    faceSdkHandle = 'face_sdk_handle'
    if not (cmds.objExists(faceSdkHandle)):
        return
    faceSkinMeshGrp = 'face_skin_mesh_grp'
    if not (cmds.objExists(faceSkinMeshGrp)):
        return
    faceBsGrp = 'face_bs_grp'
    if not (cmds.objExists(faceBsGrp)):
        return
    faceMesh, origMesh, ctrGrp, suf = sdd_getCtrMeshAnGrpInfo()

    allI = cmds.listAttr(faceSdkHandle, ud=1)
    selI = cmds.textScrollList('frCrtSdkAttrTSL', q=1, si=1)
    if (selI == None):
        mm.eval('warning "Please cmds.select one or more sdk Attribute!"')
        return
    baseName = selI[0]
    if (len(selI) > 1):
        baseName += '_%s' % selI[1].split('_')[-1]

    if (sdd_checkCtrMir()):
        result = cmds.promptDialog(t='New Blendshape', m='Enter Blendshape Name:', tx=baseName + _bs + '_' + suf,
                                   b=['OK', 'Cancel'], db='OK', cb='Cancel', ds='Cancel')
    else:
        result = cmds.promptDialog(t='New Blendshape', m='Enter Blendshape Name:', tx=baseName + _bs + '_' + suf,
                                   b=['Mirror', 'Single', 'Cancel'], db='Mirror', cb='Cancel', ds='Cancel')

    if (result == 'Cancel'):
        return
    bsMeshName = cmds.promptDialog(q=1, t=1)
    if (bsMeshName == ''):
        return
    if (cmds.objExists(bsMeshName)):
        mm.eval('warning "Name Repeat!"')
        return

    widthF = cmds.getAttr(faceSkinMeshGrp + '.boxWidthF')
    # current
    bsMeshName = cmds.duplicate(origMesh, n=bsMeshName)[0]
    sdd_frUnLockBaseAttr(bsMeshName)
    if (len(selI) > 1):
        selIdx = allI.index(selI[0])
    else:
        selIdx = allI.index(baseName)
    cmds.setAttr(bsMeshName + '.tx', widthF * selIdx)
    if (len(selI) > 1):
        cmds.setAttr(bsMeshName + '.tz', -widthF * selIdx)
    cmds.parent(bsMeshName, ctrGrp)

    # mirror
    if (sdd_checkCtrMir(result) and sdd_getMirrorName(bsMeshName) != bsMeshName):
        mirBsMesh = sdd_getMirrorName(bsMeshName)
        mirBsMesh = cmds.duplicate(origMesh, n=mirBsMesh)[0]
        sdd_frUnLockBaseAttr(mirBsMesh)
        if (len(selI) > 1):
            selIdx = allI.index(sdd_getMirrorName(selI[0]))
        else:
            selIdx = allI.index(sdd_getMirrorName(baseName))

        cmds.setAttr(mirBsMesh + '.tx', widthF * selIdx)
        if (len(selI) > 1):
            cmds.setAttr(mirBsMesh + '.tz', -widthF * selIdx)

        cmds.parent(mirBsMesh, ctrGrp)

    faceBsNode = suf + '_blendShape'
    if not (cmds.objExists(faceBsNode)):
        if (sdd_checkCtrMir(result) and sdd_getMirrorName(bsMeshName) != bsMeshName):
            cmds.blendShape(bsMeshName, mirBsMesh, faceMesh, foc=1, n=faceBsNode)
        else:
            cmds.blendShape(bsMeshName, faceMesh, foc=1, n=faceBsNode)
    else:
        exId = cmds.getAttr(faceBsNode + '.inputTarget[0].inputTargetGroup', mi=1)
        if (exId == None):
            exId = [-1]
        cmds.blendShape(faceBsNode, e=1, t=(faceMesh, exId[-1] + 1, bsMeshName, 1))
        if (sdd_checkCtrMir(result) and sdd_getMirrorName(bsMeshName) != bsMeshName):
            cmds.blendShape(faceBsNode, e=1, t=(faceMesh, exId[-1] + 2, mirBsMesh, 1))

    # current
    emStr = ''
    for i in selI:
        emStr += ':%s' % i
    emStr = emStr.strip(':')
    cmds.addAttr(bsMeshName, ln='SDK_Attr', at='enum', en=emStr, k=1)

    if (len(selI) == 1):
        cmds.setDrivenKeyframe(faceBsNode + '.' + bsMeshName, cd=faceSdkHandle + '.' + selI[0], v=0, dv=0, itt='linear',
                               ott='linear')
        cmds.setDrivenKeyframe(faceBsNode + '.' + bsMeshName, cd=faceSdkHandle + '.' + selI[0], v=1, dv=1, itt='linear',
                               ott='linear')

    elif (len(selI) == 2):
        condNode = cmds.createNode('condition', n=bsMeshName + '_cond')
        cmds.setAttr(condNode + '.op', 4)
        cmds.connectAttr(faceSdkHandle + '.' + selI[0], condNode + '.ft')
        cmds.connectAttr(faceSdkHandle + '.' + selI[1], condNode + '.st')
        cmds.connectAttr(faceSdkHandle + '.' + selI[0], condNode + '.ctr')
        cmds.connectAttr(faceSdkHandle + '.' + selI[1], condNode + '.cfr')
        cmds.setDrivenKeyframe(faceBsNode + '.' + bsMeshName, cd=condNode + '.ocr', v=0, dv=0, itt='linear',
                               ott='linear')
        cmds.setDrivenKeyframe(faceBsNode + '.' + bsMeshName, cd=condNode + '.ocr', v=1, dv=1, itt='linear',
                               ott='linear')

    # mirror
    if (sdd_checkCtrMir(result) and sdd_getMirrorName(bsMeshName) != bsMeshName):
        emStr = ''
        for i in selI:
            emStr += ':%s' % sdd_getMirrorName(i)
        emStr = emStr.strip(':')
        cmds.addAttr(mirBsMesh, ln='SDK_Attr', at='enum', en=emStr, k=1)

        if (len(selI) == 1):
            cmds.setDrivenKeyframe(faceBsNode + '.' + mirBsMesh, cd=faceSdkHandle + '.' + sdd_getMirrorName(selI[0]),
                                   v=0, dv=0, itt='linear', ott='linear')
            cmds.setDrivenKeyframe(faceBsNode + '.' + mirBsMesh, cd=faceSdkHandle + '.' + sdd_getMirrorName(selI[0]),
                                   v=1, dv=1, itt='linear', ott='linear')

        elif (len(selI) == 2):
            condNode = cmds.createNode('condition', n=mirBsMesh + '_cond')
            cmds.setAttr(condNode + '.op', 4)
            cmds.connectAttr(faceSdkHandle + '.' + sdd_getMirrorName(selI[0]), condNode + '.ft')
            cmds.connectAttr(faceSdkHandle + '.' + sdd_getMirrorName(selI[1]), condNode + '.st')
            cmds.connectAttr(faceSdkHandle + '.' + sdd_getMirrorName(selI[0]), condNode + '.ctr')
            cmds.connectAttr(faceSdkHandle + '.' + sdd_getMirrorName(selI[1]), condNode + '.cfr')

            cmds.setDrivenKeyframe(faceBsNode + '.' + mirBsMesh, cd=condNode + '.ocr', v=0, dv=0, itt='linear',
                                   ott='linear')
            cmds.setDrivenKeyframe(faceBsNode + '.' + mirBsMesh, cd=condNode + '.ocr', v=1, dv=1, itt='linear',
                                   ott='linear')

    sdd_loadBsToList()


def sdd_loadBsToList():
    faceSdkHandle = 'face_sdk_handle'
    if not (cmds.objExists(faceSdkHandle)):
        return
    TName = sdd_returnTempNameDirc()
    L_ = TName['L_']
    R_ = TName['R_']

    cmds.textScrollList('frCrtBsTSL', e=1, ra=1)
    faceMesh, origMesh, ctrGrp, suf = sdd_getCtrMeshAnGrpInfo()

    faceBsGrp = ctrGrp
    if not (cmds.objExists(faceBsGrp)):
        return
    bsList = cmds.listRelatives(faceBsGrp, c=1)
    fl = cmds.checkBox('frCrtSdkFilterLCB', q=1, v=1)
    fr = cmds.checkBox('frCrtSdkFilterRCB', q=1, v=1)
    if (bsList == None):
        return
    for i in bsList:
        if (i[:len(L_)] == L_):
            if (fl == 1):
                cmds.textScrollList('frCrtBsTSL', e=1, a=i)
        elif (i[:len(R_)] == R_):
            if (fr == 1):
                cmds.textScrollList('frCrtBsTSL', e=1, a=i)
        else:
            cmds.textScrollList('frCrtBsTSL', e=1, a=i)
    cmds.button('frCtrBsEditB', e=1, en=0)


def sdd_bsSdkBsListSelectChange():
    selI = cmds.textScrollList('frCrtBsTSL', q=1, si=1)
    if (selI == None):
        return
    selI = selI[0]
    faceSdkHandle = 'face_sdk_handle'
    if not (cmds.objExists(faceSdkHandle)):
        return
    allI = cmds.listAttr(faceSdkHandle, ud=1)
    for i in allI:
        cmds.setAttr(faceSdkHandle + '.' + i, 0)

    emStr = cmds.addAttr(selI + '.SDK_Attr', q=1, en=1)
    cnnList = emStr.split(':')
    cmds.textScrollList('frCrtSdkAttrTSL', e=1, da=1)
    allListI = cmds.textScrollList('frCrtSdkAttrTSL', q=1, ai=1)

    for i in cnnList:
        if (i in allI):
            print i
            cmds.setAttr(faceSdkHandle + '.' + i, 1.0)
        if (i in allListI):
            cmds.textScrollList('frCrtSdkAttrTSL', e=1, si=i)
    cmds.button('frCtrBsEditB', e=1, en=1)


def sdd_deleteCorrectiveBS():
    ret = cmds.confirmDialog(t='Delete Blendshape', m='Delete This ?', b=['This', 'This And Mirror', 'Cancel'],
                             db='Cancel', cb='Cancel', ds='Cancel')
    if (ret == 'Cancel'):
        return
    selI = cmds.textScrollList('frCrtBsTSL', q=1, si=1)
    if (selI == None):
        return

    faceMesh, origMesh, ctrGrp, suf = sdd_getCtrMeshAnGrpInfo()
    faceBsNode = suf + '_blendShape'

    if (cmds.objExists(selI[0])):
        if not (cmds.objExists(faceBsNode)):
            return
        cmds.blendShape(faceBsNode, e=1, tc=0, rm=1, t=[faceMesh, 1, selI[0], 1])
        cmds.delete(selI[0])
    if (ret == 'This And Mirror'):
        try:
            faceMesh = sdd_getMirrorName(faceMesh)
            if (cmds.objExists(sdd_getMirrorName(selI[0]))):
                if not (cmds.objExists(faceBsNode)):
                    return
                cmds.blendShape(faceBsNode, e=1, tc=0, rm=1, t=[faceMesh, 1, sdd_getMirrorName(selI[0]), 1])
                cmds.delete(sdd_getMirrorName(selI[0]))
        except:
            pass

    sdd_loadBsToList()


# redefine sdk ____________________________________________________________________________________====

def sdd_sdkCntListSelectChange():
    TName = sdd_returnTempNameDirc()
    _cnt = TName['_cnt']
    selI = cmds.textScrollList('frSdkCntTSL', q=1, si=1)
    if (selI == None):
        return
    cmds.select(cl=1)
    for i in selI:
        cmds.select(i + _cnt, add=1)


def sdd_sdkAttrListSelectChange():
    TName = sdd_returnTempNameDirc()
    _sdk = TName['_sdk']
    _grp = TName['_grp']
    _cnt = TName['_cnt']

    faceSdkHandle = 'face_sdk_handle'
    if not (cmds.objExists(faceSdkHandle)):
        return

    allI = cmds.listAttr(faceSdkHandle, ud=1)
    selI = cmds.textScrollList('frSdkAttrTSL', q=1, si=1)
    cmds.button('frSdkRedefineB', e=1, en=0)
    # keyValue
    kValue = sdd_getSdkKeyValue()

    if (allI == None):
        return
    if (selI == None):
        return
    for i in allI:
        cmds.setAttr(faceSdkHandle + '.' + i, 0)

    cmds.textScrollList('frSdkCntTSL', e=1, ra=1)
    sdd_setAttrSdkValue()
    if (len(selI) > 1):
        return

    objList = sdd_returnAllSdkCntList()
    for i in objList:
        sdk = i + _sdk
        cnt = i + _cnt
        sdkList = cmds.setDrivenKeyframe(sdk, q=1, dr=1)
        if (sdkList[0] == 'No drivers.'):
            continue
        for s in sdkList:
            if (s.split('.')[-1] == selI[0]):
                cmds.textScrollList('frSdkCntTSL', e=1, a=i)
                break


def sdd_setAttrSdkValue():
    faceSdkHandle = 'face_sdk_handle'
    if not (cmds.objExists(faceSdkHandle)):
        return
    selI = cmds.textScrollList('frSdkAttrTSL', q=1, si=1)
    if (selI == None):
        return
    kValue = sdd_getSdkKeyValue()
    for i in selI:
        attr = faceSdkHandle + '.' + i
        maxV = cmds.addAttr(attr, q=1, max=1)
        if (maxV > 0):
            cmds.setAttr(attr, kValue)

    if (len(selI) == 1):
        cmds.button('frSdkRedefineB', e=1, en=1)
    else:
        cmds.button('frSdkRedefineB', e=1, en=0)
    if (kValue == 0 or maxV == 0):
        cmds.button('frSdkRedefineB', e=1, en=0)


def sdd_getSdkKeyValue():
    value = 0
    if (cmds.iconTextRadioButton('frSdkKeyV5IRB', q=1, sl=1)):
        value = 0.5
    if (cmds.iconTextRadioButton('frSdkKeyV10IRB', q=1, sl=1)):
        value = 1
    return value


def sdd_deleteMoveSdkObj():
    ret = cmds.confirmDialog(t='Delete Keys', m='Are you sure ?', b=['Yes', 'No'], db='No', cb='No', ds='No')
    if (ret == 'No'):
        return
    TName = sdd_returnTempNameDirc()
    _sdk = TName['_sdk']
    _cnt = TName['_cnt']
    selI = cmds.textScrollList('frSdkCntTSL', q=1, si=1)
    cdAttr = cmds.textScrollList('frSdkAttrTSL', q=1, si=1)
    faceSdkHandle = 'face_sdk_handle'

    if (selI == None or cdAttr == None):
        return
    cdAttr = cdAttr[0]
    sdkTypeList = ['animCurveUA', 'animCurveUL', 'animCurveUT', 'animCurveUU']
    for i in selI:
        sdk = i + _sdk
        cnt = i + _cnt
        nodeList = cmds.listConnections(sdk, d=0, scn=1)
        sdkNodeList = []
        for node in nodeList:
            if (cmds.objectType(node) in sdkTypeList):
                sdkNodeList.append(node)
            elif (cmds.objectType(node) == 'blendWeighted'):
                exNodeList = cmds.listConnections(node, d=0, scn=1)
                sdkNodeList.extend(exNodeList)
        drNodeList = cmds.listConnections(faceSdkHandle + '.' + cdAttr, scn=1)
        delList = []
        for dr in drNodeList:
            if (dr in sdkNodeList):
                delList.append(dr)
        cmds.delete(delList)
        attrList = ['tx', 'ty', 'tz', 'rx', 'ry', 'rz', 'sx', 'sy', 'sz']
        valueList = [0, 0, 0, 0, 0, 0, 1, 1, 1]
        for idx in range(len(attrList)):
            cmds.setAttr(sdk + '.' + attrList[idx], valueList[idx])
            cmds.setAttr(cnt + '.' + attrList[idx], valueList[idx])
    sdd_sdkAttrListSelectChange()


def sdd_sdkRedefine():
    TName = sdd_returnTempNameDirc()
    _sdk = TName['_sdk']
    _cnt = TName['_cnt']
    _root = TName['_root']

    faceSdkHandle = 'face_sdk_handle'
    if not (cmds.objExists(faceSdkHandle)):
        return

    sdd_checkMoveCntList()
    sdkCntList = cmds.textScrollList('frSdkCntTSL', q=1, ai=1)
    if (sdkCntList == None):
        return
    curAttr = cmds.textScrollList('frSdkAttrTSL', q=1, si=1)
    allAttrList = cmds.listAttr(faceSdkHandle, ud=1)
    if (curAttr == None):
        return
    if (len(curAttr) > 1):
        cmds.textScrollList('frSdkAttrTSL', e=1, da=1)
        return
    curAttr = curAttr[0]

    attrList = ['tx', 'ty', 'tz', 'rx', 'ry', 'rz', 'sx', 'sy', 'sz']
    valueList = [0, 0, 0, 0, 0, 0, 1, 1, 1]
    mirList = [-1, 1, 1, 1, -1, -1, 1, 1, 1]
    mir = cmds.checkBox('frSdkMirrorCB', q=1, v=1)

    # keyValue
    kValue = sdd_getSdkKeyValue()
    if (kValue == 0):
        return

    for i in sdkCntList:
        cnt = i + _cnt
        sdk = i + _sdk
        pCnt = cmds.listRelatives(sdk, p=1)[0]
        if (cmds.objExists(cnt + '_offset_grp')):
            cmds.delete(cnt + '_offset_grp')
        tmpOffGrp = cmds.group(n=cnt + '_offset_grp', em=1)
        cmds.parent(tmpOffGrp, pCnt)
        cmds.delete(cmds.parentConstraint(cnt, tmpOffGrp))
        for a in range(len(attrList)):
            val = cmds.getAttr(tmpOffGrp + '.' + attrList[a])
            cmds.setAttr(cnt + '.' + attrList[a], valueList[a])

            attr = sdk + '.' + attrList[a]
            cdAttr = faceSdkHandle + '.' + curAttr
            animNode = sdd_getSDKAnimCurveNode(attr, cdAttr)

            if (round(val, 4) == valueList[a] and animNode == None):
                continue
            print animNode

            cmds.setDrivenKeyframe(attr, cd=cdAttr, v=0, dv=0, itt='linear', ott='linear')
            cmds.setDrivenKeyframe(attr, cd=cdAttr, v=val, dv=kValue, itt='linear', ott='linear')
            if (animNode == None):
                cmds.setDrivenKeyframe(attr, cd=cdAttr, v=0, dv=1, itt='linear', ott='linear')

            cmds.setAttr(cdAttr, kValue)
            # __________________
            if (not mir):
                continue
            # mirror
            mirSdk = sdd_getMirrorName(sdk)
            if (not cmds.objExists(mirSdk)):
                continue
            mirAttr = sdd_getMirrorName(curAttr)
            if (not (mirAttr in allAttrList) or mirAttr == curAttr):
                continue

            attr = mirSdk + '.' + attrList[a]
            cdAttr = faceSdkHandle + '.' + mirAttr
            animNode = sdd_getSDKAnimCurveNode(attr, cdAttr)

            cmds.setDrivenKeyframe(attr, cd=cdAttr, v=0, dv=0, itt='linear', ott='linear')
            cmds.setDrivenKeyframe(attr, cd=cdAttr, v=val * mirList[a], dv=kValue, itt='linear', ott='linear')
            if (animNode == None):
                cmds.setDrivenKeyframe(attr, cd=cdAttr, v=0, dv=1, itt='linear', ott='linear')

        cmds.delete(tmpOffGrp)


def sdd_scaleSdkKeys(typ):
    TName = sdd_returnTempNameDirc()
    _sdk = TName['_sdk']
    _cnt = TName['_cnt']
    _root = TName['_root']
    sVal = cmds.intField('frScaleSdkIF', q=1, v=1)
    sVal = sVal / 100.0
    if (typ == '+'):
        sVal = (1 - sVal) + 1
    print typ == '+'
    print sVal

    sdd_checkMoveCntList()
    sdkCntList = cmds.textScrollList('frSdkCntTSL', q=1, ai=1)
    if (sdkCntList == None):
        return
    curAttr = cmds.textScrollList('frSdkAttrTSL', q=1, si=1)
    if (len(curAttr) > 1):
        cmds.textScrollList('frSdkAttrTSL', e=1, da=1)
        return
    curAttr = curAttr[0]

    attrList = ['tx', 'ty', 'tz', 'rx', 'ry', 'rz', 'sx', 'sy', 'sz']
    valueList = [0, 0, 0, 0, 0, 0, 1, 1, 1]

    for i in sdkCntList:
        cnt = i + _cnt
        sdk = i + _sdk
        for j in range(len(attrList)):
            val = cmds.getAttr(cnt + '.' + attrList[j])
            dVal = valueList[j]
            if (val != dVal):
                cmds.setAttr(cnt + '.' + attrList[j], sVal * val)

            val = cmds.getAttr(sdk + '.' + attrList[j])
            if (val != dVal):
                cmds.setAttr(sdk + '.' + attrList[j], sVal * val)


def sdd_getSDKAnimCurveNode(attr, cdAttr):
    nodeList = cmds.listConnections(attr, s=1, d=0, scn=1)
    if (nodeList == None):
        return
    sdkTypeList = ['animCurveUA', 'animCurveUL', 'animCurveUT', 'animCurveUU']
    animNodeList = []
    if (cmds.objectType(nodeList[0]) in sdkTypeList):
        animNodeList.append(nodeList[0])
    elif (cmds.objectType(nodeList[0]) == 'blendWeighted'):
        cnnList = cmds.listConnections(nodeList[0] + '.i', s=1, d=0, scn=1)
        animNodeList.extend(cnnList)
    for i in animNodeList:
        cnn = cmds.listConnections(i + '.i', scn=1, s=1, d=0, p=1)
        if (cnn == None):
            return
        elif (cnn[0] == cdAttr):
            return i
    return


def sdd_getMirrorName(sdk):
    TName = sdd_returnTempNameDirc()
    L_ = TName['L_']
    R_ = TName['R_']
    if (sdk[:len(L_)] == L_):
        mirObj = R_ + sdk[len(L_):]
        return mirObj
    elif (sdk[:len(R_)] == R_):
        mirObj = L_ + sdk[len(R_):]
        return mirObj
    else:
        return sdk


def sdd_mirrorSdkCntPos(typ):
    TName = sdd_returnTempNameDirc()
    L_ = TName['L_']
    R_ = TName['R_']
    _sdk = TName['_sdk']
    _cnt = TName['_cnt']

    allCntList = sdd_returnAllSdkCntList()
    if (allCntList == None or len(allCntList) == 0):
        return
    attrList = ['tx', 'ty', 'tz', 'rx', 'ry', 'rz', 'sx', 'sy', 'sz']
    valueList = [0, 0, 0, 0, 0, 0, 1, 1, 1]
    mirList = [-1, 1, 1, 1, -1, -1, 1, 1, 1]
    for i in allCntList:
        cnt = i + _cnt
        sdk = i + _sdk
        if (typ == 'L>>R'):
            if (cnt[:len(R_)] != R_):
                continue
        elif (typ == 'L<<R'):
            if (cnt[:len(L_)] != L_):
                continue
        else:
            # zero
            for idx in range(len(attrList)):
                try:
                    cmds.setAttr(cnt + '.' + attrList[idx], valueList[idx])
                    cmds.setAttr(sdk + '.' + attrList[idx], valueList[idx])
                except:
                    pass
            continue
        mirCnt = sdd_getMirrorName(cnt)

        if cnt == mirCnt or not (cmds.objExists(cnt)) or not (cmds.objExists(mirCnt)):
            continue

        for idx in range(len(attrList)):
            val = cmds.getAttr(cnt + '.' + attrList[idx])
            cmds.setAttr(mirCnt + '.' + attrList[idx], val * mirList[idx])


def sdd_newSdkAttr():
    faceSdkHandle = 'face_sdk_handle'
    if not (cmds.objExists(faceSdkHandle)):
        return
    result = cmds.promptDialog(t='New Attribute', m='Enter Attribute Name:', b=['Ok', 'Cancel'], db='Ok', cb='Cancel',
                               ds='Cancel')
    if (result == 'Cancel'):
        return
    attrName = cmds.promptDialog(q=1, t=1)
    if (attrName == ''):
        return
    cmds.addAttr(faceSdkHandle, ln=attrName, at='double', min=0, max=1, k=1)
    sdd_loadSdkAttrToList()


def sdd_checkMoveCntList():
    TName = sdd_returnTempNameDirc()
    _cnt = TName['_cnt']
    _sdk = TName['_sdk']
    faceSdkHandle = 'face_sdk_handle'

    cmds.textScrollList('frSdkCntTSL', e=1, ra=1)
    allCntList = sdd_returnAllSdkCntList()
    if (len(allCntList) == 0):
        return
    curAttr = cmds.textScrollList('frSdkAttrTSL', q=1, si=1)
    if (len(curAttr) > 1):
        cmds.textScrollList('frSdkAttrTSL', e=1, da=1)
        return
    curAttr = curAttr[0]

    attrList = ['tx', 'ty', 'tz', 'rx', 'ry', 'rz', 'sx', 'sy', 'sz']
    valueList = [0, 0, 0, 0, 0, 0, 1, 1, 1]
    for i in allCntList:
        cnt = i + _cnt
        sdk = i + _sdk
        isMove = 0
        for idx in range(len(attrList)):
            val1 = cmds.getAttr(cnt + '.' + attrList[idx])
            val2 = cmds.getAttr(sdk + '.' + attrList[idx])
            val = (abs(val1) + abs(val2)) * 0.5

            attr = sdk + '.' + attrList[idx]
            cdAttr = faceSdkHandle + '.' + curAttr
            animNode = sdd_getSDKAnimCurveNode(attr, cdAttr)

            if (round(val, 4) != valueList[idx] or animNode != None):
                isMove = 1
                break
        if (isMove):
            cmds.textScrollList('frSdkCntTSL', e=1, a=i)


def sdd_returnAllSdkCntList():
    TName = sdd_returnTempNameDirc()
    _cnt = TName['_cnt']
    _sdk = TName['_sdk']
    _rig = TName['_rig']

    faceSdkRigGrp = 'face_sdk_rig_grp'
    if not (cmds.objExists(faceSdkRigGrp)):
        return
    allChildList = cmds.listRelatives(faceSdkRigGrp, c=1, ad=1)

    sdkCntList = []
    for i in allChildList:
        if (i[-len(_cnt):] == _cnt):
            baseName = i[:-len(_cnt)]
            if (cmds.objExists(baseName + _sdk)):
                sdkCntList.append(baseName)
                # and cmds.objExists(baseName+_rig)
    return sdkCntList


def sdd_sdkEditModel():
    sdd_loadSdkAttrToList()


def sdd_loadSdkAttrToList():
    TName = sdd_returnTempNameDirc()
    L_ = TName['L_']
    R_ = TName['R_']

    faceSdkHandle = 'face_sdk_handle'
    if not (cmds.objExists(faceSdkHandle)):
        return
    selI = cmds.textScrollList('frSdkAttrTSL', q=1, si=1)

    cmds.textScrollList('frSdkAttrTSL', e=1, ra=1)
    sdkAttrList = cmds.listAttr(faceSdkHandle, ud=1)
    fl = cmds.checkBox('frSdkFilterLCB', q=1, v=1)
    fr = cmds.checkBox('frSdkFilterRCB', q=1, v=1)

    for i in sdkAttrList:
        if (i[:len(L_)] == L_):
            if (fl == 1):
                cmds.textScrollList('frSdkAttrTSL', e=1, a=i)
        elif (i[:len(R_)] == R_):
            if (fr == 1):
                cmds.textScrollList('frSdkAttrTSL', e=1, a=i)
        else:
            cmds.textScrollList('frSdkAttrTSL', e=1, a=i)

    allI = cmds.textScrollList('frSdkAttrTSL', q=1, ai=1)
    if (selI != None):
        for i in selI:
            if (i in allI):
                cmds.textScrollList('frSdkAttrTSL', e=1, si=i)


# sdk cmds.joint rigging____________________________________________________________________________________====



def sdd_createSdkJointRigging():
    faceSdkSkinGrp = 'face_sdk_skin_grp'
    if not (cmds.objExists(faceSdkSkinGrp)):
        return
    faceCur = 'faceMoveCur'
    faceBaseGrp = 'face_base_rig_grp'
    if (not cmds.objExists(faceBaseGrp)):
        return
    faceBsGrp = 'face_bs_grp'
    if not (cmds.objExists(faceBsGrp)):
        faceBsGrp = cmds.group(em=1, n=faceBsGrp)
        cmds.setAttr(faceBsGrp + '.it', 0)
        cmds.parent(faceBsGrp, faceBaseGrp)
    faceAnimCtrlGrp = 'face_anim_ctrl_grp'
    if not (cmds.objExists(faceAnimCtrlGrp)):
        faceAnimCtrlGrp = cmds.group(em=1, n=faceAnimCtrlGrp)
        cmds.parent(faceAnimCtrlGrp, faceCur)

    faceMesh = cmds.textField('frFaceMeshTF', q=1, tx=1)
    if (faceMesh == '' or not cmds.objExists(faceMesh)):
        return

    faceSdkRigGrp = 'face_sdk_rig_grp'
    if cmds.objExists(faceSdkRigGrp):
        return

    faceMeshGrp = 'face_mesh_grp'
    if not (cmds.objExists(faceMeshGrp)):
        faceMeshGrp = cmds.group(n=faceMeshGrp, em=1)
        cmds.setAttr(faceMeshGrp + '.it', 0)
        cmds.parent(faceMeshGrp, faceCur)

    faceSkinMeshGrp = 'face_skin_mesh_grp'
    if not (cmds.objExists(faceSkinMeshGrp)):
        faceSkinMeshGrp = cmds.group(n=faceSkinMeshGrp, em=1)
        cmds.addAttr(faceSkinMeshGrp, ln='faceMesh', at='bool', dv=1, k=1)
        cmds.addAttr(faceSkinMeshGrp, ln='boxWidthF', at='float')
        cmds.addAttr(faceSkinMeshGrp, ln='boxWidthS', at='float')
        cmds.setAttr(faceSkinMeshGrp + '.boxWidthF', cb=1)
        cmds.setAttr(faceSkinMeshGrp + '.boxWidthS', cb=1)
        cmds.parent(faceSkinMeshGrp, faceMeshGrp)
        cmds.setAttr(faceSkinMeshGrp + '.it', 0)

    meshList = cmds.textScrollList('frFaceMeshTSL', q=1, ai=1)
    for i in meshList:
        sdd_tryParent(i, faceSkinMeshGrp)

    bbox = sdd_getBoundingBox(faceSkinMeshGrp)
    cmds.setAttr(faceSkinMeshGrp + '.boxWidthF', bbox[0])
    cmds.setAttr(faceSkinMeshGrp + '.boxWidthS', bbox[1])

    faceOrigMeshGrp = 'face_orig_mesh_grp'
    if cmds.objExists(faceOrigMeshGrp):
        cmds.delete(faceOrigMeshGrp)
    faceOrigMeshGrp = cmds.group(em=1, n=faceOrigMeshGrp)
    cmds.parent(faceOrigMeshGrp, faceBsGrp)
    cmds.setAttr(faceOrigMeshGrp + '.v', 0)

    sdd_connectAttrForce(faceMesh + '.msg', faceSkinMeshGrp + '.faceMesh')
    allMesh = cmds.textScrollList('frFaceMeshTSL', q=1, ai=1)

    for i in range(len(allMesh)):
        origMeshName = allMesh[i] + '_OrigMesh'
        origMeshName = cmds.duplicate(allMesh[i], n=origMeshName)[0]
        sdd_tryParent(origMeshName, faceOrigMeshGrp)
        iOrigAttr = sdd_tryAddMessageAttr(allMesh[i], 'origMesh')
        nOrigAttr = sdd_tryAddMessageAttr(origMeshName, 'origMesh')
        sdd_connectAttrForce(nOrigAttr, iOrigAttr)

        ctrGrp = chr(65 + i) + '_CorrectiveGrp'
        nCtrAttr = sdd_tryAddMessageAttr(origMeshName, 'ctrGrp')
        cmds.setAttr(nCtrAttr, ctrGrp, typ='string')

    sdd_createSdkJntRig()
    sdd_initDistanceAttr()
    sdd_createDefultSdk()

    faceJntList = cmds.listRelatives(faceSdkSkinGrp, c=1, ad=1, typ='joint')
    for i in allMesh:
        cmds.skinCluster(faceJntList, i, mi=1, nw=1, tsb=1)
    cmds.textField('frCurrentMeshTF', e=1, tx='')

    sdd_importAndConnectPanel()
    if (cmds.objExists('Face_Panel_grp')):
        cmds.parent('Face_Panel_grp', faceAnimCtrlGrp)

    sdd_reloadFaceMeshInfo()


def sdd_tryAddMessageAttr(i, attr):
    attrList = cmds.listAttr(i, ud=1)
    if (attrList == None or not (attr in attrList)):
        cmds.addAttr(i, ln=attr, dt='string')
    return i + '.' + attr


def sdd_importAndConnectPanel():
    global frRootPath
    T = sdd_returnTempNameDirc()
    FR, FRJntPos, FRUIPos = sdd_frTNameDirc()
    _root = T['_root']
    _sdk = T['_sdk']
    _cnt = T['_cnt']
    _grp = T['_grp']

    cmds.file(frRootPath + 'files/facePanel.ma', i=1, type="mayaAscii")
    faceCur = 'faceMoveCur'
    panelGrp = 'Face_Panel_grp'
    cmds.delete(cmds.parentConstraint(faceCur, panelGrp))
    bbox = sdd_getBoundingBox(faceCur)
    cmds.setAttr(panelGrp + '.tx', bbox[0])

    sdd_connectPanelAttr('M_brow_U', 'Face_M_brow_anim.ty', 1)
    sdd_connectPanelAttr('M_brow_D', 'Face_M_brow_anim.ty', -1)
    sdd_connectPanelAttr('L_brow_In_U', 'Face_L_brow_a_anim.ty', 1)
    sdd_connectPanelAttr('L_brow_In_D', 'Face_L_brow_a_anim.ty', -1)
    sdd_connectPanelAttr('L_brow_In_In', 'Face_L_brow_a_anim.tx', 1)
    sdd_connectPanelAttr('L_brow_Out_U', 'Face_L_brow_b_anim.ty', 1)
    sdd_connectPanelAttr('L_brow_Out_D', 'Face_L_brow_b_anim.ty', -1)

    sdd_connectPanelAttr('R_brow_In_U', 'Face_R_brow_a_anim.ty', 1)
    sdd_connectPanelAttr('R_brow_In_D', 'Face_R_brow_a_anim.ty', -1)
    sdd_connectPanelAttr('R_brow_In_In', 'Face_R_brow_a_anim.tx', 1)
    sdd_connectPanelAttr('R_brow_Out_U', 'Face_R_brow_b_anim.ty', 1)
    sdd_connectPanelAttr('R_brow_Out_D', 'Face_R_brow_b_anim.ty', -1)

    sdd_connectPanelAttr('L_brow_Mid_U', 'Face_L_brow_b_anim.rz', -15)
    sdd_connectPanelAttr('L_brow_Mid_D', 'Face_L_brow_b_anim.rz', 15)

    sdd_connectPanelAttr('R_brow_Mid_U', 'Face_R_brow_b_anim.rz', 15)
    sdd_connectPanelAttr('R_brow_Mid_D', 'Face_R_brow_b_anim.rz', -15)

    sdd_connectPanelAttr('L_eyelid_Up_U', 'Face_L_eyelid_Up_anim.ty', 1)
    sdd_connectPanelAttr('L_eyelid_Up_D', 'Face_L_eyelid_Up_anim.ty', -1)
    sdd_connectPanelAttr('L_eyelid_Dn_U', 'Face_L_eyelid_Dn_anim.ty', -1)
    sdd_connectPanelAttr('L_eyelid_Dn_D', 'Face_L_eyelid_Dn_anim.ty', 1)

    sdd_connectPanelAttr('R_eyelid_Up_U', 'Face_R_eyelid_Up_anim.ty', 1)
    sdd_connectPanelAttr('R_eyelid_Up_D', 'Face_R_eyelid_Up_anim.ty', -1)
    sdd_connectPanelAttr('R_eyelid_Dn_U', 'Face_R_eyelid_Dn_anim.ty', -1)
    sdd_connectPanelAttr('R_eyelid_Dn_D', 'Face_R_eyelid_Dn_anim.ty', 1)

    sdd_connectPanelAttr('L_eyelid_close', 'Face_L_eyelid_close_anim.ty', -1)
    sdd_connectPanelAttr('R_eyelid_close', 'Face_R_eyelid_close_anim.ty', -1)

    sdd_connectPanelAttr('L_eyelid_Squint', 'Face_L_squint_anim.tx', -1)
    sdd_connectPanelAttr('R_eyelid_Squint', 'Face_R_squint_anim.tx', -1)

    sdd_connectPanelAttr('L_eyelid_Up_side_O', 'Face_L_eyelid_Up_anim.tx', 1)
    sdd_connectPanelAttr('L_eyelid_Up_side_I', 'Face_L_eyelid_Up_anim.tx', -1)
    sdd_connectPanelAttr('L_eyelid_Dn_side_I', 'Face_L_eyelid_Dn_anim.tx', -1)
    sdd_connectPanelAttr('L_eyelid_Dn_side_O', 'Face_L_eyelid_Dn_anim.tx', 1)

    sdd_connectPanelAttr('R_eyelid_Up_side_O', 'Face_R_eyelid_Up_anim.tx', 1)
    sdd_connectPanelAttr('R_eyelid_Up_side_I', 'Face_R_eyelid_Up_anim.tx', -1)
    sdd_connectPanelAttr('R_eyelid_Dn_side_I', 'Face_R_eyelid_Dn_anim.tx', -1)
    sdd_connectPanelAttr('R_eyelid_Dn_side_O', 'Face_R_eyelid_Dn_anim.tx', 1)

    sdd_connectPanelAttr('L_mouth_corner_O', 'Face_L_mouth_anim.txLink', 1)
    sdd_connectPanelAttr('L_mouth_corner_I', 'Face_L_mouth_anim.txLink', -1)
    sdd_connectPanelAttr('L_mouth_corner_U', 'Face_L_mouth_anim.tyLink', 1)
    sdd_connectPanelAttr('L_mouth_corner_D', 'Face_L_mouth_anim.tyLink', -1)

    sdd_connectPanelAttr('R_mouth_corner_O', 'Face_R_mouth_anim.txLink', 1)
    sdd_connectPanelAttr('R_mouth_corner_I', 'Face_R_mouth_anim.txLink', -1)
    sdd_connectPanelAttr('R_mouth_corner_U', 'Face_R_mouth_anim.tyLink', 1)
    sdd_connectPanelAttr('R_mouth_corner_D', 'Face_R_mouth_anim.tyLink', -1)

    sdd_connectPanelAttr('L_mouth_Up_U', 'Face_L_lip_side_Up_anim.ty', 1)
    sdd_connectPanelAttr('L_mouth_Up_D', 'Face_L_lip_side_Up_anim.ty', -1)
    sdd_connectPanelAttr('L_mouth_Dn_U', 'Face_L_lip_side_Dn_anim.ty', 1)
    sdd_connectPanelAttr('L_mouth_Dn_D', 'Face_L_lip_side_Dn_anim.ty', -1)

    sdd_connectPanelAttr('R_mouth_Up_U', 'Face_R_lip_side_Up_anim.ty', 1)
    sdd_connectPanelAttr('R_mouth_Up_D', 'Face_R_lip_side_Up_anim.ty', -1)
    sdd_connectPanelAttr('R_mouth_Dn_U', 'Face_R_lip_side_Dn_anim.ty', 1)
    sdd_connectPanelAttr('R_mouth_Dn_D', 'Face_R_lip_side_Dn_anim.ty', -1)

    sdd_connectPanelAttr('mouth_Up_roll_O', 'Face_lip_roll_Up_anim.ty', 1)
    sdd_connectPanelAttr('mouth_Up_roll_I', 'Face_lip_roll_Up_anim.ty', -1)
    sdd_connectPanelAttr('mouth_Dn_roll_O', 'Face_lip_roll_Dn_anim.ty', 1)
    sdd_connectPanelAttr('mouth_Dn_roll_I', 'Face_lip_roll_Dn_anim.ty', -1)

    sdd_connectPanelAttr('mouth_A', 'Face_L_mouth_A_anim.tx', 1)
    sdd_connectPanelAttr('mouth_E', 'Face_L_mouth_E_anim.tx', 1)
    sdd_connectPanelAttr('mouth_F', 'Face_L_mouth_F_anim.tx', 1)
    sdd_connectPanelAttr('mouth_H', 'Face_L_mouth_H_anim.tx', 1)
    sdd_connectPanelAttr('mouth_M', 'Face_L_mouth_M_anim.tx', 1)
    sdd_connectPanelAttr('mouth_O', 'Face_L_mouth_O_anim.tx', 1)
    sdd_connectPanelAttr('mouth_U', 'Face_L_mouth_U_anim.tx', 1)

    sdd_connectPanelAttr('L_eyeBall_U', 'Face_L_eye_anim.ty', 1)
    sdd_connectPanelAttr('L_eyeBall_D', 'Face_L_eye_anim.ty', -1)
    sdd_connectPanelAttr('L_eyeBall_O', 'Face_L_eye_anim.tx', 1)
    sdd_connectPanelAttr('L_eyeBall_I', 'Face_L_eye_anim.tx', -1)

    sdd_connectPanelAttr('R_eyeBall_U', 'Face_R_eye_anim.ty', 1)
    sdd_connectPanelAttr('R_eyeBall_D', 'Face_R_eye_anim.ty', -1)
    sdd_connectPanelAttr('R_eyeBall_I', 'Face_R_eye_anim.tx', 1)
    sdd_connectPanelAttr('R_eyeBall_O', 'Face_R_eye_anim.tx', -1)

    sdd_connectPanelAttr('L_eyeAll_U', 'Face_L_eye_all_anim.ty', 1)
    sdd_connectPanelAttr('L_eyeAll_D', 'Face_L_eye_all_anim.ty', -1)
    sdd_connectPanelAttr('L_eyeAll_O', 'Face_L_eye_all_anim.tx', 1)
    sdd_connectPanelAttr('L_eyeAll_I', 'Face_L_eye_all_anim.tx', -1)

    cmds.connectAttr('Face_L_eye_all_anim.sx', FR['L_eye_root'] + _sdk + '.sx')
    cmds.connectAttr('Face_L_eye_all_anim.sy', FR['L_eye_root'] + _sdk + '.sy')

    sdd_connectPanelAttr('R_eyeAll_U', 'Face_R_eye_all_anim.ty', 1)
    sdd_connectPanelAttr('R_eyeAll_D', 'Face_R_eye_all_anim.ty', -1)
    sdd_connectPanelAttr('R_eyeAll_O', 'Face_R_eye_all_anim.tx', 1)
    sdd_connectPanelAttr('R_eyeAll_I', 'Face_R_eye_all_anim.tx', -1)
    cmds.connectAttr('Face_R_eye_all_anim.sx', FR['R_eye_root'] + _sdk + '.sx')
    cmds.connectAttr('Face_R_eye_all_anim.sy', FR['R_eye_root'] + _sdk + '.sy')

    cmds.connectAttr('Face_mouth_all_anim.sx', FR['jaw'] + _root + _sdk + '.sx')
    cmds.connectAttr('Face_mouth_all_anim.sy', FR['jaw'] + _root + _sdk + '.sy')

    cmds.connectAttr('Face_jaw_anim.jawTranslateX', FR['jaw'] + _grp + '.tx')
    cmds.connectAttr('Face_jaw_anim.jawTranslateY', FR['jaw'] + _grp + '.ty')
    cmds.connectAttr('Face_jaw_anim.jawTranslateZ', FR['jaw'] + _grp + '.tz')

    sdd_connectPanelAttr('M_nose_U', 'Face_nose_anim.ty', 1)
    sdd_connectPanelAttr('M_nose_D', 'Face_nose_anim.ty', -1)
    sdd_connectPanelAttr('M_nose_L', 'Face_nose_anim.tx', 1)
    sdd_connectPanelAttr('M_nose_R', 'Face_nose_anim.tx', -1)

    sdd_connectPanelAttr('L_nose_U', 'Face_L_nose_anim.ty', 1)
    sdd_connectPanelAttr('L_nose_D', 'Face_L_nose_anim.ty', -1)
    sdd_connectPanelAttr('L_nose_O', 'Face_L_nose_anim.tx', 1)
    sdd_connectPanelAttr('L_nose_I', 'Face_L_nose_anim.tx', -1)

    sdd_connectPanelAttr('R_nose_U', 'Face_R_nose_anim.ty', 1)
    sdd_connectPanelAttr('R_nose_D', 'Face_R_nose_anim.ty', -1)
    sdd_connectPanelAttr('R_nose_O', 'Face_R_nose_anim.tx', 1)
    sdd_connectPanelAttr('R_nose_I', 'Face_R_nose_anim.tx', -1)

    sdd_connectPanelAttr('L_cheek_U', 'Face_L_cheek_anim.ty', 1)
    sdd_connectPanelAttr('L_cheek_O', 'Face_L_cheek_anim.tx', 1)
    sdd_connectPanelAttr('L_cheek_I', 'Face_L_cheek_anim.tx', -1)

    sdd_connectPanelAttr('R_cheek_U', 'Face_R_cheek_anim.ty', 1)
    sdd_connectPanelAttr('R_cheek_O', 'Face_R_cheek_anim.tx', 1)
    sdd_connectPanelAttr('R_cheek_I', 'Face_R_cheek_anim.tx', -1)

    cmds.connectAttr('Face_mouth_sticky_anim.ty', FR['jaw'] + _cnt + '.Lip_Sticky_P')
    cmds.connectAttr('Face_L_lip_corner_anim.ty', FR['jaw'] + _cnt + '.L_Lip_Corner_P')
    cmds.connectAttr('Face_R_lip_corner_anim.ty', FR['jaw'] + _cnt + '.R_Lip_Corner_P')

    sdd_connectPanelAttr('M_jaw_U', 'Face_jaw_anim.ty', 0.5)
    sdd_connectPanelAttr('M_jaw_D', 'Face_jaw_anim.ty', -1)
    sdd_connectPanelAttr('M_jaw_L', 'Face_jaw_anim.tx', 1)
    sdd_connectPanelAttr('M_jaw_R', 'Face_jaw_anim.tx', -1)

    sdd_connectPanelAttr('M_jaw_all_U', 'Face_mouth_all_anim.ty', 1)
    sdd_connectPanelAttr('M_jaw_all_D', 'Face_mouth_all_anim.ty', -1)
    sdd_connectPanelAttr('M_jaw_all_L', 'Face_mouth_all_anim.tx', 1)
    sdd_connectPanelAttr('M_jaw_all_R', 'Face_mouth_all_anim.tx', -1)

    sdd_connectPanelAttr('M_mouth_Up_U', 'Face_lip_open_Up_anim.ty', 1)
    sdd_connectPanelAttr('M_mouth_Dn_U', 'Face_lip_open_Dn_anim.ty', 1)
    sdd_connectPanelAttr('M_mouth_Dn_D', 'Face_lip_open_Dn_anim.ty', -1)

    sdd_connectPanelAttr('L_pump_O', 'Face_L_Pump_anim.tx', 1)
    sdd_connectPanelAttr('R_pump_O', 'Face_R_Pump_anim.tx', 1)


def sdd_connectPanelAttr(sdkAttr, pCtrlAttr, dv, v=None):
    faceSdkHandle = 'face_sdk_handle'
    if not (cmds.objExists(faceSdkHandle)):
        return
    if (v == None):
        v = 1
    cmds.setDrivenKeyframe(faceSdkHandle + '.' + sdkAttr, cd=pCtrlAttr, v=0, dv=0, itt='linear', ott='linear')
    cmds.setDrivenKeyframe(faceSdkHandle + '.' + sdkAttr, cd=pCtrlAttr, v=v, dv=dv, itt='linear', ott='linear')


def sdd_createSdkJntRig():
    T = sdd_returnTempNameDirc()
    FR, FRJntPos, FRUIPos = sdd_frTNameDirc()
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
    if (not cmds.objExists(faceCur)):
        return

    _rad = cmds.getAttr(faceCur + '.sx')
    if (cmds.getAttr(faceCur + '.globalScale') == 0):
        cmds.setAttr(faceCur + '.globalScale', _rad)
    _rad = cmds.getAttr(faceCur + '.globalScale')
    _rad *= 0.5
    cmds.makeIdentity(faceCur, a=1, t=1, r=1, s=1)

    faceBaseGrp = 'face_base_rig_grp'
    # face sdk cnt rig
    faceSdkRigGrp = 'face_sdk_rig_grp'
    faceSdkRigGrp = cmds.group(n=faceSdkRigGrp, em=1)
    cmds.parent(faceSdkRigGrp, faceBaseGrp)

    faceSdkSkinGrp = 'face_sdk_skin_grp'
    if not (cmds.objExists(faceSdkSkinGrp)):
        return
    # all setDrivenKey cmds.control group
    for i in FR.keys():
        baseName = FR[i]
        cur = sdd_createCurveCnt(baseName + _cnt, typ='Cube', r=_rad)
        curGrp = sdd_zeroSdkGrp(baseName, cur)
        cmds.delete(cmds.parentConstraint(baseName + _skin, curGrp))
        cmds.parent(curGrp, faceSdkRigGrp)
        cmds.parentConstraint(cur, baseName + _skin)
        cmds.scaleConstraint(cur, baseName + _skin)

        pCtrl = cmds.listRelatives(baseName + _skin, p=1)[0]
        if (faceSdkSkinGrp != pCtrl):
            cmds.parent(baseName + _skin, faceSdkSkinGrp)

    # eyelid rig
    # L Eyelid

    lEyelidList = ['L_eyelid_In', 'L_eyelid_UpIn', 'L_eyelid_DnIn', 'L_eyelid_Up', 'L_eyelid_Dn', 'L_eyelid_UpOut',
                   'L_eyelid_DnOut', 'L_eyelid_Out']
    for i in lEyelidList:
        baseName = FR[i] + _root
        sdk = cmds.group(n=baseName + _sdk, em=1)
        grp = cmds.group(n=baseName + _grp, em=1)
        cmds.parent(sdk, grp)
        cmds.delete(cmds.parentConstraint(FR['L_eye_root'] + _cnt, grp))

        cnt = sdd_createCurveCnt(baseName + _cnt, typ='Triangle', r=_rad)
        cmds.delete(cmds.parentConstraint(FR[i] + _cnt, cnt))
        cmds.parent(cnt, sdk)
        rPos = cmds.xform(FR['L_eye_root'] + _cnt, rp=1, q=1, ws=1)
        cmds.xform(cnt, rp=rPos, ws=1)
        cmds.makeIdentity(cnt, a=1, t=1, r=1, s=1)

        cmds.parent(FR[i] + _grp, cnt)
        cmds.parent(grp, FR['L_eye_root'] + _cnt)

    baseName = FR['L_eyelid_Up'] + _root
    cnt = baseName + _cnt
    # cnt=sdd_createCurveCnt(baseName+_cnt,typ='Triangle',r=_rad)
    # cmds.delete(cmds.parentConstraint(FR['L_eyelid_Up']+_cnt,cnt))
    # rPos=cmds.xform(FR['L_eye_root']+_cnt,rp=1,q=1,ws=1)
    # cmds.xform(cnt,rp=rPos,ws=1)
    # cmds.parent(cnt,baseName+_sdk)
    # cmds.makeIdentity(cnt,a=1,t=1,r=1,s=1),FR['L_eyelid_Up']+_grp
    cmds.parent(FR['L_eyelid_UpOut'] + _root + _grp, FR['L_eyelid_UpIn'] + _root + _grp, cnt)
    followGrp = cmds.duplicate(baseName + _grp, n=baseName + '_follow', po=1)[0]
    follCon = cmds.parentConstraint(followGrp, FR['L_eye_root'] + _cnt, baseName + _grp)[0]
    cmds.parentConstraint(FR['L_eyeBall'] + _cnt, followGrp)
    cmds.addAttr(cnt, ln='eydlidFollow', at='double', min=0, max=1, dv=0.05, k=1)
    cmds.connectAttr(cnt + '.eydlidFollow', follCon + '.w0')

    baseName = FR['L_eyelid_Dn'] + _root
    cnt = baseName + _cnt
    # cnt=sdd_createCurveCnt(baseName+_cnt,typ='Triangle',r=_rad)
    # cmds.delete(cmds.parentConstraint(FR['L_eyelid_Dn']+_cnt,cnt))
    # rPos=cmds.xform(FR['L_eye_root']+_cnt,rp=1,q=1,ws=1)
    # cmds.xform(cnt,rp=rPos,ws=1)
    # cmds.parent(cnt,baseName+_sdk)
    # cmds.makeIdentity(cnt,a=1,t=1,r=1,s=1),FR['L_eyelid_Dn']+_grp
    cmds.parent(FR['L_eyelid_DnOut'] + _root + _grp, FR['L_eyelid_DnIn'] + _root + _grp, cnt)
    followGrp = cmds.duplicate(baseName + _grp, n=baseName + '_follow', po=1)[0]
    follCon = cmds.parentConstraint(followGrp, FR['L_eye_root'] + _cnt, baseName + _grp)[0]
    cmds.parentConstraint(FR['L_eyeBall'] + _cnt, followGrp)
    cmds.addAttr(cnt, ln='eydlidFollow', at='double', min=0, max=1, dv=0.05, k=1)
    cmds.connectAttr(cnt + '.eydlidFollow', follCon + '.w0')

    cmds.parent(FR['L_eyeSag_Up'] + _grp, FR['L_eyeSag_Dn'] + _grp, FR['L_eyeBall'] + _grp, FR['L_eye_root'] + _cnt)
    cmds.parent(FR['L_brow_a'] + _grp, FR['L_brow_b'] + _grp, FR['L_brow_c'] + _grp, FR['L_eye_root'] + _cnt)

    # R Eyelid
    rEyelidList = ['R_eyelid_In', 'R_eyelid_UpIn', 'R_eyelid_DnIn', 'R_eyelid_Up', 'R_eyelid_Dn', 'R_eyelid_UpOut',
                   'R_eyelid_DnOut', 'R_eyelid_Out']
    for i in rEyelidList:
        baseName = FR[i] + _root

        sdk = cmds.group(n=baseName + _sdk, em=1)
        grp = cmds.group(n=baseName + _grp, em=1)
        cmds.parent(sdk, grp)
        cmds.delete(cmds.parentConstraint(FR['R_eye_root'] + _cnt, grp))

        cnt = sdd_createCurveCnt(baseName + _cnt, typ='Triangle', r=_rad)
        cmds.delete(cmds.parentConstraint(FR[i] + _cnt, cnt))
        cmds.parent(cnt, sdk)
        rPos = cmds.xform(FR['R_eye_root'] + _cnt, rp=1, q=1, ws=1)
        cmds.xform(cnt, rp=rPos, ws=1)
        cmds.makeIdentity(cnt, a=1, t=1, r=1, s=1)

        cmds.parent(FR[i] + _grp, cnt)
        cmds.parent(grp, FR['R_eye_root'] + _cnt)

    baseName = FR['R_eyelid_Up'] + _root
    cnt = baseName + _cnt
    # cnt=sdd_createCurveCnt(baseName+_cnt,typ='Triangle',r=_rad)
    # cmds.delete(cmds.parentConstraint(FR['R_eyelid_Up']+_cnt,cnt))
    # rPos=cmds.xform(FR['R_eye_root']+_cnt,rp=1,q=1,ws=1)
    # cmds.xform(cnt,rp=rPos,ws=1)
    # cmds.parent(cnt,baseName+_sdk)
    # cmds.makeIdentity(cnt,a=1,t=1,r=1,s=1)
    cmds.parent(FR['R_eyelid_UpOut'] + _root + _grp, FR['R_eyelid_UpIn'] + _root + _grp, FR['R_eyelid_Up'] + _grp, cnt)
    followGrp = cmds.duplicate(baseName + _grp, n=baseName + '_follow', po=1)[0]
    follCon = cmds.parentConstraint(followGrp, FR['R_eye_root'] + _cnt, baseName + _grp)[0]
    cmds.parentConstraint(FR['R_eyeBall'] + _cnt, followGrp)
    cmds.addAttr(cnt, ln='eydlidFollow', at='double', min=0, max=1, dv=0.05, k=1)
    cmds.connectAttr(cnt + '.eydlidFollow', follCon + '.w0')

    baseName = FR['R_eyelid_Dn'] + _root
    cnt = baseName + _cnt
    # cnt=sdd_createCurveCnt(baseName+_cnt,typ='Triangle',r=_rad)
    # cmds.delete(cmds.parentConstraint(FR['R_eyelid_Dn']+_cnt,cnt))
    # rPos=cmds.xform(FR['R_eye_root']+_cnt,rp=1,q=1,ws=1)
    # cmds.xform(cnt,rp=rPos,ws=1)
    # cmds.parent(cnt,baseName+_sdk)
    # cmds.makeIdentity(cnt,a=1,t=1,r=1,s=1)
    cmds.parent(FR['R_eyelid_DnOut'] + _root + _grp, FR['R_eyelid_DnIn'] + _root + _grp, FR['R_eyelid_Dn'] + _grp, cnt)
    followGrp = cmds.duplicate(baseName + _grp, n=baseName + '_follow', po=1)[0]
    follCon = cmds.parentConstraint(followGrp, FR['R_eye_root'] + _cnt, baseName + _grp)[0]
    cmds.parentConstraint(FR['R_eyeBall'] + _cnt, followGrp)
    cmds.addAttr(cnt, ln='eydlidFollow', at='double', min=0, max=1, dv=0.05, k=1)
    cmds.connectAttr(cnt + '.eydlidFollow', follCon + '.w0')

    cmds.parent(FR['R_eyeSag_Up'] + _grp, FR['R_eyeSag_Dn'] + _grp, FR['R_eyeBall'] + _grp, FR['R_eye_root'] + _cnt)

    cmds.parent(FR['R_brow_a'] + _grp, FR['R_brow_b'] + _grp, FR['R_brow_c'] + _grp, FR['R_eye_root'] + _cnt)

    # #cheek rig
    # cmds.parent(FR['L_cheek_In']+_grp,FR['L_cheek_Out']+_grp,FR['L_cheek_Up']+_cnt)
    # cmds.parent(FR['R_cheek_In']+_grp,FR['R_cheek_Out']+_grp,FR['R_cheek_Up']+_cnt)

    # nose rig
    # nose root
    noseRoot = FR['M_nose'] + _root
    noseRootCnt = sdd_createCurveCnt(noseRoot + _cnt, typ='Cube', r=_rad)
    noseRootGrp = sdd_zeroSdkGrp(noseRoot, noseRootCnt)
    cmds.delete(cmds.parentConstraint(FR['L_cheek_In'] + _cnt, FR['R_cheek_In'] + _cnt, noseRootGrp))
    cmds.parent(FR['L_nose'] + _grp, noseRootCnt)
    cmds.parent(FR['R_nose'] + _grp, noseRootCnt)
    cmds.parent(FR['M_nose'] + _grp, noseRootCnt)
    cmds.parent(noseRootGrp, faceSdkRigGrp)
    # mouth rig

    # chin
    cmds.parent(FR['chin'] + _grp, FR['jaw'] + _cnt)
    # jaw_root
    mouthDnRoot = FR['jaw'] + _root
    mouthDnRootCnt = sdd_createCurveCnt(mouthDnRoot + _cnt, typ='Triangle', r=_rad)
    mouthDnRootGrp = sdd_zeroSdkGrp(mouthDnRoot, mouthDnRootCnt)
    cmds.delete(cmds.parentConstraint(FR['jaw'] + _cnt, mouthDnRootGrp))
    cmds.parent(mouthDnRootGrp, faceSdkRigGrp)

    # mouth dn loc
    jawDnLoc = FR['jaw'] + _loc
    jawDnLoc = cmds.spaceLocator(n=jawDnLoc)[0]
    cmds.delete(cmds.parentConstraint(FR['jaw'] + _grp, jawDnLoc))
    cmds.parentConstraint(FR['jaw'] + _cnt, jawDnLoc)
    cmds.parent(jawDnLoc, FR['jaw'] + _grp, mouthDnRootGrp)
    cmds.setAttr(jawDnLoc + '.v', 0)

    # attr
    jawCnt = FR['jaw'] + _cnt
    cmds.addAttr(jawCnt, ln='__MouthFollow__', at='double', min=0, max=1, k=1)
    cmds.setAttr(jawCnt + '.' + '__MouthFollow__', l=1)

    cmds.addAttr(jawCnt, ln='Lip_Sticky', at='double', min=0, max=1, k=1)
    cmds.addAttr(jawCnt, ln='L_Lip_Corner', at='double', min=-1, max=1, k=1)
    cmds.addAttr(jawCnt, ln='R_Lip_Corner', at='double', min=-1, max=1, k=1)

    # attr
    cmds.addAttr(jawCnt, ln='__Hide__', at='double', min=0, max=1, k=1)
    cmds.setAttr(jawCnt + '.' + '__Hide__', l=1)
    cmds.addAttr(jawCnt, ln=FR['M_mouth_Up'], at='double', min=0, max=1, k=1)
    cmds.addAttr(jawCnt, ln=FR['L_mouth_Up'], at='double', min=0, max=1, k=1, dv=0.05)
    cmds.addAttr(jawCnt, ln=FR['R_mouth_Up'], at='double', min=0, max=1, k=1, dv=0.05)
    cmds.addAttr(jawCnt, ln=FR['L_mouth_Corner'], at='double', min=0, max=1, k=1, dv=0.5)
    cmds.addAttr(jawCnt, ln=FR['R_mouth_Corner'], at='double', min=0, max=1, k=1, dv=0.5)
    cmds.addAttr(jawCnt, ln=FR['M_mouth_Dn'], at='double', min=0, max=1, k=1, dv=1)
    cmds.addAttr(jawCnt, ln=FR['L_mouth_Dn'], at='double', min=0, max=1, k=1, dv=0.95)
    cmds.addAttr(jawCnt, ln=FR['R_mouth_Dn'], at='double', min=0, max=1, k=1, dv=0.95)
    cmds.addAttr(jawCnt, ln='Lip_Sticky_H', at='double', min=0, max=1, k=1)
    cmds.addAttr(jawCnt, ln='L_Lip_Corner_H', at='double', min=-1, max=1, k=1)
    cmds.addAttr(jawCnt, ln='R_Lip_Corner_H', at='double', min=-1, max=1, k=1)
    cmds.addAttr(jawCnt, ln='Lip_Sticky_P', at='double', min=0, max=1, k=1)
    cmds.addAttr(jawCnt, ln='L_Lip_Corner_P', at='double', min=-1, max=1, k=1)
    cmds.addAttr(jawCnt, ln='R_Lip_Corner_P', at='double', min=-1, max=1, k=1)

    sPlus = cmds.createNode('plusMinusAverage', n='Lip_Sticky' + '_plus')
    cmds.connectAttr(jawCnt + '.Lip_Sticky_P', sPlus + '.i1[0]')
    cmds.connectAttr(jawCnt + '.Lip_Sticky', sPlus + '.i1[1]')
    cmds.connectAttr(sPlus + '.output1D', jawCnt + '.Lip_Sticky_H')

    sPlus = cmds.createNode('plusMinusAverage', n='L_Lip_Corner' + '_plus')
    cmds.connectAttr(jawCnt + '.L_Lip_Corner_P', sPlus + '.i1[0]')
    cmds.connectAttr(jawCnt + '.L_Lip_Corner', sPlus + '.i1[1]')
    cmds.connectAttr(sPlus + '.output1D', jawCnt + '.L_Lip_Corner_H')

    sPlus = cmds.createNode('plusMinusAverage', n='R_Lip_Corner' + '_plus')
    cmds.connectAttr(jawCnt + '.R_Lip_Corner_P', sPlus + '.i1[0]')
    cmds.connectAttr(jawCnt + '.R_Lip_Corner', sPlus + '.i1[1]')
    cmds.connectAttr(sPlus + '.output1D', jawCnt + '.R_Lip_Corner_H')

    # M_mouth_Up
    mouthList = ['M_mouth_Up', 'L_mouth_Up', 'L_mouth_Corner', 'L_mouth_Dn', 'M_mouth_Dn', 'R_mouth_Dn',
                 'R_mouth_Corner', 'R_mouth_Up']
    for i in mouthList:
        baseName = FR[i]
        Root = baseName + _root
        RootGrp = sdd_zeroSdkGrp(Root, FR['jaw'] + _grp, FR[i] + _grp)
        cmds.parent(RootGrp, mouthDnRootCnt)

        btaNode = cmds.createNode('blendTwoAttr', n=i + '_bta')
        cmds.connectAttr(jawCnt + '.Lip_Sticky_H', btaNode + '.ab')
        cmds.connectAttr(jawCnt + '.' + i, btaNode + '.i[0]')
        cmds.setAttr(btaNode + '.i[1]', 0.5)

        TBc = cmds.createNode('blendColors', n=baseName + '_TBC')
        cmds.setAttr(TBc + '.c2', 0, 0, 0, typ='float3')
        cmds.connectAttr(jawDnLoc + '.t', TBc + '.c1')
        cmds.connectAttr(btaNode + '.o', TBc + '.b')
        RBc = cmds.createNode('blendColors', n=baseName + '_RBC')
        cmds.setAttr(RBc + '.c2', 0, 0, 0, typ='float3')
        cmds.connectAttr(jawDnLoc + '.r', RBc + '.c1')
        cmds.connectAttr(btaNode + '.o', RBc + '.b')
        CDt = cmds.createNode('condition', n=baseName + '_cdt')
        cmds.setAttr(CDt + '.op', 4)
        cmds.connectAttr(jawDnLoc + '.rx', CDt + '.ft')
        cmds.connectAttr(jawDnLoc + '.rx', CDt + '.ctr')
        cmds.connectAttr(RBc + '.opg', CDt + '.ctg')
        cmds.connectAttr(RBc + '.opb', CDt + '.ctb')
        cmds.connectAttr(RBc + '.op', CDt + '.cf')
        cmds.connectAttr(TBc + '.op', Root + _rig + '.t')
        cmds.connectAttr(CDt + '.oc', Root + _rig + '.r')

    lipMd = cmds.createNode('multiplyDivide', n='Lip_Corner_md')
    cmds.setAttr(lipMd + '.i1x', -1)
    cmds.setAttr(lipMd + '.i1y', -1)
    cmds.connectAttr(jawCnt + '.L_Lip_Corner_H', lipMd + '.i2x')
    cmds.connectAttr(jawCnt + '.R_Lip_Corner_H', lipMd + '.i2y')

    lCornerRv = cmds.createNode('remapValue', n=FR['L_mouth_Corner'] + '_rv')
    cmds.connectAttr(lipMd + '.ox', lCornerRv + '.i')
    cmds.setAttr(lCornerRv + '.imn', -1)
    cmds.connectAttr(lCornerRv + '.ov', FR['L_mouth_Corner'] + '_bta' + '.i[0]', f=1)

    lMouthUpRv = cmds.createNode('remapValue', n=FR['L_mouth_Up'] + '_rv')
    cmds.connectAttr(lipMd + '.ox', lMouthUpRv + '.i')
    cmds.setAttr(lMouthUpRv + '.imn', -1)
    cmds.setAttr(lMouthUpRv + '.imx', 0)
    cmds.connectAttr(jawCnt + '.L_mouth_Up', lMouthUpRv + '.omx')
    cmds.connectAttr(lMouthUpRv + '.ov', FR['L_mouth_Up'] + '_bta' + '.i[0]', f=1)

    lMouthDnRv = cmds.createNode('remapValue', n=FR['L_mouth_Dn'] + '_rv')
    cmds.connectAttr(lipMd + '.ox', lMouthDnRv + '.i')
    cmds.connectAttr(jawCnt + '.L_mouth_Dn', lMouthDnRv + '.omn')
    cmds.connectAttr(lMouthDnRv + '.ov', FR['L_mouth_Dn'] + '_bta' + '.i[0]', f=1)

    rCornerRv = cmds.createNode('remapValue', n=FR['R_mouth_Corner'] + '_rv')
    cmds.connectAttr(lipMd + '.oy', rCornerRv + '.i')
    cmds.setAttr(rCornerRv + '.imn', -1)
    cmds.connectAttr(rCornerRv + '.ov', FR['R_mouth_Corner'] + '_bta' + '.i[0]', f=1)

    rMouthUpRv = cmds.createNode('remapValue', n=FR['R_mouth_Up'] + '_rv')
    cmds.connectAttr(lipMd + '.oy', rMouthUpRv + '.i')
    cmds.setAttr(rMouthUpRv + '.imn', -1)
    cmds.setAttr(rMouthUpRv + '.imx', 0)
    cmds.connectAttr(jawCnt + '.R_mouth_Up', rMouthUpRv + '.omx')
    cmds.connectAttr(rMouthUpRv + '.ov', FR['R_mouth_Up'] + '_bta' + '.i[0]', f=1)

    rMouthDnRv = cmds.createNode('remapValue', n=FR['R_mouth_Dn'] + '_rv')
    cmds.connectAttr(lipMd + '.oy', rMouthDnRv + '.i')
    cmds.connectAttr(jawCnt + '.R_mouth_Dn', rMouthDnRv + '.omn')
    cmds.connectAttr(rMouthDnRv + '.ov', FR['R_mouth_Dn'] + '_bta' + '.i[0]', f=1)

    dis = sdd_getDistanceTwoPoint([FR['M_mouth_Up'] + _skin], FR['M_mouth_Dn'] + _skin)
    for i in mouthList:
        cnt = FR[i] + _cnt
        vtxList = cmds.ls(cnt + '.cv[*]')
        cmds.move(0, 0, dis * 0.3, vtxList, r=1, os=1, wd=1)


def sdd_frLockAndAttr(obj, attrList):
    for i in attrList:
        cmds.setAttr(obj + '.' + i, l=1, k=0)


def sdd_frUnLockBaseAttr(obj):
    attrList = ['tx', 'ty', 'tz', 'rx', 'ry', 'rz', 'sx', 'sy', 'sz', 'v']
    for i in attrList:
        cmds.setAttr(obj + '.' + i, l=0, k=1)


def sdd_zeroSdkGrp(baseName, curName, grpName=None):
    T = sdd_returnTempNameDirc()
    FR, FRJntPos, FRUIPos = sdd_frTNameDirc()
    _rig = T['_rig']
    _sdk = T['_sdk']
    _grp = T['_grp']

    cursdk = cmds.group(n=baseName + _sdk, em=1)
    curRig = cmds.group(n=baseName + _rig, em=1)
    cmds.parent(curRig, cursdk)
    curGrp = cmds.group(n=baseName + _grp, em=1)
    cmds.parent(cursdk, curGrp)

    cmds.delete(cmds.parentConstraint(curName, curGrp))
    if (grpName == None):
        cmds.parent(curName, curRig)
    else:
        cmds.parent(grpName, curRig)
    return curGrp


def sdd_getAngleThreePoint(objList):
    obj1, objRoot, obj2 = objList
    grp = cmds.group(n='Tmp_arc_grp', em=1)
    cmds.delete(cmds.parentConstraint(objRoot, grp))
    cmds.delete(cmds.aimConstraint(obj1, grp, aim=[0, 0, 1], wut='vector'))
    zeroGrp = cmds.group(n='Tmp_arc_zeroGrp', em=1)
    cmds.delete(cmds.parentConstraint(grp, zeroGrp))
    cmds.parent(grp, zeroGrp)
    cmds.delete(cmds.aimConstraint(obj2, grp, aim=[0, 0, 1], wut='vector'))
    arc2 = cmds.getAttr(grp + '.rx')
    cmds.delete(zeroGrp)
    return math.ceil(arc2)


def sdd_getDistanceTwoPoint(objList, objRoot):
    sel = cmds.ls(sl=1)
    grp = cmds.group(n='Tmp_arc_grp', em=1)
    cmds.delete(cmds.parentConstraint(objList, grp))
    p1 = cmds.xform(grp, q=1, ws=1, t=1)
    p2 = cmds.xform(objRoot, q=1, ws=1, t=1)
    mp1 = OpenMaya.MPoint(p1[0], p1[1], p1[2])
    mp2 = OpenMaya.MPoint(p2[0], p2[1], p2[2])
    dis = mp1.distanceTo(mp2)
    cmds.delete(grp)
    if (len(sel) != 0):
        cmds.select(sel)
    return round(dis, 2)


def sdd_addAttrToHandle(attr, mirAttr, faceSdkHandle):
    cmds.addAttr(faceSdkHandle, ln=attr, at='double', min=0, max=1, k=1)
    if (mirAttr != None):
        cmds.addAttr(faceSdkHandle, ln=mirAttr, at='double', min=0, max=1, k=1)
    else:
        return attr
    return attr, mirAttr


def sdd_setDrivenKeyframe(c, cAttr, v, cd, cdAttr, dv, mircdAttr=None):
    cmds.setDrivenKeyframe(c + '.' + cAttr, cd=cd + '.' + cdAttr, v=0, dv=0, itt='linear', ott='linear')
    cmds.setDrivenKeyframe(c + '.' + cAttr, cd=cd + '.' + cdAttr, v=v, dv=dv, itt='linear', ott='linear')
    if (mircdAttr != None):
        attrList = ['tx', 'ty', 'tz', 'rx', 'ry', 'rz', 'sx', 'sy', 'sz']
        valList = [-1, 1, 1, 1, -1, -1, 1, 1, 1]
        mirc = sdd_getMirrorName(c)
        v = v * valList[attrList.index(cAttr)]
        cmds.setDrivenKeyframe(mirc + '.' + cAttr, cd=cd + '.' + mircdAttr, v=0, dv=0, itt='linear', ott='linear')
        cmds.setDrivenKeyframe(mirc + '.' + cAttr, cd=cd + '.' + mircdAttr, v=v, dv=dv, itt='linear', ott='linear')


def sdd_createCurveCnt(cName, typ, r):
    if (typ == 'Sphere'):
        cname = cmds.curve(n=cName, d=1, p=[(0.504214, 0, 0), (0.491572, 0.112198, 0), (0.454281, 0.21877, 0),
                                            (0.394211, 0.314372, 0), (0.314372, 0.394211, 0), (0.21877, 0.454281, 0),
                                            (0.112198, 0.491572, 0), (0, 0.504214, 0), (-0.112198, 0.491572, 0),
                                            (-0.21877, 0.454281, 0), (-0.314372, 0.394211, 0), (-0.394211, 0.314372, 0),
                                            (-0.454281, 0.21877, 0), (-0.491572, 0.112198, 0), (-0.504214, 0, 0),
                                            (-0.491572, -0.112198, 0), (-0.454281, -0.21877, 0),
                                            (-0.394211, -0.314372, 0), (-0.314372, -0.394211, 0),
                                            (-0.21877, -0.454281, 0), (-0.112198, -0.491572, 0), (0, -0.504214, 0),
                                            (0.112198, -0.491572, 0), (0.21877, -0.454281, 0), (0.314372, -0.394211, 0),
                                            (0.394211, -0.314372, 0), (0.454281, -0.21877, 0), (0.491572, -0.112198, 0),
                                            (0.504214, 0, 0), (0.491572, 0, -0.112198), (0.454281, 0, -0.21877),
                                            (0.394211, 0, -0.314372), (0.314372, 0, -0.394211), (0.21877, 0, -0.454281),
                                            (0.112198, 0, -0.491572), (0, 0, -0.504214), (-0.112198, 0, -0.491572),
                                            (-0.21877, 0, -0.454281), (-0.314372, 0, -0.394211),
                                            (-0.394211, 0, -0.314372), (-0.454281, 0, -0.21877),
                                            (-0.491572, 0, -0.112198), (-0.504214, 0, 0), (-0.491572, 0, 0.112198),
                                            (-0.454281, 0, 0.21877), (-0.394211, 0, 0.314372), (-0.314372, 0, 0.394211),
                                            (-0.21877, 0, 0.454281), (-0.112198, 0, 0.491572), (0, 0, 0.504214),
                                            (0, 0.112198, 0.491572), (0, 0.21877, 0.454281), (0, 0.314372, 0.394211),
                                            (0, 0.394211, 0.314372), (0, 0.454281, 0.21877), (0, 0.491572, 0.112198),
                                            (0, 0.504214, 0), (0, 0.491572, -0.112198), (0, 0.454281, -0.21877),
                                            (0, 0.394211, -0.314372), (0, 0.314372, -0.394211), (0, 0.21877, -0.454281),
                                            (0, 0.112198, -0.491572), (0, 0, -0.504214), (0, -0.112198, -0.491572),
                                            (0, -0.21877, -0.454281), (0, -0.314372, -0.394211),
                                            (0, -0.394211, -0.314372), (0, -0.454281, -0.21877),
                                            (0, -0.491572, -0.112198), (0, -0.504214, 0), (0, -0.491572, 0.112198),
                                            (0, -0.454281, 0.21877), (0, -0.394211, 0.314372), (0, -0.314372, 0.394211),
                                            (0, -0.21877, 0.454281), (0, -0.112198, 0.491572), (0, 0, 0.504214),
                                            (0.112198, 0, 0.491572), (0.21877, 0, 0.454281), (0.314372, 0, 0.394211),
                                            (0.394211, 0, 0.314372), (0.454281, 0, 0.21877), (0.491572, 0, 0.112198),
                                            (0.504214, 0, 0)])
    if (typ == 'Triangle'):
        cName = cmds.curve(d=1, n=cName, p=[[0, 0, 0.25], [0, 0.05, 0.1], [0, -0.05, 0.1], [0, 0, 0.25]])
    if (typ == 'Cube'):
        cName = cmds.curve(d=1, n=cName,
                           p=[[0.1, 0.1, -0.1], [-0.1, 0.1, -0.1], [-0.1, 0.1, 0.1], [0.1, 0.1, 0.1], [0.1, 0.1, -0.1],
                              [0.1, -0.1, -0.1], [0.1, -0.1, 0.1], [0.1, 0.1, 0.1], [-0.1, 0.1, 0.1], [-0.1, -0.1, 0.1],
                              [0.1, -0.1, 0.1], [0.1, -0.1, -0.1], [-0.1, -0.1, -0.1], [-0.1, -0.1, 0.1],
                              [-0.1, 0.1, 0.1], [-0.1, 0.1, -0.1], [-0.1, -0.1, -0.1]])
    cmds.scale(r, r, r, cmds.ls(cName + '.cv[*]'), r=1, ocp=1)
    return cName


# cmds.joint Tempate____________________________________________________________________________________====

def sdd_importBaseJnt():
    faceCur = 'faceMoveCur'

    T = sdd_returnTempNameDirc()
    FR, FRJntPos, FRUIPos = sdd_frTNameDirc()
    _skin = T['_skin']
    _rad = 0.1

    if (cmds.objExists(faceCur)):
        return
    faceCur = cmds.circle(n=faceCur, r=3.8, nr=[0, 0, 1], ch=0)[0]
    cmds.addAttr(faceCur, ln='globalScale', at='double', min=0, k=1)
    jntList = []
    for i in FR.keys():
        cmds.select(cl=1)
        print FR[i]
        jnt = cmds.joint(n=FR[i] + _skin, rad=_rad)
        cmds.xform(jnt, ws=1, t=FRJntPos[i])
        jntList.append(jnt)

    faceBaseGrp = 'face_base_rig_grp'
    faceBaseGrp = cmds.group(n=faceBaseGrp, em=1)
    cmds.parent(faceBaseGrp, faceCur)

    # face sdk jnt grp
    faceSdkSkinGrp = 'face_sdk_skin_grp'
    faceSdkSkinGrp = cmds.group(n=faceSdkSkinGrp, em=1)
    cmds.parent(faceSdkSkinGrp, faceBaseGrp)

    cmds.parent(jntList, faceSdkSkinGrp)
    cmds.parent(FR['chin'] + _skin, FR['jaw'] + _skin)
    cmds.parent(FR['L_eyeBall'] + _skin, FR['L_eye_root'] + _skin)
    cmds.parent(FR['R_eyeBall'] + _skin, FR['R_eye_root'] + _skin)

    cmds.setAttr(FR['L_eyeBall'] + _skin + '.radi', _rad * 0.5)
    cmds.setAttr(FR['R_eyeBall'] + _skin + '.radi', _rad * 0.5)
    cmds.select(faceCur)


def sdd_mirrorJntPos(typ):
    TName = sdd_returnTempNameDirc()
    L_ = TName['L_']
    R_ = TName['R_']

    tv = cmds.checkBoxGrp('frMirrorOptionToCBG', q=1, v1=1)
    rv = cmds.checkBoxGrp('frMirrorOptionToCBG', q=1, v2=1)

    faceSdkSkinGrp = 'face_sdk_skin_grp'
    if (not cmds.objExists(faceSdkSkinGrp)):
        return
    allJnt = cmds.listRelatives(faceSdkSkinGrp, c=1, ad=1, typ='joint')
    sel = cmds.ls(sl=1)
    mirJnt = []
    if (len(sel) > 0):
        for i in sel:
            if (i in allJnt):
                mirJnt.append(i)
    else:
        mirJnt = allJnt

    axis = [-1, 1, 1, 1, -1, -1, 1, 1, 1]
    for i in mirJnt:
        if (typ == 'L>>R'):
            if (i[:2] == L_):
                getObj = i
                mirObj = R_ + i[2:]
            else:
                continue
        else:
            if (i[:2] == R_):
                getObj = i
                mirObj = L_ + i[2:]
            else:
                continue

        if (not cmds.objExists(mirObj)):
            continue
        if (tv):
            pos = cmds.xform(getObj, ws=1, q=1, t=1)
            cmds.xform(mirObj, ws=1, t=[pos[0] * axis[0], pos[1] * axis[1], pos[2] * axis[2]])
        if (rv):
            rot = cmds.xform(getObj, ws=1, q=1, ro=1)
            cmds.xform(mirObj, ws=1, ro=[rot[0] * axis[3], rot[1] * axis[4], rot[2] * axis[5]])
    cmds.refresh(cv=1, f=1)


def sdd_getBoundingBox(obj):
    box = cmds.xform(obj, q=1, bbi=1)
    return [box[3] - box[0], box[4] - box[1], box[5] - box[2]]


# Load Face Mesh ____________________________________________________________________________________===
def sdd_ErrorVtxIdxSelectChange(typ):
    faceMesh = sdd_getCurrentMeshName()
    if (typ == 1):
        selI = cmds.textScrollList('frErrVtxTSL', q=1, si=1)
    else:
        selI = cmds.textScrollList('frErrVtxTSL', q=1, ai=1)
    if (selI == None):
        return
    faceMesh = cmds.textField('frCurrentMeshTF', q=1, tx=1)
    selVtxIdx = []
    for i in selI:
        selVtxIdx.append('%s.vtx[%s]' % (faceMesh, i))
    cmds.select(selVtxIdx)


def sdd_MiddleVtxIdxSelectChange(typ):
    faceMesh = sdd_getCurrentMeshName()
    if (typ == 1):
        selI = cmds.textScrollList('frMidVtxTSL', q=1, si=1)
    else:
        selI = cmds.textScrollList('frMidVtxTSL', q=1, ai=1)
    if (selI == None):
        return
    faceMesh = cmds.textField('frCurrentMeshTF', q=1, tx=1)
    selVtxIdx = []
    for i in selI:
        selVtxIdx.append('%s.vtx[%s]' % (faceMesh, i))
    cmds.select(selVtxIdx)


def sdd_MirrorVtxIdxSelectChange(typ):
    faceMesh = sdd_getCurrentMeshName()
    if (typ == 1):
        selI = cmds.textScrollList('frMirVtxTSL', q=1, si=1)
    else:
        selI = cmds.textScrollList('frMirVtxTSL', q=1, ai=1)
    if (selI == None):
        return
    faceMesh = cmds.textField('frCurrentMeshTF', q=1, tx=1)
    selVtxIdx = []
    for i in selI:
        idl = i.split('-')[0]
        idr = i.split('-')[1]
        selVtxIdx.append('%s.vtx[%s]' % (faceMesh, idl))
        selVtxIdx.append('%s.vtx[%s]' % (faceMesh, idr))
    cmds.select(selVtxIdx)


def sdd_ctrBsEdit():
    global ctrBsPuffDate

    label = cmds.button('frCtrBsEditB', q=1, l=1)
    selI = cmds.textScrollList('frCrtBsTSL', q=1, si=1)
    if (selI == None):
        return
    faceMesh, origMesh, ctrGrp, suf = sdd_getCtrMeshAnGrpInfo()

    finalMeshName = selI[0] + '_CorrectiveBS'
    cachGrp = selI[0] + '_CacheGrp'

    faceCur = 'faceMoveCur'
    if not (cmds.objExists(faceCur)):
        return
    faceBsNode = suf + '_blendShape'
    if not (cmds.objExists(faceBsNode)):
        return
    if (label == 'Edit'):
        if (cmds.objExists(cachGrp)):
            cmds.delete(cachGrp)
        cmds.button('frCtrBsEditB', e=1, l='Finally', bgc=[1, 0, 0])
        cmds.rowLayout('frCtrModifyRL', e=1, en=1)
        cmds.columnLayout('frCorrectiveCL', e=1, en=0)

        finalMeshName = cmds.duplicate(faceMesh, n=finalMeshName)[0]
        cmds.setAttr(finalMeshName + '.v', 1)
        cmds.setAttr(finalMeshName + '.overrideEnabled', 0)
        cachGrp = cmds.group(finalMeshName, n=cachGrp)
        cmds.parent(cachGrp, faceCur)
        cmds.setAttr(faceMesh + '.v', 0)
        cmds.select(finalMeshName)
    else:
        cmds.deleteUI('frCtrBsEditB')
        cmds.button('frCtrBsEditB', l='Edit', p='frCorrectiveDnCL', h=35, c='sdd_ctrBsEdit()')
        cmds.columnLayout('frCorrectiveCL', e=1, en=1)
        cmds.rowLayout('frCtrModifyRL', e=1, en=0)
        sdd_bsSdkBsListSelectChange()

        try:
            cmds.setAttr(faceBsNode + '.' + selI[0], 0)
            skinNodeName = mm.eval('findRelatedSkinCluster %s' % faceMesh)
            sdd_inverseCaclBlendShape(selI[0], faceMesh, finalMeshName, skinNodeName)
            if (sdd_checkCtrMir()):
                sdd_flipMirrorCtrBS(selI[0], ctrGrp)
            cmds.delete(cachGrp)
        finally:
            ctrBsPuffDate = None
            cmds.setAttr(faceBsNode + '.' + selI[0], 1)
            cmds.setAttr(faceMesh + '.v', 1)


def sdd_checkCtrMir(ret='Single'):
    if (cmds.checkBox('frCrtMirrorCB', q=1, v=1) and cmds.checkBox('frCrtMirrorCB', q=1, en=1)) or ret == 'Mirror':
        return True
    return False


def sdd_meshReferenceChange(typ):
    faceSkinMeshGrp = 'face_skin_mesh_grp'
    if not (cmds.objExists(faceSkinMeshGrp)):
        return
    if (cmds.checkBox('frMeshReferenceCB', q=1, v=1) and typ == 4):
        cmds.setAttr(faceSkinMeshGrp + '.overrideEnabled', 1)
        cmds.setAttr(faceSkinMeshGrp + '.overrideDisplayType', 2)
    else:
        cmds.setAttr(faceSkinMeshGrp + '.overrideEnabled', 0)


# def sdd_loadEyeBallMesh(idx):
#     cmds.textField(idx,e=1,tx='')
#     sel=cmds.ls(sl=1)
#     if(len(sel)==0):
#         return
#     extraStr=''
#     for i in sel:
#         shape=cmds.listRelatives(i,s=1,f=1)
#         if(shape==None):
#             continue
#         if(cmds.objectType(shape[0])!='mesh'):
#             continue
#         extraStr+='%s,'%i
#     extraStr=extraStr.strip(',')
#     cmds.textField(idx,e=1,tx=extraStr)


def sdd_setFaceMesh():
    selI = cmds.textScrollList('frFaceMeshTSL', q=1, si=1)
    if (selI == None):
        return
    skinMesh = selI[0]
    cmds.textField('frFaceMeshTF', e=1, tx=skinMesh)
    cmds.button('frSdkRiggingB', e=1, en=1)


def sdd_setCurrentCtrMesh(skinMesh):
    mirX, mirY, mirZ = -1, 1, 1
    faceBsGrp = 'face_bs_grp'

    origMesh = cmds.listConnections(skinMesh + '.origMesh')[0]
    ctrGrp = cmds.listConnections(origMesh + '.ctrGrp')

    if (ctrGrp == None):
        nCtrAttr = origMesh + '.ctrGrp'
        ctrGrp = cmds.getAttr(nCtrAttr)
        if (cmds.objExists(ctrGrp)):
            cmds.delete(ctrGrp)
        ctrGrp = cmds.group(em=1, n=ctrGrp)
        cmds.setAttr(ctrGrp + '.v', 0)

        iCtrAttr = sdd_tryAddMessageAttr(ctrGrp, 'ctrGrp')
        sdd_connectAttrForce(iCtrAttr, nCtrAttr)

        sdd_tryParent(ctrGrp, faceBsGrp)
    else:
        ctrGrp = ctrGrp[0]

    cmds.textField('frCurrentMeshTF', e=1, tx=skinMesh)
    sdd_loadBsToList()


# def sdd_resetBindPreMatrix(skinNodeName):
#     exIdx=cmds.getAttr(skinNodeName+'.matrix',mi=1)
#     bindPose=cmds.listConnections(skinNodeName+'.bindPose')
#     for i in exIdx:
#         cnnJnt=cmds.listConnections(skinNodeName+'.matrix[%s]'%i)
#         if(cnnJnt==None):
#             continue
#         invMatrix=cmds.getAttr(cnnJnt[0]+'.worldInverseMatrix')
#         cmds.setAttr(skinNodeName+'.bindPreMatrix[%s]'%i,invMatrix,typ='matrix')
#         if(bindPose!=None):
#             cmds.dagPose(cnnJnt[0],rs=1,n=bindPose[0])
#     cmds.delete(skinNodeName)
#     cmds.undo()

def sdd_flipMirrorCtrBS(curMesh, ctrGrp):
    mirX, mirY, mirZ = -1, 1, 1
    mirMesh = sdd_getMirrorName(curMesh)
    if (mirMesh == curMesh):
        return
    if not (cmds.objExists(mirMesh)):
        return
    sdd_calcMeshMirrorInfor(1)
    mVtxList = cmds.getAttr(ctrGrp + '.MiddleVtxIdx')
    lVtxList = cmds.getAttr(ctrGrp + '.LeftVtxIdx')
    rVtxList = cmds.getAttr(ctrGrp + '.RightVtxIdx')

    curMeshFn = sdd_getMfnMeshByName(curMesh)
    curVtxPointList = OpenMaya.MPointArray()
    curMeshFn.getPoints(curVtxPointList)

    finalVtxPointList = OpenMaya.MPointArray()
    finalVtxPointList.copy(curVtxPointList)
    try:
        cmds.progressBar('frMainStatePB', e=1, max=len(lVtxList) + len(mVtxList), bp=1, vis=1)
        for i in range(len(lVtxList)):
            cmds.progressBar('frMainStatePB', e=1, s=1)
            lIdx = lVtxList[i]
            rIdx = rVtxList[i]
            finalVtxPointList[rIdx].x = curVtxPointList[lIdx].x * mirX
            finalVtxPointList[rIdx].y = curVtxPointList[lIdx].y * mirY
            finalVtxPointList[rIdx].z = curVtxPointList[lIdx].z * mirZ

            finalVtxPointList[lIdx].x = curVtxPointList[rIdx].x * mirX
            finalVtxPointList[lIdx].y = curVtxPointList[rIdx].y * mirY
            finalVtxPointList[lIdx].z = curVtxPointList[rIdx].z * mirZ
        for i in range(len(mVtxList)):
            cmds.progressBar('frMainStatePB', e=1, s=1)
            mIdx = mVtxList[i]
            finalVtxPointList[mIdx].x = curVtxPointList[mIdx].x * mirX
            finalVtxPointList[mIdx].y = curVtxPointList[mIdx].y * mirY
            finalVtxPointList[mIdx].z = curVtxPointList[mIdx].z * mirZ


    finally:
        cmds.progressBar('frMainStatePB', e=1, ep=1)
        cmds.progressBar('frMainStatePB', e=1, vis=0)

    mirMeshFn = sdd_getMfnMeshByName(mirMesh)
    mirMeshFn.setPoints(finalVtxPointList)


def sdd_getCurrentCatchCtrBs():
    selI = cmds.textScrollList('frCrtBsTSL', q=1, si=1)
    if (selI == None):
        return
    finalMeshName = selI[0] + '_CorrectiveBS'
    if not (cmds.objExists(finalMeshName)):
        return
    return finalMeshName


def sdd_mirrorAndResetCrtBS(typ):
    mirX, mirY, mirZ = -1, 1, 1

    finalMeshName = sdd_getCurrentCatchCtrBs()
    faceMesh, origMesh, ctrGrp, suf = sdd_getCtrMeshAnGrpInfo()
    if (sdd_calcMeshMirrorInfor(1) == False):
        return

    lVtxList = cmds.getAttr(ctrGrp + '.LeftVtxIdx')
    rVtxList = cmds.getAttr(ctrGrp + '.RightVtxIdx')

    finalMeshFn = sdd_getMfnMeshByName(finalMeshName)
    finalVPList = OpenMaya.MPointArray()
    finalMeshFn.getPoints(finalVPList)

    origMeshFn = sdd_getMfnMeshByName(origMesh)
    origVPList = OpenMaya.MPointArray()
    origMeshFn.getPoints(origVPList)

    if (typ == 'R<<L'):
        aVtxList = lVtxList
        bVtxList = rVtxList
    else:
        aVtxList = rVtxList
        bVtxList = lVtxList

    try:
        if (typ == 'Reset'):
            cmds.progressBar('frMainStatePB', e=1, max=finalVPList.length(), bp=1, vis=1)
            for i in range(finalVPList.length()):
                cmds.progressBar('frMainStatePB', e=1, s=1)

                if (finalVPList[i] == origVPList[i]):
                    continue
                vp = [origVPList[i].x, origVPList[i].y, origVPList[i].z]
                cmds.xform(finalMeshName + '.vtx[%s]' % i, ws=1, t=vp)
        else:
            cmds.progressBar('frMainStatePB', e=1, max=len(aVtxList), bp=1, vis=1)
            for i in aVtxList:
                cmds.progressBar('frMainStatePB', e=1, s=1)
                vp = [finalVPList[i].x * mirX, finalVPList[i].y * mirY, finalVPList[i].z * mirZ]
                mirI = bVtxList[aVtxList.index(i)]
                cmds.xform(finalMeshName + '.vtx[%s]' % mirI, ws=1, t=vp)


    finally:
        cmds.progressBar('frMainStatePB', e=1, ep=1)
        cmds.progressBar('frMainStatePB', e=1, vis=0)


def sdd_calcMeshMirrorInfor(typ):
    mirX, mirY, mirZ = -1, 1, 1
    faceMesh, origMesh, ctrGrp, suf = sdd_getCtrMeshAnGrpInfo()
    attrList = cmds.listAttr(ctrGrp, ud=1)
    if not ('MiddleVtxIdx' in attrList):
        cmds.addAttr(ctrGrp, ln='MiddleVtxIdx', dt='Int32Array')
        cmds.addAttr(ctrGrp, ln='LeftVtxIdx', dt='Int32Array')
        cmds.addAttr(ctrGrp, ln='RightVtxIdx', dt='Int32Array')
        cmds.addAttr(ctrGrp, ln='ErrorVtxIdx', dt='Int32Array')

    leftVtxIdx = cmds.getAttr(ctrGrp + '.LeftVtxIdx')

    if leftVtxIdx == None or typ == 2:
        meshFn = sdd_getMfnMeshByName(origMesh)

        vtxPointList = OpenMaya.MPointArray()
        mirPos = OpenMaya.MPoint()
        clostP = OpenMaya.MPoint()
        space = OpenMaya.MSpace.kObject
        util = OpenMaya.MScriptUtil()
        util.createFromInt(0)
        idPointer = util.asIntPtr()

        meshFn.getPoints(vtxPointList)
        mVtxList = []
        lVtxList = []
        rVtxList = []
        eVtxList = []

        cmds.progressBar('frMainStatePB', e=1, max=vtxPointList.length(), bp=1, vis=1)
        try:
            mirDis = cmds.floatField('frMirDisTF', q=1, v=1)
            for i in range(vtxPointList.length()):
                cmds.progressBar('frMainStatePB', e=1, s=1)
                curPos = vtxPointList[i]
                if (curPos.x < mirDis and curPos.x > -mirDis):
                    mVtxList.append(i)
                elif (curPos.x > mirDis):
                    mirPos.x = curPos.x * mirX
                    mirPos.y = curPos.y * mirY
                    mirPos.z = curPos.z * mirZ
                    meshFn.getClosestPoint(mirPos, clostP, space, idPointer)
                    idx = OpenMaya.MScriptUtil(idPointer).asInt()
                    nearestList = OpenMaya.MIntArray()
                    meshFn.getPolygonVertices(idx, nearestList)
                    tmpdis = None
                    retIdx = None
                    for d in nearestList:
                        dis = vtxPointList[d].distanceTo(mirPos)
                        if (tmpdis == None or dis < tmpdis):
                            tmpdis = dis
                            retIdx = d
                    if (vtxPointList[retIdx].distanceTo(mirPos) < mirDis and i != retIdx):
                        lVtxList.append(i)
                        rVtxList.append(retIdx)
                    else:
                        eVtxList.append(i)

        finally:
            cmds.progressBar('frMainStatePB', e=1, ep=1)
            cmds.progressBar('frMainStatePB', e=1, vis=0)

        if (len(lVtxList) + len(rVtxList) + len(mVtxList) == 0):
            eVtxList = range(vtxPointList.length())
        cmds.setAttr(ctrGrp + '.MiddleVtxIdx', mVtxList, typ='Int32Array')
        cmds.setAttr(ctrGrp + '.LeftVtxIdx', lVtxList, typ='Int32Array')
        cmds.setAttr(ctrGrp + '.RightVtxIdx', rVtxList, typ='Int32Array')
        cmds.setAttr(ctrGrp + '.ErrorVtxIdx', eVtxList, typ='Int32Array')
        if (len(lVtxList) == 0):
            cmds.confirmDialog(title='Mirror Error', message='This model can\'t Mirror.', button=['Yes'], db='Yes')
            return False
    return True


def sdd_inverseCaclBlendShape(outMeshName, skinMeshName, finalMeshName, skinNodeName):
    skinItMesh = sdd_getMItMeshVertexByName(skinMeshName)
    skinDagPath = sdd_getMDagPathByName(skinMeshName)
    finalItMesh = sdd_getMItMeshVertexByName(finalMeshName)
    mfnskin, origItMesh = sdd_getMfnSkinclusterByName(skinNodeName)

    preBindPlug = mfnskin.findPlug('bindPreMatrix')
    worldMatrixPlug = mfnskin.findPlug('matrix')

    exIdx = OpenMaya.MIntArray()
    worldMatrixPlug.getExistingArrayAttributeIndices(exIdx)
    mulMatrixList = []
    for i in exIdx:
        curPBPlug = preBindPlug.elementByLogicalIndex(i)
        curWDPlug = worldMatrixPlug.elementByLogicalIndex(i)
        if curWDPlug.isConnected():
            preBindMatrix = OpenMaya.MMatrix(OpenMaya.MFnMatrixData(curPBPlug.asMObject()).matrix())
            worldMatrix = OpenMaya.MMatrix(OpenMaya.MFnMatrixData(curWDPlug.asMObject()).matrix())
            mulMatrixList.append(preBindMatrix * worldMatrix)

    unitl = OpenMaya.MScriptUtil()
    unitl.createFromInt(0)
    countPtr = unitl.asUintPtr()
    outPointArray = OpenMaya.MPointArray()

    # origItMesh.reset()
    try:
        cmds.progressBar('frMainStatePB', e=1, max=skinItMesh.count(), bp=1, vis=1)
        for i in range(skinItMesh.count()):
            cmds.progressBar('frMainStatePB', e=1, s=1)
            # after matrix
            finalPoint = finalItMesh.position(OpenMaya.MSpace.kObject)
            skinPoint = skinItMesh.position(OpenMaya.MSpace.kObject)
            origPoint = origItMesh.position(OpenMaya.MSpace.kObject)
            outPoint = origPoint
            if (finalPoint != skinPoint):
                afterMatrix = sdd_convertPointToMatrix(finalPoint)
                skinMatrix = sdd_convertPointToMatrix(skinPoint)
                # weight
                wt = OpenMaya.MFloatArray()
                mfnskin.getWeights(skinDagPath, skinItMesh.currentItem(), wt, countPtr)
                # unit matrix
                unitMatrix = sdd_createZeroMatrix()
                for a in range(len(mulMatrixList)):
                    if (wt[a] != 0):
                        unitMatrix += mulMatrixList[a] * wt[a]
                # inverse cacl
                inverseMatrix = unitMatrix.inverse()
                finalbeforeMatrix = afterMatrix * inverseMatrix
                skinBeforeMatrix = skinMatrix * inverseMatrix
                finalBeforePoint = sdd_convertMatrixToPoint(finalbeforeMatrix)
                skinBeforePoint = sdd_convertMatrixToPoint(skinBeforeMatrix)

                if (finalBeforePoint != finalPoint):
                    outPoint = origPoint + (finalBeforePoint - skinBeforePoint)

            outPointArray.append(outPoint)

            finalItMesh.next()
            skinItMesh.next()
            origItMesh.next()

    finally:
        cmds.progressBar('frMainStatePB', e=1, ep=1)
        cmds.progressBar('frMainStatePB', e=1, vis=0)

    meshPolygon = sdd_getMfnMeshByName(outMeshName)
    meshPolygon.setPoints(outPointArray, OpenMaya.MSpace.kObject)


def sdd_printMatrix(inputMatrix):
    returnList = []
    for row in range(0, 4):
        for col in range(0, 4):
            matrixValue = 0.0
            matrixValue = OpenMaya.MScriptUtil.getDoubleArrayItem(inputMatrix[row], col)
            returnList.append(matrixValue)
    print returnList


def sdd_convertMatrixToPoint(mMatrix):
    x = OpenMaya.MScriptUtil.getDoubleArrayItem(mMatrix[3], 0)
    y = OpenMaya.MScriptUtil.getDoubleArrayItem(mMatrix[3], 1)
    z = OpenMaya.MScriptUtil.getDoubleArrayItem(mMatrix[3], 2)
    newPoint = OpenMaya.MPoint(x, y, z)
    return newPoint


def sdd_convertPointToMatrix(mpoint):
    mMatrix = OpenMaya.MMatrix()
    tmpList = [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, mpoint.x, mpoint.y, mpoint.z, 1]
    OpenMaya.MScriptUtil.createMatrixFromList(tmpList, mMatrix)
    return mMatrix


def sdd_createZeroMatrix():
    mMatrix = OpenMaya.MMatrix()
    tmpList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    OpenMaya.MScriptUtil.createMatrixFromList(tmpList, mMatrix)
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
    mFnSkinCluster = OpenMayaAnim.MFnSkinCluster(mObj)
    inpuObjArray = OpenMaya.MObjectArray()
    mFnSkinCluster.getInputGeometry(inpuObjArray)
    meshItPolygon = OpenMaya.MItMeshVertex(inpuObjArray[0])
    return mFnSkinCluster, meshItPolygon


def sdd_caclCtrBsPuff(typ):
    global ctrBsPuffDate
    finalMesh = sdd_getCurrentCatchCtrBs()
    unitl = OpenMaya.MScriptUtil()
    unitl.createFromInt(0)
    preInt = unitl.asIntPtr()

    if (finalMesh == None):
        return
    if (ctrBsPuffDate == None):
        ctrBsPuffDate = []
        faceMesh, origMesh, ctrGrp, suf = sdd_getCtrMeshAnGrpInfo()

        finalMeshFn = sdd_getMfnMeshByName(finalMesh)
        finalVPList = OpenMaya.MPointArray()
        finalMeshFn.getPoints(finalVPList)
        finalMeshIt = sdd_getMItMeshVertexByName(finalMesh)

        origMeshFn = sdd_getMfnMeshByName(origMesh)
        origVPList = OpenMaya.MPointArray()
        origMeshFn.getPoints(origVPList)
        origMeshIt = sdd_getMItMeshVertexByName(origMesh)

        try:
            step = 3
            cmds.progressBar('frMainStatePB', e=1, max=origMeshIt.count() * (4 + step), bp=1, vis=1)
            nearList = []
            nearWList = []
            for i in range(origMeshIt.count()):
                cmds.progressBar('frMainStatePB', e=1, s=1)

                idArray = OpenMaya.MIntArray()
                origMeshIt.getConnectedVertices(idArray)
                nearList.append(idArray)
                curP = origMeshIt.position()
                nearDis = []
                disSum = 0
                for i in idArray:
                    origMeshIt.setIndex(i, preInt)
                    dis = curP.distanceTo(origMeshIt.position())
                    disSum += dis
                    nearDis.append(dis)
                invList = []
                invSum = 0
                for i in nearDis:
                    inv = disSum / i
                    invSum += inv
                    invList.append(inv)
                nearW = []
                for i in invList:
                    nearW.append(i / invSum)
                nearWList.append(nearW)
                origMeshIt.next()
            normalList = []
            for i in range(finalMeshIt.count()):
                cmds.progressBar('frMainStatePB', e=1, s=1)

                normal = OpenMaya.MVector()
                finalMeshIt.getNormal(normal)
                normalList.append(normal)
                finalMeshIt.next()

            wtList = []
            maxWt = 0
            for i in range(finalVPList.length()):
                cmds.progressBar('frMainStatePB', e=1, s=1)
                if (finalVPList[i] == origVPList[i]):
                    wtList.append(0)
                else:
                    weight = 0
                    for near in nearList[i]:
                        dis1 = finalVPList[near].distanceTo(finalVPList[i])
                        dis2 = origVPList[near].distanceTo(origVPList[i])
                        if (dis1 < dis2):
                            weight += (dis2 - dis1)
                    if (maxWt < weight):
                        maxWt = weight

                    wtList.append(weight)

            smoothValue = 0.5
            for a in range(3):
                for i in range(len(wtList)):
                    cmds.progressBar('frMainStatePB', e=1, s=1)
                    wt = wtList[i]
                    nWt = 0
                    for near in range(nearList[i].length()):
                        nIdx = nearList[i][near]
                        nDisWt = nearWList[i][near]
                        nWt += wtList[nIdx] * nDisWt
                    wt = wt * (1 - smoothValue) + nWt * smoothValue
                    wtList[i] = wt
            for i in range(len(wtList)):
                cmds.progressBar('frMainStatePB', e=1, s=1)
                if (wtList[i] != 0):
                    ctrBsPuffDate.append([i, wtList[i], normalList[i]])
                    # cmds.polyColorPerVertex(finalMesh+'.vtx[%s]'%i,r=wtList[i]/maxWt,g=0,b=0,a=1,cdo=1)

        finally:
            cmds.progressBar('frMainStatePB', e=1, ep=1)
            cmds.progressBar('frMainStatePB', e=1, vis=0)

    try:
        finalMeshIt = sdd_getMItMeshVertexByName(finalMesh)
        cmds.progressBar('frMainStatePB', e=1, max=len(ctrBsPuffDate), bp=1, vis=1)

        mul = cmds.floatSlider('frCtrBsPuffFS', q=1, v=1)
        if (typ == '-'):
            mul *= -1

        for i in range(len(ctrBsPuffDate)):
            cmds.progressBar('frMainStatePB', e=1, s=1)
            idx = ctrBsPuffDate[i][0]
            wt = ctrBsPuffDate[i][1]
            normal = ctrBsPuffDate[i][2]
            finalMeshIt.setIndex(idx, preInt)
            finalMeshIt.translateBy(normal * wt * mul)
    finally:
        cmds.progressBar('frMainStatePB', e=1, ep=1)
        cmds.progressBar('frMainStatePB', e=1, vis=0)


# defult setDrivenKeyframe____________________________________________________________________________________====
def sdd_getDefultSdkName():
    T = sdd_returnTempNameDirc()
    FR, FRJntPos, FRUIPos = sdd_frTNameDirc()
    _sdk = T['_sdk']
    _root = T['_root']
    _cnt = T['_cnt']
    faceSdkHandle = 'face_sdk_handle'
    faceCur = 'faceMoveCur'
    return FR, _sdk, _root, _cnt, faceSdkHandle, faceCur


def sdd_initDistanceAttr():
    FR, _sdk, _root, _cnt, faceSdkHandle, faceCur = sdd_getDefultSdkName()

    attr = sdd_tryAddFloatAttr(faceCur, 'eyeBrow_factor')
    objList = [FR['M_brow'] + _cnt, FR['L_brow_a'] + _cnt, FR['L_brow_b'] + _cnt, FR['L_brow_c'] + _cnt]
    dis = sdd_getAvergeDistance(objList)
    cmds.setAttr(attr, dis)

    attr = sdd_tryAddFloatAttr(faceCur, 'eyeBall_factor')
    objList = [FR['R_eyeBall'] + _cnt, FR['L_eyeBall'] + _cnt]
    dis = sdd_getAvergeDistance(objList)
    cmds.setAttr(attr, dis)

    attr = sdd_tryAddFloatAttr(faceCur, 'eyeLid_factor')
    objList = [FR['L_eyelid_Up'] + _cnt, FR['L_eyelid_UpOut'] + _cnt, FR['L_eyelid_Out'] + _cnt,
               FR['L_eyelid_DnOut'] + _cnt, FR['L_eyelid_Dn'] + _cnt]
    dis = sdd_getAvergeDistance(objList)
    cmds.setAttr(attr, dis)

    attr = sdd_tryAddFloatAttr(faceCur, 'eyeAngle_factor')
    objList = [FR['L_eyelid_Up'] + _cnt, FR['L_eye_root'] + _cnt, FR['L_eyelid_Dn'] + _cnt]
    dis = sdd_getAngleThreePoint(objList)
    cmds.setAttr(attr, dis)

    attr = sdd_tryAddFloatAttr(faceCur, 'nose_factor')
    objList = [FR['L_nose'] + _cnt, FR['M_nose'] + _cnt, FR['R_nose'] + _cnt]
    dis = sdd_getAvergeDistance(objList)
    cmds.setAttr(attr, dis)

    attr = sdd_tryAddFloatAttr(faceCur, 'cheek_factor')
    objList = [FR['L_cheek_In'] + _cnt, FR['L_cheek_Up'] + _cnt, FR['L_cheek_Out'] + _cnt]
    dis = sdd_getAvergeDistance(objList)
    cmds.setAttr(attr, dis)

    attr = sdd_tryAddFloatAttr(faceCur, 'mouth_factor')
    objList = [FR['M_mouth_Up'] + _cnt, FR['L_mouth_Up'] + _cnt, FR['L_mouth_Corner'] + _cnt, FR['L_mouth_Dn'] + _cnt,
               FR['M_mouth_Dn'] + _cnt]
    dis = sdd_getAvergeDistance(objList)
    cmds.setAttr(attr, dis)


def sdd_saveSdkToFile():
    path = cmds.fileDialog2(ff='SDK Files(*.sdk)', ds=2, fm=0)
    if (path == None):
        return

    FR, _sdk, _root, _cnt, faceSdkHandle, faceCur = sdd_getDefultSdkName()

    allCntList = sdd_returnAllSdkCntList()
    if (len(allCntList) == 0):
        return

    sdkAttrList = cmds.listAttr(faceSdkHandle, ud=1)
    for attr in sdkAttrList:
        cmds.setAttr(faceSdkHandle + '.' + attr, 0)

    attrList = ['tx', 'ty', 'tz', 'rx', 'ry', 'rz', 'sx', 'sy', 'sz']
    valueList = [0, 0, 0, 0, 0, 0, 1, 1, 1]
    fAttrList = ['tx', 'ty', 'tz']

    sdkList = []

    try:
        cmds.progressWindow(t='Save SDK', pr=0, st=path[0], max=len(sdkAttrList))
        for sdkAttr in sdkAttrList:

            cmds.progressWindow(e=1, s=1)
            minVal = cmds.addAttr(faceSdkHandle + '.' + sdkAttr, q=1, min=1)
            maxVal = cmds.addAttr(faceSdkHandle + '.' + sdkAttr, q=1, max=1)
            if (minVal == maxVal):
                continue

            sdkList.append('@' + sdkAttr)
            cmds.setAttr(faceSdkHandle + '.' + sdkAttr, 1)

            for i in allCntList:
                sdk = i + _sdk
                transformList = [None, None, None, None, None, None, None, None, None]
                isMove = 0
                for idx in range(len(attrList)):
                    # val=cmds.getAttr(sdk+'.'+attrList[idx])
                    attr = sdk + '.' + attrList[idx]
                    cdAttr = faceSdkHandle + '.' + sdkAttr
                    animNode = sdd_getSDKAnimCurveNode(attr, cdAttr)
                    # round(val,4)!=valueList[idx] and
                    fVal = sdd_getSdkFactor(i)
                    if (animNode != None):
                        idxList = cmds.keyframe(animNode, q=1, iv=1)
                        valList = cmds.keyframe(animNode, q=1, vc=1)

                        for v in range(len(valList)):
                            if (attrList[idx] in fAttrList):
                                valList[v] /= fVal

                        transformList[idx] = [idxList, valList]
                        isMove = 1
                if (isMove):
                    sdkList.append(i + '^' + str(transformList))
            cmds.setAttr(faceSdkHandle + '.' + sdkAttr, 0)

    finally:
        cmds.progressWindow(ep=1)

    f = open(path[0], 'w')
    try:
        for i in sdkList:
            f.write(i)
            f.write(os.linesep)
    finally:
        f.close()


def sdd_loadSdkFromFile():
    FR, _sdk, _root, _cnt, faceSdkHandle, faceCur = sdd_getDefultSdkName()

    path = cmds.fileDialog2(ff='SDK Files(*.sdk)', ds=2, fm=1)
    if (path == None):
        return
    f = open(path[0], 'r')
    sdkList = []
    try:
        while True:
            temp = f.readline()
            if (not temp):
                break
            temp = temp.strip('\r\n')
            sdkList.append(temp)
    finally:
        f.close()

    setSDKList = []
    cntList = []
    for i in sdkList:
        if (i[0] == '@'):
            if (len(cntList) > 0):
                setSDKList.append([sdkAttr, cntList])
            sdkAttr = i[1:]
            cntList = []

        else:
            cnt, transformList = i.split('^')
            transformList = sdd_eval(transformList)
            cntList.append([cnt, transformList])
    setSDKList.append([sdkAttr, cntList])

    attrList = ['tx', 'ty', 'tz', 'rx', 'ry', 'rz', 'sx', 'sy', 'sz']
    fAttrList = ['tx', 'ty', 'tz']

    try:
        cmds.progressWindow(t='Load SDK', pr=0, st=path[0], max=len(setSDKList))
        for i in setSDKList:
            cmds.progressWindow(e=1, s=1)

            sdkAttr = i[0]
            cdAttr = faceSdkHandle + '.' + sdkAttr
            cntList = i[1]
            print sdkAttr

            for cI in cntList:

                cnt = cI[0] + _sdk

                transformList = cI[1]
                fVal = sdd_getSdkFactor(i)
                # delete Anim
                for a in attrList:
                    attr = cnt + '.' + a

                    animNode = sdd_getSDKAnimCurveNode(attr, cdAttr)
                    print '%s-%s-%s' % (cdAttr, attr, animNode)
                    if (animNode != None):
                        cmds.delete(animNode)
                # SDK
                for aI in range(len(attrList)):
                    attr = cnt + '.' + attrList[aI]
                    if (transformList[aI] == None):
                        continue
                    idxList = transformList[aI][0]
                    valList = transformList[aI][1]

                    for iv in range(len(idxList)):
                        if (attrList[aI] in fAttrList):
                            cmds.setDrivenKeyframe(attr, cd=cdAttr, v=valList[iv] * fVal, dv=idxList[iv], itt='linear',
                                                   ott='linear')
                        else:
                            cmds.setDrivenKeyframe(attr, cd=cdAttr, v=valList[iv], dv=idxList[iv], itt='linear',
                                                   ott='linear')
    finally:
        cmds.progressWindow(ep=1)


def sdd_eval(sCmd):
    return sys.modules['__builtin__'].eval(sCmd)


def sdd_getSdkFactor(cnt):
    FR, _sdk, _root, _cnt, faceSdkHandle, faceCur = sdd_getDefultSdkName()
    eyeBrow_factor = cmds.getAttr(faceCur + '.eyeBrow_factor')
    eyeBall_factor = cmds.getAttr(faceCur + '.eyeBall_factor')
    eyeLid_factor = cmds.getAttr(faceCur + '.eyeLid_factor')
    eyeAngle_factor = cmds.getAttr(faceCur + '.eyeAngle_factor')
    nose_factor = cmds.getAttr(faceCur + '.nose_factor')
    cheek_factor = cmds.getAttr(faceCur + '.cheek_factor')
    mouth_factor = cmds.getAttr(faceCur + '.mouth_factor')
    avg_factor = (eyeBrow_factor + eyeBall_factor + eyeLid_factor + nose_factor + cheek_factor + mouth_factor) / 6

    browList = [FR['M_brow'], FR['L_brow_a'], FR['L_brow_b'], FR['L_brow_c'], FR['R_brow_a'], FR['R_brow_b'],
                FR['R_brow_c'], FR['L_temple'], FR['R_temple'], FR['L_eyeSag_Up'], FR['R_eyeSag_Up']]
    eyeBallList = [FR['L_eye_root'], FR['R_eye_root']]
    eyeLidList = [FR['L_eyelid_Up'], FR['L_eyelid_UpOut'], FR['L_eyelid_Out'], FR['L_eyelid_DnOut'], FR['L_eyelid_Dn'],
                  FR['L_eyelid_DnIn'], FR['L_eyelid_In'], FR['L_eyelid_UpIn']]
    eyeAngleList = [FR['L_eyelid_Up'] + _root, FR['L_eyelid_Dn'] + _root, FR['R_eyelid_Up'] + _root,
                    FR['R_eyelid_Dn'] + _root]
    noseList = [FR['L_nose'], FR['R_nose'], FR['M_nose'], FR['L_noseFold'], FR['R_noseFold']]
    cheekList = [FR['L_cheek_In'], FR['L_cheek_Up'], FR['L_cheek_Out'], FR['L_cheek'], FR['R_cheek_In'],
                 FR['R_cheek_Up'], FR['R_cheek_Out'], FR['R_cheek'], FR['L_eyeSag_Dn'], FR['R_eyeSag_Dn']]
    mouthList = [FR['M_mouth_Up'], FR['L_mouth_Up'], FR['L_mouth_Corner'], FR['L_mouth_Dn'], FR['M_mouth_Dn'],
                 FR['R_mouth_Dn'], FR['R_mouth_Corner'], FR['R_mouth_Up']]

    if (cnt in browList):
        return eyeBrow_factor
    elif (cnt in eyeBallList):
        return eyeBall_factor
    elif (cnt in eyeLidList):
        return eyeLid_factor
    elif (cnt in eyeAngleList):
        return eyeAngle_factor
    elif (cnt in noseList):
        return nose_factor
    elif (cnt in cheekList):
        return cheek_factor
    elif (cnt in mouthList):
        return mouth_factor
    else:
        return avg_factor


def sdd_tryAddFloatAttr(faceCur, attrName):
    exList = cmds.listAttr(faceCur, ud=1)
    if (not attrName in exList):
        cmds.addAttr(faceCur, ln=attrName, at='double', min=0, k=0)
        cmds.setAttr(faceCur + '.' + attrName, cb=1)
    return faceCur + '.' + attrName


def sdd_createDefultSdk():
    FR, _sdk, _root, _cnt, faceSdkHandle, faceCur = sdd_getDefultSdkName()
    faceBaseGrp = 'face_base_rig_grp'
    if (not cmds.objExists(faceBaseGrp)):
        return
    faceSdkHandle = cmds.group(n=faceSdkHandle, em=1)
    cmds.parent(faceSdkHandle, faceBaseGrp)
    attrList = ['tx', 'ty', 'tz', 'rx', 'ry', 'rz', 'sx', 'sy', 'sz', 'v']
    sdd_frLockAndAttr(faceSdkHandle, attrList)
    sdd_browDefultSdk()
    sdd_eyeballDefultSdk()
    sdd_eyelidDefultSdk()
    sdd_noseDefultSdk()
    sdd_cheekDefultSdk()
    sdd_mouthDefultSdk()
    sdd_mouthShapeDefultSdk()


def sdd_getAvergeDistance(objList):
    posList = []
    for i in objList:
        pos = cmds.xform(i, q=1, ws=1, t=1)
        posList.append(pos)
    tempCur = cmds.curve(n='temp_dis_curve', d=1, p=posList)
    dis = cmds.arclen(tempCur, ch=0)
    val = round(dis / len(objList), 3)
    cmds.delete(tempCur)
    return val


def sdd_browDefultSdk():
    FR, _sdk, _root, _cnt, faceSdkHandle, faceCur = sdd_getDefultSdkName()

    # brow
    cmds.addAttr(faceSdkHandle, ln='______brow________', at='double', min=0, max=0, k=0)
    cmds.setAttr(faceSdkHandle + '.' + '______brow________', cb=1)

    dis = cmds.getAttr(faceCur + '.eyeBrow_factor')

    cdAttr = sdd_addAttrToHandle('M_brow_U', None, faceSdkHandle)
    sdd_setDrivenKeyframe(FR['M_brow'] + _sdk, 'ty', dis, faceSdkHandle, cdAttr, 1)
    cdAttr = sdd_addAttrToHandle('M_brow_D', None, faceSdkHandle)
    sdd_setDrivenKeyframe(FR['M_brow'] + _sdk, 'ty', -dis, faceSdkHandle, cdAttr, 1)

    cdAttr, mircdAttr = sdd_addAttrToHandle('L_brow_In_U', 'R_brow_In_U', faceSdkHandle)
    sdd_setDrivenKeyframe(FR['L_brow_a'] + _sdk, 'ty', dis, faceSdkHandle, cdAttr, 1, mircdAttr)
    sdd_setDrivenKeyframe(FR['L_brow_b'] + _sdk, 'ty', dis * 0.5, faceSdkHandle, cdAttr, 1, mircdAttr)

    cdAttr, mircdAttr = sdd_addAttrToHandle('L_brow_In_D', 'R_brow_In_D', faceSdkHandle)
    sdd_setDrivenKeyframe(FR['L_brow_a'] + _sdk, 'ty', -dis, faceSdkHandle, cdAttr, 1, mircdAttr)
    sdd_setDrivenKeyframe(FR['L_brow_b'] + _sdk, 'ty', -dis * 0.5, faceSdkHandle, cdAttr, 1, mircdAttr)

    cdAttr, mircdAttr = sdd_addAttrToHandle('L_brow_Out_U', 'R_brow_Out_U', faceSdkHandle)
    sdd_setDrivenKeyframe(FR['L_brow_c'] + _sdk, 'ty', dis, faceSdkHandle, cdAttr, 1, mircdAttr)
    sdd_setDrivenKeyframe(FR['L_brow_b'] + _sdk, 'ty', dis * 0.5, faceSdkHandle, cdAttr, 1, mircdAttr)

    cdAttr, mircdAttr = sdd_addAttrToHandle('L_brow_Out_D', 'R_brow_Out_D', faceSdkHandle)
    sdd_setDrivenKeyframe(FR['L_brow_c'] + _sdk, 'ty', -dis, faceSdkHandle, cdAttr, 1, mircdAttr)
    sdd_setDrivenKeyframe(FR['L_brow_b'] + _sdk, 'ty', -dis * 0.5, faceSdkHandle, cdAttr, 1, mircdAttr)

    cdAttr, mircdAttr = sdd_addAttrToHandle('L_brow_Mid_U', 'R_brow_Mid_U', faceSdkHandle)
    sdd_setDrivenKeyframe(FR['L_brow_b'] + _sdk, 'ty', dis * 0.5, faceSdkHandle, cdAttr, 1, mircdAttr)

    cdAttr, mircdAttr = sdd_addAttrToHandle('L_brow_Mid_D', 'R_brow_Mid_D', faceSdkHandle)
    sdd_setDrivenKeyframe(FR['L_brow_b'] + _sdk, 'ty', -dis * 0.5, faceSdkHandle, cdAttr, 1, mircdAttr)

    cdAttr, mircdAttr = sdd_addAttrToHandle('L_brow_In_In', 'R_brow_In_In', faceSdkHandle)
    sdd_setDrivenKeyframe(FR['L_brow_a'] + _sdk, 'tx', -dis * 0.5, faceSdkHandle, cdAttr, 1, mircdAttr)


def sdd_eyeballDefultSdk():
    FR, _sdk, _root, _cnt, faceSdkHandle, faceCur = sdd_getDefultSdkName()

    # eyeball
    cmds.addAttr(faceSdkHandle, ln='______eyeBall______', at='double', min=0, max=0, k=0)
    cmds.setAttr(faceSdkHandle + '.______eyeBall______', cb=1)
    dis = cmds.getAttr(faceCur + '.eyeBall_factor')

    cdAttr, mircdAttr = sdd_addAttrToHandle('L_eyeBall_U', 'R_eyeBall_U', faceSdkHandle)
    sdd_setDrivenKeyframe(FR['L_eyeBall'] + _sdk, 'rx', -70, faceSdkHandle, cdAttr, 1, mircdAttr)
    cdAttr, mircdAttr = sdd_addAttrToHandle('L_eyeBall_D', 'R_eyeBall_D', faceSdkHandle)
    sdd_setDrivenKeyframe(FR['L_eyeBall'] + _sdk, 'rx', 70, faceSdkHandle, cdAttr, 1, mircdAttr)
    cdAttr, mircdAttr = sdd_addAttrToHandle('L_eyeBall_O', 'R_eyeBall_O', faceSdkHandle)
    sdd_setDrivenKeyframe(FR['L_eyeBall'] + _sdk, 'ry', 70, faceSdkHandle, cdAttr, 1, mircdAttr)
    cdAttr, mircdAttr = sdd_addAttrToHandle('L_eyeBall_I', 'R_eyeBall_I', faceSdkHandle)
    sdd_setDrivenKeyframe(FR['L_eyeBall'] + _sdk, 'ry', -70, faceSdkHandle, cdAttr, 1, mircdAttr)

    cdAttr, mircdAttr = sdd_addAttrToHandle('L_eyeAll_U', 'R_eyeAll_U', faceSdkHandle)
    sdd_setDrivenKeyframe(FR['L_eye_root'] + _sdk, 'ty', dis * 0.5, faceSdkHandle, cdAttr, 1, mircdAttr)
    cdAttr, mircdAttr = sdd_addAttrToHandle('L_eyeAll_D', 'R_eyeAll_D', faceSdkHandle)
    sdd_setDrivenKeyframe(FR['L_eye_root'] + _sdk, 'ty', -dis * 0.5, faceSdkHandle, cdAttr, 1, mircdAttr)
    cdAttr, mircdAttr = sdd_addAttrToHandle('L_eyeAll_O', 'R_eyeAll_O', faceSdkHandle)
    sdd_setDrivenKeyframe(FR['L_eye_root'] + _sdk, 'tx', dis * 0.5, faceSdkHandle, cdAttr, 1, mircdAttr)
    cdAttr, mircdAttr = sdd_addAttrToHandle('L_eyeAll_I', 'R_eyeAll_I', faceSdkHandle)
    sdd_setDrivenKeyframe(FR['L_eye_root'] + _sdk, 'tx', -dis * 0.5, faceSdkHandle, cdAttr, 1, mircdAttr)


def sdd_eyelidDefultSdk():
    FR, _sdk, _root, _cnt, faceSdkHandle, faceCur = sdd_getDefultSdkName()
    # eyelid
    cmds.addAttr(faceSdkHandle, ln='______eyelid______', at='double', min=0, max=0, k=0)
    cmds.setAttr(faceSdkHandle + '.______eyelid______', cb=1)

    arcMid = cmds.getAttr(faceCur + '.eyeAngle_factor')

    cdAttr, mircdAttr = sdd_addAttrToHandle('L_eyelid_Up_U', 'R_eyelid_Up_U', faceSdkHandle)
    sdd_setDrivenKeyframe(FR['L_eyelid_Up'] + _root + _sdk, 'rx', -5, faceSdkHandle, cdAttr, 1, mircdAttr)

    cdAttr, mircdAttr = sdd_addAttrToHandle('L_eyelid_Up_D', 'R_eyelid_Up_D', faceSdkHandle)
    sdd_setDrivenKeyframe(FR['L_eyelid_Up'] + _root + _sdk, 'rx', arcMid + 2, faceSdkHandle, cdAttr, 1, mircdAttr)

    cdAttr, mircdAttr = sdd_addAttrToHandle('L_eyelid_Dn_U', 'R_eyelid_Dn_U', faceSdkHandle)
    sdd_setDrivenKeyframe(FR['L_eyelid_Dn'] + _root + _sdk, 'rx', -arcMid - 2, faceSdkHandle, cdAttr, 1, mircdAttr)

    cdAttr, mircdAttr = sdd_addAttrToHandle('L_eyelid_Dn_D', 'R_eyelid_Dn_D', faceSdkHandle)
    sdd_setDrivenKeyframe(FR['L_eyelid_Dn'] + _root + _sdk, 'rx', 5, faceSdkHandle, cdAttr, 1, mircdAttr)

    cdAttr, mircdAttr = sdd_addAttrToHandle('L_eyelid_Up_side_O', 'R_eyelid_Up_side_O', faceSdkHandle)
    sdd_setDrivenKeyframe(FR['L_eyelid_UpIn'] + _root + _sdk, 'rx', 15, faceSdkHandle, cdAttr, 1, mircdAttr)
    sdd_setDrivenKeyframe(FR['L_eyelid_Up'] + _sdk, 'rz', 15, faceSdkHandle, cdAttr, 1, mircdAttr)
    sdd_setDrivenKeyframe(FR['L_eyelid_UpOut'] + _root + _sdk, 'rx', -15, faceSdkHandle, cdAttr, 1, mircdAttr)

    cdAttr, mircdAttr = sdd_addAttrToHandle('L_eyelid_Up_side_I', 'R_eyelid_Up_side_I', faceSdkHandle)
    sdd_setDrivenKeyframe(FR['L_eyelid_UpIn'] + _root + _sdk, 'rx', -15, faceSdkHandle, cdAttr, 1, mircdAttr)
    sdd_setDrivenKeyframe(FR['L_eyelid_Up'] + _sdk, 'rz', -15, faceSdkHandle, cdAttr, 1, mircdAttr)
    sdd_setDrivenKeyframe(FR['L_eyelid_UpOut'] + _root + _sdk, 'rx', 15, faceSdkHandle, cdAttr, 1, mircdAttr)

    cdAttr, mircdAttr = sdd_addAttrToHandle('L_eyelid_Dn_side_O', 'R_eyelid_Dn_side_O', faceSdkHandle)
    sdd_setDrivenKeyframe(FR['L_eyelid_DnIn'] + _root + _sdk, 'rx', -15, faceSdkHandle, cdAttr, 1, mircdAttr)
    sdd_setDrivenKeyframe(FR['L_eyelid_Dn'] + _sdk, 'rz', -15, faceSdkHandle, cdAttr, 1, mircdAttr)
    sdd_setDrivenKeyframe(FR['L_eyelid_DnOut'] + _root + _sdk, 'rx', 15, faceSdkHandle, cdAttr, 1, mircdAttr)

    cdAttr, mircdAttr = sdd_addAttrToHandle('L_eyelid_Dn_side_I', 'R_eyelid_Dn_side_I', faceSdkHandle)
    sdd_setDrivenKeyframe(FR['L_eyelid_DnIn'] + _root + _sdk, 'rx', 15, faceSdkHandle, cdAttr, 1, mircdAttr)
    sdd_setDrivenKeyframe(FR['L_eyelid_Dn'] + _sdk, 'rz', 15, faceSdkHandle, cdAttr, 1, mircdAttr)
    sdd_setDrivenKeyframe(FR['L_eyelid_DnOut'] + _root + _sdk, 'rx', -15, faceSdkHandle, cdAttr, 1, mircdAttr)

    cdAttr, mircdAttr = sdd_addAttrToHandle('L_eyelid_close', 'R_eyelid_close', faceSdkHandle)
    sdd_setDrivenKeyframe(FR['L_eyelid_Up'] + _root + _sdk, 'rx', (arcMid + 2) * 0.7, faceSdkHandle, cdAttr, 1,
                          mircdAttr)
    sdd_setDrivenKeyframe(FR['L_eyelid_Dn'] + _root + _sdk, 'rx', (-arcMid - 2) * 0.3, faceSdkHandle, cdAttr, 1,
                          mircdAttr)

    cdAttr, mircdAttr = sdd_addAttrToHandle('L_eyelid_Squint', 'R_eyelid_Squint', faceSdkHandle)
    sdd_setDrivenKeyframe(FR['L_eyelid_Up'] + _root + _sdk, 'rx', (arcMid + 2) * 0.7, faceSdkHandle, cdAttr, 1,
                          mircdAttr)
    sdd_setDrivenKeyframe(FR['L_eyelid_Dn'] + _root + _sdk, 'rx', (-arcMid - 2) * 0.3, faceSdkHandle, cdAttr, 1,
                          mircdAttr)
    dis = cmds.getAttr(faceCur + '.eyeBrow_factor')

    sdd_setDrivenKeyframe(FR['L_brow_a'] + _sdk, 'ty', -dis * 0.8, faceSdkHandle, cdAttr, 1, mircdAttr)
    sdd_setDrivenKeyframe(FR['L_brow_b'] + _sdk, 'ty', -dis * 0.8, faceSdkHandle, cdAttr, 1, mircdAttr)
    sdd_setDrivenKeyframe(FR['L_brow_c'] + _sdk, 'ty', -dis * 0.8, faceSdkHandle, cdAttr, 1, mircdAttr)

    sdd_setDrivenKeyframe(FR['L_eyeSag_Up'] + _sdk, 'ty', -dis * 0.4, faceSdkHandle, cdAttr, 1, mircdAttr)

    sdd_setDrivenKeyframe(FR['L_eyeSag_Dn'] + _sdk, 'ty', dis * 0.25, faceSdkHandle, cdAttr, 1, mircdAttr)
    sdd_setDrivenKeyframe(FR['L_cheek_In'] + _sdk, 'ty', dis * 0.4, faceSdkHandle, cdAttr, 1, mircdAttr)
    sdd_setDrivenKeyframe(FR['L_cheek_Up'] + _sdk, 'ty', dis * 0.6, faceSdkHandle, cdAttr, 1, mircdAttr)
    sdd_setDrivenKeyframe(FR['L_cheek_Out'] + _sdk, 'ty', dis * 0.9, faceSdkHandle, cdAttr, 1, mircdAttr)


def sdd_noseDefultSdk():
    FR, _sdk, _root, _cnt, faceSdkHandle, faceCur = sdd_getDefultSdkName()
    # nose
    cmds.addAttr(faceSdkHandle, ln='______nose________', at='double', min=0, max=0, k=0)
    cmds.setAttr(faceSdkHandle + '.______nose________', cb=1)

    cdAttr = sdd_addAttrToHandle('M_nose_U', None, faceSdkHandle)
    sdd_setDrivenKeyframe(FR['M_nose'] + _root + _sdk, 'rx', -30, faceSdkHandle, cdAttr, 1)
    cdAttr = sdd_addAttrToHandle('M_nose_D', None, faceSdkHandle)
    sdd_setDrivenKeyframe(FR['M_nose'] + _root + _sdk, 'rx', 15, faceSdkHandle, cdAttr, 1)
    cdAttr = sdd_addAttrToHandle('M_nose_L', None, faceSdkHandle)
    sdd_setDrivenKeyframe(FR['M_nose'] + _root + _sdk, 'rz', 30, faceSdkHandle, cdAttr, 1)
    cdAttr = sdd_addAttrToHandle('M_nose_R', None, faceSdkHandle)
    sdd_setDrivenKeyframe(FR['M_nose'] + _root + _sdk, 'rz', -30, faceSdkHandle, cdAttr, 1)

    dis = cmds.getAttr(faceCur + '.nose_factor')

    cdAttr, mircdAttr = sdd_addAttrToHandle('L_nose_U', 'R_nose_U', faceSdkHandle)
    sdd_setDrivenKeyframe(FR['L_nose'] + _sdk, 'ty', dis * 0.25, faceSdkHandle, cdAttr, 1, mircdAttr)
    cdAttr, mircdAttr = sdd_addAttrToHandle('L_nose_D', 'R_nose_D', faceSdkHandle)
    sdd_setDrivenKeyframe(FR['L_nose'] + _sdk, 'ty', -dis * 0.25, faceSdkHandle, cdAttr, 1, mircdAttr)
    cdAttr, mircdAttr = sdd_addAttrToHandle('L_nose_O', 'R_nose_O', faceSdkHandle)
    sdd_setDrivenKeyframe(FR['L_nose'] + _sdk, 'tx', dis * 0.25, faceSdkHandle, cdAttr, 1, mircdAttr)
    cdAttr, mircdAttr = sdd_addAttrToHandle('L_nose_I', 'R_nose_I', faceSdkHandle)
    sdd_setDrivenKeyframe(FR['L_nose'] + _sdk, 'tx', -dis * 0.25, faceSdkHandle, cdAttr, 1, mircdAttr)


def sdd_cheekDefultSdk():
    FR, _sdk, _root, _cnt, faceSdkHandle, faceCur = sdd_getDefultSdkName()
    # cheek
    cmds.addAttr(faceSdkHandle, ln='______cheek_______', at='double', min=0, max=0, k=0)
    cmds.setAttr(faceSdkHandle + '.______cheek_______', cb=1)

    dis = cmds.getAttr(faceCur + '.cheek_factor')

    cdAttr, mircdAttr = sdd_addAttrToHandle('L_cheek_U', 'R_cheek_U', faceSdkHandle)
    sdd_setDrivenKeyframe(FR['L_cheek'] + _sdk, 'ty', dis * 0.8, faceSdkHandle, cdAttr, 1, mircdAttr)
    # sdd_setDrivenKeyframe(FR['L_cheek_Up']+_sdk,'ty',dis*0.05,faceSdkHandle,cdAttr,1,mircdAttr)

    cdAttr, mircdAttr = sdd_addAttrToHandle('L_cheek_O', 'R_cheek_O', faceSdkHandle)
    sdd_setDrivenKeyframe(FR['L_cheek'] + _sdk, 'tx', dis * 0.8, faceSdkHandle, cdAttr, 1, mircdAttr)

    cdAttr, mircdAttr = sdd_addAttrToHandle('L_cheek_I', 'R_cheek_I', faceSdkHandle)
    sdd_setDrivenKeyframe(FR['L_cheek'] + _sdk, 'tx', -dis * 0.8, faceSdkHandle, cdAttr, 1, mircdAttr)

    cdAttr, mircdAttr = sdd_addAttrToHandle('L_pump_O', 'R_pump_O', faceSdkHandle)
    sdd_setDrivenKeyframe(FR['L_cheek'] + _sdk, 'tx', dis, faceSdkHandle, cdAttr, 1, mircdAttr)


def sdd_mouthDefultSdk():
    FR, _sdk, _root, _cnt, faceSdkHandle, faceCur = sdd_getDefultSdkName()
    # mouth
    cmds.addAttr(faceSdkHandle, ln='______jaw_________', at='double', min=0, max=0, k=0)
    cmds.setAttr(faceSdkHandle + '.______jaw_________', cb=1)

    dis = cmds.getAttr(faceCur + '.mouth_factor')

    cdAttr = sdd_addAttrToHandle('M_jaw_U', None, faceSdkHandle)
    sdd_setDrivenKeyframe(FR['jaw'] + _sdk, 'rx', -5, faceSdkHandle, cdAttr, 0.5)
    cdAttr = sdd_addAttrToHandle('M_jaw_D', None, faceSdkHandle)
    sdd_setDrivenKeyframe(FR['jaw'] + _sdk, 'rx', 30, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['L_mouth_Corner'] + _sdk, 'tz', -dis * 0.2, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['R_mouth_Corner'] + _sdk, 'tz', -dis * 0.2, faceSdkHandle, cdAttr, 1)

    cdAttr = sdd_addAttrToHandle('M_jaw_L', None, faceSdkHandle)
    sdd_setDrivenKeyframe(FR['jaw'] + _sdk, 'ry', 20, faceSdkHandle, cdAttr, 1)
    cdAttr = sdd_addAttrToHandle('M_jaw_R', None, faceSdkHandle)
    sdd_setDrivenKeyframe(FR['jaw'] + _sdk, 'ry', -20, faceSdkHandle, cdAttr, 1)

    cdAttr = sdd_addAttrToHandle('M_jaw_all_U', None, faceSdkHandle)
    sdd_setDrivenKeyframe(FR['jaw'] + _root + _sdk, 'ty', dis * 0.5, faceSdkHandle, cdAttr, 1)
    cdAttr = sdd_addAttrToHandle('M_jaw_all_D', None, faceSdkHandle)
    sdd_setDrivenKeyframe(FR['jaw'] + _root + _sdk, 'ty', -dis * 0.5, faceSdkHandle, cdAttr, 1)
    cdAttr = sdd_addAttrToHandle('M_jaw_all_L', None, faceSdkHandle)
    sdd_setDrivenKeyframe(FR['jaw'] + _root + _sdk, 'tx', dis * 0.5, faceSdkHandle, cdAttr, 1)
    cdAttr = sdd_addAttrToHandle('M_jaw_all_R', None, faceSdkHandle)
    sdd_setDrivenKeyframe(FR['jaw'] + _root + _sdk, 'tx', -dis * 0.5, faceSdkHandle, cdAttr, 1)

    cmds.addAttr(faceSdkHandle, ln='______mouth_______', at='double', min=0, max=0, k=0)
    cmds.setAttr(faceSdkHandle + '.______mouth_______', cb=1)

    cdAttr, mircdAttr = sdd_addAttrToHandle('L_mouth_corner_O', 'R_mouth_corner_O', faceSdkHandle)
    sdd_setDrivenKeyframe(FR['L_mouth_Corner'] + _sdk, 'tx', dis, faceSdkHandle, cdAttr, 1, mircdAttr)
    sdd_setDrivenKeyframe(FR['L_mouth_Up'] + _sdk, 'tx', dis * 0.5, faceSdkHandle, cdAttr, 1, mircdAttr)
    sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'tx', dis * 0.5, faceSdkHandle, cdAttr, 1, mircdAttr)
    sdd_setDrivenKeyframe(FR['L_cheek'] + _sdk, 'tx', dis * 0.5, faceSdkHandle, cdAttr, 1, mircdAttr)
    sdd_setDrivenKeyframe(FR['L_cheek'] + _sdk, 'tz', dis * 0.5, faceSdkHandle, cdAttr, 1, mircdAttr)
    sdd_setDrivenKeyframe(FR['L_noseFold'] + _sdk, 'tx', dis * 0.125, faceSdkHandle, cdAttr, 1, mircdAttr)

    cdAttr, mircdAttr = sdd_addAttrToHandle('L_mouth_corner_I', 'R_mouth_corner_I', faceSdkHandle)
    sdd_setDrivenKeyframe(FR['L_mouth_Corner'] + _sdk, 'tx', -dis * 1.25, faceSdkHandle, cdAttr, 1, mircdAttr)
    sdd_setDrivenKeyframe(FR['L_mouth_Up'] + _sdk, 'tx', -dis * 0.625, faceSdkHandle, cdAttr, 1, mircdAttr)
    sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'tx', -dis * 0.625, faceSdkHandle, cdAttr, 1, mircdAttr)
    sdd_setDrivenKeyframe(FR['M_mouth_Up'] + _sdk, 'tz', dis * 0.03, faceSdkHandle, cdAttr, 1, mircdAttr)
    sdd_setDrivenKeyframe(FR['M_mouth_Dn'] + _sdk, 'tz', dis * 0.03, faceSdkHandle, cdAttr, 1, mircdAttr)
    sdd_setDrivenKeyframe(FR['L_cheek'] + _sdk, 'tx', -dis * 0.5, faceSdkHandle, cdAttr, 1, mircdAttr)
    sdd_setDrivenKeyframe(FR['L_noseFold'] + _sdk, 'tx', -dis * 0.125, faceSdkHandle, cdAttr, 1, mircdAttr)

    cdAttr, mircdAttr = sdd_addAttrToHandle('L_mouth_corner_U', 'R_mouth_corner_U', faceSdkHandle)
    sdd_setDrivenKeyframe(FR['L_mouth_Corner'] + _sdk, 'ty', dis, faceSdkHandle, cdAttr, 1, mircdAttr)
    sdd_setDrivenKeyframe(FR['L_mouth_Up'] + _sdk, 'ty', dis * 0.25, faceSdkHandle, cdAttr, 1, mircdAttr)
    sdd_setDrivenKeyframe(FR['L_mouth_Up'] + _sdk, 'rz', 5, faceSdkHandle, cdAttr, 1, mircdAttr)
    sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'ty', dis * 0.25, faceSdkHandle, cdAttr, 1, mircdAttr)
    sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'rz', 5, faceSdkHandle, cdAttr, 1, mircdAttr)
    sdd_setDrivenKeyframe(FR['L_mouth_Corner'] + _sdk, 'tz', -dis * 0.25, faceSdkHandle, cdAttr, 1, mircdAttr)
    sdd_setDrivenKeyframe(FR['L_mouth_Corner'] + _sdk, 'rz', 10, faceSdkHandle, cdAttr, 1, mircdAttr)
    sdd_setDrivenKeyframe(FR['L_mouth_Up'] + _sdk, 'rz', 5, faceSdkHandle, cdAttr, 1, mircdAttr)
    sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'rz', 5, faceSdkHandle, cdAttr, 1, mircdAttr)
    sdd_setDrivenKeyframe(FR['L_cheek'] + _sdk, 'ty', dis * 0.5, faceSdkHandle, cdAttr, 1, mircdAttr)
    sdd_setDrivenKeyframe(FR['L_noseFold'] + _sdk, 'ty', dis * 0.125, faceSdkHandle, cdAttr, 1, mircdAttr)

    cdAttr, mircdAttr = sdd_addAttrToHandle('L_mouth_corner_D', 'R_mouth_corner_D', faceSdkHandle)
    sdd_setDrivenKeyframe(FR['L_mouth_Corner'] + _sdk, 'ty', -dis * 0.625, faceSdkHandle, cdAttr, 1, mircdAttr)
    sdd_setDrivenKeyframe(FR['L_mouth_Up'] + _sdk, 'ty', -dis * 0.25, faceSdkHandle, cdAttr, 1, mircdAttr)
    sdd_setDrivenKeyframe(FR['L_mouth_Up'] + _sdk, 'rz', -5, faceSdkHandle, cdAttr, 1, mircdAttr)
    sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'ty', -dis * 0.25, faceSdkHandle, cdAttr, 1, mircdAttr)
    sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'rz', -5, faceSdkHandle, cdAttr, 1, mircdAttr)
    sdd_setDrivenKeyframe(FR['L_mouth_Corner'] + _sdk, 'tz', -dis * 0.25, faceSdkHandle, cdAttr, 1, mircdAttr)
    sdd_setDrivenKeyframe(FR['L_mouth_Corner'] + _sdk, 'rz', -10, faceSdkHandle, cdAttr, 1, mircdAttr)
    sdd_setDrivenKeyframe(FR['L_mouth_Up'] + _sdk, 'rz', -5, faceSdkHandle, cdAttr, 1, mircdAttr)
    sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'rz', -5, faceSdkHandle, cdAttr, 1, mircdAttr)
    sdd_setDrivenKeyframe(FR['L_cheek'] + _sdk, 'ty', -dis * 0.5, faceSdkHandle, cdAttr, 1, mircdAttr)
    sdd_setDrivenKeyframe(FR['L_noseFold'] + _sdk, 'ty', -dis * 0.125, faceSdkHandle, cdAttr, 1, mircdAttr)

    #
    cdAttr, mircdAttr = sdd_addAttrToHandle('L_mouth_Up_U', 'R_mouth_Up_U', faceSdkHandle)
    sdd_setDrivenKeyframe(FR['L_mouth_Up'] + _sdk, 'ty', dis * 0.6, faceSdkHandle, cdAttr, 1, mircdAttr)
    sdd_setDrivenKeyframe(FR['M_mouth_Up'] + _sdk, 'ty', dis * 0.25, faceSdkHandle, cdAttr, 1, mircdAttr)
    sdd_setDrivenKeyframe(FR['M_mouth_Up'] + _sdk, 'rz', 10, faceSdkHandle, cdAttr, 1, mircdAttr)

    cdAttr, mircdAttr = sdd_addAttrToHandle('L_mouth_Up_D', 'R_mouth_Up_D', faceSdkHandle)
    sdd_setDrivenKeyframe(FR['L_mouth_Up'] + _sdk, 'ty', -dis * 0.6, faceSdkHandle, cdAttr, 1, mircdAttr)
    sdd_setDrivenKeyframe(FR['M_mouth_Up'] + _sdk, 'ty', -dis * 0.25, faceSdkHandle, cdAttr, 1, mircdAttr)
    sdd_setDrivenKeyframe(FR['M_mouth_Up'] + _sdk, 'rz', -10, faceSdkHandle, cdAttr, 1, mircdAttr)

    cdAttr, mircdAttr = sdd_addAttrToHandle('L_mouth_Dn_U', 'R_mouth_Dn_U', faceSdkHandle)
    sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'ty', -dis * 0.6, faceSdkHandle, cdAttr, 1, mircdAttr)
    sdd_setDrivenKeyframe(FR['M_mouth_Dn'] + _sdk, 'ty', -dis * 0.1, faceSdkHandle, cdAttr, 1, mircdAttr)
    sdd_setDrivenKeyframe(FR['M_mouth_Dn'] + _sdk, 'rz', -10, faceSdkHandle, cdAttr, 1, mircdAttr)

    cdAttr, mircdAttr = sdd_addAttrToHandle('L_mouth_Dn_D', 'R_mouth_Dn_D', faceSdkHandle)
    sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'ty', dis * 0.6, faceSdkHandle, cdAttr, 1, mircdAttr)
    sdd_setDrivenKeyframe(FR['M_mouth_Dn'] + _sdk, 'ty', dis * 0.1, faceSdkHandle, cdAttr, 1, mircdAttr)
    sdd_setDrivenKeyframe(FR['M_mouth_Dn'] + _sdk, 'rz', 10, faceSdkHandle, cdAttr, 1, mircdAttr)

    cdAttr = sdd_addAttrToHandle('M_mouth_Up_U', None, faceSdkHandle)
    sdd_setDrivenKeyframe(FR['L_mouth_Up'] + _sdk, 'ty', dis * 0.5, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['M_mouth_Up'] + _sdk, 'ty', dis * 0.5, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['R_mouth_Up'] + _sdk, 'ty', dis * 0.5, faceSdkHandle, cdAttr, 1)

    cdAttr = sdd_addAttrToHandle('M_mouth_Dn_U', None, faceSdkHandle)
    sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'ty', dis * 0.4, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'tz', dis * 0.2, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['M_mouth_Dn'] + _sdk, 'ty', dis * 0.6, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['M_mouth_Dn'] + _sdk, 'tz', dis * 0.4, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['R_mouth_Dn'] + _sdk, 'ty', dis * 0.4, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['R_mouth_Dn'] + _sdk, 'tz', dis * 0.2, faceSdkHandle, cdAttr, 1)

    cdAttr = sdd_addAttrToHandle('M_mouth_Dn_D', None, faceSdkHandle)
    sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'ty', -dis * 0.5, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['M_mouth_Dn'] + _sdk, 'ty', -dis * 0.5, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['R_mouth_Dn'] + _sdk, 'ty', -dis * 0.5, faceSdkHandle, cdAttr, 1)
    #

    cdAttr = sdd_addAttrToHandle('mouth_Up_roll_O', None, faceSdkHandle)
    sdd_setDrivenKeyframe(FR['L_mouth_Up'] + _sdk, 'rx', -35, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['M_mouth_Up'] + _sdk, 'rx', -35, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['R_mouth_Up'] + _sdk, 'rx', -35, faceSdkHandle, cdAttr, 1)

    cdAttr = sdd_addAttrToHandle('mouth_Up_roll_I', None, faceSdkHandle)
    sdd_setDrivenKeyframe(FR['L_mouth_Up'] + _sdk, 'rx', 35, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['M_mouth_Up'] + _sdk, 'rx', 35, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['R_mouth_Up'] + _sdk, 'rx', 35, faceSdkHandle, cdAttr, 1)

    cdAttr = sdd_addAttrToHandle('mouth_Dn_roll_O', None, faceSdkHandle)
    sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'rx', 35, faceSdkHandle, cdAttr, 1, mircdAttr)
    sdd_setDrivenKeyframe(FR['M_mouth_Dn'] + _sdk, 'rx', 35, faceSdkHandle, cdAttr, 1, mircdAttr)
    sdd_setDrivenKeyframe(FR['R_mouth_Dn'] + _sdk, 'rx', 35, faceSdkHandle, cdAttr, 1, mircdAttr)

    cdAttr = sdd_addAttrToHandle('mouth_Dn_roll_I', None, faceSdkHandle)
    sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'rx', -35, faceSdkHandle, cdAttr, 1, mircdAttr)
    sdd_setDrivenKeyframe(FR['M_mouth_Dn'] + _sdk, 'rx', -35, faceSdkHandle, cdAttr, 1, mircdAttr)
    sdd_setDrivenKeyframe(FR['R_mouth_Dn'] + _sdk, 'rx', -35, faceSdkHandle, cdAttr, 1, mircdAttr)


def sdd_mouthShapeDefultSdk():
    FR, _sdk, _root, _cnt, faceSdkHandle, faceCur = sdd_getDefultSdkName()
    # mouthShape
    cmds.addAttr(faceSdkHandle, ln='______motion______', at='double', min=0, max=0, k=0)
    cmds.setAttr(faceSdkHandle + '.______motion______', cb=1)

    dis = cmds.getAttr(faceCur + '.mouth_factor')

    cdAttr = sdd_addAttrToHandle('mouth_A', None, faceSdkHandle)
    sdd_setDrivenKeyframe(FR['jaw'] + _sdk, 'ty', -dis * 0.25, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['jaw'] + _sdk, 'rx', 15, faceSdkHandle, cdAttr, 1)

    sdd_setDrivenKeyframe(FR['L_mouth_Corner'] + _sdk, 'tx', dis * 0.5, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['L_mouth_Corner'] + _sdk, 'tz', -dis * 0.3, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['L_mouth_Corner'] + _sdk, 'ty', dis * 0.2, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['R_mouth_Corner'] + _sdk, 'tx', -dis * 0.5, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['R_mouth_Corner'] + _sdk, 'tz', -dis * 0.3, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['R_mouth_Corner'] + _sdk, 'ty', dis * 0.2, faceSdkHandle, cdAttr, 1)

    sdd_setDrivenKeyframe(FR['L_mouth_Up'] + _sdk, 'tx', dis * 0.3, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['R_mouth_Up'] + _sdk, 'tx', -dis * 0.3, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'tx', dis * 0.3, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['R_mouth_Dn'] + _sdk, 'tx', -dis * 0.3, faceSdkHandle, cdAttr, 1)

    sdd_setDrivenKeyframe(FR['L_cheek_Up'] + _sdk, 'tx', dis * 0.1, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['R_cheek_Up'] + _sdk, 'tx', -dis * 0.1, faceSdkHandle, cdAttr, 1)

    sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'ry', 8, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['R_mouth_Dn'] + _sdk, 'ry', -8, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'rx', -10, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['R_mouth_Dn'] + _sdk, 'rx', -10, faceSdkHandle, cdAttr, 1)

    sdd_setDrivenKeyframe(FR['L_mouth_Up'] + _sdk, 'ry', 8, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['R_mouth_Up'] + _sdk, 'ry', -8, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['L_mouth_Up'] + _sdk, 'rx', 5, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['R_mouth_Up'] + _sdk, 'rx', 5, faceSdkHandle, cdAttr, 1)

    cdAttr = sdd_addAttrToHandle('mouth_E', None, faceSdkHandle)
    sdd_setDrivenKeyframe(FR['jaw'] + _sdk, 'rx', 3, faceSdkHandle, cdAttr, 1)

    sdd_setDrivenKeyframe(FR['L_mouth_Corner'] + _sdk, 'tx', dis * 0.5, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['L_mouth_Corner'] + _sdk, 'tz', -dis * 0.3, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['L_mouth_Corner'] + _sdk, 'ty', dis * 0.2, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['R_mouth_Corner'] + _sdk, 'tx', -dis * 0.5, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['R_mouth_Corner'] + _sdk, 'tz', -dis * 0.3, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['R_mouth_Corner'] + _sdk, 'ty', dis * 0.2, faceSdkHandle, cdAttr, 1)

    sdd_setDrivenKeyframe(FR['L_mouth_Up'] + _sdk, 'tx', dis * 0.1, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['R_mouth_Up'] + _sdk, 'tx', -dis * 0.1, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'tx', dis * 0.1, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['R_mouth_Dn'] + _sdk, 'tx', -dis * 0.1, faceSdkHandle, cdAttr, 1)

    sdd_setDrivenKeyframe(FR['L_cheek'] + _sdk, 'tz', dis * 0.1, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['R_cheek'] + _sdk, 'tz', dis * 0.1, faceSdkHandle, cdAttr, 1)

    sdd_setDrivenKeyframe(FR['L_cheek_Up'] + _sdk, 'tx', dis * 0.05, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['R_cheek_Up'] + _sdk, 'tx', -dis * 0.05, faceSdkHandle, cdAttr, 1)

    sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'ty', -dis * 0.15, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['R_mouth_Dn'] + _sdk, 'ty', -dis * 0.15, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['M_mouth_Dn'] + _sdk, 'ty', -dis * 0.2, faceSdkHandle, cdAttr, 1)

    sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'tz', -dis * 0.1, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['R_mouth_Dn'] + _sdk, 'tz', -dis * 0.1, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['M_mouth_Dn'] + _sdk, 'tz', -dis * 0.1, faceSdkHandle, cdAttr, 1)

    sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'rx', 10, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['R_mouth_Dn'] + _sdk, 'rx', 10, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['M_mouth_Dn'] + _sdk, 'rx', 15, faceSdkHandle, cdAttr, 1)

    sdd_setDrivenKeyframe(FR['L_mouth_Up'] + _sdk, 'ty', dis * 0.2, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['R_mouth_Up'] + _sdk, 'ty', dis * 0.2, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['M_mouth_Up'] + _sdk, 'ty', dis * 0.2, faceSdkHandle, cdAttr, 1)

    cdAttr = sdd_addAttrToHandle('mouth_F', None, faceSdkHandle)
    sdd_setDrivenKeyframe(FR['jaw'] + _root + _sdk, 'ty', dis * 0.2, faceSdkHandle, cdAttr, 1)

    sdd_setDrivenKeyframe(FR['L_mouth_Corner'] + _sdk, 'tx', dis * 0.5, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['L_mouth_Corner'] + _sdk, 'tz', -dis * 0.3, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['L_mouth_Corner'] + _sdk, 'ty', dis * 0.4, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['R_mouth_Corner'] + _sdk, 'tx', -dis * 0.5, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['R_mouth_Corner'] + _sdk, 'tz', -dis * 0.3, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['R_mouth_Corner'] + _sdk, 'ty', dis * 0.4, faceSdkHandle, cdAttr, 1)

    sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'tx', dis * 0.25, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['R_mouth_Dn'] + _sdk, 'tx', -dis * 0.25, faceSdkHandle, cdAttr, 1)

    sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'ty', dis * 0.2, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['R_mouth_Dn'] + _sdk, 'ty', dis * 0.2, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['M_mouth_Dn'] + _sdk, 'ty', dis * 0.2, faceSdkHandle, cdAttr, 1)

    sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'tz', -dis * 0.15, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['R_mouth_Dn'] + _sdk, 'tz', -dis * 0.15, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['M_mouth_Dn'] + _sdk, 'tz', -dis * 0.2, faceSdkHandle, cdAttr, 1)

    sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'rx', -20, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['R_mouth_Dn'] + _sdk, 'rx', -20, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['M_mouth_Dn'] + _sdk, 'rx', -15, faceSdkHandle, cdAttr, 1)

    sdd_setDrivenKeyframe(FR['L_mouth_Up'] + _sdk, 'ty', dis * 0.3, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['R_mouth_Up'] + _sdk, 'ty', dis * 0.3, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['M_mouth_Up'] + _sdk, 'ty', dis * 0.4, faceSdkHandle, cdAttr, 1)

    sdd_setDrivenKeyframe(FR['L_mouth_Up'] + _sdk, 'tx', dis * 0.5, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['R_mouth_Up'] + _sdk, 'tx', -dis * 0.5, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['M_mouth_Up'] + _sdk, 'tz', dis * 0.2, faceSdkHandle, cdAttr, 1)

    sdd_setDrivenKeyframe(FR['jaw'] + _sdk, 'rx', 2, faceSdkHandle, cdAttr, 1)

    sdd_setDrivenKeyframe(FR['L_mouth_Up'] + _sdk, 'rz', -15, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['R_mouth_Up'] + _sdk, 'rz', 15, faceSdkHandle, cdAttr, 1)

    sdd_setDrivenKeyframe(FR['L_cheek'] + _sdk, 'ty', dis * 0.4, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['R_cheek'] + _sdk, 'ty', dis * 0.4, faceSdkHandle, cdAttr, 1)

    sdd_setDrivenKeyframe(FR['L_cheek_Up'] + _sdk, 'ty', dis * 0.1, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['R_cheek_Up'] + _sdk, 'ty', dis * 0.1, faceSdkHandle, cdAttr, 1)

    sdd_setDrivenKeyframe(FR['L_cheek_Up'] + _sdk, 'tz', dis * 0.05, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['R_cheek_Up'] + _sdk, 'tz', dis * 0.05, faceSdkHandle, cdAttr, 1)

    cdAttr = sdd_addAttrToHandle('mouth_H', None, faceSdkHandle)
    sdd_setDrivenKeyframe(FR['jaw'] + _sdk, 'rx', 1, faceSdkHandle, cdAttr, 1)

    sdd_setDrivenKeyframe(FR['L_mouth_Corner'] + _sdk, 'tx', -dis * 0.5, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['R_mouth_Corner'] + _sdk, 'tx', dis * 0.5, faceSdkHandle, cdAttr, 1)

    sdd_setDrivenKeyframe(FR['L_mouth_Up'] + _sdk, 'ty', dis * 0.2, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['R_mouth_Up'] + _sdk, 'ty', dis * 0.2, faceSdkHandle, cdAttr, 1)

    sdd_setDrivenKeyframe(FR['L_mouth_Up'] + _sdk, 'ry', 15, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['R_mouth_Up'] + _sdk, 'ry', -15, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['L_mouth_Up'] + _sdk, 'rz', -30, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['R_mouth_Up'] + _sdk, 'rz', 30, faceSdkHandle, cdAttr, 1)

    sdd_setDrivenKeyframe(FR['M_mouth_Up'] + _sdk, 'ty', dis * 0.5, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['M_mouth_Up'] + _sdk, 'rx', -30, faceSdkHandle, cdAttr, 1)

    sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'ry', 10, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['R_mouth_Dn'] + _sdk, 'ry', -10, faceSdkHandle, cdAttr, 1)

    sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'rz', 30, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['R_mouth_Dn'] + _sdk, 'rz', -30, faceSdkHandle, cdAttr, 1)

    sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'tz', dis * 0.1, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['R_mouth_Dn'] + _sdk, 'tz', dis * 0.1, faceSdkHandle, cdAttr, 1)

    sdd_setDrivenKeyframe(FR['M_mouth_Dn'] + _sdk, 'ty', -dis * 0.4, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['M_mouth_Dn'] + _sdk, 'tz', dis * 0.2, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['M_mouth_Dn'] + _sdk, 'rx', 30, faceSdkHandle, cdAttr, 1)

    sdd_setDrivenKeyframe(FR['L_cheek'] + _sdk, 'tx', -dis * 0.4, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['R_cheek'] + _sdk, 'tx', dis * 0.4, faceSdkHandle, cdAttr, 1)

    cdAttr = sdd_addAttrToHandle('mouth_M', None, faceSdkHandle)
    sdd_setDrivenKeyframe(FR['jaw'] + _sdk, 'rx', 3, faceSdkHandle, cdAttr, 1)

    sdd_setDrivenKeyframe(FR['L_mouth_Up'] + _sdk, 'rx', 35, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['R_mouth_Up'] + _sdk, 'rx', 35, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['M_mouth_Up'] + _sdk, 'rx', 35, faceSdkHandle, cdAttr, 1)

    sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'rx', -15, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['R_mouth_Dn'] + _sdk, 'rx', -15, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['M_mouth_Dn'] + _sdk, 'rx', -15, faceSdkHandle, cdAttr, 1)

    sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'ty', dis * 0.1, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['R_mouth_Dn'] + _sdk, 'ty', dis * 0.1, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['M_mouth_Dn'] + _sdk, 'ty', dis * 0.1, faceSdkHandle, cdAttr, 1)

    sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'tz', dis * 0.1, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['R_mouth_Dn'] + _sdk, 'tz', dis * 0.1, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['M_mouth_Dn'] + _sdk, 'tz', dis * 0.1, faceSdkHandle, cdAttr, 1)

    sdd_setDrivenKeyframe(FR['L_mouth_Up'] + _sdk, 'ty', -dis * 0.2, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['R_mouth_Up'] + _sdk, 'ty', -dis * 0.2, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['M_mouth_Up'] + _sdk, 'ty', -dis * 0.2, faceSdkHandle, cdAttr, 1)

    sdd_setDrivenKeyframe(FR['L_mouth_Up'] + _sdk, 'tz', -dis * 0.1, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['R_mouth_Up'] + _sdk, 'tz', -dis * 0.1, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['M_mouth_Up'] + _sdk, 'tz', -dis * 0.1, faceSdkHandle, cdAttr, 1)

    cdAttr = sdd_addAttrToHandle('mouth_O', None, faceSdkHandle)
    sdd_setDrivenKeyframe(FR['jaw'] + _sdk, 'rx', 3, faceSdkHandle, cdAttr, 1)

    sdd_setDrivenKeyframe(FR['L_mouth_Corner'] + _sdk, 'tx', -dis, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['R_mouth_Corner'] + _sdk, 'tx', dis, faceSdkHandle, cdAttr, 1)

    sdd_setDrivenKeyframe(FR['L_mouth_Corner'] + _sdk, 'tz', dis * 0.1, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['R_mouth_Corner'] + _sdk, 'tz', dis * 0.1, faceSdkHandle, cdAttr, 1)

    sdd_setDrivenKeyframe(FR['L_mouth_Up'] + _sdk, 'tx', -dis * 0.2, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['R_mouth_Up'] + _sdk, 'tx', dis * 0.2, faceSdkHandle, cdAttr, 1)

    sdd_setDrivenKeyframe(FR['L_mouth_Up'] + _sdk, 'ry', 15, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['R_mouth_Up'] + _sdk, 'ry', -15, faceSdkHandle, cdAttr, 1)

    sdd_setDrivenKeyframe(FR['L_mouth_Up'] + _sdk, 'rz', -15, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['R_mouth_Up'] + _sdk, 'rz', 15, faceSdkHandle, cdAttr, 1)

    sdd_setDrivenKeyframe(FR['M_mouth_Up'] + _sdk, 'ty', dis * 0.3, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['M_mouth_Up'] + _sdk, 'tz', dis * 0.2, faceSdkHandle, cdAttr, 1)

    sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'tx', -dis * 0.3, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['R_mouth_Dn'] + _sdk, 'tx', dis * 0.3, faceSdkHandle, cdAttr, 1)

    sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'tz', dis * 0.1, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['R_mouth_Dn'] + _sdk, 'tz', dis * 0.1, faceSdkHandle, cdAttr, 1)

    sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'ry', 10, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['R_mouth_Dn'] + _sdk, 'ry', -10, faceSdkHandle, cdAttr, 1)

    sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'rz', 10, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['R_mouth_Dn'] + _sdk, 'rz', -10, faceSdkHandle, cdAttr, 1)

    sdd_setDrivenKeyframe(FR['M_mouth_Dn'] + _sdk, 'ty', -dis * 0.4, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['M_mouth_Dn'] + _sdk, 'tz', dis * 0.2, faceSdkHandle, cdAttr, 1)

    sdd_setDrivenKeyframe(FR['L_cheek'] + _sdk, 'tx', -dis * 0.4, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['R_cheek'] + _sdk, 'tx', dis * 0.4, faceSdkHandle, cdAttr, 1)

    sdd_setDrivenKeyframe(FR['L_cheek'] + _sdk, 'tz', -dis * 0.2, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['R_cheek'] + _sdk, 'tz', -dis * 0.2, faceSdkHandle, cdAttr, 1)

    cdAttr = sdd_addAttrToHandle('mouth_U', None, faceSdkHandle)
    sdd_setDrivenKeyframe(FR['jaw'] + _sdk, 'rx', 3, faceSdkHandle, cdAttr, 1)

    sdd_setDrivenKeyframe(FR['L_mouth_Corner'] + _sdk, 'tx', -dis, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['R_mouth_Corner'] + _sdk, 'tx', dis, faceSdkHandle, cdAttr, 1)

    sdd_setDrivenKeyframe(FR['L_mouth_Corner'] + _sdk, 'tz', dis * 0.1, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['R_mouth_Corner'] + _sdk, 'tz', dis * 0.1, faceSdkHandle, cdAttr, 1)

    sdd_setDrivenKeyframe(FR['L_mouth_Up'] + _sdk, 'tx', -dis * 0.2, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['R_mouth_Up'] + _sdk, 'tx', dis * 0.2, faceSdkHandle, cdAttr, 1)

    sdd_setDrivenKeyframe(FR['L_mouth_Up'] + _sdk, 'ty', -dis * 0.1, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['R_mouth_Up'] + _sdk, 'ty', -dis * 0.1, faceSdkHandle, cdAttr, 1)

    sdd_setDrivenKeyframe(FR['L_mouth_Up'] + _sdk, 'ry', 15, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['R_mouth_Up'] + _sdk, 'ry', -15, faceSdkHandle, cdAttr, 1)

    sdd_setDrivenKeyframe(FR['L_mouth_Up'] + _sdk, 'rz', -20, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['R_mouth_Up'] + _sdk, 'rz', 20, faceSdkHandle, cdAttr, 1)

    sdd_setDrivenKeyframe(FR['M_mouth_Up'] + _sdk, 'ty', dis * 0.3, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['M_mouth_Up'] + _sdk, 'tz', dis * 0.2, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['M_mouth_Up'] + _sdk, 'rx', -30, faceSdkHandle, cdAttr, 1)

    sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'tx', -dis * 0.3, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['R_mouth_Dn'] + _sdk, 'tx', dis * 0.3, faceSdkHandle, cdAttr, 1)

    sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'ty', dis * 0.3, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['R_mouth_Dn'] + _sdk, 'ty', dis * 0.3, faceSdkHandle, cdAttr, 1)

    sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'tz', dis * 0.1, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['R_mouth_Dn'] + _sdk, 'tz', dis * 0.1, faceSdkHandle, cdAttr, 1)

    sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'ry', 10, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['R_mouth_Dn'] + _sdk, 'ry', -10, faceSdkHandle, cdAttr, 1)

    sdd_setDrivenKeyframe(FR['L_mouth_Dn'] + _sdk, 'rz', 20, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['R_mouth_Dn'] + _sdk, 'rz', -20, faceSdkHandle, cdAttr, 1)

    sdd_setDrivenKeyframe(FR['M_mouth_Dn'] + _sdk, 'rx', 30, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['M_mouth_Dn'] + _sdk, 'ty', -dis * 0.1, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['M_mouth_Dn'] + _sdk, 'tz', dis * 0.3, faceSdkHandle, cdAttr, 1)

    sdd_setDrivenKeyframe(FR['L_cheek'] + _sdk, 'tx', -dis * 0.4, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['R_cheek'] + _sdk, 'tx', dis * 0.4, faceSdkHandle, cdAttr, 1)

    sdd_setDrivenKeyframe(FR['L_cheek'] + _sdk, 'tz', -dis * 0.2, faceSdkHandle, cdAttr, 1)
    sdd_setDrivenKeyframe(FR['R_cheek'] + _sdk, 'tz', -dis * 0.2, faceSdkHandle, cdAttr, 1)


def sdd_frTNameDirc():
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

        'R_ear': 'R_ear',
        'L_ear': 'L_ear',
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

        'R_ear': [-3.3, -0.5, 2],
        'L_ear': [3.3, -0.5, 2],

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

        'R_ear': [5, 40],
        'L_ear': [92, 40],

    }
    return FR, FRJntPos, FRUIPos


def sdd_returnTempNameDirc():
    TName = {'_fol': '_fol', '_loc': '_loc', '_final': '_final', '_target': '_target', 'face': 'face', '_base': '_base',
             '_bsNode': '_blendShape', '_bs': '_bs', '_skin': '_skin', 'M_': 'M_', 'L_': 'L_', 'R_': 'R_',
             '_ctrl': '_ctrl', '_rig': '_rig', '_jnt': '_jnt', '_root': '_root', '_rot': '_rot', '_cur': '_cur',
             '_cnt': '_cnt', '_sdk': '_sdk', '_grp': '_grp', '_anim': '_anim'}
    return TName


# reg________________________________________________________________________________________________====


def sdd_checkRegister():
    try:
        key = _reg.OpenKey(_reg.HKEY_LOCAL_MACHINE, 'SOFTWARE\\Autodesk\\Maya')
    except:
        return False

    nameList = sdd_enumRegeditKey(key)
    if not ('FRRequest' in nameList):
        n1 = random.randint(1000, 9999)
        n2 = random.randint(1000, 9999)
        n3 = random.randint(1000, 9999)
        n4 = random.randint(1000, 9999)
        n5 = random.randint(1000, 9999)
        requestCode = '%s-%s-%s-%s-%s' % (n1, n2, n3, n4, n5)
        _reg.CreateKey(key, 'FRRequest')
        _reg.SetValue(key, 'FRRequest', 1, requestCode)

    if not ('FRActive' in nameList):
        ret = cmds.layoutDialog(ui=sdd_frRegisterWin, t='Register Window')
        if (ret == 'dismiss'):
            return False
        requestCode, activeCode = ret.split('|')
        if (sdd_getActiveString(requestCode) == activeCode):
            _reg.CreateKey(key, 'FRActive')
            _reg.SetValue(key, 'FRActive', 1, activeCode)
            return True
        return False

    try:
        key = _reg.OpenKey(_reg.HKEY_LOCAL_MACHINE, 'SOFTWARE\\Autodesk\\Maya\\FRRequest')
        name, requestCode, typ = _reg.EnumValue(key, 0)
        key = _reg.OpenKey(_reg.HKEY_LOCAL_MACHINE, 'SOFTWARE\\Autodesk\\Maya\\FRActive')
        name, activeCode, typ = _reg.EnumValue(key, 0)
        return sdd_getActiveString(requestCode) == activeCode
    except:
        return False

    return False


def sdd_frRegisterWin():
    try:
        key = _reg.OpenKey(_reg.HKEY_LOCAL_MACHINE, 'SOFTWARE\\Autodesk\\Maya\\FRRequest')
        name, SerialString, typ = _reg.EnumValue(key, 0)
    except:
        mm.eval('warning "sdd_faceRigging Register Error!"')
        cmds.layoutDialog(dis='dismiss')
    form = cmds.setParent(q=True)
    cmds.columnLayout('frrMainCL', p=form, rs=10, adj=1)
    cmds.rowLayout('frrSerialRL', cw=[[2, 200], [1, 80]], nc=2)
    cmds.text(w=80, al='right', l='Request Code:')
    cmds.textField('frrSerialTF', w=200, ed=0, tx=SerialString)
    cmds.rowLayout('frrActiveRL', p='frrMainCL', cw=[[2, 200], [1, 80]], nc=2)
    cmds.text(al='right', w=80, l='Activation Code:')
    cmds.textField('frrActivelTF', ed=1, w=200)
    cmds.separator(p='frrMainCL')
    cmds.button(p='frrMainCL', l='Register', c='sdd_frRegisterWinClose()')


def sdd_frRegisterWinClose():
    requestCode = cmds.textField('frrSerialTF', q=1, tx=1)
    activeCode = cmds.textField('frrActivelTF', q=1, tx=1)
    if (activeCode == ''):
        cmds.layoutDialog(dis='dismiss')
    else:
        cmds.layoutDialog(dis='%s|%s' % (requestCode, activeCode))


def sdd_getActiveString(requestCode):
    serList = requestCode.split('-')
    ret = []
    for i in serList:
        ret.append(sdd_getActiveType(i))
    serStr = '%s-%s-%s-%s-%s' % (ret[0], ret[1], ret[2], ret[3], ret[4])
    return serStr


def sdd_getActiveType(valStr):
    newStr = ''
    for i in valStr:
        newVal = (int(i) + int(i) + 1) % 10
        newStr += '%s' % newVal

    retVal = int(newStr) | int(valStr)
    retVal %= 10000
    return '%.4i' % retVal


def sdd_enumRegeditKey(key):
    nameList = []
    try:
        i = 0
        while 1:
            name = _reg.EnumKey(key, i)
            nameList.append(name)
            i += 1
    except:
        pass
    return nameList


# ============================================================================================================
def sdd_loadWrapMeshToList():
    sel = cmds.ls(sl=1)
    if (len(sel) == 0):
        return
    cmds.textScrollList('frwmMeshTLS', e=1, ra=1)
    for i in sel:
        shape = cmds.listRelatives(i, s=1, f=1)
        if (shape == None):
            continue
        if (cmds.objectType(shape[0]) != 'mesh'):
            continue
        cmds.textScrollList('frwmMeshTLS', e=1, a=i)


def sdd_createWrapCylinder():
    meshList = cmds.textScrollList('frwmMeshTLS', q=1, ai=1)
    cyMesh = cmds.polyCylinder(r=1, h=2, sx=20, sy=1, sz=1, ax=[0, 1, 0], rcp=0, cuv=3, ch=1)
    cmds.setAttr(cyMesh[0] + '.sx', k=0, l=1)
    cmds.setAttr(cyMesh[0] + '.sy', k=0, l=1)
    cmds.setAttr(cyMesh[0] + '.sz', k=0, l=1)
    cmds.setAttr(cyMesh[0] + '.v', k=0, l=1)
    cmds.addAttr(cyMesh[0], ln='radius', at='double', min=0, dv=1, k=1)
    cmds.addAttr(cyMesh[0], ln='height', at='double', min=0, dv=2, k=1)
    cmds.addAttr(cyMesh[0], ln='subdivisionsAxis', at='long', min=0, dv=22, k=1)
    cmds.addAttr(cyMesh[0], ln='subdivisionsHeight', at='long', min=0, dv=22, k=1)
    cmds.connectAttr(cyMesh[0] + '.radius', cyMesh[1] + '.radius')
    cmds.connectAttr(cyMesh[0] + '.height', cyMesh[1] + '.height')
    cmds.connectAttr(cyMesh[0] + '.subdivisionsAxis', cyMesh[1] + '.subdivisionsAxis')
    cmds.connectAttr(cyMesh[0] + '.subdivisionsHeight', cyMesh[1] + '.subdivisionsHeight')
    cmds.textField('frwmCylinderTF', e=1, tx=cyMesh[0])

    mBox = [None, None, None, None, None, None]
    mObj = ['', '', '', '', '', '']
    for i in meshList:
        box = cmds.xform(i, q=1, bbi=1)
        for a in range(3):
            if (mBox[a] == None):
                mBox[a] = box[a]
                mObj[a] = i
            elif (box[a] < mBox[a]):
                mBox[a] = box[a]
                mObj[a] = i
        for a in range(3, 6):
            if (mBox[a] == None):
                mBox[a] = box[a]
                mObj[a] = i
            elif (box[a] > mBox[a]):
                mBox[a] = box[a]
                mObj[a] = i
    cBox = cmds.xform(cyMesh[0], q=1, bbi=1)
    mabsLen = [mBox[3] - mBox[0], mBox[4] - mBox[1], mBox[5] - mBox[2]]
    cabsLen = [cBox[3] - cBox[0], cBox[4] - cBox[1], cBox[5] - cBox[2]]
    mmaxrad = mabsLen[0]
    if (mabsLen[0] > mabsLen[2]):
        maxrad = mabsLen[2]
    cmaxrad = cabsLen[0]
    rad = mmaxrad / cmaxrad * 1.1
    mmaxheight = mabsLen[1]
    cmaxheight = cabsLen[1]
    height = mmaxheight / cmaxheight * 2.1

    cmds.setAttr(cyMesh[0] + '.radius', rad)
    cmds.setAttr(cyMesh[0] + '.height', height)

    pos = [(mBox[3] + mBox[0]) / 2, (mBox[4] + mBox[1]) / 2, (mBox[5] + mBox[2]) / 2]

    cmds.setAttr(cyMesh[0] + '.t', pos[0], pos[1], pos[2], typ='float3')


def sdd_wrapMeshProc():
    global wpOrigArray
    meshList = cmds.textScrollList('frwmMeshTLS', q=1, ai=1)
    wapMesh = cmds.textField('frwmCylinderTF', q=1, tx=1)

    pcyFnMesh = sdd_getMfnMeshByName(wapMesh)
    pcyItMesh = sdd_getMItMeshVertexByName(wapMesh)

    unitl = OpenMaya.MScriptUtil()
    unitl.createFromInt(0)
    preInt = unitl.asIntPtr()

    normalArray = OpenMaya.MFloatVectorArray()
    pcyFnMesh.getNormals(normalArray, OpenMaya.MSpace.kTransform)

    vtxList = cmds.ls(wapMesh + '.vtx[*]', fl=1)
    pos1 = cmds.xform(vtxList[-1], q=1, ws=1, t=1)
    pos2 = cmds.xform(vtxList[-2], q=1, ws=1, t=1)
    point1 = OpenMaya.MPoint(pos1[0], pos1[1], pos1[2])
    point2 = OpenMaya.MPoint(pos2[0], pos2[1], pos2[2])
    normalVector = point1 - point2
    normalVector = normalVector.normal()
    rootPoint = cmds.xform(wapMesh, q=1, ws=1, t=1)
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
    for mesh in meshList:
        meshFnFace = sdd_getMfnMeshByName(mesh)
        meshFnList.append(meshFnFace)

    cmds.progressBar('frMainStatePB', e=1, max=pcyItMesh.count(), bp=1, vis=1)
    try:
        for i in range(pcyItMesh.count()):
            cmds.progressBar('frMainStatePB', e=1, s=1)

            pcyItMesh.setIndex(i, preInt)
            arrawPoint = rootPoint + normalVector * lenList[i]
            normal = arrawPoint - pointArray[i]
            # cmds.spaceLocator(p=[arrawPoint.x,arrawPoint.y,arrawPoint.z])
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
        cmds.progressBar('frMainStatePB', e=1, ep=1)
        cmds.progressBar('frMainStatePB', e=1, vis=0)


        # pcyFnMesh.setPoints(pointArray,OpenMaya.MSpace.kWorld)


def sdd_wrapMeshRestore():
    global wpOrigArray
    wapMesh = cmds.textField('frwmCylinderTF', q=1, tx=1)
    pcyFnMesh = sdd_getMfnMeshByName(wapMesh)
    if (pcyFnMesh.numVertices() != wpOrigArray.length()):
        return
    pcyFnMesh.setPoints(wpOrigArray)


# ============================================================================================================

sdd_FaceRigging('C:/Users/sundongdong/Desktop/sdd_faceRigging/')
