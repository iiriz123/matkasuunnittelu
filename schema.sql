CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password_hash TEXT
);

CREATE TABLE items(
    id INTEGER PRIMARY KEY,
    destination TEXT,
    travel_dates TEXT,
    description TEXT,
    user_id INTEGER REFERENCES users
);