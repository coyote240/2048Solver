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
                    out += '. '
                else:
                    out += str(value) + ' '
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

    def get_lateral_rows(self):
        rows = [[], [], [], []]
        for x in range(self.size):
            for y in range(self.size):
                rows[x].append(self.get((x, y)))
        return rows

    def set_lateral_rows(self, rows):
        for x in range(self.size):
            for y in range(self.size):
                self[(x, y)] = rows[x][y]
        return self

    def get_longitudinal_rows(self):
        rows = [[], [], [], []]
        for x in range(self.size):
            for y in range(self.size):
                rows[y].append(self.get((x, y)))
        return rows

    def set_longitudinal_rows(self, rows):
        for x in range(self.size):
            for y in range(self.size):
                self[(x, y)] = rows[y][x]
        return self

    def collapse_row(self, row):
        filled = [x for x in row if x is not None]
        output = []

        def collapse(row):
            if len(row) > 1:
                (a, b), rest = row[:2], row[2:]
                if a == b:
                    output.append(a + b)
                    collapse(rest)
                else:
                    output.append(a)
                    collapse([b] + rest)
            elif len(row) is 1:
                output.append(row[0])
            else:
                pass

        collapse(filled)
        return output + [None] * (self.size - len(output))
