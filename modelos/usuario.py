from aplicacion import baseDatos, aplicacion
 
class ModeloUsuario(baseDatos.Model):
    __tablename__ = "usuarios"
    id = baseDatos.Column(baseDatos.Integer, primary_key = True)
    nombre = baseDatos.Column(baseDatos.String(100), nullable = False)
    clave = baseDatos.Column(baseDatos.String(100), nullable = False)
    esAdministrador = baseDatos.Column(baseDatos.Boolean, nullable = False)
    imagen = baseDatos.Column(baseDatos.String(200), nullable = False)
    
    def __init__(self, nombre, clave, esAdministrador, imagen):
        self.nombre = nombre
        self.clave = clave
        self.esAdministrador = esAdministrador
        self.imagen = imagen
        
with aplicacion.app_context():
    baseDatos.create_all()