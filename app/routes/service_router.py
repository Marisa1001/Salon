from flask import Blueprint
#llamar clase controlador del main
from app.controllers.ServiceController import servicecontroller

#definir el nombre de ruta
service_router = Blueprint('service_router', __name__)

#devuelve un main controller con get
@service_router.route('/servicess',methods=['GET'])
def index():
    return servicecontroller.index4()

@service_router.route('/servicess/create',methods=['GET'])
def create():
    return servicecontroller.create()   
