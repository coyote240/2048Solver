from .board import Board


class Game (object):

    score = 0

    def __init__(self):
        self.moves = []
        self.current_state = Board.new_board()

    def commit(self, board):
        self.moves.append(self.current_state)
        self.current_state = board

    def move(self, direction=None):
        score = 0
        new_board = None

        if direction is 'RIGHT':
            new_board, score = self.current_state.shift_right()
        elif direction is 'LEFT':
            new_board, score = self.current_state.shift_left()
        elif direction is 'UP':
            new_board, score = self.current_state.shift_up()
        elif direction is 'DOWN':
            new_board, score = self.current_state.shift_down()
        else:
            raise ValueError('Not a valid direction.')

        self.score += score
        new_board = new_board.add_random_cell()
        self.commit(new_board)
