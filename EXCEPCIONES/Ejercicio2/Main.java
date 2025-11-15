package EXCEPCIONES.Ejercicio2;

class NumeroInvalidoException extends Exception {
    public NumeroInvalidoException(String mensaje) {
        super(mensaje);
    }
}

class Calculadora {

    public static int sumar(int a, int b) {
        return a + b;
    }

    public static int restar(int a, int b) {
        return a - b;
    }

    public static int multiplicar(int a, int b) {
        return a * b;
    }

    public static double dividir(int a, int b) {
        if (b == 0)
            throw new ArithmeticException("División entre cero");
        return (double) a / b;
    }

    public static int convertirEntero(String s) throws NumeroInvalidoException {
        try {
            return Integer.parseInt(s);
        } catch (NumberFormatException e) {
            throw new NumeroInvalidoException("Valor no numérico");
        }
    }
}

public class Main {
    public static void main(String[] args) {

        System.out.println(Calculadora.sumar(5, 3));
        System.out.println(Calculadora.restar(10, 4));
        System.out.println(Calculadora.multiplicar(6, 7));

        try {
            System.out.println(Calculadora.dividir(10, 0));
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }

        try {
            System.out.println(Calculadora.convertirEntero("123"));
            System.out.println(Calculadora.convertirEntero("abc"));
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}
