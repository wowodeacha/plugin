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

    # current function dir 获取当前脚本路径
    @staticmethod
    def get_cur_dir_fun(self):
        cur_file = inspect.getfile(inspect.currentframe())
        cur_path = os.path.dirname(cur_file) + "/"
        return cur_path

if __name__ == '__main__':
    CSet = CustomAttrSetCla()
    CSet.getCurDirFun()