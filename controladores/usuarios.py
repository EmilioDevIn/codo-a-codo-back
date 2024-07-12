from flask import Blueprint, request

from aplicacion import aplicacion
from servicios.usuarios import ServicioUsuario
from esquemas.usuarios import jsonify

usuarios = Blueprint("usuarios", __name__)

@usuarios.route('/crear', methods=['POST'])  
def registrar():
    usuarioNuevo = ServicioUsuario.crear(request.get_json())
    return jsonify(usuarioNuevo)

@usuarios.route("/ingresar", methods = ["POST"])
def ingresar():
    pass
    
@usuarios.route("/salir/<id>", methods = ["GET"])
def salir():
    pass

@usuarios.route('/leer', methods = ['GET'])
def leer():
    usuarios = ServicioUsuario.leer()
    return jsonify(usuarios, many = True)

@usuarios.route('/modificar/<id>' , methods = ['PUT'])
def modificar(id):
    datosAnteriores = ServicioUsuario.modificiar(id, request.get_json())
    return jsonify(datosAnteriores)

@usuarios.route('/eliminar/<id>', methods = ['DELETE'])
def eliminar(id):
    usuarioEliminado = ServicioUsuario.eliminar(id)
    return jsonify(usuarioEliminado)

@usuarios.route("/obtener/<id>", methods = ["GET"])
def obtener(id):
    usuario = ServicioUsuario.obtener(id)
    return jsonify(usuario)

aplicacion.register_blueprint(usuarios, url_prefix="/usuarios")