from ScrambleRubixcube import xInitial, make_move
import numpy as np
from datetime import datetime
import time


array = np.array([
    [[0, 0, 2], [1, 0, 2], [2, 0, 2]],
    [[0, 0, 1], [1, 0, 1], [2, 0, 1]],
    [[0, 0, 0], [1, 0, 0], [2, 0, 0]],
    [[0, 0, 2], [0, 1, 2], [0, 2, 2]],
    [[0, 0, 1], [0, 1, 1], [0, 2, 1]],
    [[0, 0, 0], [0, 1, 0], [0, 2, 0]],
    [[0, 0, 0], [1, 0, 0], [2, 0, 0]],
    [[0, 1, 0], [1, 1, 0], [2, 1, 0]],
    [[0, 2, 0], [1, 2, 0], [2, 2, 0]],
    [[2, 0, 0], [2, 0, 1], [2, 0, 2]],
    [[2, 1, 0], [2, 1, 1], [2, 1, 2]],
    [[2, 2, 0], [2, 2, 1], [2, 2, 2]],
    [[2, 0, 2], [1, 0, 2], [0, 0, 2]],
    [[2, 1, 2], [1, 1, 2], [0, 1, 2]],
    [[2, 2, 2], [1, 2, 2], [0, 2, 2]],
    [[0, 2, 0], [1, 2, 0], [2, 2, 0]],
    [[0, 2, 1], [1, 2, 1], [2, 2, 1]],
    [[0, 2, 2], [1, 2, 2], [2, 2, 2]],
])


class State:
    cube = None
    g = 0
    h = 0
    parent = None
    move = None


# checks if goal reached. if reached writes goal state in output.txt
def goal_reached(curr):
    if curr.h != 0:
        return False

    # goal reached
    cube = curr.cube
    file = open('output.txt', 'w')
    file.write("              " + str(cube[0, 0:3]) + '\n')
    file.write("              " + str(cube[1, 0:3]) + '\n')
    file.write("              " + str(cube[2, 0:3]) + '\n')
    file.write(str(cube[3, 0:3]) + ' ' + str(cube[6, 0:3]) + ' ' + str(cube[9, 0:3]) + ' ' + str(cube[12, 0:3]) + '\n')
    file.write(str(cube[4, 0:3]) + ' ' + str(cube[7, 0:3]) + ' ' + str(cube[10, 0:3]) + ' ' + str(cube[13, 0:3]) + '\n')
    file.write(str(cube[5, 0:3]) + ' ' + str(cube[8, 0:3]) + ' ' + str(cube[11, 0:3]) + ' ' + str(cube[14, 0:3]) + '\n')
    file.write("              " + str(cube[15, 0:3]) + '\n')
    file.write("              " + str(cube[16, 0:3]) + '\n')
    file.write("              " + str(cube[17, 0:3]) + '\n')

    return True


# checks if child ascendant of parent
def contains1(child, parent):
    curr = parent.parent
    while curr is not None:
        if np.array_equal(curr.cube, child): return True
        curr = curr.parent

    return False


# checks if frontier contains child
def contains2(child, frontier):
    for curr in frontier:
        if np.array_equal(curr.cube, child): return True

    return False


