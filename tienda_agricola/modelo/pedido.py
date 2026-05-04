class Pedido:
    def __init__(self, fecha):
        self.fecha = fecha
        self.productos = []      
        self.valor_total = 0.0

    def agregar_producto(self, producto):
        self.productos.append(producto)
        
        if hasattr(producto, 'valor'):
            self.valor_total += producto.valor
        elif hasattr(producto, 'precio'):
            self.valor_total += producto.precio

    def __str__(self):
        return f"Pedido del {self.fecha} | Total: ${self.valor_total} | Productos: {len(self.productos)}"
