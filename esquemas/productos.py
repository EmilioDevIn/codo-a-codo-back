from aplicacion import marshmallow

class EsquemaProducto(marshmallow.Schema):
    
    class Meta:
        fields = ('id', 'nombre', 'descripcion', 'precio', 'inventario', 'imagen')
        
def jsonify(datos, many = False):
    if many:
        return EsquemaProducto(many = True).dump(datos)
    return EsquemaProducto().jsonify(datos)