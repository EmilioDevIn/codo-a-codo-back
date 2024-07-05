from aplicacion import baseDatos
 
class Usuarios(baseDatos.Model):
    id = baseDatos.Column(baseDatos.Integer, primary_key = True)
    nombre = baseDatos.Column(baseDatos.String(100), nullable = False)
    clave = baseDatos.Column(baseDatos.String(100), nullable = False)
    esAdminstrador = baseDatos.Column(baseDatos.Boolean, nullable = False)
    imagen = baseDatos.Column(baseDatos.String(200), nullable = False)
    
    def __init__(self, id, nombre, clave, esAdministrador, imagen):
        self.id = id
        self.nombre = nombre
        self.clave = clave
        self.esAdministardor = esAdministrador
        self.imagen = imagen