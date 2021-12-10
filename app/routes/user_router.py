from flask import Blueprint
from flask_login import login_required
#llamar clase controlador del main
from app.controllers.UserController import usercontroller

#definir el nombre de ruta
user_router = Blueprint('user_router', __name__)

#devuelve un main controller con get
@user_router.route('/users',methods=['GET'])
@login_required
def index():
    return usercontroller.index5()

@user_router.route('/users/create',methods=['GET'])
@login_required
def create():
    return usercontroller.create()    

@user_router.route('/users/store',methods=['POST'])
@login_required
def store():
    return usercontroller.store()

@user_router.route('/users/<int:id>/delete',methods=['GET'])
@login_required
def delete(id):
    return usercontroller.delete(id)   

@user_router.route('/users/<int:id>/edit',methods=['GET'])
@login_required
def edit(id):
    return usercontroller.edit(id)  

@user_router.route('/users/<int:id>/update',methods=['POST'])
@login_required
def update(id):
    return usercontroller.update(id)  