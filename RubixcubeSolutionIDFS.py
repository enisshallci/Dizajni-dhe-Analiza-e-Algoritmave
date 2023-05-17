from ScrambleRubixcube import xInitial, make_move
import numpy as np
from datetime import datetime
import time


class State:
    cube = None
    cost = 0
    parent = None
    move = None


# checks if goal reached. if reached writes goal state in output.txt
def goal_reached(cube):
    for ref in [0, 3, 6, 9, 12, 15]:
        first = cube[ref, 0]
        for i in range(3):
            for j in range(3):
                if first != cube[ref + i, j]:
                    return False

    # goal reached
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


def idfs(start):
    cost_limit = 1
    nodes = 0
    frontier = list()
    branching_factors = list()

    while True:
        frontier.append(start)

        while len(frontier) != 0:
            curr = frontier.pop()

            if goal_reached(curr.cube):
                print('Goal Height:', curr.cost)
                print('Branching Factor:', sum(branching_factors)/len(branching_factors))
                # while curr is not None:
                #    if curr.move is not None:
                #        print(curr.move)
                #    curr = curr.parent
                print("Nodes Generated:", nodes)
                return

