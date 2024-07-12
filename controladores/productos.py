from flask import Blueprint, request, jsonify as j

from aplicacion import aplicacion
from servicios.tipoProducto import ServicioTipoProducto
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
    productosJson = []
        
    for producto in productos:
        productosJson.append({
            "id": producto.id,
            "nombre": producto.nombre,
            "descripcion": producto.descripcion,
            "precio": producto.precio,
            "inventario": producto.inventario,
            "imagen": producto.imagen,
            "tipoId": producto.tipo_id
            } | {
            "tipo": (ServicioTipoProducto.obtener(producto.tipo_id).nombre)}
        )
        
    return productosJson        

@productos.route('/modificar/<id>', methods=['PUT'])
def modificar(id):
    datosAnteriores = ServicioProducto.modificar(id, request.get_json())
    return jsonify(datosAnteriores)

@productos.route('/eliminar/<id>', methods=['DELETE'])
def eliminar(id):
    productoEliminado = ServicioProducto.eliminar(id)
    return jsonify(productoEliminado)

aplicacion.register_blueprint(productos, url_prefix="/productos")