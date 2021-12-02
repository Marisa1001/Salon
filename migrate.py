from app.models.User import User
from app.models.Contract import Contract

from app import db

db.drop_all()
db.create_all()