import sqlite3
from flask import Flask, app, g
from flask_sqlalchemy import SQLAlchemy
from .config import config
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            config["Database"]["path"],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


class User(db.Model):
    __tablename__ = "Users"
    name: Mapped[str] = mapped_column(primary_key=True)
    gender: Mapped[str]
    age: Mapped[int]
    socialClass: Mapped[str]
    country: Mapped[str]