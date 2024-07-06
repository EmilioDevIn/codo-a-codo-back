from modelos.usuarios import Usuarios
from aplicacion import baseDatos

class ServicioUsuario():
      
    @staticmethod
    def crear(datos):
        usuario = Usuarios(
            datos["nombre"],
            datos["clave"],
            datos["esAdministrador"],
            datos["imagen"]
        )
        
        baseDatos.session.add(usuario)
        baseDatos.session.commit()
        
        return usuario
    
    @staticmethod
    def leer():
        usuarios = Usuarios.query.all()
        
        return usuarios
    
    @staticmethod
    def modificar(id, datos):
        usuario = Usuarios.query.get(id)
        
        usuario.nombre = datos["nombre"]
        usuario.clave = datos["clave"]
        usuario.esAdministrador = datos["esAdministrador"]
        usuario.imagen = datos["imagen"]
       
        baseDatos.session.commit()
        
        return usuario

    @staticmethod
    def eliminar(id):
        usuario = Usuarios.query.get(id)
        
        baseDatos.session.delete(usuario)
        baseDatos.session.commit()
        
        return usuario