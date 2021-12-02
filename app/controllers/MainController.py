
from app import db
from flask import render_template
#definimos clase controlador
class MainController():
    def __init__(self):
        pass
 
    #se retorna el metodo index igual con self
    def index(self):
       # users = {'name': 'Tupaj Katali','surname': 'Suarez'}
        #users = User.query.all()
        return render_template('index.html')

maincontroller = MainController()