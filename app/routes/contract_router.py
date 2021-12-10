from flask import Blueprint
from flask_login import login_required
#llamar clase controlador del main
from app.controllers.ContractController import contractcontroller

#definir el nombre de ruta
contract_router = Blueprint('contract_router', __name__)

#devuelve un main controller con get
@contract_router.route('/contracts',methods=['GET'])
@login_required
def index():
    return contractcontroller.index1()

@contract_router.route('/contracts/create',methods=['GET'])
@login_required
def create():
    return contractcontroller.create()   

@contract_router.route('/contracts/store',methods=['POST'])
@login_required
def store():
    return contractcontroller.store()   

@contract_router.route('/contracts/<int:id>/delete',methods=['GET'])
@login_required
def delete(id):
    return contractcontroller.delete(id)   

@contract_router.route('/contracts/<int:id>/edit',methods=['GET'])
@login_required
def edit(id):
    return contractcontroller.edit(id)  

@contract_router.route('/contracts/<int:id>/update',methods=['POST'])
@login_required
def update(id):
    return contractcontroller.update(id)  

#print
@contract_router.route('/convertpdf',methods=['GET'])
@login_required
def convertpdf():
    return contractcontroller.convertpdf()
