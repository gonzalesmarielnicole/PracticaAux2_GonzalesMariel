class ProductoFarmaceutico:
    def __init__(self, nombre, laboratorio):
        self.nombre = nombre
        self.laboratorio = laboratorio


class Medicamento(ProductoFarmaceutico):
    def __init__(self, nombre, laboratorio, dosis, via_administracion):
        super().__init__(nombre, laboratorio)
        self.dosis = dosis
        self.via_administracion = via_administracion


class CosmeticoFarmaceutico(ProductoFarmaceutico):
    def __init__(self, nombre, laboratorio, tipo_piel, fragancia):
        super().__init__(nombre, laboratorio)
        self.tipo_piel = tipo_piel
        self.fragancia = fragancia


class Cliente:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo


class Registro:
    def __init__(self, cantidad, precio_unitario, medicamento):
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.medicamento = medicamento


class Venta:
    def __init__(self, fecha, cliente):
        self.fecha = fecha
        self.cliente = cliente
        self.registros = []   
        self.total = 0

