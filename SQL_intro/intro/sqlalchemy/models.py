"""
ORM model definitions.

ORM (Object Relational Mapping) maps Python classes to database tables.
Each class in this file represents one table in the database.

This module defines structure only:
- table names
- columns
- data types
"""

from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Boolean,
    DateTime,
    ForeignKey,
)

# Base is the declarative ORM base.
# It collects table metadata from all model classes
# so SQLAlchemy knows which tables exist.
from db import Base


class Category(Base):
    """Product category (parent table)."""

    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)


class Product(Base):
    """Product belonging to a category (child table)."""

    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    in_stock = Column(Boolean, default=True)

    category_id = Column(
        Integer,
        ForeignKey("categories.id"),
        nullable=False,
    )

    created_at = Column(DateTime, default=datetime.utcnow)
