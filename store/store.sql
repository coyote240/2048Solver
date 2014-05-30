-- Boards
CREATE TABLE IF NOT EXISTS boards (
    id INTEGER PRIMARY KEY NOT NULL,
    state TEXT NOT NULL,
    empty_cells INTEGER
);

-- Board state next moves

CREATE TABLE IF NOT EXISTS boards_next_states (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    board_id INTEGER NOT NULL,
    next_state_id INTEGER NOT NULL,
    score INTEGER,
    empty_cells INTEGER
);

-- Games
CREATE TABLE IF NOT EXISTS games (
    id INTEGER PRIMARY KEY AUTOINCREMENT
);

-- Games Moves
CREATE TABLE IF NOT EXISTS games_moves (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    game_id INTEGER NOT NULL
);
