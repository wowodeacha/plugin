# -*- coding: utf-8 -*-
#
# author     YangJie
# mail      wowodeacha@gmail.com
# created   2016.09.21
# Nothing Impossible
#
#
import maya.cmds as mpy
from PathAboutFile.NT_PathSet import _pathAbout


class _FaceJnt_Create():       
    _BaseLocFile = "Face_Base_Loc"
    _pathAbout = _pathAbout() 
    
    def __init__(self,_charName = '_testChar'):        
        self._charName = _charName


# Import Base Locator
    def import_base_loc(self):
        
        _LocFilePath = self._pathAbout._getMayaFilePath() + self._BaseLocFile
        _LocFile = _LocFilePath + '.ma'
        _LocFile = _LocFile.replace("\\" , "/")
        try:
            mpy.file(_LocFile, i = 1,type="mayaAscii",ra = 0 , mergeNamespacesOnClash = 0)
        except:
            pass
        print _LocFile,_LocFilePath

    def test(self):
        _newDis = self._baseDis
        print _newDis
    
    
    
if __name__ == "__main__":
    
    _FaceJntCreate = _FaceJnt_Create()

    _FaceJntCreate.import_base_loc()