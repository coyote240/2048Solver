from game import Game


class Solver (object):

    def __init__(self):
        self.game = Game()


if __name__ == '__main__':
    solver = Solver()
    for i in range(10):
        solver.game.move('UP')
        solver.game.move('DOWN')
        solver.game.move('LEFT')
        solver.game.move('RIGHT')

    print solver.game.score
