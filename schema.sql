CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password_hash TEXT
);

CREATE TABLE items(
    id INTEGER PRIMARY KEY,
    destination TEXT,
    start_date TEXT,
    end_date TEXT,
    description TEXT,
    user_id INTEGER REFERENCES users
);