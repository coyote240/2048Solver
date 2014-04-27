from board import Board


class Game (object):

    score = 0

    def __init__(self):
        self.moves = []
        self.current_state = Board()

    def move(self, direction=None):
        score = 0
        self.moves.append(self.current_state)
        self.current_state = Board(self.current_state)

        if direction is 'RIGHT':
            score += self.current_state.shift_right()
        elif direction is 'LEFT':
            score += self.current_state.shift_left()
        elif direction is 'UP':
            score += self.current_state.shift_up()
        elif direction is 'DOWN':
            score += self.current_state.shift_down()
        else:
            pass

        self.score += score

        self.current_state.set_random_cell()
        print self.current_state
        print score
