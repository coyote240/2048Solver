from board import Board


class Game (object):

    score = 0

    def __init__(self):
        self.moves = []
        self.current_state = Board()

    def move(self, direction):
        self.moves.append(self.current_state)
        self.current_state = Board(self.current_state)

    def collapse_row(self, row):
        filled = [x for x in row if x is not None]
        output = []

        def collapse(row):
            if len(row) > 1:
                (a, b), rest = row[:2], row[2:]
                if a == b:
                    self.score += a + b
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
        return output + [None] * (4 - len(output))
