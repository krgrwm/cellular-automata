from time import sleep
import disp_term
import nbhd
import model
import CA

if __name__ == '__main__':
    N=80
    lifegame = CA.CA(N, model.lifegame())
    amoeba = CA.CA(N, model.amoeba())
    cubism = CA.CA(N, model.cubism())
    lava = CA.CA(N, model.lavalamp())
    perfect = CA.CA(N, model.perfect())
    ss = CA.CA(N, model.squarish_spirals())
    cs = CA.CA(N, model.cyclic_spirals())
    ca = cs

    while True:
        sleep(0.06)
        ca.next_gen()
        disp_term.print_board(ca.b, ca.get_length())
