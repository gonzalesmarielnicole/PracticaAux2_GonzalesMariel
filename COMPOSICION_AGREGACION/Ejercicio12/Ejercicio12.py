class Doctor:
    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad


class Hospital:
    def __init__(self, nombre):
        self.nombre = nombre
        self.doctores = []

    def agregar_doctor(self, doctor):
        self.doctores.append(doctor)

    def mostrar_doctores(self):
        print(f"Hospital: {self.nombre}")
        for d in self.doctores:
            print(f"- {d.nombre} ({d.especialidad})")


d1 = Doctor("Carlos Ruiz", "Cardiología")
d2 = Doctor("María López", "Pediatría")
d3 = Doctor("Juan Rojas", "Neurología")

h1 = Hospital("Hospital Central")
h2 = Hospital("Hospital Viedma")

h1.agregar_doctor(d1)
h1.agregar_doctor(d2)
h2.agregar_doctor(d2)
h2.agregar_doctor(d3)

h1.mostrar_doctores()
h2.mostrar_doctores()
