class animal():
    @property
    def terrestre(self):
        return True

#classe padre
class felino(animal):
    @property
    def garras_retractiles(self):
        return True

    def cazar(self):
        print("el felino esta cazando")

class mascota():
    nombre = ''
    
    def mostrar_nombre(self):
        print("el gato es de la clase padre: {}".format(self.nombre))

#clase gato hereda de felino.
class gato(felino, mascota):
    def gato_cazador(self):
        self.cazar()


    def mostrar_nombre(self):
        mascota.mostrar_nombre(self)
        print("el gato es: {}".format(self.nombre))


#clase jaguar hereda de felino.
class jaguar(felino):
    pass

gato = gato()
jaguar = jaguar()

print(gato.garras_retractiles)
print(gato.terrestre)
gato.nombre = "enel"
print(gato.mostrar_nombre())

print(gato.cazar())