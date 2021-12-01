from flask import Blueprint
#llamar clase controlador del main
from app.controllers.ClientController import clientcontroller

#definir el nombre de ruta
client_router = Blueprint('client_router', __name__)

#devuelve un main controller con get
@client_router.route('/clientss',methods=['GET'])
def index():
    return clientcontroller.index2()

@client_router.route('/clientss/create',methods=['GET'])
def create():
    return clientcontroller.create()   

