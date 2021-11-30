from flask import render_template
#definimos clase controlador
class MainController():
    def __init__(self):
        pass
 
    #se retorna el metodo index igual con self
    def index(self):
        user1 = {'name': 'Tupaj Katali','surname': 'Suarez'}
        return render_template('index.html', user=user1)

maincontroller = MainController()