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
