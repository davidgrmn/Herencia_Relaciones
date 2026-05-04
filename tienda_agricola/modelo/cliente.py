class Cliente:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula
        self.pedidos = []        # composición: un cliente tiene muchos pedidos

    def agregar_pedido(self, pedido):
        self.pedidos.append(pedido)

    def __str__(self):
        return f"Cliente: {self.nombre} | CC: {self.cedula} | Pedidos: {len(self.pedidos)}"