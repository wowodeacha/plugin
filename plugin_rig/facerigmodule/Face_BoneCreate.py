# -*- coding: utf-8 -*-
#
# author     YangJie
# mail      wowodeacha@gmail.com
# created   2016.09.21
# Nothing Impossible
#
#
import maya.cmds as mpy


class FaceJntCreate():
    def __init__(self, char_name='test_char'):
        self.char_name = char_name

    # Import Base Locator
    def import_base_loc(self):

        _LocFilePath = self._pathAbout._getMayaFilePath() + self._BaseLocFile
        _LocFile = _LocFilePath + '.ma'
        _LocFile = _LocFile.replace("\\", "/")
        try:
            mpy.file(_LocFile, i=1, type="mayaAscii", ra=0, mergeNamespacesOnClash=0)
        except:
            pass
        print _LocFile, _LocFilePath

    def test(self):
        _newDis = self._baseDis
        print _newDis


if __name__ == "__main__":
    _FaceJntCreate = FaceJntCreate()

    _FaceJntCreate.import_base_loc()
