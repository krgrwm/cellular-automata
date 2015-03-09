import curses
from time import sleep

def colorRGB(r, g, b):
    "r,g,b: 0-5"
    return 16 +(r * 36) + (g * 6) + (b * 1)

def colorGrey(n):
    return (232 + n) % 255


def print_board(stdscr, b, lxy):
    #stdscr.clear()
    my, mx = stdscr.getmaxyx()
    w, h = lxy
    x = w if mx>w else mx-1
    y = h if my>h else my-1

    for j in range(y):
        for i in range(int(x/2)):
            stdscr.addstr(j, i*2, "  ", curses.color_pair(colorGrey((b[j][i]+1))))#curses.color_pair(b[j][i]))
    

def main(stdscr, ca):
    curses.use_default_colors()
    stdscr.clear()
    curses.curs_set(False)

    for i in range(0, curses.COLORS):
        curses.init_pair(i + 1, -1, i)

    while(True):
        print_board(stdscr, ca.b, ca.get_length())

        stdscr.refresh()
        sleep(0.01)
#        stdscr.getch()
        ca.next_gen()


#    for i in range(0, 255):
#        stdscr.addstr(0, 0, " ", curses.color_pair(i))
#        stdscr.refresh()
#        stdscr.getch()

    stdscr.refresh()
    stdscr.getch()

def start(ca):
    curses.wrapper(main, ca)
