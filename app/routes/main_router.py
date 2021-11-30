from flask import Blueprint
#llamar clase controlador del main
from app.controllers.MainController import maincontroller

#definir el nombre de ruta
main_router = Blueprint('main_router', __name__)

#devuelve un main controller con get
@main_router.route('/',methods=['GET'])
def main():
    return maincontroller.index()
