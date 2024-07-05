from modelos.productos import Productos
from aplicacion import baseDatos

class ServicioProducto():
    
    @staticmethod
    def crear(datos):
        producto = Productos(
            datos["nombre"],
            datos["descripcion"],
            datos["precio"],
            datos["inventario"],
            datos["imagen"]
        )
        
        baseDatos.session.add(producto)
        baseDatos.session.commit()
        
        return producto
    
    @staticmethod
    def leer():
        productos = Productos.query.all()
        
        return productos
    
    @staticmethod
    def modificar(id, datos):
        producto = Productos.query.get(id)
        
        producto.nombre = datos["nombre"]
        producto.precio = datos["precio"]
        producto.inventario = datos["inventario"]
        producto.imagen = datos["imagen"]
        
        baseDatos.session.commit()
        
        return producto

    @staticmethod
    def eliminar(id):
        producto = Productos.query.get(id)
        
        baseDatos.session.delete(producto)
        baseDatos.session.commit()
        
        return producto