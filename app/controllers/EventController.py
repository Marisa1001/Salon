from flask import render_template
#definimos clase controlador
class EventController():
    def __init__(self):
        pass
 
    #se retorna el metodo index igual con self
    def index3(self):
        #users = User.query.all()
        return render_template('eventss/index.html')

eventcontroller = EventController()