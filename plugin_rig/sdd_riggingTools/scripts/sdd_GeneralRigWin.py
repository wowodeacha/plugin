#===============================================================================================
# Author: SunDongDong
# E-mail: 136941679@qq.com
# Version: 2.5.0
# Copyright (c) 2015 SDD.Co.Ltd. All rights reserved.
#===============================================================================================

from maya.cmds import *
import maya.mel as mm

def sdd_GeneralRigWin(rootPath):
    if(window('GeneralRigWin',q=1,ex=1)):
        cmds.deleteUI('GeneralRigWin',window=1)
    cmds.window('GeneralRigWin',rtf=1,menuBar=1,s=1,t='sdd_General Rig Win v1.5.0')
    cmds.columnLayout('ikfkMainCL',adj=1)
    cmds.tabLayout('ikfkMainTL',p='ikfkMainCL')

#===========joint
    cmds.columnLayout('RigMainCL',p='ikfkMainTL',adj=0)


    cmds.frameLayout(p='RigMainCL',mw=10,mh=1,w=290,l="Global Setting",collapsable=1,cl=0)
    cmds.columnLayout('globalCL')
    cmds.radioCollection()
    cmds.rowLayout(p='globalCL',nc=4,cw4=[50,50,50,50])
    cmds.text(l='FrontAxis:',w=50,al='right')
    cmds.radioButton('axisXRB',l='X',sl=1)
    cmds.radioButton('axisYRB',l='Y')
    cmds.radioButton('axisZRB',l='Z')

    cmds.radioCollection()
    cmds.rowLayout(p='globalCL',nc=5,cw5=[50,50,50,15,85])
    cmds.text(l='Suffix:',w=50,al='right')
    cmds.radioButton('sufAnimRB',l='_anim',sl=1)
    cmds.radioButton('sufCtrlRB',l='_ctrl')
    cmds.radioButton('sufCustomRB',l='')
    cmds.textField('sufCustomTF',tx='',w=85)


    cmds.rowLayout(p='globalCL',nc=4,cw4=[50,50,50,100])
    cmds.radioCollection()
    cmds.text(l='Remove:',w=50,al='right')
    cmds.radioButton('remPreRB',l='prefix')
    cmds.radioButton('remSufRB',l='suffix',sl=1)
    cmds.intSliderGrp('removeNumISG',f=1,min=0,max=10,fmn=0,v=0,cw2=[0,100],adj=1,ad3=3,ad2=2)



#fk cnt
    cmds.frameLayout(p='RigMainCL',mw=10,mh=1,w=290,l="Fk Contol",collapsable=1,cl=0)
    cmds.columnLayout('CreatFkCntCL')
    cmds.rowLayout(p='CreatFkCntCL',nc=2,cw2=[65,195],cal=[(2,'right')])
    cmds.text(l='Constraint:',w=60,al='right')
    cmds.rowLayout(nc=3,cw3=[70,60,65])
    cmds.checkBox('fkConTCB',l='Translate',w=70,v=1)
    cmds.checkBox('fkConRCB',l='Rotate',w=60,v=1)
    cmds.checkBox('fkConSCB',l='Scale',w=60,v=0)

    cmds.button(p='CreatFkCntCL',w=265,h=35,l='FK Contrl',c='sdd_CreateFkCnt()')


#ikfk
    cmds.frameLayout(p='RigMainCL',w=290,l="IKFK",collapsable=1,cl=0)
    cmds.columnLayout('ArmIkFkCL',adj=0)
    cmds.rowLayout('ifOptionRL',p='ArmIkFkCL',nc=2,cw2=[82,80],cal=[(2,'right')])
    cmds.text(l='Option:',w=80,al='right')
    cmds.checkBox('ifOpStrechCB',l='Stretch',w=80,v=0)

    cmds.textFieldButtonGrp('ifStartJntBG',p='ArmIkFkCL',bl='Load',l='Start Jnt:',cw3=[80,160,40],bc='sdd_JointLoad("ifStartJntBG")')
    cmds.textFieldButtonGrp('ifEndJntBG',p='ArmIkFkCL',bl='Load',l='End Jnt:',cw3=[80,160,40],bc='sdd_JointLoad("ifEndJntBG")')
    cmds.separator(p="ArmIkFkCL",style="none",h=8)
    cmds.rowLayout('ArmIkFkRL',p='ArmIkFkCL',nc=2,cw2=[10,265],cal=[(2,'center')])
    cmds.text(p='ArmIkFkRL',l='')
    cmds.button(p='ArmIkFkRL',w=265,h=30,l='Create',c='sdd_ikfkSwitch()')


#spline ikfk
    cmds.frameLayout('SplineIkFkFL',p='RigMainCL',w=290,l="Spline IkFk",collapsable=1,cl=0)
    cmds.columnLayout('SplineIkFkCL',p='SplineIkFkFL',adj=0)
    cmds.rowLayout('SplineIkFkRL',p='SplineIkFkCL',nc=2,cw2=[80,195],cal=[(2,'right')])

    cmds.text(p='SplineIkFkRL',l='Option:',w=80,al='right')
    cmds.columnLayout('sikOptionCL',p='SplineIkFkRL')
    cmds.rowLayout('sikOptionRL1',p='sikOptionCL',nc=3,cw3=[65,65,65])
    cmds.checkBox('sikIkfkCB',p='sikOptionRL1',l='Ik/Fk',w=60,v=1)
    cmds.checkBox('sikStretchCB',p='sikOptionRL1',l='Stretch',w=60,v=1)
    cmds.checkBox('sikTwistCB',p='sikOptionRL1',l='Twist',w=60,v=0)
    #rowLayout('sikOptionRL2',p='sikOptionCL',nc=3,cw3=[65,65,65])
    #checkBox('sikSquashCB',p='sikOptionRL2',l='Squash',w=60,v=0)


    cmds.intSliderGrp('sikCntNumberSG',l='Cnt Number:',p='SplineIkFkCL',f=1,min=3,max=20,v=4,cw3=[80,35,157])
    cmds.textFieldButtonGrp('sIkStartJntCL',p='SplineIkFkCL',bl='Load',l='Start Joint:',cw3=[80,160,40],bc='sdd_JointLoad("sIkStartJntCL")')
    cmds.textFieldButtonGrp('sIkEndJntCL',p='SplineIkFkCL',bl='Load',l='End Joint:',cw3=[80,160,40],bc='sdd_JointLoad("sIkEndJntCL")')
    cmds.separator(p="SplineIkFkCL",style="none",h=8)
    cmds.rowLayout('sIkCreateRL',p='SplineIkFkCL',nc=2,cw2=[10,265],cal=[(2,'center')])
    cmds.text(p='sIkCreateRL',l='')
    cmds.button(p='sIkCreateRL',w=265,h=30,l='Create Control',c='sdd_SplineCnt()')
    cmds.rowLayout('sIkRigRL',p='SplineIkFkCL',nc=2,cw2=[10,265],cal=[(2,'center')])
    cmds.text(p='sIkRigRL',l='')
    cmds.button(p='sIkRigRL',w=265,h=30,l='Rigging',c='sdd_SplineIkRig()')
