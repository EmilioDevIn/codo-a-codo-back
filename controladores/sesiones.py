from aplicacion import Flask, Blueprint, request, aplicacion

from esquemas.sesiones import jsonify

from servicios.sesion import ServicioSesion

sesiones = Blueprint("sesiones", __name__)

@sesiones.route("/iniciar", methods = ["POST"])
def iniciar():
    nuevaSesion = ServicioSesion.iniciar(request.get_json())
    
    return nuevaSesion.codigo_cliente

@sesiones.route("/leer", methods = ["GET"])
def leer():
    sesiones = ServicioSesion.leer()
    
    return jsonify(sesiones, many = True)

@sesiones.route("/obtener/<codigo>", methods = ["GET"])
def obtener(codigo):
    sesion = ServicioSesion.obtener_sesion(codigo)
    
    if not(sesion):
        return ({})
    
    return jsonify(sesion)

@sesiones.route("/cerrar/<codigo>", methods = ["GET"])
def cerrar(codigo):
    sesionCerrada = ServicioSesion.cerrar(codigo)
    
    return jsonify(sesionCerrada)

aplicacion.register_blueprint(sesiones, url_prefix="/sesiones")