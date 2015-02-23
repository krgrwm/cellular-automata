import CA

def next_lifegame(ca, x, y):
    "Life game"
    cell = ca.get_cell(x, y)
    next_cell = cell
    live = sum(ca.get_nbhd(x, y))
    if cell==0:
        if live==3:
            next_cell=1
    else:
        if live==2 or live==3:
            next_cell=1
        elif live <= 1 or live >=4:
            next_cell=0
    return next_cell