#===========changColor
    cmds.columnLayout('rtControlCL',p='ikfkMainTL',adj=1)
    cmds.frameLayout('rtchangColFL',w=260,l=' Change Color',collapsable=1,cl=0)
    cmds.columnLayout('rtchangColCL')
    cmds.separator(style='none',h=6)
    cmds.rowLayout('rtchangColRL',p='rtchangColCL',nc=2,cw2=(20,240))
    cmds.text(l='',w=20)
    cmds.columnLayout('rtchangColCL2',p='rtchangColRL',adj=0)

    cmds.separator(w=240)
    cmds.separator(style='none',h=3)
    cmds.gridLayout('rtchangColGL',numberOfRows=4,numberOfColumns=8,cellWidthHeight=(30,30))
    bgcIconList=[(0.627,0.627,0.627),(0.467,0.467,0.467),(0.000,0.000,0.000),(0.247,0.247,0.247),(0.498,0.498,0.498),(0.608,0.000,0.157),(0.000,0.016,0.373),(0.000,0.000,1.000),(0.000,0.275,0.094),(0.145,0.000,0.263),(0.780,0.000,0.780),(0.537,0.278,0.200),(0.243,0.133,0.122),(0.600,0.145,0.000),(1.000,0.000,0.000),(0.000,1.000,0.000),(0.000,0.255,0.600),(1.000,1.000,1.000),(1.000,1.000,0.000),(0.388,0.863,1.000),(0.263,1.000,0.635),(1.000,0.686,0.686),(0.890,0.675,0.475),(1.000,1.000,0.384),(0.000,0.600,0.325),(0.627,0.412,0.188),(0.620,0.627,0.188),(0.408,0.627,0.188),(0.188,0.627,0.365),(0.188,0.627,0.627),(0.188,0.404,0.627),(0.435,0.188,0.627)]
    for i in range(len(bgcIconList)):
        cmds.iconTextButton(p='rtchangColGL',bgc=bgcIconList[i],c='sdd_ChangeOverColor(%d)'%i)
    cmds.separator(p='rtchangColCL2',style='none',h=3)
    cmds.separator(p='rtchangColCL2',w=240)
    cmds.separator(p='rtchangColCL2',style='none',h=3)

    cmds.rowLayout('rtchangOpRL',p='rtchangColCL2',nc=3,cw3=(40,100,100))
    cmds.text(l='Type:')
    cmds.radioCollection('rtchangOpRC')
    cmds.radioButton('rtcoShapeRB',l='Shape',sl=1)
    cmds.radioButton('rtcoTransformRB',l='Transform')
    cmds.separator(p='rtchangColCL2',style='none',h=6)
#===========Control
    cmds.frameLayout('rtreplaceShapeFL',p='rtControlCL',w=260,l=' Change Shape',collapsable=1,cl=0)
    cmds.columnLayout('rtreplaceShapeFL')
    cmds.separator(style='none',h=6)
    
    cmds.rowLayout('rtreplaceShapeRL',nc=2,cw2=(20,240))
    cmds.text(l='',w=20)
    cmds.columnLayout('rtreplaceShapeCL2',adj=0)
    cmds.separator(w=240)
    cmds.separator(style='none',h=3)
    cmds.gridLayout('rtreplaceShapeGL',nc=6,cellWidthHeight=(40,40))
    cmds.separator(p='rtreplaceShapeCL2',style='none',h=3)
    cmds.separator(p='rtreplaceShapeCL2',w=240)
    cmds.separator(p='rtreplaceShapeCL2',style='none',h=3)



    cmds.rowLayout('rtreplaceOpRL',p='rtreplaceShapeCL2',nc=4,cw4=(40,70,60,55))
    cmds.text(l='Type:')
    cmds.radioCollection('replaceOpRC')
    cmds.radioButton('rtroReplaceRB',l='Replace')
    cmds.radioButton('rtroAddRB',l='Add')
    cmds.radioButton('rtroCreateRB',l='Create',sl=1)

    cmds.rowLayout('rtrsOffsetRL',p='rtreplaceShapeCL2',nc=4,cw4=(40,65,65,65))
    cmds.text(l='Offset:')
    cmds.optionMenuGrp('rtrsTypeXOMG',label='X',cw2=[10, 30])
    cmds.menuItem(l='0')
    cmds.menuItem(l='90')
    cmds.menuItem(l='180')
    cmds.menuItem(l='-90')
    cmds.optionMenuGrp('rtrsTypeYOMG',label='Y',cw2=[10, 30])
    cmds.menuItem(l='0')
    cmds.menuItem(l='90')
    cmds.menuItem(l='180')
    cmds.menuItem(l='-90')
    cmds.optionMenuGrp('rtrsTypeZOMG',label='Z',cw2=[10, 30])
    cmds.menuItem(l='0')
    cmds.menuItem(l='90')
    cmds.menuItem(l='180')
    cmds.menuItem(l='-90')

    cmds.rowLayout(p='rtreplaceShapeCL2',nc=2,cw2=[140,100],cal=[(1,'center'),(2,'center')])
    cmds.button(l='Parent Select Shape',w=140,c='sdd_parentShape()')
    cmds.button(l='Zero Group',w=100,c='sdd_CreateZoreGrpBySel()')

    cmds.separator(p='rtreplaceShapeCL2',style='none',h=6)

    #adjust cnt
    cmds.frameLayout('rtadjustCntFL',p='rtControlCL',w=260,l=' Adjust Shape',collapsable=1,cl=0)
    cmds.columnLayout('rtadjustCntCL')
    
    cmds.rowLayout('rtadjustCntRL',nc=2,cw2=(20,240))
    cmds.text(l='',w=20)
    cmds.columnLayout('rtadjustCntCL2',adj=0)

    #mirror shape
    cmds.separator(style='none',h=6)
    cmds.radioCollection('rtMirShapeOpRC')
    cmds.rowLayout('rtrsMirShapeRL',nc=5,cw5=[55,55,60,5,65],cal=[(2,'center'),(3,'center'),(4,'center'),(5,'center')])
    cmds.text(l='Mir Shape:',w=55)
    cmds.button('rtrsMirShapeX',l='X',w=45,h=20,c='sdd_mirShapePoint(1)')
    cmds.button('rtrsMirShapeY',l='Z',w=45,h=20,c='sdd_mirShapePoint(2)')
    cmds.text(l='')
    cmds.button('rtrsMirShapeZ',l='Unlock',w=65,h=20,c='sdd_unlockAttrFromChannels()')
    #select cv
    cmds.separator(p='rtadjustCntCL2',style='none',h=8)
    cmds.rowLayout('rtrsScaleCVRL',p='rtadjustCntCL2',nc=4,cw4=[80,28,105,28],cal=[(1,'center')])
    cmds.button(l='Select All CV',w=80,c='sdd_selectAllCurveCVProc()')
    cmds.floatField('rtrsScaleMinCVFS',v=-1,max=-0.1,w=28,pre=1,cc='sdd_chgScaCVSMaxMinProc(1)')
    cmds.floatSlider('rtrsScaleCVFS',max=1,w=105,min=-1,v=0,cc='sdd_changeScaleCVSliderProc()')
    cmds.floatField('rtrsScaleMaxCVFS',v=1,min=0.1,w=28,pre=1,cc='sdd_chgScaCVSMaxMinProc(1)')

    cmds.separator(p='rtadjustCntCL2',style='none',h=6)

    

    cmds.tabLayout('ikfkMainTL',e=1,tli=[(1,'General Rigging'),(2,'Shape Color')])
    cmds.showWindow('GeneralRigWin')
    sdd_loadicons(rootPath)


