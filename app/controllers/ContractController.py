from flask import render_template, url_for
#definimos clase controlador
class ContractController():
    def __init__(self):
        pass
 
    #se retorna el metodo index igual con self
    def index1(self):
        #users = User.query.all()
        return render_template('contracts/index.html')

    def create(self):
        #users = User.query.all()
        return render_template('contracts/create.html')


contractcontroller = ContractController()