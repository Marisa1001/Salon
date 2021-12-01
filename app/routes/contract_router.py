from flask import Blueprint
#llamar clase controlador del main
from app.controllers.ContractController import contractcontroller

#definir el nombre de ruta
contract_router = Blueprint('contract_router', __name__)

#devuelve un main controller con get
@contract_router.route('/contracts',methods=['GET'])
def index():
    return contractcontroller.index1()

@contract_router.route('/contracts/create',methods=['GET'])
def create():
    return contractcontroller.create()   
