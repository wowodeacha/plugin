# -*- coding: utf-8 -*-
'''
autor yangjie
mail wowodeacha@gmail.com

'''
import maya.cmds as mpy

# from faceRigPubFuc import faceRigPubFuc
from faceNameDir import defFaceNameDir

class CreateForeHead():
    def __init__(self):
        pass

    # 创建额头基础骨骼
    def createForeheadBone(self):
        baseForeHeadList, baseForeHeadPivList = defFaceNameDir.setForeHeadDir()


if __name__ == '__main__':
    CreateForeHead = CreateForeHead()
    CreateForeHead.createForeheadBone()
