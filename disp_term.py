from termcolor import color

def clear_display():
    print("\033[2J") # clear
    print("\033[1H") # hidari ue

def print_board(b, lxy):
    color_01 = {0:'clear', 1:'cyan'}
    clear_display()

    for j in range(lxy[0]):
        for i in range(lxy[1]):
            print(color(color_01[b[i][j]], '  '), end='')
        print("")
