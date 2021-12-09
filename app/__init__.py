__version__ = "0.1"
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import secrets

UPLOAD_FOLDER = 'app/static/uploads/'
#app = Flask('app')

app = Flask(__name__, template_folder="views")

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

#Conexion con la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root@localhost/dbpysalon"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db = SQLAlchemy(app)
bycrypt = Bcrypt(app)

secret = secrets.token_urlsafe(32)
app.config['SECRET_KEY'] = secret

app.debug = True

#esto usamos si trabajamos con rutas
# 

from app.routes.auth_router import auth_router
app.register_blueprint(auth_router)

from app.routes.main_router import main_router
app.register_blueprint(main_router)

from app.routes.contract_router import contract_router
app.register_blueprint(contract_router)


from app.routes.user_router import user_router
app.register_blueprint(user_router)
