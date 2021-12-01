__version__ = "0.1"
#importando flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#generar claves de envio o trabajo
import secrets
 
#archivo de almacenamiento de imagenes
UPLOAD_FOLDER = 'app/static/img/uploads/'
#app = Flask('app')
 
 #definiendo el nombre de la vista definimos como views
app = Flask(__name__, template_folder="views")
 
#configuracion imagenes
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

#conexion a la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root@localhost/dbpysalon"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db = SQLAlchemy(app)

#codigos de encriptado
secret = secrets.token_urlsafe(32)
app.config['SECRET_KEY'] = secret
 

#debug verdadero para reiniciar el servidor de forma automatica
app.debug = True

#esto usamos si trabajamos con rutas 
from app.routes.main_router import main_router
app.register_blueprint(main_router)

from app.routes.client_router import client_router
app.register_blueprint(client_router)

from app.routes.contract_router import contract_router
app.register_blueprint(contract_router)

from app.routes.event_router import event_router
app.register_blueprint(event_router)

from app.routes.service_router import service_router
app.register_blueprint(service_router)

from app.routes.user_router import user_router
app.register_blueprint(user_router)
