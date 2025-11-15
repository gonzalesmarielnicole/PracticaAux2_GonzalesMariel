class Ropa:
    def __init__(self, tipo, material):
        self.tipo = tipo
        self.material = material

    def __str__(self):
        return f"{self.tipo} - {self.material}"


class Ropero:
    def __init__(self, material):
        self.material = material
        self.ropas = []
        self.nroRopas = 0

    def adicionar(self, ropa):
        if self.nroRopas < 20:
            self.ropas.append(ropa)
            self.nroRopas += 1

    def adicionar_n(self, lista_ropas):
        for r in lista_ropas:
            if self.nroRopas < 20:
                self.ropas.append(r)
                self.nroRopas += 1

    def eliminar_por_material(self, material):
        self.ropas = [r for r in self.ropas if r.material != material]
        self.nroRopas = len(self.ropas)

    def eliminar_por_tipo(self, tipo):
        self.ropas = [r for r in self.ropas if r.tipo != tipo]
        self.nroRopas = len(self.ropas)

    def mostrar_por_material(self, material):
        for r in self.ropas:
            if r.material == material:
                print(r)

    def mostrar_por_tipo(self, tipo):
        for r in self.ropas:
            if r.tipo == tipo:
                print(r)


rop = Ropero("Madera")

lista = [
    Ropa("Camisa", "Algodón"),
    Ropa("Pantalón", "Jean"),
    Ropa("Chaqueta", "Cuero"),
    Ropa("Falda", "Algodón"),
    Ropa("Suéter", "Lana")
]

rop.adicionar_n(lista)

print("Prendas de material Algodón:")
rop.mostrar_por_material("Algodón")

rop.eliminar_por_tipo("Pantalón")

print("\nPrendas de tipo Camisa:")
rop.mostrar_por_tipo("Camisa")
