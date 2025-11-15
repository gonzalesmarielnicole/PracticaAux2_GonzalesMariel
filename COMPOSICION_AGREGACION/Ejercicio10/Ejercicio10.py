class Persona:
    def __init__(self, nombre, apellido, edad, ci):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.ci = ci


class Participante(Persona):
    def __init__(self, nombre, apellido, edad, ci, nroTicket):
        super().__init__(nombre, apellido, edad, ci)
        self.nroTicket = nroTicket


class Speaker(Persona):
    def __init__(self, nombre, apellido, edad, ci, especialidad):
        super().__init__(nombre, apellido, edad, ci)
        self.especialidad = especialidad


class Charla:
    def __init__(self, lugar, nombreCharla, speaker):
        self.lugar = lugar
        self.nombreCharla = nombreCharla
        self.speaker = speaker
        self.participantes = []

    def agregar_participante(self, p):
        self.participantes.append(p)

    def num_participantes(self):
        return len(self.participantes)


class Evento:
    def __init__(self, nombre):
        self.nombre = nombre
        self.charlas = []

    def agregar_charla(self, charla):
        self.charlas.append(charla)

    def edad_promedio(self):
        edades = []
        for charla in self.charlas:
            for p in charla.participantes:
                edades.append(p.edad)
        return sum(edades)/len(edades) if edades else 0

    def buscar_persona(self, nombre, apellido):
        for charla in self.charlas:
            if charla.speaker.nombre == nombre and charla.speaker.apellido == apellido:
                return True
            for p in charla.participantes:
                if p.nombre == nombre and p.apellido == apellido:
                    return True
        return False

    def eliminar_charlas_por_speaker(self, ci):
        self.charlas = [c for c in self.charlas if c.speaker.ci != ci]

    def ordenar_charlas_por_participantes(self):
        self.charlas.sort(key=lambda c: c.num_participantes())


sp1 = Speaker("Carlos", "Lopez", 45, 1001, "IA")
sp2 = Speaker("María", "Perez", 38, 2002, "Robótica")

p1 = Participante("Ana", "Suarez", 22, 3001, 10)
p2 = Participante("Luis", "Flores", 25, 3002, 11)
p3 = Participante("Marta", "Rios", 30, 3003, 12)
p4 = Participante("Juan", "Vega", 20, 3004, 13)

c1 = Charla("Auditorio A", "Introducción a IA", sp1)
c2 = Charla("Auditorio B", "Robótica Moderna", sp2)
c3 = Charla("Auditorio C", "Machine Learning", sp1)

c1.agregar_participante(p1)
c1.agregar_participante(p2)
c2.agregar_participante(p3)
c3.agregar_participante(p4)

evento = Evento("Tech Conference")
evento.agregar_charla(c1)
evento.agregar_charla(c2)
evento.agregar_charla(c3)

print("Edad promedio:", evento.edad_promedio())
print("¿Existe Ana Suarez?:", evento.buscar_persona("Ana", "Suarez"))

evento.eliminar_charlas_por_speaker(1001)
print("Charlas luego de eliminar speaker 1001:")
for x in evento.charlas:
    print(x.nombreCharla)

evento.ordenar_charlas_por_participantes()
print("Charlas ordenadas por número de participantes:")
for x in evento.charlas:
    print(x.nombreCharla, x.num_participantes())
