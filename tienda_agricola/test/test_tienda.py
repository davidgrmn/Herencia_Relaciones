import unittest
from modelo.control_plagas import ControlPlagas
from modelo.control_fertilizantes import ControlFertilizantes
from modelo.antibiotico import Antibiotico
from modelo.pedido import Pedido
from modelo.cliente import Cliente

class TestTiendaAgricola(unittest.TestCase):

    def test_control_plagas_hereda_producto_control(self):
        p = ControlPlagas("ICA-001", "Roundup", 15, 35000, 10)
        self.assertEqual(p.nombre, "Roundup")
        self.assertEqual(p.periodo_carencia, 10)

    def test_control_fertilizantes_hereda_producto_control(self):
        f = ControlFertilizantes("ICA-002", "Nitrogeno Plus", 30, 42000, "2025-03-01")
        self.assertEqual(f.fecha_ultima_aplicacion, "2025-03-01")

    def test_antibiotico_dosis_invalida(self):
        with self.assertRaises(ValueError):
            Antibiotico("Penicilina", 300, "bovino", 15000)  # dosis < 400

    def test_antibiotico_animal_invalido(self):
        with self.assertRaises(ValueError):
            Antibiotico("Penicilina", 500, "canino", 15000)  # animal no válido

    def test_pedido_calcula_total(self):
        pedido = Pedido("2025-04-18")
        pedido.agregar_producto(ControlPlagas("ICA-001", "Roundup", 15, 35000, 10))
        pedido.agregar_producto(Antibiotico("Pen-G", 500, "porcino", 12000))
        self.assertEqual(pedido.valor_total, 47000)

    def test_cliente_tiene_multiples_pedidos(self):
        cliente = Cliente("Juan Pérez", "1234567")
        cliente.agregar_pedido(Pedido("2025-04-01"))
        cliente.agregar_pedido(Pedido("2025-04-18"))
        self.assertEqual(len(cliente.pedidos), 2)

if __name__ == '__main__':
    unittest.main()