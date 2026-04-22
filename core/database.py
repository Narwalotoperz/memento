import sqlite3
from flask import Flask, app, g
from flask_sqlalchemy import SQLAlchemy
from .config import config
from sqlalchemy.orm import Mapped, mapped_column


db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"

    name: Mapped[str] = mapped_column(primary_key=True)
    gender: Mapped[str]
    age: Mapped[int]
    social_class: Mapped[str]
    country: Mapped[str]