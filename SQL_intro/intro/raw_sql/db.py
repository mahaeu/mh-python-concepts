"""
Low-level database access using Python's built-in sqlite3 module.

This module provides a single responsibility:
- open a connection to the SQLite database file

No ORM, no abstractions, no SQL generation.
"""

from pathlib import Path
import sqlite3

# Directory where this file lives
BASE_DIR = Path(__file__).resolve().parent

# SQLite database file for raw SQL experiments
DB_PATH = BASE_DIR / "docs.db"


def get_connection() -> sqlite3.Connection:
    """
    Create and return a new database connection.

    Each call returns a fresh connection.
    Transaction handling is done by the caller.
    """
    return sqlite3.connect(DB_PATH)
