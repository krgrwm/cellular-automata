from functools import partial

def moore(r):
    nbhd_list = [(i,j) for i in range(-r, r+1) for j in range(-r, r+1)]
    nbhd_list.remove((0, 0))
    return lambda: nbhd_list

def neumann(r):
    nbhd_list = [(i,j) for i in range(-r, r+1) for j in range(-r, r+1) if abs(i)+abs(j) <= r]
    nbhd_list.remove((0, 0))
    return lambda: nbhd_list
