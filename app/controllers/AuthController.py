from app.models.User import User
from app import db, bycrypt, app
from flask_login import LoginManager, login_manager, login_user, logout_user, current_user
from flask import render_template, request, flash, redirect, url_for, session

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth_router.login'
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class AuthController():
    def __init__(self):
        pass

    def principal(self):  
        return render_template('auth/login.html')
    

    def login(self):
        if request.method == 'POST':
            user = User.query.filter_by(username=request.form['username']).first()
            if user:
                if bycrypt.check_password_hash(user.password, request.form['password']):
                    login_user(user)
                    return redirect(url_for('main_router.main'))
            
            flash('Contraseña y/o  Nombre de Usuario incorrectos :c')
            return redirect(url_for('auth_router.login'))
        return render_template('auth/login.html')
    def logout(self):
        session.clear()
        logout_user()
        return redirect(url_for('auth_router.login'))

authcontroller = AuthController()