from time import sleep
import disp_term
import nbhd
import model
import CA

if __name__ == '__main__':

    cell_types = 2
    moore1 = nbhd.nbhd_moore(1)
    ca = CA.CA(40, moore1, model.next_lifegame)

    while True:
        ca.next_gen()
        disp_term.print_board(ca.b, ca.get_length())
        sleep(0.1)
