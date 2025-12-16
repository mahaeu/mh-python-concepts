"""
Core SQLAlchemy setup.

Defines:
- engine: database connection
- SessionLocal: unit-of-work factory
- Base: declarative ORM base class
"""
from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


# Absolute directory of this file (SQL_intro/intro)
BASE_DIR = Path(__file__).resolve().parent

# Database URL.
# SQLite stores all data directly in this file.
DB_PATH = BASE_DIR / "docs.db"
DB_URL = f"sqlite:///{DB_PATH}"

# Engine manages the connection to the database and SQL execution.
engine = create_engine(DB_URL, echo=True)

# Session factory.
# Each session represents one transactional unit of work.
SessionLocal = sessionmaker(bind=engine)

# Declarative base.
# All ORM models inherit from this to register table metadata.
Base = declarative_base()
