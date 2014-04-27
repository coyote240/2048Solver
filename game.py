from board import Board


class Game (object):

    score = 0

    def __init__(self):
        self.moves = []
        self.current_state = Board()

    def move(self, direction=None):
        self.moves.append(self.current_state)
        self.current_state = Board(self.current_state)

        rows = self.current_state.get_longitudinal_rows()
        for index, row in enumerate(rows):
            rows[index] = self.current_state.collapse_row(row)

        self.current_state.set_longitudinal_rows(rows)
        self.current_state.set_random_cell()
        print self.current_state
