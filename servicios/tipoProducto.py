from aplicacion import baseDatos
from modelos.tipoProducto import ModeloTipoProducto

class ServicioTipoProducto():
    
    @staticmethod
    def obtener(id):
        tipo = ModeloTipoProducto.query.get(id)

        return tipo
    
    @staticmethod
    def crear(datos):
        tipoProducto = ModeloTipoProducto(
            datos["nombre"]
        )
        
        baseDatos.session.add(tipoProducto)
        baseDatos.session.commit()
        
    @staticmethod
    def leer(datos): 
        tipos = ModeloTipoProducto.query.get_all()
        
        return tipos

    @staticmethod    
    def modificar(id, datos):
        tipo = ModeloTipoProducto.query.get(id)
        
        tipo.nombre = datos["nombre"]
        
        baseDatos.session.commit()
        
    @staticmethod
    def eliminar(id):
        tipoEliminado = ModeloTipoProducto.query.get(id)
        
        baseDatos.session.delete(tipoEliminado)
        baseDatos.session.commit()
        
        return tipoEliminado