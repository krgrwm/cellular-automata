from time import sleep
import disp_term
import disp_curses
import nbhd
import model
import CA

if __name__ == '__main__':
    w=150
    h=70
    lifegame = CA.CA(w, h, model.lifegame())
    amoeba   = CA.CA(w, h, model.amoeba())
    cubism   = CA.CA(w, h, model.cubism())
    lava     = CA.CA(w, h, model.lavalamp())
    perfect  = CA.CA(w, h, model.perfect())
    ss       = CA.CA(w, h, model.squarish_spirals())
    cs       = CA.CA(w, h, model.cyclic_spirals())
    cave     = CA.CA(w, h, model.cave())
    ca = lifegame

    disp_curses.start(ca)

#    while True:
#        sleep(0.06)
#        ca.next_gen()
#        disp_term.print_board(ca.b, ca.get_length())