def sdd_ikfkSwitch():
    startJnt=textFieldButtonGrp('ifStartJntBG',q=1,tx=1)
    endJnt=textFieldButtonGrp('ifEndJntBG',q=1,tx=1)
    if(startJnt=='' or endJnt==''):
        mm.eval('warning "Please load joint!"')
        return
    suf='_anim'
    if(radioButton('sufCtrlRB',q=1,sl=1)):
        suf='_cnt'
    if(radioButton('sufCustomRB',q=1,sl=1)):
        suf=textField('sufCustomTF',q=1,tx=1)

    jntList=sdd_GetJntChainList(startJnt,endJnt)
    if(jntList==''):
        mm.eval('warning "Please load right joint!"')
        return

    baseName=sdd_GetBaseName(startJnt)
    allGrp=group(em=1,n=baseName+'_all_grp')

    ikJntList=sdd_DuplicateList(jntList,'_ik')
    cmds.parent(ikJntList[0],allGrp)
    fkJntList=sdd_DuplicateList(jntList,'_fk')
    cmds.parent(fkJntList[0],allGrp)

    endBaseName=sdd_GetBaseName(endJnt)
    
    ikfkOpCnt=circle(ch=0,nr=(1,0,0),r=1,n=endBaseName+'_Options'+suf)[0]
    ikfkOpCntGrp=group(ikfkOpCnt,n=ikfkOpCnt+'_grp')
    cmds.delete(parentConstraint(endJnt,ikfkOpCntGrp))

    cmds.addAttr(ikfkOpCnt,ln="ikFk",at='double',min=0,max=1,k=1)
    revNode=createNode('reverse',n=jntList[-1]+'_rev')
    cmds.connectAttr(ikfkOpCnt+'.ikFk',revNode+'.ix')

    attrList=['.tx','.ty','.tz','.rx','.ry','.rz','.sx','.sy','.sz','.v']
    sdd_LockHideAttr([ikfkOpCnt],attrList)
    cmds.parent(ikfkOpCntGrp,allGrp)

    for i in range(len(jntList)):
        con=parentConstraint(ikJntList[i],fkJntList[i],jntList[i])[0]
        cmds.connectAttr(ikfkOpCnt+'.ikFk',con+'.w1')
        cmds.connectAttr(revNode+'.ox',con+'.w0')

    con=parentConstraint(ikJntList[-1],fkJntList[-1],ikfkOpCntGrp)[0]
    cmds.connectAttr(ikfkOpCnt+'.ikFk',con+'.w1')
    cmds.connectAttr(revNode+'.ox',con+'.w0')

    ikH=ikHandle(sj=ikJntList[0],sol='ikRPsolver',ee=ikJntList[-1],n=baseName+'_ikH')
    #ikCnt
    ikCnt=circle(ch=0,nr=(1,0,0),r=3,n=endBaseName+'_ik'+suf)[0]

    
    ikCntGrp=group(ikCnt,n=ikCnt+'_grp')
    cmds.delete(parentConstraint(ikJntList[-1],ikCntGrp))

    attrList=['.sx','.sy','.sz','.v']
    sdd_LockHideAttr([ikCnt],attrList)
    #ikPole
    ikPole=circle(ch=0,nr=(1,0,0),r=1,n=endBaseName+'_ikPole'+suf)[0]
    ikPoleGrp=group(ikPole,n=ikPole+'_grp')
    cmds.delete(parentConstraint(ikJntList[1],ikPoleGrp))
    attrList=['.rx','.ry','.rz','.sx','.sy','.sz','.v']
    sdd_LockHideAttr([ikPole],attrList)
    #
    cmds.parent(ikH[0],ikCnt)
    cmds.setAttr(ikH[0]+'.v',0)
    cmds.poleVectorConstraint(ikPole,ikH[0])
    cmds.orientConstraint(ikCnt,ikJntList[-1])
    #fkcnt
    grpList=sdd_CreateCntByList(fkJntList,suf)
    for i in range(len(fkJntList)-1):
        cmds.parentConstraint(grpList[0][i],grpList[1][i+1],mo=1)
    fkCntGrp=group(grpList[1],n=fkJntList[1]+'_cnt_grp')
    cmds.connectAttr(ikfkOpCnt+'.ikFk',fkCntGrp+'.v')
    cmds.connectAttr(ikfkOpCnt+'.ikFk',fkJntList[0]+'.v')
    ikGrp=group(ikPoleGrp,ikCntGrp,n=jntList[0]+'_ikGrp')
    cmds.connectAttr(revNode+'.ox',ikGrp+'.v')
    cmds.connectAttr(revNode+'.ox',ikJntList[0]+'.v')
    cmds.parent(fkCntGrp,allGrp)

    
    if(checkBox('ifOpStrechCB',q=1,v=1)):
        sGrp=sdd_createIkStretch(ikCnt,ikJntList)
        cmds.setAttr(sGrp+'.v',0)
        cmds.parent(sGrp,ikGrp)

def sdd_createIkStretch(ikCnt,ikJntList):
    remove=intSliderGrp('removeNumISG',q=1,v=1)
    remType='suffix'
    if(radioButton('remPreRB',q=1,sl=1)):
        remType='prefix'

    axis='.tx'
    if(radioButton('axisYRB',q=1,sl=1)):
        axis='.ty'
    if(radioButton('axisZRB',q=1,sl=1)):
        axis='.tz'

    cmds.addAttr(ikCnt,ln="stretch",at='double',min=0,max=1,k=1)

    loc1=spaceLocator(n=ikJntList[0]+'_loc')[0]
    loc2=spaceLocator(n=ikJntList[-1]+'_loc')[0]

    cmds.pointConstraint(ikJntList[0],loc1)
    cmds.pointConstraint(ikCnt,loc2)
    cmds.delete(parentConstraint(ikJntList[0],loc1))
    cmds.delete(parentConstraint(ikJntList[-1],loc2))
    baseName=ikJntList[0]

    dis=createNode('distanceBetween',n=baseName+'_dis')
    cmds.connectAttr(loc1+'.t',dis+'.p1')
    cmds.connectAttr(loc2+'.t',dis+'.p2')

    #pos=sdd_GetJointListPos(ikJntList)
    #cur2=curve(d=1,p=pos,n=cur1+'_gl')
    #cur2Shape=listRelatives(cur2,f=1)[0]

    #val=getAttr(info2+'.al')
    #glMDNode=createNode('multiplyDivide',n=cur1+'_gl_md')
    #connectAttr(info2+'.al',glMDNode+'.i1x')
    #setAttr(glMDNode+'.op',2)
    #setAttr(glMDNode+'.i2x',getAttr(glMDNode+'.i1x'))

    mdNode=createNode('multiplyDivide',n=baseName+'_md')
    cmds.connectAttr(dis+'.d',mdNode+'.i1x')
    #connectAttr(info2+'.al',mdNode+'.i2x')
    cmds.setAttr(mdNode+'.op',2)
    

    conNode=createNode('condition',n=baseName+'_con')
    cmds.setAttr(conNode+'.st',1)
    cmds.setAttr(conNode+'.op',2)
    cmds.connectAttr(mdNode+'.ox',conNode+'.ft')
    cmds.connectAttr(mdNode+'.ox',conNode+'.ctr')

    bcNode=createNode('blendColors',n=ikJntList[0]+'_bc')
    cmds.setAttr(bcNode+'.c2r',1)
    cmds.connectAttr(ikCnt+'.stretch',bcNode+'.b')
    cmds.connectAttr(conNode+'.ocr',bcNode+'.c1r')

    arcValue=0
    smdList=[]
    for i in ikJntList[1:]:
        val=getAttr(i+axis)
        arcValue+=val
        smd=createNode('multiplyDivide',n=i+'_scaleMD')
        cmds.connectAttr(bcNode+'.opr',smd+'.i1x')
        cmds.connectAttr(smd+'.ox',i+axis)
        cmds.setAttr(smd+'.i2x',val)
        smdList.append(smd)
    cmds.setAttr(mdNode+'.i2x',arcValue)
    retGrp=group(loc1,loc2,n=ikJntList[0]+'_Stretch_grp')
    return retGrp

