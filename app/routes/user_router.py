from flask import Blueprint
#llamar clase controlador del main
from app.controllers.UserController import usercontroller

#definir el nombre de ruta
user_router = Blueprint('user_router', __name__)

#devuelve un main controller con get
@user_router.route('/users',methods=['GET'])
def index():
    return usercontroller.index5()

@user_router.route('/users/create',methods=['GET'])
def create():
    return usercontroller.create()    

@user_router.route('/users/store',methods=['POST'])
def store():
    return usercontroller.store()

@user_router.route('/users/<int:id>/delete',methods=['GET'])
def delete(id):
    return usercontroller.delete(id)   

@user_router.route('/users/<int:id>/edit',methods=['GET'])
def edit(id):
    return usercontroller.edit(id)  

@user_router.route('/users/<int:id>/update',methods=['POST'])
def update(id):
    return usercontroller.update(id)  