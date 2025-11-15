class NumeroInvalidoException(Exception):
    pass


class Calculadora:
    @staticmethod
    def sumar(a, b):
        return a + b

    @staticmethod
    def restar(a, b):
        return a - b

    @staticmethod
    def multiplicar(a, b):
        return a * b

    @staticmethod
    def dividir(a, b):
        if b == 0:
            raise ArithmeticError("División entre cero")
        return a / b

    @staticmethod
    def convertir_entero(cadena):
        if not cadena.lstrip("-").isdigit():
            raise NumeroInvalidoException("Valor no numérico")
        return int(cadena)


def main():
    print(Calculadora.sumar(5, 3))
    print(Calculadora.restar(10, 4))
    print(Calculadora.multiplicar(6, 7))

    try:
        print(Calculadora.dividir(10, 0))
    except Exception as e:
        print("Error:", e)

    try:
        print(Calculadora.convertir_entero("123"))
        print(Calculadora.convertir_entero("abc"))
    except Exception as e:
        print("Error:", e)


main()
