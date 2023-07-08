class Empleados:
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        return "{} que trabaja en el cargo de {} tiene un salario de{}".format(self.nombre, self.cargo, self.salario)


listaEmpleados = [
    Empleados("Carlos", "Director", 540000),
    Empleados("Maria", "Subdirector", 640000),
    Empleados("Manuel", "Contador", 340000),
    Empleados("Lorena", "Comercial", 240000),
    Empleados("Yina", "Comercial", 440000),
    Empleados("Andres", "Contador", 740000),
]

salarios_altos= filter(lambda empleado:empleado.salario>340000, listaEmpleados)

for empleados_salarios in salarios_altos:
    print(empleados_salarios,"\n")