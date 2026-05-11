from modelo.cliente import Cliente
from modelo.pedido import Pedido
from modelo.control_plagas import ControlPlagas
from modelo.control_fertilizantes import ControlFertilizantes
from modelo.antibiotico import Antibiotico

class Crud:
    def __init__(self):
        self.clientes = []  

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    def buscar_por_cedula(self, cedula):
        for cliente in self.clientes:
            if cliente.cedula == cedula:
                return cliente
        return None  # si no lo encuentra retorna None

    def listar_clientes(self):
        return self.clientes