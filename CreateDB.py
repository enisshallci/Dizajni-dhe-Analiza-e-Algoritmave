from ScrambleRubixcube import xInitial, make_move
import numpy as np
import sqlite3
from sqlite3 import Error


class St:
    cube = None
    cost = 0


def get_corner_string(cube):
    string = ''
    for i in range(18):
        if i % 3 == 0 or i % 3 == 2:
            string = string + cube[i, 0] + cube[i, 2]
    return string