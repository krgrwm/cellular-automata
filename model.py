from abc import ABCMeta, abstractmethod
import CA
import nbhd

class Model(object, metaclass=ABCMeta):
    def __init__(self, r, num_states, nbhd):
        self.r = r
        self.num_states = num_states
        self.nbhd = nbhd
        
    @abstractmethod
    def next_cell(self):
        pass

class lifegame(Model):
    def __init__(self):
        r=1
        num_states=2
        Model.__init__(self, r, num_states, nbhd.moore(r))

    def next_cell(self, ca, x, y):
        cell = ca.get_cell(x, y)
        next_cell = cell
        live = sum(ca.get_nbhd(x, y))

        if cell==0:
            if live==3:
                next_cell=1
        else:
            if live==2 or live==3:
                next_cell=1
            elif live <= 1 or live >=4:
                next_cell=0

        return next_cell

class cyclic(Model):
    def __init__(self, r, threshold, num_states, neighbor):
        Model.__init__(self, r, num_states, neighbor(r))
        self.threshold = threshold

    def next_state(self, cell):
        return (cell+1) % self.num_states

    def next_cell(self, ca, x, y):
        cell = ca.get_cell(x, y)
        next_cell = cell
        num_next = ca.get_nbhd(x, y).count(self.next_state(cell))

        if num_next >= self.threshold:
            next_cell = self.next_state(cell)

        return next_cell
        
def cubism():
    return cyclic(2, 5, 3, nbhd.neumann)

def amoeba():
    return cyclic(3, 10, 2, nbhd.neumann)

def lavalamp():
    return cyclic(2, 10, 3, nbhd.moore)

def perfect():
    return cyclic(1, 3, 4, nbhd.moore)

def squarish_spirals():
    return cyclic(2, 2, 6, nbhd.neumann)

def cyclic_spirals():
    return cyclic(3, 5, 8, nbhd.moore)

class cave(Model):
    def __init__(self):
        r=1
        num_states=2
        Model.__init__(self, r, num_states, nbhd.moore(r))

    def next_cell(self, ca, x, y):
        cell = ca.get_cell(x, y)
        num_walls = ca.get_nbhd(x, y).count(1)

        if (cell == 0 and num_walls >= 5) or (cell == 1 and num_walls >= 4):
            next_cell = 1
        else:
            next_cell = 0

        return next_cell
