from flask import render_template
#definimos clase controlador
class ClientController():
    def __init__(self):
        pass
 
    #se retorna el metodo index igual con self
    def index2(self):
        #users = User.query.all()
        return render_template('clientss/index.html')

clientcontroller = ClientController()