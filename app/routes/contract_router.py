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

@contract_router.route('/contracts/store',methods=['POST'])
def store():
    return contractcontroller.store()   

@contract_router.route('/contracts/<int:id>/delete',methods=['GET'])
def delete(id):
    return contractcontroller.delete(id)   

@contract_router.route('/contracts/<int:id>/edit',methods=['GET'])
def edit(id):
    return contractcontroller.edit(id)  

@contract_router.route('/contracts/<int:id>/update',methods=['POST'])
def update(id):
    return contractcontroller.update(id)  

#print
@contract_router.route('/convertpdf',methods=['GET'])
def convertpdf():
    return contractcontroller.convertpdf()
