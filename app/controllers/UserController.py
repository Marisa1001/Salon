from flask import render_template, url_for, request, redirect, flash
from app.models.User import User
from app import db
#definimos clase controlador
class UserController():
    def __init__(self):
        pass
 
    #se retorna el metodo index igual con self
    def index5(self):
        #users = User.query.all()
        return render_template('users/index.html')
    def create(self):
        #users = User.query.all()
        return render_template('users/create.html')

    def store(self):
        if request.method == 'POST':
            name = request.form['name']
            email = request.form['email']
            username = request.form['username']
            password = request.form['password']
            cargo = request.form['cargo']

            #from app.models.Alumno import Alumno
            useradd = User(name = name, email = email, username = username, password = password, cargo=cargo)

            db.session.add(useradd)
            db.session.commit()

            flash('El nuevo usuario ha sido registrado correctamente!!!')

            return redirect(url_for('user_router.index'))

usercontroller = UserController()