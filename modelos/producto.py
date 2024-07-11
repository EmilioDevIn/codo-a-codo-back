from aplicacion import baseDatos

class ModeloProducto(baseDatos.Model):
    __tablename__ = "productos"
    id = baseDatos.Column(baseDatos.Integer, primary_key = True)
    nombre = baseDatos.Column(baseDatos.String(100), nullable = False)
    descripcion = baseDatos.Column(baseDatos.String(200), nullable = False)
    precio = baseDatos.Column(baseDatos.Numeric(precision = 10, scale = 2), nullable = False)
    inventario = baseDatos.Column(baseDatos.Integer, nullable = False)
    tipo_id = baseDatos.Column(baseDatos.Integer, baseDatos.ForeignKey("tipos.id"), nullable = True)
    imagen = baseDatos.Column(baseDatos.String(200), nullable = False)
    
    def __init__(self, nombre, descripcion, precio, inventario, tipoId, imagen):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.inventario = inventario
        self.imagen = imagen
        self.tipo_id = tipoId