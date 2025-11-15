class ProductoNoEncontradoException(Exception):
    pass

class StockInsuficienteException(Exception):
    pass

class ProductoInvalidoException(Exception):
    pass


class Producto:
    def __init__(self, codigo, nombre, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def reducir_stock(self, cantidad):
        self.stock -= cantidad


class Inventario:
    def __init__(self, size):
        self.productos = [None] * size
        self.count = 0

    def agregar_producto(self, p):
        if p.precio < 0 or p.stock < 0:
            raise ProductoInvalidoException("Precio o stock negativo")

        for i in range(self.count):
            if self.productos[i].codigo == p.codigo:
                raise ProductoInvalidoException("Código duplicado")

        if self.count >= len(self.productos):
            raise ProductoInvalidoException("Inventario lleno")

        self.productos[self.count] = p
        self.count += 1

    def buscar_producto(self, codigo):
        for i in range(self.count):
            if self.productos[i].codigo == codigo:
                return self.productos[i]
        raise ProductoNoEncontradoException("Producto no encontrado")

    def vender_producto(self, codigo, cantidad):
        producto = self.buscar_producto(codigo)

        if producto.stock < cantidad:
            raise StockInsuficienteException("Stock insuficiente")

        producto.reducir_stock(cantidad)


def main():
    inv = Inventario(10)

    try:
        inv.agregar_producto(Producto("A1", "Laptop", 5000, 5))
        inv.agregar_producto(Producto("B2", "Mouse", 50, 20))
        inv.agregar_producto(Producto("A1", "Teclado", 80, 10))
    except Exception as e:
        print("Error:", e)

    try:
        p = inv.buscar_producto("B2")
        print("Encontrado:", p.nombre)
    except Exception as e:
        print("Error:", e)

    try:
        inv.vender_producto("A1", 3)
        print("Venta realizada. Stock restante:", inv.buscar_producto("A1").stock)

        inv.vender_producto("A1", 10)
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
