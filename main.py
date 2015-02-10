import random
from functools import partial
from time import sleep
from termcolor import color

random.seed()

cell_types = 2
N = 50

def gen_rand01(i,j):
    return random.randint(0,1)

def make_board(N, gen=gen_rand01):
#    return [[(i,j) for j in range(N)] for i in range(N)]
    return [[gen(i,j) for i in range(N)] for j in range(N)]

def get_length(b):
    return len(b[0]), len(b)

def get_cell(b,x,y):
    lx, ly = get_length(b)

#周期境界条件
    x = x % lx
    y = y % ly
    return b[y][x]

def get_nbhd(b, r, x, y):
    "Moore"
    nbhd_list = [(i+x,j+y) for i in range(-r, r+1) for j in range(-r, r+1)]
    nbhd_list.remove((x, y))
    return [get_cell(b, *nbhd_xy) for nbhd_xy in nbhd_list]

def next_cell(b, nbhd_func, x, y):
    "Life game"
    cell = get_cell(b, x, y)
    next_cell=cell
    live = sum(get_nbhd(b, 1, x, y))
    if cell==0:
        if live==3:
            next_cell=1
    else:
        if live==2 or live==3:
            next_cell=1
        elif live <= 1 or live >=4:
            next_cell=0
    return next_cell

def next_gen(b, nbhd_func, next_func):
    return make_board(N, partial(next_func, b, nbhd_func))

def print_board(b):
    x,y = get_length(b)
    color_01 = {0:'clear', 1:'green'}
    for j in range(y):
        for i in range(x):
            print(color(color_01[b[i][j]], '  '), end='')
        print("")

#b
#get_cell(b, 5,6)
#next_cell(b, get_nbhd, 5, 6)

b = make_board(N)
b
b = next_gen(b, get_nbhd, next_cell)

for i in range(10000):
    b = next_gen(b, get_nbhd, next_cell)
    print("\033[2J")
    print_board(b)
    sleep(0.1)
