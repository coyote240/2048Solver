import random


def collapse_row(row):
    size = len(row)
    filled_cells = [x for x in row if x is not None]
    output, score = _collapse_row_aux(filled_cells, [], 0)
    return _pad_row(output, size), score


def _collapse_row_aux(input_list, output_list, score):
    if len(input_list) > 1:
        (a, b), rest = input_list[:2], input_list[2:]
        if a == b:
            c = a + b
            score += c
            output_list.append(c)
            output_list, score = _collapse_row_aux(
                rest, output_list, score)
        else:
            output_list.append(a)
            output_list, score = _collapse_row_aux(
                [b] + rest, output_list, score)
    elif len(input_list) is 1:
        output_list.append(input_list[0])

    return output_list, score


def _pad_row(row, size):
    return row + ([None] * (size - len(row)))


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

    def empty_cells(self):
        return [key for key in self if self[key] is None]

    def set_random_cell(self):
        coords = self.empty_cells()
        selected = random.choice(coords)
        self[selected] = random.randint(1, 2) * 2

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

    def pad_row(self, row):
        '''Pad the given row to size with a value of None.
        '''
        return row + [None] * (self.size - len(row))

    def shift_up(self):
        move_score = 0
        rows = self.get_longitudinal_rows()
        for index, row in enumerate(rows):
            rows[index], score = collapse_row(row)
            move_score += score
        self.set_longitudinal_rows(rows)
        return move_score

    def shift_down(self):
        move_score = 0
        rows = self.get_longitudinal_rows()

        for index, row in enumerate(rows):
            rows[index].reverse()
            rows[index], score = collapse_row(row)
            rows[index].reverse()
            move_score += score

        self.set_longitudinal_rows(rows)
        return move_score

    def shift_left(self):
        move_score = 0
        rows = self.get_lateral_rows()
        for index, row in enumerate(rows):
            rows[index], score = collapse_row(row)
            move_score += score
        self.set_lateral_rows(rows)
        return move_score

    def shift_right(self):
        move_score = 0
        rows = self.get_lateral_rows()

        for index, row in enumerate(rows):
            rows[index].reverse()
            rows[index], score = collapse_row(row)
            rows[index].reverse()
            move_score += score

        self.set_lateral_rows(rows)
        return move_score
