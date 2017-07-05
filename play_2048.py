# /usr/bin python
# -*- coding: utf-8 -*-
import numpy as np
import pythoncom
import pyHook
enter_key = ''

def update_Grid():
    pass

def main(event):
    global enter_key
    enter_key = event.Key
    # print "Key:", event.Key
    print "enter_key:", enter_key
    return event.Key

def start_det_keyboard():
    hm = pyHook.HookManager()
    # 监听所有键盘事件
    hm.KeyDown = main
    # 设置键盘“钩子”
    hm.HookKeyboard()
    # 进入循环，如不手动关闭，程序将一直处于监听状态
    pythoncom.PumpMessages()

def merge_Grid():
    pass

def is_Over():
    pass

if __name__ == "__main__":
    target_num = 32
    # test rec_key()
    start_det_keyboard()
