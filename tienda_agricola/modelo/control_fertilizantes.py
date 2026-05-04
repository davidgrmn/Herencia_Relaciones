from modelo.producto_control import ProductoControl

class ControlFertilizantes(ProductoControl):
    def __init__(self, registro_ica, nombre, frecuencia_aplicacion, valor, fecha_ultima_aplicacion):
        super().__init__(registro_ica, nombre, frecuencia_aplicacion, valor)
        self.fecha_ultima_aplicacion = fecha_ultima_aplicacion

    def __str__(self):
        return super().__str__() + f" | Última aplicación: {self.fecha_ultima_aplicacion}"