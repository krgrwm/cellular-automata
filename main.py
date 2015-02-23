from time import sleep
import disp_term
import nbhd
import model
import CA

if __name__ == '__main__':
    N=100
    lifegame = CA.CA(N, model.lifegame())
    amoeba = CA.CA(N, model.amoeba())
    cubism = CA.CA(N, model.cubism())
    ca = amoeba

    while True:
        disp_term.print_board(ca.b, ca.get_length())
        ca.next_gen()
        #sleep(0.08)
