# -*- coding: utf-8 -*-
#
# author yangjie
# mail wowodeacha@gmail.com
# date 2016/08/26
#
import os,inspect
import json


class CustomAttrSetCla(object):
    def __init__(self):
        pass

    # current function dir 获取当前脚本路径
    @staticmethod
    def get_cur_dir_fun():
        cur_file = inspect.getfile(inspect.currentframe())
        cur_path = os.path.dirname(cur_file) + "/"
        # print cur_path  # test get path
        return cur_path

    ###文件操作
    @staticmethod
    def write_data( in_file, in_data):
        json.dump(in_data, open(in_file, 'w'))

    @staticmethod
    def load_data( in_file):
        data = json.load(open(in_file, 'r'))
        return data

if __name__ == '__main__':
    CSet = CustomAttrSetCla()
    CSet.get_cur_dir_fun()