def sdd_CreateFkCnt():
    conT=checkBox('fkConTCB',q=1,v=1)
    conR=checkBox('fkConRCB',q=1,v=1)
    conS=checkBox('fkConSCB',q=1,v=1)

    sel=ls(sl=1)
    if(len(sel)==0):
        mm.eval('warning "Please cmds.select joint!"')
        return

    suf='_anim'
    if(radioButton('sufCtrlRB',q=1,sl=1)):
        suf='_cnt'
    if(radioButton('sufCustomRB',q=1,sl=1)):
        suf=textField('sufCustomTF',q=1,tx=1)

    remove=intSliderGrp('removeNumISG',q=1,v=1)
    remType='suffix'
    if(radioButton('remPreRB',q=1,sl=1)):
        remType='prefix'

    curList=[]
    grpList=[]
    for i in sel:
        baseName=i[:]+suf
        if(remType=='suffix'):
            if remove!=0:
                baseName=i[:-remove]+suf
        else:
            if remove!=0:
                baseName=i[remove:]+suf

        cirName=circle(ch=0,nr=(1,0,0),r=2,n=baseName)[0]
        curList.append(cirName)
        cmds.setAttr(cirName+'.v',k=0,l=1)
        grp=group(cirName,n=baseName+'_grp')
        grpList.append(grp)
        cmds.delete(parentConstraint(i,grp))

        if(conT and conR):
            cmds.parentConstraint(cirName,i)
        elif(conT):
            cmds.pointConstraint(cirName,i)
            cmds.setAttr(cirName+'.rx',k=0,l=1)
            cmds.setAttr(cirName+'.ry',k=0,l=1)
            cmds.setAttr(cirName+'.rz',k=0,l=1)
        elif(conR):
            cmds.orientConstraint(cirName,i)
            cmds.setAttr(cirName+'.tx',k=0,l=1)
            cmds.setAttr(cirName+'.ty',k=0,l=1)
            cmds.setAttr(cirName+'.tz',k=0,l=1)
        if(conS):
            cmds.scaleConstraint(cirName,i)
        else:
            cmds.setAttr(cirName+'.sx',k=0,l=1)
            cmds.setAttr(cirName+'.sy',k=0,l=1)
            cmds.setAttr(cirName+'.sz',k=0,l=1)


def sdd_SplineCnt():
    startJnt=textFieldButtonGrp('sIkStartJntCL',q=1,tx=1)
    endJnt=textFieldButtonGrp('sIkEndJntCL',q=1,tx=1)
    cntNum=intSliderGrp('sikCntNumberSG',q=1,v=1)
    suf='_anim'
    if(radioButton('sufCtrlRB',q=1,sl=1)):
        suf='_cnt'
    if(radioButton('sufCustomRB',q=1,sl=1)):
        suf=textField('sufCustomTF',q=1,tx=1)
    
    if(startJnt=='' or endJnt==''):
        mm.eval('warning "Please load joint!"')
        return
    jntList=sdd_GetJntChainList(startJnt,endJnt)
    if(jntList==''):
        mm.eval('warning "Please load right joint!"')
        return

    baseName=sdd_GetBaseName(startJnt)
    posList=sdd_GetJointListPos(jntList)
    ik_cur=curve(d=3,ep=posList,n=baseName+'_Cur')
    cmds.rebuildCurve(ik_cur,ch=0,rpo=1,rt=0,end=1,kr=0,kcp=0,kep=1,kt=0,s=0,d=3,tol=0)
    cntPosList=sdd_GetCurPosList(cntNum,ik_cur)


    ctrlJntList=sdd_CreateJointByList(cntPosList,baseName)

    cmds.delete(ik_cur)

    curList=[]
    for i in ctrlJntList:
        ctrlCur=circle(ch=0,nr=(1,0,0),r=2,n=i+suf)[0]
        cmds.delete(parentConstraint(i,ctrlCur))
        cmds.parent(i,ctrlCur)
        cmds.setAttr(i+'.v',0)
        curList.append(ctrlCur)

    ctrlGrp=group(curList,n=baseName+'_ctrl_grp')

def sdd_GetBaseName(startJnt):
    remType='suffix'
    if(radioButton('remPreRB',q=1,sl=1)):
        remType='prefix'
    remove=intSliderGrp('removeNumISG',q=1,v=1)
    baseName=startJnt
    if(remType=='suffix'):
        if remove!=0:
            baseName=startJnt[:-remove]
    else:
        if remove!=0:
            baseName=startJnt[remove:]
    return baseName

def sdd_SplineIkRig():
    startJnt=textFieldButtonGrp('sIkStartJntCL',q=1,tx=1)
    endJnt=textFieldButtonGrp('sIkEndJntCL',q=1,tx=1)
    suf='_anim'
    if(radioButton('sufCtrlRB',q=1,sl=1)):
        suf='_cnt'
    if(radioButton('sufCustomRB',q=1,sl=1)):
        suf=textField('sufCustomTF',q=1,tx=1)

    baseName=sdd_GetBaseName(startJnt)
    ctrlGrp=baseName+'_ctrl_grp'
    if(not cmds.objExists(ctrlGrp)):
        return
    curList=listRelatives(ctrlGrp,c=1,s=0)

    curGrpList=[]
    ctrlJntList=[]
    for i in curList:
        ctrlJntList.append(listRelatives(i,c=1,typ='joint')[0])
        curGrp=group(n=i+'_grp',em=1)
        curGrpList.append(curGrp)
        cmds.delete(parentConstraint(i,curGrp))
        pName=listRelatives(i,p=1)
        cmds.parent(i,curGrp)
        cmds.parent(curGrp,pName)


    if(startJnt=='' or endJnt==''):
        mm.eval('warning "Please load joint!"')
        return
    jntList=sdd_GetJntChainList(startJnt,endJnt)
    if(jntList==''):
        mm.eval('warning "Please load right joint!"')
        return

    allGrp=group(n=baseName+'_all_grp',em=1)
    cmds.parent(ctrlGrp,allGrp)


    ikJntList=sdd_DuplicateList(jntList,'_ik')
    startJnt=ikJntList[0]
    endJnt=ikJntList[-1]
    cmds.parent(ikJntList[0],allGrp)

    posList=sdd_GetJointListPos(jntList)
    ik_cur=curve(d=3,ep=posList,n=baseName+'_Cur')
    ik_H=ikHandle(sol='ikSplineSolver',pcv=0,ccv=0,sj=startJnt,ee=endJnt,c=ik_cur,n=baseName+'_ikH')[0]
    cmds.parent(ik_cur,ik_H,allGrp)

    cmds.skinCluster(ctrlJntList,ik_cur,mi=4,dr=4)
    cmds.setAttr(ik_cur+'.it',0)

    if(checkBox('sikIkfkCB',q=1,v=1)):
        sdd_SplineIkFkSwich(curList,curGrpList)
    if(checkBox('sikStretchCB',q=1,v=1)):
        globalCur=sdd_SplineIkStretch(ik_cur,curList,ikJntList)
    if(checkBox('sikTwistCB',q=1,v=1)):
        sdd_SplineIkTwist(curList,ik_H)
    #if(checkBox('sikSquashCB',q=1,v=1)):
    #    sdd_splineIkSquashControls(curList,jntList)

    for i in range(len(ikJntList)):
        cmds.parentConstraint(ikJntList[i],jntList[i])

    cmds.setAttr(ik_cur+'.v',0)
    cmds.setAttr(ik_H+'.v',0)
    cmds.setAttr(ikJntList[0]+'.v',0)
    attrList=['.sx','.sy','.sz','.v']
    sdd_LockHideAttr(curList,attrList)

