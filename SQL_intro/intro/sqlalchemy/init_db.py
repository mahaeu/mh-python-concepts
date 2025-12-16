"""
Create database tables from ORM models.

This script is responsible for creating the database schema.
It does NOT insert data and does NOT run migrations.

What happens step by step:
1. The database engine is created (connection to SQLite).
2. ORM models are imported so their table definitions are registered.
3. SQLAlchemy creates missing tables in the database.
"""

from db import engine, Base
from models import Product  # Importing the model registers its table metadata


# Base.metadata contains all table definitions collected from ORM models.
# create_all() compares these definitions with the actual database
# and creates tables that do not exist yet.
#
# bind=engine tells SQLAlchemy:
# "Execute the CREATE TABLE statements using this database connection."
Base.metadata.create_all(bind=engine)
