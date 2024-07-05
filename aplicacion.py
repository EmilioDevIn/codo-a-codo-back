from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

URI = 'mysql+pymysql://user:123456@localhost/proyecto-python'

aplicacion = Flask(__name__)

CORS(aplicacion)

aplicacion.config['SQLALCHEMY_DATABASE_URI'] = URI
aplicacion.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # None

baseDatos = SQLAlchemy(aplicacion)
marshmallow = Marshmallow(aplicacion)

from controladores.productos import *
from controladores.usuarios import *

if __name__=='__main__':  
    aplicacion.run(debug = True, port = 5000)