def sdd_LockHideAttr(objlist,attrList):
    for o in objlist:
        for a in attrList:
            cmds.setAttr(o+a,l=1,k=0)

def sdd_SplineIkStretch(ik_cur,curList,ikJntList):
    axis='.tx'
    if(radioButton('axisYRB',q=1,sl=1)):
        axis='.ty'
    if(radioButton('axisZRB',q=1,sl=1)):
        axis='.tz'

    curInfo=createNode('curveInfo',n=ik_cur+'_curInfo')
    curShape=listRelatives(ik_cur,s=1,f=1)[0]
    cmds.connectAttr(curShape+'.worldSpace[0]',curInfo+'.inputCurve')

    globalCur=duplicate(ik_cur,rr=1,n=ik_cur+'_gl')[0]
    cmds.setAttr(globalCur+'.it',1)
    cmds.setAttr(globalCur+'.v',0)
    globalCurInfo=createNode('curveInfo',n=globalCur+'_curInfo')
    globalCurShape=listRelatives(globalCur,s=1,f=1)[0]
    cmds.connectAttr(globalCurShape+'.worldSpace[0]',globalCurInfo+'.ic')

    ikCurMd=createNode('multiplyDivide',n=ik_cur+'_md')
    cmds.setAttr(ikCurMd+'.op',2)
    cmds.connectAttr(curInfo+'.al',ikCurMd+'.i1x')
    cmds.connectAttr(globalCurInfo+'.al',ikCurMd+'.i2x')

    ikCurBC=createNode('blendColors',n=ik_cur+'_bc')
    cmds.setAttr(ikCurBC+'.c2r',1)
    cmds.connectAttr(ikCurMd+'.ox',ikCurBC+'.c1r')

    cmds.addAttr(curList[-1],k=1,ln="Stretch",at='float',min=0,max=1,dv=1)
    cmds.connectAttr(curList[-1]+'.Stretch',ikCurBC+'.b')

    ikCurCD=createNode('condition',n=ik_cur+'_cd')
    cmds.setAttr(ikCurCD+'.st',1)
    cmds.setAttr(ikCurCD+'.op',2)
    cmds.connectAttr(ikCurBC+'.opr',ikCurCD+'.ft')
    cmds.connectAttr(ikCurBC+'.opr',ikCurCD+'.ctr')

    for i in ikJntList[1:]:
        val=getAttr(i+axis)
        md=createNode('multiplyDivide',n=i+'_md')
        cmds.setAttr(md+'.i1x',val)
        cmds.connectAttr(ikCurCD+'.ocr',md+'.i2x')
        cmds.connectAttr(md+'.ox',i+axis)
    return globalCur

def sdd_SplineIkTwist(curList,ik_H):
    start=curList[0]
    end=curList[-1]
    startLoc=spaceLocator(p=[0,0,0],n=start+'_loc')[0]
    endLoc=spaceLocator(p=[0,0,0],n=end+'_loc')[0]
    cmds.delete(parentConstraint(start,startLoc))
    cmds.delete(parentConstraint(end,endLoc))
    cmds.move(0,1,0,startLoc,endLoc,r=1,wd=1)
    cmds.parent(startLoc,start)
    cmds.parent(endLoc,end)
    cmds.setAttr(ik_H+'.dtce',1)
    cmds.setAttr(ik_H+'.dwut',4)
    cmds.connectAttr(startLoc+'.worldMatrix[0]',ik_H+'.dwum')
    cmds.connectAttr(endLoc+'.worldMatrix[0]',ik_H+'.dwue')
    cmds.setAttr(startLoc+'.v',0)
    cmds.setAttr(endLoc+'.v',0)

def sdd_SplineIkFkSwich(curList,curGrpList):
    conList=[]
    for i in range(len(curList)-1):
        con=parentConstraint(curList[i],curGrpList[i+1],mo=1)[0]
        conList.append(con)
    cmds.addAttr(curList[-1],k=1,ln="IkFk",at='long',min=0,max=1,dv=1)
    for i in conList:
        cmds.connectAttr(curList[-1]+'.IkFk',i+'.w0')

def sdd_CreateCntByList(cntNameList,suf):
    axis='.tx'
    if(radioButton('axisYRB',q=1,sl=1)):
        axis='.ty'
    if(radioButton('axisZRB',q=1,sl=1)):
        axis='.tz'
    curList=[]
    grpList=[]
    for i in cntNameList:
        baseName=i[:]+suf
        cirName=circle(ch=0,nr=(1,0,0),r=2,n=baseName)[0]
        curList.append(cirName)
        grp=group(cirName,n=baseName+'_grp')
        grpList.append(grp)
        cmds.delete(parentConstraint(i,grp))
        cmds.parentConstraint(cirName,i)
        attrList=['.sx','.sy','.sz','.v']
        sdd_LockHideAttr([cirName],attrList)


    return [curList,grpList]

def sdd_GetJointListPos(jntList):
    posList=[]
    for i in jntList:
        tmp=xform(i,q=1,ws=1,t=1)
        posList.append(tmp)
    return posList

def sdd_GetCurPosList(cntNum,ik_cur):
    cntPosList=[]
    curLen=getAttr(ik_cur+'.maxValue')
    for i in range(cntNum):
        pm=min(1,max(0,curLen/(cntNum-1)*i))
        tmp=pointOnCurve(ik_cur,pr=pm,p=1)
        cntPosList.append(tmp)
    return cntPosList

def sdd_CreateJointByList(cntPosList,baseName):
    cmds.select(cl=1)
    ctrlJntList=[]
    for i in range(len(cntPosList)):
        jnt=joint(p=cntPosList[i],n=baseName+'_Ctrl_%s'%(i+1))
        ctrlJntList.append(jnt)
    for i in ctrlJntList:
        if(i!=ctrlJntList[-1]):
            cmds.joint(i,e=1,oj='xyz',sao='yup')
        else:
            cmds.setAttr(i+'.jo',0,0,0,typ='float3')
    for i in ctrlJntList:
        if(i!=ctrlJntList[0]):
            cmds.parent(i,w=1)
    return ctrlJntList

def sdd_GetJntChainList(startJnt,endJnt):
    if(objectType(startJnt)!='joint' and cmds.objectType(endJnt)!='joint'):
        return ''
    jntList=[startJnt,]
    nextJnt=startJnt
    while(1):
        nextJnt=listRelatives(nextJnt,c=1,pa=1)
        if(nextJnt==None):
            return ''
            break
        else:
            jntList.append(nextJnt[0])
        if(nextJnt[0]==endJnt):
            return jntList
            break

def sdd_DuplicateList(jntList,suf):
    ikJntList=[]
    pJnt=''
    for i in jntList:
        baseName=sdd_GetBaseName(i)
        jnt=duplicate(i,po=1,rr=1,n=baseName+suf)[0]
        ikJntList.append(jnt)
        if(pJnt!='' and pJnt!=None):
            cmds.parent(jnt,pJnt)
        pJnt=jnt
    return ikJntList


def sdd_JointLoad(id):
    sel=ls(sl=1,typ='joint')
    if(len(sel)>0):
        cmds.textFieldButtonGrp(id,e=1,tx=sel[0])
    else:
        mm.eval('warning "Please cmds.select joint!"')

