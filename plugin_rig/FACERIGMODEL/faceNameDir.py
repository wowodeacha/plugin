# -*- coding: utf-8 -*-
'''
autor     yangjie
mail      wowodeacha@gmail.com
created   2016.07.20
'''

class defFaceNameDir():
    nameList = ['ForeHead','Brow','Eye','Check','Nose']
    def __init__(self):
        return

    #设置额头的名称规范
    def setForeHeadDir(self):
        nameBase = self.nameList[0]
        foreHeadList = [ nameBase + '_R', nameBase + '_M',nameBase + '_L']
        foreHeadPivList = [[-4.161,11.294,9.394],[-0.003,11.592,10.558],[4.16,11.294,9.394]]
        return foreHeadList,foreHeadPivList

