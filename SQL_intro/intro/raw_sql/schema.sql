-- Database schema for raw SQL experiments (DDL only)

CREATE TABLE IF NOT EXISTS categories (
    id INTEGER PRIMARY KEY,                 -- unique row identifier
    name TEXT NOT NULL,                     -- category must have a name
    created_at TEXT DEFAULT CURRENT_TIMESTAMP -- auto-set on insert
);

CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,                 -- unique row identifier
    name TEXT NOT NULL,                     -- product name (required)
    price REAL NOT NULL,                    -- product price
    in_stock INTEGER DEFAULT 1,             -- boolean flag (0 / 1)
    category_id INTEGER NOT NULL,            -- references categories.id
    created_at TEXT DEFAULT CURRENT_TIMESTAMP, -- auto-set on insert
    FOREIGN KEY (category_id) REFERENCES categories(id) -- enforce relationship
);
