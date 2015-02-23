import random
from functools import partial

class CA:
    def __init__(self, N, model):
        random.seed()
        self.N = N
        self.model = model
        self.b = self.make_board(self.gen_rand)

    def get_length(self):
        return len(self.b[0]), len(self.b)

    def get_cell(self, x, y):
        lx, ly = self.get_length()
#周期境界条件
        x = x % lx
        y = y % ly
        return self.b[y][x]

    def get_nbhd(self, x, y):
        return [self.get_cell(x+x0, y+y0) for x0,y0 in self.model.nbhd()]

    def gen_rand(self, i,j):
        return random.randint(0, self.model.num_states-1)

    def make_board(self, gen):
        return [[gen(i,j) for i in range(self.N)] for j in range(self.N)]

    def next_gen(self):
        self.b = self.make_board(partial(self.model.next_cell, self))
