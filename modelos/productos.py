from aplicacion import baseDatos

class Productos(baseDatos.Model):
    id = baseDatos.Column(baseDatos.Integer, primary_key = True)
    nombre = baseDatos.Column(baseDatos.String(100), nullable = False)
    descripcion = baseDatos.Column(baseDatos.String(200), nullable = False)
    precio = baseDatos.Column(baseDatos.Numeric(precision = 10, scale = 2), nullable = False)
    inventario = baseDatos.Column(baseDatos.Integer, nullable = False)
    imagen = baseDatos.Column(baseDatos.String(200), nullable = False)
    
    def __init__(self, nombre, descripcion, precio, inventario, imagen):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.inventario = inventario
        self.imagen = imagen