from time import sleep
import disp_term
import disp_curses
import disp_pygame
import nbhd
import model
import CA

if __name__ == '__main__':
    w=70
    h=70
    lifegame = model.life([2,3], [3])
    amoeba   = model.amoeba()
    cubism   = model.cubism()
    lava     = model.lavalamp()
    perfect  = model.perfect()
    ss       = model.squarish_spirals()
    cs       = model.cyclic_spirals()
    cave     = model.cave()
    brians_brain = model.generations([], [2], 3)
    xtasy        = model.generations([1,4,5,6], [2,3,5,6], 16)
    thril_gril   = model.generations([1,2,3,4], [3,4], 48)
    swirl        = model.generations([2,3], [3,4], 8)
    bloomerang   = model.generations([2,3,4], [2,4], 25)
    fireworks    = model.generations([2], [1,3], 21)
    nova         = model.generations([4,5,6,7,8], [2,4,7,8], 25)
    RainZha      = model.generations([2], [2,3], 8)
    Fredkin      = model.vote_for_life([1,3,5,7,9])
    vote_45      = model.vote_for_life([4,6,7,8,9])
    ca = CA.CA(w, h, RainZha)

#    disp_curses.start(ca)
#    ca.reset()
    disp_pygame.start(ca)
#    while True:
#        sleep(0.06)
#        ca.next_gen()
#        disp_term.print_board(ca.b, ca.get_length())
