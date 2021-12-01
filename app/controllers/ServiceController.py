from flask import render_template, url_for
#definimos clase controlador
class ServiceController():
    def __init__(self):
        pass
 
    #se retorna el metodo index igual con self
    def index4(self):
        #users = User.query.all()
        return render_template('servicess/index.html')
    
    def create(self):
        #users = User.query.all()
        return render_template('servicess/create.html')

servicecontroller = ServiceController()