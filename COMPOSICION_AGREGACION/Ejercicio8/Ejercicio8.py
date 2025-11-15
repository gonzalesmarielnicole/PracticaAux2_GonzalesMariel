class Facultad:
    def __init__(self, nombre, sigla):
        self.nombre = nombre
        self.sigla = sigla


class Fraternidad:
    def __init__(self, nombre, encargado):
        self.nombre = nombre
        self.encargado = encargado
        self.bailarines = []

    def agregar_bailarin(self, persona):
        if persona.fraternidad is not None:
            print(f"ERROR: {persona.nombre} ya pertenece a {persona.fraternidad.nombre}")
            return
        persona.fraternidad = self
        self.bailarines.append(persona)


class Persona:
    def __init__(self, nombre, edad, facultad):
        self.nombre = nombre
        self.edad = edad
        self.facultad = facultad
        self.fraternidad = None


fcyt = Facultad("Ciencias y Tecnología", "FCyT")
fabe = Facultad("Arquitectura", "FABE")

enc1 = Persona("Carlos Encargado", 40, fcyt)
enc2 = Persona("María Encargada", 35, fabe)

frat_macheteros = Fraternidad("Macheteros", enc1)
frat_tinkus = Fraternidad("Tinkus", enc2)

p1 = Persona("Juan", 20, fcyt)
p2 = Persona("Lucía", 19, fabe)
p3 = Persona("Mario", 21, fcyt)
p4 = Persona("Ana", 22, fabe)
p5 = Persona("Pedro", 18, fcyt)

frat_macheteros.agregar_bailarin(p1)
frat_macheteros.agregar_bailarin(p3)
frat_tinkus.agregar_bailarin(p2)
frat_tinkus.agregar_bailarin(p4)

frat_tinkus.agregar_bailarin(p1)

def mostrar_bailarines():
    print("\n LISTA DE BAILARINES")
    for p in [p1, p2, p3, p4, p5]:
        fraternidad = p.fraternidad.nombre if p.fraternidad else "Ninguna"
        print(f"{p.nombre}, {p.edad} años - {p.facultad.sigla} - Fraternidad: {fraternidad}")

def mostrar_fraternidades():
    print("\nFRATERNIDADES Y ENCARGADOS")
    for frat in [frat_macheteros, frat_tinkus]:
        print(f"\n{frat.nombre} - Encargado: {frat.encargado.nombre}")
        print("Bailarines:")
        for b in frat.bailarines:
            print(f" - {b.nombre} ({b.edad} años)")

mostrar_bailarines()
mostrar_fraternidades()
