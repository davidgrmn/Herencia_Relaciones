from crud.crud import Crud
from modelo.cliente import Cliente
from modelo.pedido import Pedido
from modelo.control_plagas import ControlPlagas
from modelo.control_fertilizantes import ControlFertilizantes
from modelo.antibiotico import Antibiotico

crud = Crud()

def menu_principal():
    while True:
        print("\n===== TIENDA AGRÍCOLA =====")
        print("1. Registrar cliente")
        print("2. Agregar pedido a cliente")
        print("3. Buscar cliente por cédula")
        print("4. Listar todos los clientes")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_cliente()
        elif opcion == "2":
            agregar_pedido()
        elif opcion == "3":
            buscar_cliente()
        elif opcion == "4":
            listar_clientes()
        elif opcion == "5":
            print("Hasta luego.")
            break
        else:
            print("Opción inválida, intente de nuevo.")

def registrar_cliente():
    print("\n--- Registrar Cliente ---")
    nombre = input("Nombre: ")
    cedula = input("Cédula: ")
    cliente = Cliente(nombre, cedula)
    crud.agregar_cliente(cliente)
    print(f"Cliente '{nombre}' registrado exitosamente.")

def agregar_pedido():
    print("\n--- Agregar Pedido ---")
    cedula = input("Cédula del cliente: ")
    cliente = crud.buscar_por_cedula(cedula)

    if cliente is None:
        print("Cliente no encontrado.")
        return

    fecha = input("Fecha del pedido (ej: 2025-04-18): ")
    pedido = Pedido(fecha)

    while True:
        print("\n¿Qué producto desea agregar?")
        print("1. Control de Plagas")
        print("2. Control de Fertilizantes")
        print("3. Antibiótico")
        print("4. Finalizar pedido")
        opcion = input("Opción: ")

        if opcion == "1":
            pedido.agregar_producto(crear_control_plagas())
        elif opcion == "2":
            pedido.agregar_producto(crear_control_fertilizantes())
        elif opcion == "3":
            pedido.agregar_producto(crear_antibiotico())
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")

    cliente.agregar_pedido(pedido)
    print(f"Pedido agregado. Total: ${pedido.valor_total}")

def crear_control_plagas():
    print("\n-- Control de Plagas --")
    registro_ica = input("Registro ICA: ")
    nombre = input("Nombre: ")
    frecuencia = int(input("Frecuencia de aplicación (días): "))
    valor = float(input("Valor: "))
    carencia = int(input("Periodo de carencia (días): "))
    return ControlPlagas(registro_ica, nombre, frecuencia, valor, carencia)

def crear_control_fertilizantes():
    print("\n-- Control de Fertilizantes --")
    registro_ica = input("Registro ICA: ")
    nombre = input("Nombre: ")
    frecuencia = int(input("Frecuencia de aplicación (días): "))
    valor = float(input("Valor: "))
    fecha = input("Fecha última aplicación (ej: 2025-03-01): ")
    return ControlFertilizantes(registro_ica, nombre, frecuencia, valor, fecha)

def crear_antibiotico():
    print("\n-- Antibiótico --")
    nombre = input("Nombre: ")
    dosis = int(input("Dosis (400-600 kg): "))
    tipo_animal = input("Tipo de animal (bovino/caprino/porcino): ")
    precio = float(input("Precio: "))
    return Antibiotico(nombre, dosis, tipo_animal, precio)

def buscar_cliente():
    print("\n--- Buscar Cliente por Cédula ---")
    cedula = input("Cédula: ")
    cliente = crud.buscar_por_cedula(cedula)

    if cliente is None:
        print("Cliente no encontrado.")
        return

    print(f"\nCliente: {cliente.nombre} | Cédula: {cliente.cedula}")
    print(f"Total de pedidos: {len(cliente.pedidos)}")

    for i, pedido in enumerate(cliente.pedidos):
        print(f"\n  Pedido {i+1} - Fecha: {pedido.fecha} | Total: ${pedido.valor_total}")
        for producto in pedido.productos:
            print(f"    - {producto}")

def listar_clientes():
    print("\n--- Clientes Registrados ---")
    clientes = crud.listar_clientes()
    if not clientes:
        print("No hay clientes registrados.")
        return
    for cliente in clientes:
        print(f"- {cliente.nombre} | Cédula: {cliente.cedula} | Pedidos: {len(cliente.pedidos)}")