import random


class Solver (object):

    def __init__(self):
        pass


class Game (object):

    score = 0

    def __init__(self):
        pass


class Board (dict):

    '''Board.
    Representing a single state of a board when playing the game 2048.
    '''

    width = 4
    height = 4

    def __init__(self, base=None):
        if base is None:
            self.create_board()

    def __str__(self):
        out = ''
        for x in range(self.width):
            for y in range(self.height):
                value = self.get((x, y))
                out += str(value)
            out += '\n'
        return out

    def create_board(self):
        for x in range(self.width):
            for y in range(self.height):
                self[(x, y)] = None
        self.set_random_cell()
        self.set_random_cell()

    def set_random_cell(self):
        x = random.randint(0, self.width - 1)
        y = random.randint(0, self.height - 1)

        current = self.get((x, y))
        if current is not None:
            self.set_random_cell()
        else:
            self[(x, y)] = random.randint(1, 2) * 2
