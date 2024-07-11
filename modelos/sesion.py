from datetime import datetime
from aplicacion import baseDatos, aplicacion 

class ModeloSesion(baseDatos.Model):
    __tablename__ = "sesiones"
    id = baseDatos.Column(baseDatos.Integer, primary_key = True)
    usuario_id = baseDatos.Column(baseDatos.Integer, baseDatos.ForeignKey("usuarios.id"), nullable = False)
    codigo_cliente = baseDatos.Column(baseDatos.String(100), nullable = False)
    activo = baseDatos.Column(baseDatos.Boolean, default = True, nullable = False)
    inicio_sesion = baseDatos.Column(baseDatos.DateTime, default = datetime.utcnow, nullable = False)
    cierre_sesion = baseDatos.Column(baseDatos.DateTime)
    
    def __init__(self, usuarioId):
        self.usuario_id = usuarioId
        
with aplicacion.app_context():
    baseDatos.create_all()