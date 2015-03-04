from termcolor import color

color_map = {0:'clear', 1:'red', 2:'green', 3:'white', 4:'blue', 5:'purple', 6:'cyan', 7:'yellow'}

def clear_display():
    print("\033[2J") # clear
    print("\033[1H") # hidari ue

def print_board(b, lxy):
    clear_display()

    for j in range(lxy[0]):
        for i in range(lxy[1]):
            print(color(color_map[b[i][j]], '  '), end='')
        print("")
