from modelo.control_plagas import ControlPlagas
from modelo.control_fertilizantes import ControlFertilizantes
from modelo.antibiotico import Antibiotico
from modelo.pedido import Pedido
from modelo.cliente import Cliente


plagas = ControlPlagas("ICA-001", "Roundup", 15, 35000, 10)
fertilizante = ControlFertilizantes("ICA-002", "Nitrogeno Plus", 30, 42000, "2025-03-01")
antibiotico = Antibiotico("Pen-G", 500, "porcino", 12000)


pedido1 = Pedido("2025-04-18")
pedido1.agregar_producto(plagas)
pedido1.agregar_producto(fertilizante)
pedido1.agregar_producto(antibiotico)


cliente = Cliente("Juan Pérez", "1234567")
cliente.agregar_pedido(pedido1)


print("fin")

