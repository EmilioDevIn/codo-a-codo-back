from flask import Blueprint, request

from aplicacion import aplicacion
from servicios.usuarios import ServicioUsuario
from esquemas.usuarios import EsquemaUsuario

usuarios = Blueprint("usuarios", __name__)

'''
@usuarios.route('/crear', methods=['POST'])  
def registrar():
    productoNuevo = ServicioProducto.crear(request.get_json())
    return EsquemaProducto.jsonsify(productoNuevo)
'''

@usuarios.route("/ingresar", methods = ["POST"])
def ingresar():
    pass
    
@usuarios.route("/salir/<id>", methods = ["GET"])
def salir():
    pass

@usuarios.route('/leer', methods = ['GET'])
def leer():
    pass

'''
@usuarios.route('/modificar/<id>' , methods = ['PUT'])
def modificar(id):
    datosAnteriores = ServicioProducto.modificiar(id, request.get_json())
    return EsquemaProducto.jsonsify(datosAnteriores)

@usuarios.route('/eliminar/<id>', methods = ['DELETE'])
def eliminar(id):
    productoEliminado = ServicioProducto.eliminar(id)
    return EsquemaProducto.jsonsify(productoEliminado)

aplicacion.register_blueprint(productos, url_prefix="/productos"
'''

'''
from flask import  jsonify,request  #,Flask# del modulo flask importar la clase Flask y los métodos jsonify,request
from app import app, db, ma
from modelos.usuario_modelo import *

class UsuarioSchema(ma.Schema):
    class Meta:
        fields=('id','usuario','clave','rol')
        
usuario_schema=UsuarioSchema()            # El objeto usuario_schema es para traer un usuario
usuarios_schema=UsuarioSchema(many=True)  # El objeto usuarios_schema es para traer multiples registros de usuario

# crea los endpoint o rutas (json)
@app.route('/usuarios',methods=['GET'])
def get_Usuarios():
    all_usuarios= Usuario.query.all()         # el metodo query.all() lo hereda de db.Model
    result=usuarios_schema.dump(all_usuarios)  # el metodo dump() lo hereda de ma.schema y
                                               # trae todos los registros de la tabla
    return jsonify(result)                       # retorna un JSON de todos los registros de la tabla

@app.route('/usuarios/<id>',methods=['GET'])
def get_id(id):
    usuario=Usuario.query.get(id)
    return usuario_schema.jsonify(usuario)   # retorna el JSON de un usuario recibido como parametro

@app.route("/usuarios/<nombre>", methods = ["GET"])
def obtener_usuario(nombre):
    usuario = Usuario.query.get(nombre)
    return usuario_schema.jsonify(usuario) # Retorna un usuario o nada

@app.route('/usuarios/<id>',methods=['DELETE'])
def delete_usuario(id):
    usuario=Usuario.query.get(id)
    db.session.delete(usuario)
    db.session.commit()
    return usuario_schema.jsonify(usuario)   # me devuelve un json con el registro eliminado

@app.route('/usuarios', methods=['POST']) # crea ruta o endpoint
def create_usuario():
    #print(request.json)  # request.json contiene el json que envio el cliente
    usuario=request.json['nombre']
    clave=request.json['clave']
    rol=request.json['rol']
    new_usuario=Usuario(usuario,clave,rol)
    db.session.add(new_usuario)
    db.session.commit()
    return usuario_schema.jsonify(new_usuario)


@app.route('/usuarios/<id>' ,methods=['PUT'])
def update_usuario(id):
    usuario=Usuario.query.get(id)
    usuario.usuario=request.json['usuario']
    usuario.clave=request.json['clave']
    usuario.rol=request.json['rol']
    db.session.commit()
    return usuario_schema.jsonify(usuario)

'''