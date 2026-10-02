from datetime import datetime


class Venta:
    def __init__(
        self,
        usuario_identificacion: str,
        producto_codigo: str,
        fecha: str = None
    ):
        self.usuario_identificacion = usuario_identificacion
        self.producto_codigo = producto_codigo
        self.fecha = fecha if fecha else self.obtener_fecha_actual()

    @staticmethod
    def obtener_fecha_actual():
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def a_diccionario(self):
        return {
            "usuario_identificacion": self.usuario_identificacion,
            "producto_codigo": self.producto_codigo,
            "fecha": self.fecha
        }