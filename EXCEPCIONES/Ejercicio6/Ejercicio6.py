class FondosInsuficientesException(Exception):
    pass


class CuentaBancaria:
    def __init__(self, numeroCuenta, titular, saldo):
        self.numeroCuenta = numeroCuenta
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto):
        if monto <= 0:
            raise ValueError("El monto debe ser positivo")
        self.saldo += monto

    def retirar(self, monto):
        if monto > self.saldo:
            raise FondosInsuficientesException("Fondos insuficientes")
        self.saldo -= monto

    def mostrarInfo(self):
        print("Cuenta:", self.numeroCuenta)
        print("Titular:", self.titular)
        print("Saldo:", self.saldo)


def main():
    cuenta = CuentaBancaria("12345", "Juan Pérez", 1000)

    cuenta.mostrarInfo()
    print()

    try:
        cuenta.depositar(500)
        print("Depósito exitoso. Nuevo saldo:", cuenta.saldo)
    except Exception as e:
        print("Error:", e)

    try:
        cuenta.depositar(-200)
    except Exception as e:
        print("Error:", e)

    print()

    try:
        cuenta.retirar(300)
        print("Retiro exitoso. Nuevo saldo:", cuenta.saldo)
    except Exception as e:
        print("Error:", e)

    try:
        cuenta.retirar(5000)
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
