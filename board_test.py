import unittest
import board


class BoardTests(unittest.TestCase):

    rows = []

    def setUp(self):
        self.rows = [
            ([None, None, None, None], [None, None, None, None], 0),
            ([None, None, None, 2], [2, None, None, None], 0),
            ([2, None, None, 2], [4, None, None, None], 4),
            ([None, 4, None, 4], [8, None, None, None], 8),
            ([4, 4, 2, 2], [8, 4, None, None], 12),
            ([2, 2, 2, 4], [4, 2, 4, None], 4),
            ([2, 2, 2, 2], [4, 4, None, None], 8)
        ]

        self.board = board.Board.new_board()

    def test_collapse_row_score(self):
        for start, result, score in self.rows:
            actual_result, actual_score = board.collapse_row(start)
            self.assertEqual(actual_score, score)

    def test_collapse_row_result(self):
        for start, result, score in self.rows:
            actual_result, actual_score = board.collapse_row(start)
            self.assertEqual(actual_result, result)

    def test_get_empty_cells(self):
        empty_cells = self.board.get_empty_cells()
        self.assertEqual(len(empty_cells), 14)

    def test_get_lateral_rows(self):
        size = self.board.size
        rows = self.board.get_lateral_rows()
        self.assertEqual(len(rows), size)
        for row in rows:
            self.assertEqual(len(row), size)

    def test_get_longitudinal_rows(self):
        size = self.board.size
        rows = self.board.get_longitudinal_rows()
        self.assertEqual(len(rows), size)
        for row in rows:
            self.assertEqual(len(row), size)


suite = unittest.TestLoader().loadTestsFromTestCase(BoardTests)
unittest.TextTestRunner(verbosity=2).run(suite)
