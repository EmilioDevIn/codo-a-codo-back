from modelos.usuario import ModeloUsuario
from aplicacion import baseDatos

class ServicioUsuario():

      
    @staticmethod
    def crear(datos):
        usuario = ModeloUsuario(
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
        usuarios = ModeloUsuario.query.all()
        
        return usuarios
    
    @staticmethod
    def modificar(id, datos):
        usuario = ModeloUsuario.query.get(id)
        
        usuario.nombre = datos["nombre"]
        usuario.clave = datos["clave"]
        usuario.esAdministrador = datos["esAdministrador"]
        usuario.imagen = datos["imagen"]
       
        baseDatos.session.commit()
        
        return usuario

    @staticmethod
    def eliminar(id):
        usuario = ModeloUsuario.query.get(id)
        
        baseDatos.session.delete(usuario)
        baseDatos.session.commit()
        
        return usuario