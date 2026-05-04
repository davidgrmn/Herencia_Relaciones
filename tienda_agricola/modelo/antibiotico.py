class Antibiotico:
    ANIMALES_VALIDOS = ["bovino", "caprino", "porcino"]

    def __init__(self, nombre, dosis, tipo_animal, precio):
        if not (400 <= dosis <= 600):
            raise ValueError("La dosis debe estar entre 400 y 600 kg")
        if tipo_animal.lower() not in self.ANIMALES_VALIDOS:
            raise ValueError(f"Tipo de animal inválido. Opciones: {self.ANIMALES_VALIDOS}")
        self.nombre = nombre
        self.dosis = dosis
        self.tipo_animal = tipo_animal
        self.precio = precio

    def __str__(self):
        return f"{self.nombre} | Dosis: {self.dosis}kg | Animal: {self.tipo_animal} | Precio: ${self.precio}"