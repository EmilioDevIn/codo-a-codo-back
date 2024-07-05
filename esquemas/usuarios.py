from aplicacion import marshmallow

class EsquemaUsuario(marshmallow.Schema):
    
    class Meta:
        fields = ('id', 'nombre', 'clave', 'esAdministrador', 'imagen')

    @staticmethod
    def jsonsify(datos):
        return EsquemaUsuario().jsonsify(datos)      
    
    @staticmethod
    def jsonsifyArray(datos):
        return EsquemaUsuario(many = True).dump(datos)
        