from game import Game


class Solver (object):

    def __init__(self):
        self.game = Game()

    def play(self):

        board = self.game.current_state

        while(board is not None):
            board = self.best_move(board)

    def best_move(self, board):
        '''Process.

        1. Establish first board.
        2. Play each possible move.
        3. Evaluate the value of each possible move.
            . Score of move
            . Empty spaces on the board
        4. Commit to the "best" move.
        5. Repeat
        '''
        pass


if __name__ == '__main__':
    solver = Solver()
    solver.play()
