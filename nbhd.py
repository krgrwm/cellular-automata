from functools import partial

def nbhd_moore(r):
    def _nbhd_moore(r, b, x, y):
        "Moore"
        nbhd_list = [(i+x,j+y) for i in range(-r, r+1) for j in range(-r, r+1)]
        nbhd_list.remove((x, y))
        return nbhd_list
#        return [get_cell(b, *nbhd_xy) for nbhd_xy in nbhd_list]

    return partial(_nbhd_moore, r)
