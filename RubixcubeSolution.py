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


def ida(start):
    start.h = corner_edge_sum_max(start.cube)
    cost_limit = start.h
    nodes = 0
    frontier = list()
    branching_factors = list()

    while True:
        minimum = None
        frontier.append(start)

        while len(frontier) != 0:
            curr = frontier.pop()

            if goal_reached(curr):
                print('Goal Height:', curr.g)
                print('Branching Factor:', sum(branching_factors)/len(branching_factors))
                # while curr is not None:
                #    if curr.move is not None:
                #        print(curr.move)
                #    curr = curr.parent
                print("Nodes Generated:", nodes)
                return

            b = 0
            nodes = nodes + 12
            for i in range(12):
                new = State()
                new.cube = np.array(curr.cube)
                new.g = curr.g + 1
                new.parent = curr
                new.move = make_move(new.cube, i + 1, 0)
                new.h = corner_edge_sum_max(new.cube)

                if new.g + new.h > cost_limit:
                    if minimum is None or new.g + new.h < minimum:
                        minimum = new.g + new.h
                    continue
                if curr.parent is not None and (contains1(new.cube, curr) or contains2(new.cube, frontier)):
                    continue
                frontier.append(new)
                b = b + 1
            if b != 0:
                branching_factors.append(b)

        cost_limit = minimum
