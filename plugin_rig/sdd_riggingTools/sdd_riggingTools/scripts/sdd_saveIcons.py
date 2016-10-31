if(window('SaveCurveControlCamWin',q=1,ex=1)):
    deleteUI('SaveCurveControlCamWin',window=1)
windowPref('SaveCurveControlCamWin',ra=1)
window('SaveCurveControlCamWin',rtf=1,menuBar=1,s=1,t='SaveCurveControlCamWin')

formLayout('sccMainFormFL',w=282,h=282)
paneLayout('sccMainPL')
if(modelPanel('sccCamPanel',q=1,ex=1)):
    deleteUI('sccCamPanel',pnl=1)
modelPanel('sccCamPanel',p='sccMainPL',mbv=1)
bar=modelPanel('sccCamPanel',q=1,bl=1)
modelPanel('sccCamPanel',e=1,mbv=0)
layout(bar,e=1,vis=0)
columnLayout(p='sccMainFormFL')
textField('iconName',tx='',w=582)
button(l="save",w=282,c='sdd_blastIcons()')
modelEditor('sccCamPanel',e=1,cam='persp',gr=0,alo=0,hud=0,pm=1,m=0,j=1,nc=1)#nc=1
formLayout('sccMainFormFL',e=1,af=[('sccMainPL','bottom',50),('sccMainPL','top',50),('sccMainPL','left',50),('sccMainPL','right',50),])

showWindow('SaveCurveControlCamWin')
def sdd_blastIcons():
	setAttr('defaultRenderGlobals.imageFormat',20)
	setFocus('sccCamPanel')
	iconsName=textField('iconName',q=1,tx=1)
	playblast(v=0,frame=0,w=64,h=64,orn=0,p=100,cf="C:/Users/Administrator/Desktop/sdd_riggingTools/icons/"+iconsName+'.bmp',fmt='image')
