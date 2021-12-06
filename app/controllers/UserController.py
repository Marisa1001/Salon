from flask import render_template, url_for, request, redirect, flash
from app.models.User import User
from app import db
#definimos clase controlador
class UserController():
    def __init__(self):
        pass
 
    #se retorna el metodo index igual con self
    def index5(self):
        users = User.query.all()
        return render_template('users/index.html',users = users)
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

    def delete(self, _id):
        user = User.query.get(_id)
        db.session.delete(user)
        db.session.commit()
        flash('El usuario se ha eliminado con exito')
        return redirect(url_for('user_router.index'))

    def edit(self, _id):
        user = User.query.get(_id)
        return render_template('users/edit.html', user = user)
    
    def update(self, _id):
        if request.method == 'POST':
            namev = request.form['name']
            emailv = request.form['email']
            usernamev = request.form['username']
            passwordv = request.form['password']
            cargov = request.form['cargo']
            #from app.models.Alumno import Alumno
            userDB = User.query.get(_id)
            userDB.name = namev
            userDB.email = emailv
            userDB.username = usernamev
            userDB.password = passwordv
            userDB.cargo = cargov
            db.session.commit()
            flash('El usuario se ha editado correctamente!!!')
            return redirect(url_for('user_router.index'))

usercontroller = UserController()