from app.models.User import User
from app import db
from flask import render_template
class MainController():
    def __init__(self):
        pass

    def index(self):
        #user = {'name': 'Tupaj','surname':'Martinez'}
        users = User.query.all()
        return render_template('index.html', users=users)
maincontroller = MainController()