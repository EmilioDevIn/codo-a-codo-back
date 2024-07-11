from aplicacion import baseDatos

class ModeloTipoProducto(baseDatos.Model):
    __tablename__ = "tipos"
    id = baseDatos.Column(baseDatos.Integer, primary_key = True)
    nombre = baseDatos.Column(baseDatos.String(100), nullable = False)
    
    def __init__(self, nombre):
        self.nombre = nombre
    
    