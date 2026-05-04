class ProductoControl:
    def __init__(self, registro_ica, nombre, frecuencia_aplicacion, valor):
        self.registro_ica = registro_ica
        self.nombre = nombre
        self.frecuencia_aplicacion = frecuencia_aplicacion  # días
        self.valor = valor

    def __str__(self):
        return f"[{self.registro_ica}] {self.nombre} - Frecuencia: {self.frecuencia_aplicacion} días - Valor: ${self.valor}"