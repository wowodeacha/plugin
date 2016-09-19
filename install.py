# -*- coding: utf-8 -*-
#
# author yangjie
# mail wowodeacha@gmail.com
# date 2016/09/19
#
import os,inspect
from plugin_rig.customui.intallui import

class InstallPlug(object):
    def __init__(self):
        pass

    # current function dir 获取当前脚本路径
    @staticmethod
    def get_cur_dir_fun():
        cur_file = inspect.getfile(inspect.currentframe())
        cur_path = os.path.dirname(cur_file) + "/"
        print cur_path
        return cur_path

if __name__ == '__main__':
    CSet = InstallPlug()
    CSet.get_cur_dir_fun()