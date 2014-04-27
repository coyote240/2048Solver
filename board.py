import random


class Board (dict):

    '''Board.
    Representing a single state of a board when playing the game 2048.
    '''

    size = 4

    def __init__(self, base=None):
        if base is None:
            self.create()
            return
        for key, val in base.iteritems():
            self[key] = val

    def __str__(self):
        out = ''
        for x in range(self.size):
            for y in range(self.size):
                value = self.get((x, y))
                if value is None:
                    out += '.'
                else:
                    out += str(value)
            out += '\n'
        return out

    def create(self):
        for x in range(self.size):
            for y in range(self.size):
                self[(x, y)] = None
        self.set_random_cell()
        self.set_random_cell()

    def set_random_cell(self):
        # TODO: Rewrite using dictionary comprehension!!!
        x = random.randint(0, self.size - 1)
        y = random.randint(0, self.size - 1)

        current = self.get((x, y))
        if current is not None:
            self.set_random_cell()
        else:
            self[(x, y)] = random.randint(1, 2) * 2
