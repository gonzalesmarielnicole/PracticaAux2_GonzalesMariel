class Ropa {
    private String tipo;
    private String material;

    public Ropa(String tipo, String material) {
        this.tipo = tipo;
        this.material = material;
    }

    public String getTipo() {
        return tipo;
    }

    public String getMaterial() {
        return material;
    }

    @Override
    public String toString() {
        return tipo + " - " + material;
    }
}

class Ropero {
    private String material;
    private Ropa[] ropas;
    private int nroRopas;

    public Ropero(String material) {
        this.material = material;
        this.ropas = new Ropa[20];
        this.nroRopas = 0;
    }

    public void adicionar(Ropa ropa) {
        if (nroRopas < 20) {
            ropas[nroRopas] = ropa;
            nroRopas++;
        }
    }

    public void adicionarN(Ropa[] lista) {
        for (Ropa r : lista) {
            if (r != null && nroRopas < 20) {
                ropas[nroRopas] = r;
                nroRopas++;
            }
        }
    }

    public void eliminarPorMaterial(String mat) {
        int j = 0;
        for (int i = 0; i < nroRopas; i++) {
            if (!ropas[i].getMaterial().equals(mat)) {
                ropas[j] = ropas[i];
                j++;
            }
        }
        nroRopas = j;
    }

    public void eliminarPorTipo(String tipo) {
        int j = 0;
        for (int i = 0; i < nroRopas; i++) {
            if (!ropas[i].getTipo().equals(tipo)) {
                ropas[j] = ropas[i];
                j++;
            }
        }
        nroRopas = j;
    }

    public void mostrarPorMaterial(String mat) {
        for (int i = 0; i < nroRopas; i++) {
            if (ropas[i].getMaterial().equals(mat)) {
                System.out.println(ropas[i]);
            }
        }
    }

    public void mostrarPorTipo(String tipo) {
        for (int i = 0; i < nroRopas; i++) {
            if (ropas[i].getTipo().equals(tipo)) {
                System.out.println(ropas[i]);
            }
        }
    }

    public void mostrarTodo() {
        for (int i = 0; i < nroRopas; i++) {
            System.out.println(ropas[i]);
        }
    }
}

public class Main {
    public static void main(String[] args) {

        Ropero rop = new Ropero("Madera");

        Ropa[] lista = {
                new Ropa("Camisa", "Algodón"),
                new Ropa("Pantalón", "Jean"),
                new Ropa("Chaqueta", "Cuero"),
                new Ropa("Falda", "Algodón"),
                new Ropa("Suéter", "Lana")
        };

        rop.adicionarN(lista);

        System.out.println("Prendas de Algodón:");
        rop.mostrarPorMaterial("Algodón");

        rop.eliminarPorTipo("Pantalón");

        System.out.println("\nPrendas de tipo Camisa:");
        rop.mostrarPorTipo("Camisa");

        System.out.println("\nContenido total del ropero:");
        rop.mostrarTodo();
    }
}
