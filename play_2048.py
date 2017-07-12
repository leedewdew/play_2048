# /usr/bin python
# -*- coding: utf-8 -*-
import numpy as np
import pythoncom
import pyHook
import random

# global variable
enter_key = ''
grid_core = "list_version" # "numpy_version"
grid_board = [[0,0,0,0] for j in range(4)] if grid_core == "list_version" else np.zeros((4,4))
state = 'start'

def row_Display_Format(value):
    if not value:
        return " "
    else:
        return value

def disply_Grid():
    global grid_board
    for row in range(4):
        row_grid_board = map(str,map(row_Display_Format,grid_board[row]))
        row_grid_board.insert(0,' ')
        row_grid_board.append(' ')
        print "   +-----+-----+-----+-----+"
        print '  |  '.join(row_grid_board)
    print "   +-----+-----+-----+-----+"

def grid_Rand_Fill(choice,key=None):
    global grid_board
    blank_block = [] # blank block which equals to 0
    # record each block whose value equals to 0
    for row in range(4):
        for col in range(4):
            if not grid_board[row][col]:
                blank_block.append(row*4+col)
    # random choose a blank block
    block_to_fill = random.choice(blank_block)
    row_to_fill = block_to_fill / 4
    col_to_fill = block_to_fill % 4
    grid_board[row_to_fill][col_to_fill] = random.choice([2,4])

def shiftAndMerge(lst,direction):
    pass

def merge_Grid(enter_key):
    global grid_board
    shift_row_list= []
    merge_row_list = []
    shift_list_compen_zero = []

    if enter_key == 'W': # up
        for col in range(4):
            for row in range(4):
                pass
    elif enter_key == 'S': # down
        for col in range(4):
            for row in range(4):
                pass
    elif enter_key == 'A': # left
        # get non-zero element
        shift_row_list = [filter(lambda x: x != 0, row) for row in grid_board]
        # fill zero to len=4
        for i, row in enumerate(shift_row_list):
            while len(shift_row_list[i]) < 4:
                shift_row_list[i].append(0)
        # update grid_board
        grid_board = shift_row_list
        for row in range(4):
            for col in range(4):
                if col <= 2:
                    if  (not grid_board[row][col]) and (grid_board[row][col] == grid_board[row][col+1]):
                        grid_board[row][col] *= 2
                        grid_board[row][col + 1] = 0 # remove element in case merging with next one
                    merge_row_list.append(grid_board[row][col])
                else: # col+1 out of index
                    merge_row_list.append(grid_board[row][col])
    elif enter_key == 'D': # right
        # get non-zero element
        shift_row_list = [filter(lambda x: x != 0, row) for row in grid_board]
        # fill zero to len=4
        for i, row in enumerate(shift_row_list):
            while len(shift_row_list[i]) < 4:
                shift_row_list[i].insert(0,0)
        # update grid_board
        grid_board = shift_row_list
        for row in range(4):
            for col in range(4):
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
        merge_Grid(enter_key)
        grid_Rand_Fill('update')

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