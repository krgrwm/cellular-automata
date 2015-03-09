#!/usr/bin/env python
import pygame
from pygame.locals import *
import sys
from time import sleep
from math import floor
 
SCREEN_SIZE = (1400, 800)
OFFSET = (10, 10)

cell_size = 5
step = 0
ofsx, ofsy = OFFSET
print_flag = True

def color_grey(cell_state, num_states):
    v = cell_state * (255/num_states)
    return (v, v, v)

def color_green(cell_state, num_states):
    v = cell_state * (255/num_states)
    return (0, v, 0)

def print_board(screen, ca):
    w, h = ca.get_length()
    b = ca.b

    for j in range(h):
        for i in range(w):
            x, y = ofsx + i*(cell_size+step), ofsy + j*(cell_size+step)
            R = Rect(x, y, cell_size, cell_size)
            pygame.draw.rect(screen, color_green(b[j][i], ca.model.num_states), R)
 
def get_board_pos(x, y):
    i = floor((x-ofsx)/(cell_size + step))
    j = floor((y-ofsx)/(cell_size + step))
    return i,j
    

def start(ca):
    pygame.init()

    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("Cellular Automata")
     
    while True:
        global print_flag
        screen.fill([0,0,0])
        print_board(screen, ca)
        pygame.display.update()

        if print_flag:
            ca.next_gen()
            sleep(0.01)

        
        pressed_key = pygame.key.get_pressed()
        pressed_mouse = pygame.mouse.get_pressed()

        if pressed_key[K_n]:
            ca.next_gen()

        if pressed_mouse[0]:
            x, y = pygame.mouse.get_pos()
#                    print(pygame.mouse.get_pos())
            i, j = get_board_pos(x, y)
            ca.set(i, j, ca.model.num_states-1)

        for event in pygame.event.get():
            if event.type == QUIT:  # 終了イベント
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_r:
                    ca.reset_board()
                    print("reset")
                elif event.key == K_s:
                    print_flag = True ^ print_flag
                    print("switch")
                elif event.key == K_e:
                    print("erase")
                    ca.reset()

            if event.type == MOUSEBUTTONDOWN:
                pressed = pygame.mouse.get_pressed()
                if pressed[0]:
                    x, y = pygame.mouse.get_pos()
                    i, j = get_board_pos(x, y)
#                    print(i, j)
                    ca.set(i, j, ca.model.num_states-1)
