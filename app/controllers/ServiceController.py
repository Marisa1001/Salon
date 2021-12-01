from flask import render_template
#definimos clase controlador
class ServiceController():
    def __init__(self):
        pass
 
    #se retorna el metodo index igual con self
    def index4(self):
        #users = User.query.all()
        return render_template('servicess/index.html')

servicecontroller = ServiceController()