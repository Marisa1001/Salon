from flask import Blueprint
from flask_login import login_required
from app.controllers.MainController import maincontroller

main_router = Blueprint('main_router', __name__)

@main_router.route('/home',methods=['GET'])
@login_required
def main():
    return maincontroller.index()
