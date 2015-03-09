import random
from functools import partial

class CA:
    def __init__(self, width, height, model):
        random.seed()
        self.width = width
        self.height = height
        self.model = model
        self.b = self.__make_board(self.__gen_rand)

    def get_length(self):
        return self.width, self.height

    def get_cell(self, x, y):
        lx, ly = self.get_length()
#周期境界条件
        x = x % lx
        y = y % ly
        return self.b[y][x]

    def get_nbhd(self, x, y):
        return [self.get_cell(x+x0, y+y0) for x0,y0 in self.model.nbhd()]

    def __gen_rand(self, i,j):
        return random.randint(0, self.model.num_states-1)

    def __make_board(self, gen):
        return [[gen(i,j) for i in range(self.width)] for j in range(self.height)]

    def next_gen(self):
        self.b = self.__make_board(partial(self.model.next_cell, self))

    def reset_board(self):
        self.b = self.__make_board(self.__gen_rand)

    def set(self, x, y, v):
        self.b[y][x] = v

    def reset(self):
        self.b = self.__make_board(lambda x,y: 0)

class CA2D(CA):
    def __init__(self, width, height, model):
        CA.__init__(self, width, height, model)
        self.current_line=0

    def next_gen(self):
        line_next_gen = [self.model.next_cell(self, x, self.current_line) for x in range(self.width)]
        self.b[current_line] = line_next_gen
        self.current_line = (self.current_line + 1) % self.height