#=========================================color========================
def sdd_loadicons(rootPath):
    bgcImageList=['sphere','cube','cone','arrow4','circleArrow4','circleArrow2','ring','circle2','arrow','squre','circle','triangleEqual','cross','locator','triangle','lineSquare','lineTriangle','lineCircle']
    for i in bgcImageList:
        iconPath=rootPath+i+'.bmp'
        cmds.iconTextButton(p='rtreplaceShapeGL',bgc=(0.9,0.9,0.9),image=iconPath,c='sdd_changeCntShapeProc("%s")'%i)

#=================================================================
def sdd_unlockAttrFromChannels():
    sel=ls(sl=1)
    channelAttr=['tx','ty','tz','rx','ry','rz','sx','sy','sz','v']
    for i in sel:
        allAttr=listAttr(i,ud=1)
        if(allAttr!=None):
            channelAttr.extend(allAttr)
        for a in channelAttr:
                cmds.setAttr(i+'.'+a,k=1,l=0)

#===========parentShape
def sdd_parentShape():
    sel=ls(sl=1)
    if(len(sel)<2):
        return
    for i in sel[1:]:
        selShape=listRelatives(i,s=1,f=1)
        for s in selShape:
            newShape=rename(s,sel[0].split('|')[-1]+'Shape')
            cmds.parent(i,sel[0])
            cmds.makeIdentity(i,apply=1,t=1,r=1,s=1,n=0)
            cmds.parent(i,w=1)
            cmds.parent(newShape,sel[0],r=1,s=1)
        cmds.delete(i)
#===========keyable
def sdd_lockHideAttrFromChannels(typ):
    sel=ls(sl=1)
    channelAttr=['tx','ty','tz','rx','ry','rz','sx','sy','sz','v']
    for i in sel:
        allAttr=listAttr(i,ud=1)
        if(allAttr!=None):
            channelAttr.extend(allAttr)
        for a in channelAttr:
            if(typ==1):
                cmds.setAttr(i+'.'+a,k=1)
            if(typ==2):
                cmds.setAttr(i+'.'+a,l=0)


def sdd_mirShapePoint(typ):
    sel=ls(sl=1)
    if(len(sel)<2):
        mm.eval('warning "Please cmds.select two Curve!"')
        return
    cur1=sel[0]
    cur2=sel[1]
    cv1=ls(cur1+'.cv[*]',fl=1)
    cv2=ls(cur2+'.cv[*]',fl=1)
    if typ==1:
        axi=[-1,1,1]
    if typ==2:
        axi=[1,1,-1]
    if typ==3:
        axi=[1,-1,1]

    if(len(cv1)!=len(cv2) or len(cv1)==0):
        mm.eval('warning "Curve CV not matching!"')
        return
    for i in range(len(cv1)):
        pos=xform(cv1[i],q=1,ws=1,t=1)
        cmds.xform(cv2[i],ws=1,t=[pos[0]*axi[0],pos[1]*axi[1],pos[2]*axi[2]])
#===========OverColor
def sdd_ChangeOverColor(typ):
    sel=ls(sl=1)
    for i in sel:
        objList=listRelatives(i,s=1,f=1)
        if(radioCollection('rtchangOpRC',q=1,sl=1)=='rtcoTransformRB' or objList==None):
            objList=[i,]
        if(typ==0):
            typ=4
        for o in objList:
            cmds.setAttr(o+'.overrideEnabled',1)
            cmds.setAttr(o+'.overrideColor',typ-1)


#===========shape
def sdd_chgScaCVSMaxMinProc(typ):
    if(typ==1):
        ma=floatField('rtrsScaleMaxCVFS',q=1,v=1)
        cmds.floatSlider('rtrsScaleCVFS',e=1,en=0,max=ma)
        cmds.floatSlider('rtrsScaleCVFS',e=1,en=1)
    if(typ==2):
        mi=floatField('rtrsScaleMinCVFS',q=1,v=1)
        cmds.floatSlider('rtrsScaleCVFS',e=1,min=mi)

def sdd_changeScaleCVSliderProc():
    sel=ls(sl=1,fl=1)
    if(len(sel)==0):
        cmds.floatSlider('rtrsScaleCVFS',e=1,v=0)
        return
    sV=floatSlider('rtrsScaleCVFS',q=1,v=1)
    if(sV>0):
        sV=sV+1
    if(sV<0):
        sV=1-abs(sV)/2
    for i in sel:
        cmds.select(i)
        if(len(i.split('.'))!=1):
            cmds.scale(sV,sV,sV,r=1)
        else:
            cmds.scale(sV,sV,sV,i+'.cv[*]',r=1)
    cmds.select(sel)
    cmds.floatSlider('rtrsScaleCVFS',e=1,v=0)

def sdd_selectAllCurveCVProc():
    sel=ls(sl=1)
    cmds.select(cl=1)
    for i in sel:
        cmds.select(i+'.cv[*]',add=1)

def sdd_changeCntShapeProc(idx):
    typ=radioCollection('replaceOpRC',q=1,sl=1)
    if(typ=='rtroCreateRB'):
        sdd_createCurveControl(idx,'tmp_shape')
        cmds.makeIdentity(apply=1,t=1,r=1,s=1)
        return
    sel=ls(sl=1)
    if(len(sel)==0):
        mm.eval('warning "please cmds.select object!"')
        return
    if(typ=='rtroReplaceRB'):
        sdd_replaceCntShapeProc(idx,sel,1)
    if(typ=='rtroAddRB'):
        sdd_replaceCntShapeProc(idx,sel,0)


def sdd_replaceCntShapeProc(idx,sel,de):
    for i in sel:
        delShape=listRelatives(i,s=1,f=1)
        if(delShape==None):
            delShape=[i,]
        if(de==1):
            cmds.delete(delShape)
        newName=sdd_createCurveControl(idx,i+'_tmpShape')
        tmpPos=xform(i,q=1,ws=1,t=1)
        tmpPos=[round(tmpPos[0],3),round(tmpPos[1],3),round(tmpPos[2],3)]
        if(tmpPos==[0,0,0]):
            cmds.parentConstraint(i,newName,n='tmp_shape_con')
            cmds.delete('tmp_shape_con')
        cmds.makeIdentity(apply=1,t=1,r=1,s=1)
        tmpShape=listRelatives(newName,s=1,f=1)
        tmpName=rename(tmpShape[0],i+'Shape')
        cmds.parent(tmpName,i,add=1,s=1)
        cmds.delete(newName)
    cmds.select(sel)
