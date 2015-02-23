from functools import partial

def moore(r):
    def _moore(r):
        nbhd_list = [(i,j) for i in range(-r, r+1) for j in range(-r, r+1)]
        nbhd_list.remove((0, 0))
        return nbhd_list

    return partial(_moore, r)

def neumann(r):
    def _neumann(r):
        nbhd_list = [(i,j) for i in range(-r, r+1) for j in range(-r, r+1) if abs(i)+abs(j) <= r]
        nbhd_list.remove((0, 0))
        return nbhd_list
    return partial(_neumann, r)
