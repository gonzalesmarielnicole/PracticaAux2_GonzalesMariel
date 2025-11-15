class Empleado:
    def __init__(self, nombre, puesto, salario):
        self.nombre = nombre
        self.puesto = puesto
        self.salario = salario


class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def mostrar_info(self):
        print(f"Empresa: {self.nombre}")
        print("Empleados:")
        for e in self.empleados:
            print(f"- {e.nombre}, {e.puesto}, salario: {e.salario}")

    def buscar_empleado(self, nombre):
        for e in self.empleados:
            if e.nombre == nombre:
                return e
        return None

    def eliminar_empleado(self, nombre):
        self.empleados = [e for e in self.empleados if e.nombre != nombre]

    def promedio_salarial(self):
        if not self.empleados:
            return 0
        return sum(e.salario for e in self.empleados) / len(self.empleados)

    def empleados_con_salario_mayor(self, minimo):
        return [e for e in self.empleados if e.salario > minimo]


e1 = Empleado("Ana", "Gerente", 5000)
e2 = Empleado("Luis", "Contador", 3500)
e3 = Empleado("Marta", "Secretaria", 2500)
e4 = Empleado("Pedro", "Técnico", 3000)

empresa = Empresa("TechCorp")
empresa.agregar_empleado(e1)
empresa.agregar_empleado(e2)
empresa.agregar_empleado(e3)
empresa.agregar_empleado(e4)

empresa.mostrar_info()

emp = empresa.buscar_empleado("Luis")
if emp:
    print(f"\nEncontrado: {emp.nombre}, {emp.puesto}, salario: {emp.salario}")

empresa.eliminar_empleado("Marta")

print("\nDespués de eliminar Marta:")
empresa.mostrar_info()

print("\nPromedio salarial:", empresa.promedio_salarial())

print("\nEmpleados con salario mayor a 3000:")
for x in empresa.empleados_con_salario_mayor(3000):
    print(f"- {x.nombre} ({x.salario})")
