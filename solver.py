from board import Board


class Solver (object):
    '''Process.

    1. Establish first board.
    2. Play each possible move.
    3. Evaluate the value of each possible move.
        . Score of move
        . Empty spaces on the board
    4. Commit to the "best" move.
    5. Add random cell
    6. Repeat
    '''

    def __init__(self):
        self.board = Board.new_board()

    def solve(self):
        moves = sorted(
            self.board.shift_right(),
            self.board.shift_left(),
            self.board.shift_up(),
            self.board.shift_down(),
            key=lambda move: move[1])

        return moves

if __name__ == '__main__':
    solver = Solver()
    solver.solve()
