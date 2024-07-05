from flask import Blueprint, request

from aplicacion import aplicacion
from servicios.productos import ServicioProducto
from esquemas.productos import jsonify

productos = Blueprint("productos", __name__)

@productos.route('/crear', methods=['POST'])  
def crear():
    productoNuevo = ServicioProducto.crear(request.get_json())
    return jsonify(productoNuevo)

@productos.route('/leer', methods = ['GET'])
def leer():
    productos = ServicioProducto.leer()
    return jsonify(productos, many = True)

@productos.route('/modificar/<id>', methods=['PUT'])
def modificar(id):
    datosAnteriores = ServicioProducto.modificar(id, request.get_json())
    return jsonify(datosAnteriores)

@productos.route('/eliminar/<id>', methods=['DELETE'])
def eliminar(id):
    productoEliminado = ServicioProducto.eliminar(id)
    return jsonify(productoEliminado)

aplicacion.register_blueprint(productos, url_prefix="/productos")