#===========Create cnt
def sdd_createCurveControl(cnt,name):
    cname=''
    if(cnt=='sphere'):
        cname=curve(n=name,d=1,p=[(0.504214,0,0),(0.491572,0.112198,0),(0.454281,0.21877,0),(0.394211,0.314372,0),(0.314372,0.394211,0),(0.21877,0.454281,0),(0.112198,0.491572,0),(0,0.504214,0),(-0.112198,0.491572,0),(-0.21877,0.454281,0),(-0.314372,0.394211,0),(-0.394211,0.314372,0),(-0.454281,0.21877,0),(-0.491572,0.112198,0),(-0.504214,0,0),(-0.491572,-0.112198,0),(-0.454281,-0.21877,0),(-0.394211,-0.314372,0),(-0.314372,-0.394211,0),(-0.21877,-0.454281,0),(-0.112198,-0.491572,0),(0,-0.504214,0),(0.112198,-0.491572,0),(0.21877,-0.454281,0),(0.314372,-0.394211,0),(0.394211,-0.314372,0),(0.454281,-0.21877,0),(0.491572,-0.112198,0),(0.504214,0,0),(0.491572,0,-0.112198),(0.454281,0,-0.21877),(0.394211,0,-0.314372),(0.314372,0,-0.394211),(0.21877,0,-0.454281),(0.112198,0,-0.491572),(0,0,-0.504214),(-0.112198,0,-0.491572),(-0.21877,0,-0.454281),(-0.314372,0,-0.394211),(-0.394211,0,-0.314372),(-0.454281,0,-0.21877),(-0.491572,0,-0.112198),(-0.504214,0,0),(-0.491572,0,0.112198),(-0.454281,0,0.21877),(-0.394211,0,0.314372),(-0.314372,0,0.394211),(-0.21877,0,0.454281),(-0.112198,0,0.491572),(0,0,0.504214),(0,0.112198,0.491572),(0,0.21877,0.454281),(0,0.314372,0.394211),(0,0.394211,0.314372),(0,0.454281,0.21877),(0,0.491572,0.112198),(0,0.504214,0),(0,0.491572,-0.112198),(0,0.454281,-0.21877),(0,0.394211,-0.314372),(0,0.314372,-0.394211),(0,0.21877,-0.454281),(0,0.112198,-0.491572),(0,0,-0.504214),(0,-0.112198,-0.491572),(0,-0.21877,-0.454281),(0,-0.314372,-0.394211),(0,-0.394211,-0.314372),(0,-0.454281,-0.21877),(0,-0.491572,-0.112198),(0,-0.504214,0),(0,-0.491572,0.112198),(0,-0.454281,0.21877),(0,-0.394211,0.314372),(0,-0.314372,0.394211),(0,-0.21877,0.454281),(0,-0.112198,0.491572),(0,0,0.504214),(0.112198,0,0.491572),(0.21877,0,0.454281),(0.314372,0,0.394211),(0.394211,0,0.314372),(0.454281,0,0.21877),(0.491572,0,0.112198),(0.504214,0,0)])
    if(cnt=='cube'):
        cname=curve(n=name,d=1,p=[(-0.5,0.5,0.5),(0.5,0.5,0.5),(0.5,0.5,-0.5),(-0.5,0.5,-0.5),(-0.5,0.5,0.5),(-0.5,-0.5,0.5),(-0.5,-0.5,-0.5),(0.5,-0.5,-0.5),(0.5,-0.5,0.5),(-0.5,-0.5,0.5),(0.5,-0.5,0.5),(0.5,0.5,0.5),(0.5,0.5,-0.5),(0.5,-0.5,-0.5),(-0.5,-0.5,-0.5),(-0.5,0.5,-0.5)])

    if(cnt=='cone'):
        cname=curve(n=name,d=1,p=[(0.0,-0.5,0.5),(0.0,0.5,0.5),(0.0,0.5,-0.5),(0.0,-0.5,-0.5),(0.0,-0.5,0.5),(1.0,0.0,0.0),(0.0,0.5,-0.5),(0.0,-0.5,-0.5),(1.0,0.0,0.0),(0.0,0.5,0.5)])

    if(cnt=='circleArrow4'):
        cname=curve(n=name,d=1,p=[(0.0,0.0,0.972),(0.289,0.0,0.683),(0.144,0.0,0.683),(0.144,0.0,0.538),(0.17,0.0,0.532),(0.216,0.0,0.516),(0.28,0.0,0.485),(0.341,0.0,0.444),(0.396,0.0,0.396),(0.444,0.0,0.341),(0.485,0.0,0.28),(0.516,0.0,0.216),(0.532,0.0,0.17),(0.539,0.0,0.144),(0.683,0.0,0.144),(0.683,0.0,0.289),(0.972,0.0,0.0),(0.683,0.0,-0.289),(0.683,0.0,-0.144),(0.538,0.0,-0.144),(0.532,0.0,-0.17),(0.516,0.0,-0.216),(0.485,0.0,-0.28),(0.444,0.0,-0.341),(0.396,0.0,-0.396),(0.341,0.0,-0.444),(0.28,0.0,-0.485),(0.216,0.0,-0.516),(0.17,0.0,-0.532),(0.144,0.0,-0.539),(0.144,0.0,-0.683),(0.289,0.0,-0.683),(0.0,0.0,-0.972),(-0.289,0.0,-0.683),(-0.144,0.0,-0.683),(-0.144,0.0,-0.538),(-0.17,0.0,-0.532),(-0.216,0.0,-0.516),(-0.28,0.0,-0.485),(-0.341,0.0,-0.444),(-0.396,0.0,-0.396),(-0.444,0.0,-0.341),(-0.485,0.0,-0.28),(-0.516,0.0,-0.216),(-0.532,0.0,-0.17),(-0.539,0.0,-0.144),(-0.683,0.0,-0.144),(-0.683,0.0,-0.289),(-0.972,0.0,0.0),(-0.683,0.0,0.289),(-0.683,0.0,0.144),(-0.538,0.0,0.144),(-0.533,0.0,0.168),(-0.517,0.0,0.214),(-0.485,0.0,0.28),(-0.444,0.0,0.341),(-0.396,0.0,0.396),(-0.341,0.0,0.444),(-0.28,0.0,0.485),(-0.216,0.0,0.516),(-0.17,0.0,0.532),(-0.144,0.0,0.539),(-0.144,0.0,0.683),(-0.289,0.0,0.683),(0.0,0.0,0.972)])

    if(cnt=='circle2'):
        cname=curve(n=name,d=3,p=[(0.0,-0.001,0.758),(0.0,-0.0,0.758),(0.0,-0.0,0.758),(0.0,0.023,0.76),(0.0,0.091,0.774),(0.0,0.123,0.881),(0.0,0.087,0.956),(0.0,-0.0,0.992),(0.0,-0.087,0.956),(0.0,-0.124,0.868),(0.0,-0.085,0.782),(0.0,-0.021,0.758),(0.0,-0.001,0.758),(0.0,-0.001,0.758),(0.0,-0.0,0.758),(0.0,-0.0,-0.764),(0.0,-0.0,-0.764),(0.0,-0.0,-0.764),(0.0,-0.021,-0.764),(0.0,-0.085,-0.788),(0.0,-0.124,-0.874),(0.0,-0.087,-0.962),(0.0,-0.0,-0.998),(0.0,0.087,-0.962),(0.0,0.123,-0.887),(0.0,0.091,-0.78),(0.0,0.023,-0.766),(0.0,-0.0,-0.764),(0.0,-0.0,-0.764)])

    if(cnt=='circleArrow2'):
        cname=curve(n=name,d=1,p=[(0.0,0.0,0.976),(0.0,-0.29,0.686),(0.0,-0.145,0.686),(0.0,-0.145,0.541),(0.0,-0.209,0.523),(0.0,-0.321,0.47),(0.0,-0.452,0.347),(0.0,-0.54,0.183),(0.0,-0.57,0.0),(0.0,-0.54,-0.183),(0.0,-0.452,-0.347),(0.0,-0.317,-0.474),(0.0,-0.204,-0.525),(0.0,-0.145,-0.541),(0.0,-0.145,-0.686),(0.0,-0.29,-0.686),(0.0,0.0,-0.976),(0.0,0.29,-0.686),(0.0,0.145,-0.686),(0.0,0.145,-0.541),(0.0,0.209,-0.523),(0.0,0.321,-0.47),(0.0,0.452,-0.347),(0.0,0.54,-0.183),(0.0,0.57,0.0),(0.0,0.54,0.183),(0.0,0.452,0.347),(0.0,0.321,0.47),(0.0,0.209,0.523),(0.0,0.145,0.54),(0.0,0.145,0.686),(0.0,0.29,0.686),(0.0,0.0,0.976)])

    if(cnt=='arrow'):
        cname=curve(n=name,d=1,p=[(-0.4,0.0,0.2),(0.2,0.0,0.2),(0.2,0.0,0.4),(0.6,0.0,0.0),(0.2,0.0,-0.4),(0.2,0.0,-0.2),(-0.4,0.0,-0.2),(-0.4,0.0,0.2)])

    if(cnt=='arrow4'):
        cname=curve(n=name,d=1,p=[(0.0,0.0,0.5),(0.0,-0.15,0.35),(0.0,-0.05,0.35),(0.0,-0.05,0.05),(0.0,-0.35,0.05),(0.0,-0.35,0.15),(0.0,-0.5,0.0),(0.0,-0.35,-0.15),(0.0,-0.35,-0.05),(0.0,-0.05,-0.05),(0.0,-0.05,-0.35),(0.0,-0.15,-0.35),(0.0,0.0,-0.5),(0.0,0.15,-0.35),(0.0,0.05,-0.35),(0.0,0.05,-0.05),(0.0,0.35,-0.05),(0.0,0.35,-0.15),(0.0,0.5,0.0),(0.0,0.35,0.15),(0.0,0.35,0.05),(0.0,0.05,0.05),(0.0,0.05,0.35),(0.0,0.15,0.35),(0,0,0.5)])

    if(cnt=='triangle'):
        cname=curve(n=name,d=1,p=[[0,0,0],[0,0.6,-0.15],[0,0.6,0.15],[0,0,0]])

    if(cnt=='triangleEqual'):
        cname=curve(n=name,d=1,p=[(-.5,.5,0),(.5,0,0),(-.5,-.5,0),(-.5,.5,0)])

    if(cnt=='squre'):
        cname=curve(n=name,d=1,p=[(0,-.5,.5),(0,-.5,-.5),(0,.5,-.5),(0,.5,.5),(0,-.5,.5)])

    if(cnt=='circle'):
        cname=circle(n='dd',nr=[1,0,0],r=0.5,ch=0)

    if(cnt=='cross'):
        cname=curve(n=name,d=1,p=[(0.075,-0.075,0.0),(0.298,-0.075,0.0),(0.3,0.075,0.0),(0.075,0.075,0.0),(0.075,0.3,0.0),(-0.075,0.3,0.0),(-0.075,0.075,0.0),(-0.3,0.075,0.0),(-0.3,-0.075,0.0),(-0.075,-0.075,0.0),(-0.075,-0.3,0.0),(0.075,-0.3,0.0),(0.075,-0.075,0.0)])

    if(cnt=='locator'):
        cname=curve(n=name,d=1,p=[(0,.5,0),(0,-.5,0),(0,0,0),(-.5,0,0),(.5,0,0),(0,0,0),(0,0,.5),(0,0,-.5)])

    if(cnt=='lineSquare'):
        cname=curve(n=name,d=1,p=[(0.0,0.0,0.0),(0.0,0.654,0.0),(0.0,0.756,-0.103),(0.0,0.859,0.0),(0.0,0.756,0.103),(0.0,0.654,0.0),(0.0,0.859,0.0),(0.0,0.756,-0.103),(0.0,0.756,0.103)])

    if(cnt=='lineTriangle'):
        cname=curve(n=name,d=1,p=[(0.0,0.0,0.0),(0.0,0.669,0.0),(0.0,0.669,-0.118),(0.0,0.846,0.0),(0.0,0.669,0.118),(0.0,0.669,0.0)])

    if(cnt=='lineCircle'):
        cname=curve(n=name,d=3,p=[(0.0,0.0,0.0),(0.0,0.66,0.0),(0.0,0.66,0.0),(0.0,0.66,0.0),(0.0,0.661,-0.02),(0.0,0.683,-0.081),(0.0,0.768,-0.107),(0.0,0.834,-0.076),(0.0,0.866,0.0),(0.0,0.834,0.077),(0.0,0.757,0.108),(0.0,0.682,0.075),(0.0,0.661,0.019),(0.0,0.66,0.0),(0.0,0.66,0.0)])

    if(cnt=='ring'):
        cname=curve(n=name,d=3,p=[(0,0.055,-0.495),(-0.11,0.055,-0.495),(-0.37796,0.055,-0.411902),(-0.55,0.055,0),(-0.388909,0.055,0.388909),(0,0.055,0.55),(0.388909,0.055,0.388909),(0.55,0.055,0),(0.39325,0.055,-0.3575),(0.189373,0.055,-0.459162),(0.189373,0.055,-0.459162),(0.189373,0.055,-0.459162),(0.189373,0.055,-0.459162),(0.189373,0.11,-0.459162),(0.189373,0.11,-0.459162),(0.189373,0.11,-0.459162),(0,0,-0.495),(0,0,-0.495),(0,0,-0.495),(0.189373,-0.11,-0.459162),(0.189373,-0.11,-0.459162),(0.189373,-0.11,-0.459162),(0.189373,-0.055,-0.459162),(0.189373,-0.055,-0.459162),(0.189373,-0.055,-0.459162),(0.393078,-0.055,-0.358684),(0.55,-0.055,0),(0.388909,-0.055,0.388909),(0,-0.055,0.55),(-0.388909,-0.055,0.388909),(-0.55,-0.055,0),(-0.385624,-0.055,-0.382339),(-0.11,-0.055,-0.495),(0,-0.055,-0.495),(0,-0.055,-0.495),(0,-0.055,-0.495),(0,0.055,-0.495)])
        
    offsetX=optionMenuGrp('rtrsTypeXOMG',q=1,v=1)
    offsetY=optionMenuGrp('rtrsTypeYOMG',q=1,v=1)
    offsetZ=optionMenuGrp('rtrsTypeZOMG',q=1,v=1)

    if(type(cname)==list):
        cname=cname[0]
    cmds.rotate(int(offsetX),int(offsetY),int(offsetZ),cname+'.cv[*]')

    return cname

