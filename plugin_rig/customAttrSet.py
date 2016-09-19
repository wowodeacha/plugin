# -*- coding: utf-8 -*-
'''
autor yangjie
mail wowodeacha@gmail.com
date 2016/08/26
'''
import os,inspect

class CustomAttrSetCla(object):
    def __init__(self):
        pass

    # current fuction dir 获取当前脚本路径
    def getCurDirFun(self):
        curFile = inspect.getfile(inspect.currentframe())
        Curpath = os.path.dirname(curFile) + "/"
        return Curpath

if __name__ == '__main__':
    CSet = CustomAttrSetCla()
    CSet.getCurDirFun()