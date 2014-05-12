import random


def collapse_row(row):
    '''Collapse a row, being a list of <size> values, combining
    like cells as appropriate to the game.
    This function assumes that the collapse and score action is always
    a right-to-left operation.  All methods that employ this function assume
    responsibility for ensuring so.

    Returns a tuple containing the new row and the operation's score.
    Returns a score of None if the row could not be collapsed.
    '''
    size = len(row)
    filled_cells = [x for x in row if x is not None]
    output, score = _collapse_row_aux(filled_cells, [], 0)
    output = _pad_row(output, size)

    if output == row:
        score = None

    return output, score


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
        if base is not None:
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

    @classmethod
    def new_board(self):
        board = Board()
        for x in range(self.size):
            for y in range(self.size):
                board[(x, y)] = None
        board = board.add_random_cell()
        board = board.add_random_cell()
        return board

    @property
    def id(self):
        return hash(
            tuple(
                sorted(self.items())))

    def get_empty_cells(self):
        '''Return a list of coordinate tuples for each empty cell on the board.
        '''
        return [key for key in self if self[key] is None]

    def add_random_cell(self):
        '''Return a new board with the addition of one random cell.
        '''
        board = Board(self)
        coords = board.get_empty_cells()
        selected = random.choice(coords)
        board[selected] = random.randint(1, 2) * 2
        return board

    def get_lateral_rows(self):
        '''Return the current board state as a list of lists, oriented
        laterally.
        '''
        rows = [[], [], [], []]
        for x in range(self.size):
            for y in range(self.size):
                rows[x].append(self.get((x, y)))
        return rows

    def _board_with_lateral_rows(self, rows):
        board = Board()
        for x in range(self.size):
            for y in range(self.size):
                board[(x, y)] = rows[x][y]
        return board

    def get_longitudinal_rows(self):
        '''Return the current board state as a list of lists, oriented
        longitudinally.
        '''
        rows = [[], [], [], []]
        for x in range(self.size):
            for y in range(self.size):
                rows[y].append(self.get((x, y)))
        return rows

    def _board_with_longitudinal_rows(self, rows):
        board = Board()
        for x in range(self.size):
            for y in range(self.size):
                board[(x, y)] = rows[y][x]
        return board

    def shift_up(self):
        rows = self.get_longitudinal_rows()
        rows, move_score = self._shift_rows(rows)

        return self._board_with_longitudinal_rows(rows), move_score

    def shift_down(self):
        rows = self.get_longitudinal_rows()
        rows, move_score = self._reverse_shift_rows(rows)

        return self._board_with_longitudinal_rows(rows), move_score

    def shift_left(self):
        rows = self.get_lateral_rows()
        rows, move_score = self._shift_rows(rows)

        return self._board_with_lateral_rows(rows), move_score

    def shift_right(self):
        rows = self.get_lateral_rows()
        rows, move_score = self._reverse_shift_rows(rows)

        return self._board_with_lateral_rows(rows), move_score

    def _shift_rows(self, rows):
        move_score = None

        for index, row in enumerate(rows):
            rows[index], score = collapse_row(row)
            if score is not None:
                if move_score is None:
                    move_score = 0
                move_score += score

        return rows, move_score

    def _reverse_shift_rows(self, rows):
        move_score = None

        for index, row in enumerate(rows):
            rows[index].reverse()
            rows[index], score = collapse_row(row)
            rows[index].reverse()
            if score is not None:
                if move_score is None:
                    move_score = 0
                move_score += score

        return rows, move_score


class StatefulBoard(Board):

    def __init__(self, base=None):
        super(StatefulBoard, self).__init__(base)

    def add_random_cell(self):
        coords = self.get_empty_cells()
        selected = random.choice(coords)
        self[selected] = random.randint(1, 2) * 2

    def set_lateral_rows(self, rows):
        for x in range(self.size):
            for y in range(self.size):
                self[(x, y)] = rows[x][y]
        return self

    def set_longitudinal_rows(self, rows):
        for x in range(self.size):
            for y in range(self.size):
                self[(x, y)] = rows[y][x]
        return self

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
