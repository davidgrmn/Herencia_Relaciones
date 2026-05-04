# Tienda Agrícola - Sistema de Facturación

---

## Descripción

Sistema de facturación para una tienda agrícola desarrollado en Python. Permite gestionar clientes, pedidos y productos especializados como controles de plagas, fertilizantes y antibioticos para animales de granja.

El proyecto se enfoca principalmente en la aplicacion de los conceptos de **herencia**, **composición** y **modularidad**.

---

## Estructura del Proyecto

```
tienda_agricola/
│
├── modelo/
│   ├── __init__.py
│   ├── producto_control.py
│   ├── control_plagas.py
│   ├── control_fertilizantes.py
│   ├── antibiotico.py
│   ├── pedido.py
│   └── cliente.py
│
├── test/
│   ├── __init__.py
│   └── test_tienda.py
```

## Diagrama de Clases

![Diagrama de Clases](evidencias/diagrama_clases.png)

---

## Diagrama de Componentes

![Diagrama de Componentes](evidencias/diagrama_componentes.png)

---

## Cómo correr las pruebas

Desde la carpeta raíz del proyecto ejecutar:

```bash
python -m unittest discover -s test -v
```

---

## Evidencias

### Pruebas Unitarias

![Pruebas unitarias](evidencias/tests_pasando.png)

---

### Debug — Composición (Cliente → Pedido → Productos)

![Debug composición](evidencias/debug_composicion.png)

---

### Debug — Herencia ControlPlagas

![Debug herencia ControlPlagas](evidencias/debug_control_plagas.png)

---

### Debug — Herencia ControlFertilizantes

![Debug herencia ControlFertilizantes](evidencias/debug_control_fertilizantes.png)

