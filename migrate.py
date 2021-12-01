from app.models.User import User
from app.models.Contract import Contract
from app.models.Client import Client
from app.models.Event import Event
from app.models.Service import Service

from app import db

db.drop_all()
db.create_all()