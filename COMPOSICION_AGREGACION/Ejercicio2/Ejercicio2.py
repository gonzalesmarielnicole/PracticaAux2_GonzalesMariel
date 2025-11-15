class Empleado:
    def __init__(self, nombre, cargo, sueldo):
        self.nombre = nombre
        self.cargo = cargo
        self.sueldo = sueldo

    def __str__(self):
        return f"{self.nombre} - {self.cargo} - ${self.sueldo}"


class Departamento:
    def __init__(self, nombre, area):
        self.nombre = nombre
        self.area = area
        self.empleados = []

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def mostrar_empleados(self):
        print(f"Departamento: {self.nombre}")
        if not self.empleados:
            print("  No hay empleados.")
        else:
            for e in self.empleados:
                print(" ", e)
        print()

    def cambio_salario(self, porcentaje):
        for e in self.empleados:
            e.sueldo = e.sueldo + e.sueldo * porcentaje / 100

    def tiene_empleado(self, empleado):
        return empleado in self.empleados

    def mover_empleados_a(self, destino):
        for e in self.empleados:
            destino.agregar_empleado(e)
        self.empleados.clear()


d1 = Departamento("Contabilidad", "Finanzas")
d2 = Departamento("Marketing", "Comercial")

d1.agregar_empleado(Empleado("Ana", "Contadora", 3500))
d1.agregar_empleado(Empleado("Luis", "Auxiliar", 2000))
d1.agregar_empleado(Empleado("Maria", "Analista", 3000))
d1.agregar_empleado(Empleado("Carlos", "Auditor", 4000))
d1.agregar_empleado(Empleado("Sofia", "Secretaria", 1800))

print(" ANTES ")
d1.mostrar_empleados()
d2.mostrar_empleados()

d1.cambio_salario(10)

print("SALARIOS MODIFICADOS D1 ")
d1.mostrar_empleados()

hay_comun = any(d2.tiene_empleado(e) for e in d1.empleados)
print("¿Algún empleado de d1 está en d2?", hay_comun)

d1.mover_empleados_a(d2)

print("DESPUÉS DE MOVER")
d1.mostrar_empleados()
d2.mostrar_empleados()
