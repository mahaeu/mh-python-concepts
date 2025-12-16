"""
Initialize the database schema using raw SQL.

This script applies table definitions from schema.sql
directly to the SQLite database using Python's DB-API.
"""

from pathlib import Path

from db import get_connection


# Load the SQL schema (DDL statements)
SCHEMA_PATH = Path(__file__).resolve().parent / "schema.sql"
schema_sql = SCHEMA_PATH.read_text(encoding="utf-8")


# --- Database interaction ---

# Open a database connection.
# A connection represents an active session with the database
# and manages transactions and file locking.
conn = get_connection()

# Create a cursor from the connection.
# A cursor is required to execute SQL statements.
# It represents an execution context, not the connection itself.
cursor = conn.cursor()

# Execute the SQL statements.
# executescript() runs multiple SQL commands inside
# the same implicit transaction.
cursor.executescript(schema_sql)

# Commit the transaction.
# This permanently applies all schema changes.
# Without commit(), all changes would be rolled back
# when the connection is closed.
conn.commit()

# Close the connection.
# This releases database resources and file locks.
conn.close()
