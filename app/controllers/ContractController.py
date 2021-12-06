
from flask import render_template, url_for, request, redirect, flash
from app.models.Contract import Contract
from app import db
#definimos clase controlador
class ContractController():
    def __init__(self):
        pass
 
    #se retorna el metodo index igual con self
    def index1(self):
        contracts = Contract.query.all()
        return render_template('contracts/index.html', contracts = contracts)

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

    def delete(self, _id):
        contract = Contract.query.get(_id)
        db.session.delete(contract)
        db.session.commit()
        flash('El contrato se ha eliminado con exito')
        return redirect(url_for('contract_router.index'))

    def edit(self, _id):
        contract = Contract.query.get(_id)
        return render_template('contracts/edit.html', contract = contract)

    def update(self, _id):
        if request.method == 'POST':
            clientv = request.form['client']
            tipev = request.form['tipe']
            datev = request.form['date']
            colorv = request.form['color']
            totalv = request.form['total']
            #from app.models.Alumno import Alumno
            contractDB = Contract.query.get(_id)
            contractDB.client = clientv
            contractDB.tipe = tipev
            contractDB.date = datev
            contractDB.color = colorv
            contractDB.total = totalv
            db.session.commit()
            flash('El contrato se ha editado correctamente!!!')
            return redirect(url_for('contract_router.index'))


contractcontroller = ContractController()