#===========system cmds.joint tool
def sdd_InsertJointTool():
    sel=ls(sl=1)
    if(len(sel)>0):
        mm.eval('enableIsolateSelect modelPanel4 1;')
    InsertJointTool()

#===========Local rotation Axes
def sdd_orientEndJnt():
    sel=ls(sl=1)
    for i in sel:
        cmds.setAttr(i+'.jointOrient',0,0,0,typ='float3')

def sdd_showHideLocalAxes():
    sel=ls()
    for i in sel:
        attrList=listAttr(i)
        if('displayLocalAxis' in attrList):
            cmds.setAttr(i+'.dla',show)


#=================================================================
#===========zore group
def sdd_CreateZoreGrpBySel():
    sel=ls(sl=1)
    if(len(sel)==0):
        return
    grpList=[]
    for i in sel:
        grpName=i+'_zeroGrp'
        grpName=sdd_returnRepeatName(grpName)
        grpName=group(em=1,n=grpName)
        grpList.append(grpName)
        cmds.delete(parentConstraint(i,grpName))
        gP=listRelatives(i,p=1)
        cmds.parent(i,grpName)
        if(gP!=None):
            cmds.parent(grpName,gP)
    cmds.select(grpList)

def sdd_returnRepeatName(name):
    if not(objExists(name)):
        return name
    idx=1
    while True :
        ret=name+'%s'%idx
        if not(objExists(ret)):
            break
        idx+=1
        if(idx>100):
            break
    return ret

