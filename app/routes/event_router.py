from flask import Blueprint
#llamar clase controlador del main
from app.controllers.EventController import eventcontroller

#definir el nombre de ruta
event_router = Blueprint('event_router', __name__)

#devuelve un main controller con get
@event_router.route('/eventss',methods=['GET'])
def index():
    return eventcontroller.index3()

@event_router.route('/eventss/create',methods=['GET'])
def create():
    return eventcontroller.create()   

