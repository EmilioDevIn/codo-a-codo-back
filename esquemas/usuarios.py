from aplicacion import marshmallow

class EsquemaUsuario(marshmallow.Schema):
    
    class Meta:
        fields = ('id', 'nombre', 'clave', 'esAdministrador', 'imagen')

def jsonify(datos, many = False):
    if many:
        return EsquemaUsuario(many = True).dump(datos)
    return EsquemaUsuario().jsonify(datos) 