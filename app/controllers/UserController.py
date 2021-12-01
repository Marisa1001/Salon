from flask import render_template
#definimos clase controlador
class UserController():
    def __init__(self):
        pass
 
    #se retorna el metodo index igual con self
    def index5(self):
        #users = User.query.all()
        return render_template('users/index.html')

usercontroller = UserController()