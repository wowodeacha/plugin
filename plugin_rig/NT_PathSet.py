'''
Nothing       Impossible

Autor      :    Yang Jie

Created On :   2016.6.16

Version    :       NT_01

'''

import sys,os,inspect

class _pathAbout(object):
    def __init__(self):
        pass 

    def _getMayaFilePath(self):
        _curFile = inspect.getfile(inspect.currentframe())
        _Curpath = os.path.dirname(_curFile)
        _mayaFilePath = os.path.dirname(_Curpath) + "/" + "MayaFile" +"/"
        return _mayaFilePath

if __name__ == '__main__':
    _pathAbout = _pathAbout()
    _CurPath = _pathAbout._getMayaFilePath()

    print _CurPath
   