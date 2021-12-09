from flask_login import UserMixin
from enum import unique
from app import db

class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50),unique=True)
    username = db.Column(db.String(50),unique=True)
    password = db.Column(db.String(100))
    cargo = db.Column(db.String(50))

    #relacion uno a muchos con contract
   # contract = db.relationship("Contract", back_populates="users")


