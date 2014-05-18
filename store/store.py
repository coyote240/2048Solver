import os
import pickle
import sqlite3


class Store(object):

    def __init__(self, dbfile='2048.db'):
        dbfile = os.path.join(os.path.dirname(__file__), dbfile)
        self.connection = sqlite3.connect(dbfile)
        self.setup()

    def save_board(self, board):
        c = self.connection.cursor()
        c.execute('INSERT INTO boards VALUES (?, ?, ?)', (
            board.id,
            pickle.dumps(board),
            len(board.get_empty_cells())))
        self.connection.commit()

    def get_board(self, id):
        c = self.connection.cursor()
        c.execute('SELECT state FROM boards WHERE id = ?', (id))
        res = c.fetchone()
        if res is not None:
            return pickle.loads(res[0])
        else:
            return None

    def setup(self):
        self.create_board_table()

    def create_board_table(self):
        c = self.connection.cursor()
        c.execute('''
        CREATE TABLE IF NOT EXISTS boards (
            id INTEGER PRIMARY KEY NOT NULL,
            state TEXT NOT NULL,
            empty_cells INTEGER
        );
        ''')
        self.connection.commit()
