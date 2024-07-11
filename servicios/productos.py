from modelos.tipoProducto import ModeloTipoProducto
from modelos.producto import ModeloProducto

from aplicacion import baseDatos

class ServicioProducto():
    
    @staticmethod
    def crear(datos):
        producto = ModeloProducto(
            datos["nombre"],
            datos["descripcion"],
            datos["precio"],
            datos["inventario"],
            datos["tipoId"],
            datos["imagen"]
        )
        
        baseDatos.session.add(producto)
        baseDatos.session.commit()
        
        return producto
    
    @staticmethod
    def leer():
        productos = ModeloProducto.query.all()

        return productos
    
    @staticmethod
    def modificar(id, datos):
        producto = ModeloProducto.query.get(id)
        
        producto.nombre = datos["nombre"]
        producto.precio = datos["precio"]
        producto.inventario = datos["inventario"]
        producto.imagen = datos["imagen"]
        producto.tipo_id = datos["tipoId"]
        
        baseDatos.session.commit()
        
        return producto

    @staticmethod
    def eliminar(id):
        producto = ModeloProducto.query.get(id)
        
        baseDatos.session.delete(producto)
        baseDatos.session.commit()
        
        return producto