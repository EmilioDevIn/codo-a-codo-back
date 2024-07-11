from datetime import datetime

from modelos.sesion import ModeloSesion
from modelos.usuario import ModeloUsuario

from aplicacion import baseDatos

class ServicioSesion():
    
    @staticmethod
    def cerrar(codigo):
        sesion = ModeloSesion.query.filter_by(codigo_cliente = codigo).first()
        
        sesion.activo = False
        
        baseDatos.session.commit()
        return sesion
    
    @staticmethod
    def generar_codigo(sesion):
        usuario = ModeloUsuario.query.get(sesion.usuario_id)
        codigo = f"{sesion.id}|{usuario.id}"
        
        sesion.codigo_cliente = codigo
        
        baseDatos.session.commit()
        
        return codigo
    
    @staticmethod
    def obtener_sesion(codigo):
        sesion = ModeloSesion.query.filter_by(codigo_cliente = codigo).first()

        return sesion            
    
    @staticmethod
    def iniciar(usuario):

        usuarioReal = ModeloUsuario.query.filter_by(nombre=usuario["nombre"]).first()
        
        if usuarioReal.clave != usuario["clave"]:
            return
        
        nuevaSesion = ModeloSesion(usuarioReal.id)
        nuevaSesion.codigo_cliente = "generating"

        baseDatos.session.add(nuevaSesion)
        baseDatos.session.commit()
        
        nuevaSesion.codigo_cliente = ServicioSesion.generar_codigo(nuevaSesion)
        
        baseDatos.session.commit()

        return nuevaSesion
    
    @staticmethod
    def leer():
        sesiones = ModeloSesion.query.all()
                
        return sesiones
    
    @staticmethod
    def eliminar(id):
        sesionEliminada = ModeloSesion.query.get(id)
        
        baseDatos.session.delete(sesionEliminada)
        baseDatos.session.commit()
        
        return sesionEliminada        
        
'''
    - en cada pagina se revisa el SesionStorage, se comprueba si hay un usuario.
    - si:
        - en la barra de navegacion figuran los datos del usuario
        es cliente:
            - puede reducir el "inventario" de un producto
        es administardor:
            - pestaña de administración
            - la página para el administrador comprueba si el usuario es administrador, si no lo es redirige al inicio
        

    Comprobar sesion de usuario
        - codigo "1|1" 

    FRONT
        - sesion de usuario
        - codigo
    
        - SesionStorage -> guarda un codigo
        
    BACK
        - registro de sesiones
        - registro de usuarios
'''
'''
    ESTADO
        - SesionUsuario
            - codigoSesion
        - PeticionPendiente
            - 
'''