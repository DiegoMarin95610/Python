class Circulo():

    def __init__(self, radio):
        self.radio = radio

    def area(self): #Metodo de instancia.
        return self.radio * self.radio #* self.pi()

    @staticmethod
    def pi(): #Metodo estatico
        return 3.1416

circulo1 = Circulo(4)
circulo2 = Circulo(5)

print(circulo1.area() * Circulo.pi())

# print(circulo2.area())
    