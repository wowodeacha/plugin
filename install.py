# -*- coding: utf-8 -*-
#
# author yangjie
# mail wowodeacha@gmail.com
# date 2016/09/19
#
import os,inspect
from Tkinter import*


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

    # 获取已安装maya版本
    # TODO： 写一段获取当前maya版本的功能函数

    # 创建窗口
    # def plug_install_win():
    #     # _version=GetVersion()
    #     mtk=Tk()
    #     mtk.title('Maya Plug Install')
    #     if _version==[]:
    #         Label(mtk,text='Warning:You should firstly setup maya !').pack()
    #     else:
    #         Label(mtk,text='Maya Version As Follow:').pack()
    #         for i in range(len(_version)):
    #             _stateGrp.append(IntVar())
    #             ckb=Checkbutton(mtk,variable = _stateGrp[i],text=_version[i])
    #             ckb.select()
    #             ckb.pack()
    #         Button(mtk,text='Install',width=30,command=InstallCMD).pack()
    #     mtk.mainloop()

if __name__ == '__main__':
    CSet = InstallPlug()
    CSet.get_cur_dir_fun()