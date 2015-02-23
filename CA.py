import random
from functools import partial

class CA:
    def __init__(self, N, nbhd, next):
        self.N = N
        random.seed()
        self.nbhd = nbhd
        self.next = next
        self.b = self.make_board()

    def get_length(self):
        return len(self.b[0]), len(self.b)

    def get_cell(self, x, y):
        lx, ly = self.get_length()
#周期境界条件
        x = x % lx
        y = y % ly
        return self.b[y][x]

    def get_nbhd(self, x, y):
        nbhd_list = self.nbhd(self.b, x, y)
        return [self.get_cell(*nbhd_xy) for nbhd_xy in nbhd_list]

    def gen_rand01(i,j):
        return random.randint(0,1)

    def make_board(self, gen=gen_rand01):
        return [[gen(i,j) for i in range(self.N)] for j in range(self.N)]

    def next_gen(self):
        self.b = self.make_board(partial(self.next, self))
