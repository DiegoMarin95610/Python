class Empleados:
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        return "{} que trabaja en el cargo de {} tiene un salario de{}".format(self.nombre, self.cargo, self.salario)


listaEmpleados = [
    Empleados("Carlos", "Director", 240000),
    Empleados("Maria", "Subdirector", 340000),
    Empleados("Manuel", "Contador", 140000),
    Empleados("Lorena", "Comercial", 140000),
    Empleados("Yina", "Comercial", 240000),
    Empleados("Andres", "Contador", 340000),
]

#Funcion Map
def calculoComision(empleado):

    if empleado.salario <= 240000:
        empleado.salario = empleado.salario*1.03
    return empleado

listaEmpleadosFunc = map(calculoComision, listaEmpleados)

for empleado in listaEmpleadosFunc:
    print(empleado)