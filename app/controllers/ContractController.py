
from flask import render_template, url_for, request, redirect, flash
from app.models.Contract import Contract
from app import db
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

    def store(self):
        if request.method == 'POST':
            client = request.form['client']
            tipe = request.form['tipe']
            date = request.form['date']
            color = request.form['color']
            total = request.form['total']

            #from app.models.Alumno import Alumno
            contractadd = Contract(client = client, tipe = tipe, date = date, color = color, total=total)

            db.session.add(contractadd)
            db.session.commit()

            flash('El nuevo contrato se ha registrado correctamente!!!')

            return redirect(url_for('contract_router.index'))

contractcontroller = ContractController()