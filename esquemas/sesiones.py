from aplicacion import marshmallow

class EsquemaSesion(marshmallow.Schema):
    
    class Meta:
        fields = ('id', 'usuario_id', 'codigo_cliente', 'activo', 'inicio_sesion', 'cierre_sesion')

def jsonify(datos, many = False):
    if many:
        return EsquemaSesion(many = True).dump(datos)
    return EsquemaSesion().jsonify(datos)