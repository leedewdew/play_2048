# /usr/bin python
# -*- coding: utf-8 -*-
import numpy as np
import pythoncom
import pyHook

# global variable
enter_key = ''
grid_core = "list_version" # "numpy_version"
grid_board = [lst for lst in [range(4)] for i in range(4)] if grid_core == "list_version" \
    else np.zeros((4,4))
state = 'start'

def disply_Grid():
    global grid_board
    for row in range(4):
        print "+---+---+---+---+"
        print "|%3d|%3d|%3d|%3d|" % (grid_board[row][0], \
                grid_board[row][1],grid_board[row][2],grid_board[row][3])
    print "+---+---+---+---+"

def grid_Rand_Fill(choice,key=None):
    if choice == 'start':
        print "start:", key
    elif choice == 'update':
        print "update:", key

def merge_Grid():
    pass

def is_Over():
    pass

def main(event):
    global enter_key, state
    enter_key = event.Key
    print "enter_key:", enter_key
    if state == 'start':
        grid_Rand_Fill('start')
        state = 'update'
    else:
        merge_Grid()
        grid_Rand_Fill('update',enter_key)

    disply_Grid()
    if is_Over():
        print "Over!"
    return True

def start_det_keyboard():
    hm = pyHook.HookManager()
    hm.KeyDown = main
    hm.HookKeyboard()

    pythoncom.PumpMessages()

if __name__ == "__main__":
    target_num = 32
    start_det_keyboard()