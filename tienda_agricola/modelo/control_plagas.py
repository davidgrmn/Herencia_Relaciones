from modelo.producto_control import ProductoControl

class ControlPlagas(ProductoControl):
    def __init__(self, registro_ica, nombre, frecuencia_aplicacion, valor, periodo_carencia):
        super().__init__(registro_ica, nombre, frecuencia_aplicacion, valor)
        self.periodo_carencia = periodo_carencia  # días

    def __str__(self):
        return super().__str__() + f" | Carencia: {self.periodo_carencia} días"