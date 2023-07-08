# Se usa self cuando es metodo de una clase.

class lapiz:
    

    def __init__(self, color = 'sin color', contiene_borrador = False, usa_grafito = True):
        self.color = color
        self.contiene_borrador = contiene_borrador
        self.usa_grafito = usa_grafito

    def dibujar(self):
        print("el lapiz esta dibujando")

    def borrar(self):
        if self.es_valido_para_borrar():
            print("el lapiz esta borrando")
        else:
            print("No es posible borrar")

    def es_valido_para_borrar(self):
        return self.contiene_borrador

lapiz_generico = lapiz(contiene_borrador = True)
print(lapiz_generico.color)
lapiz_generico.dibujar()
lapiz_generico.borrar()
lapiz_generico.contiene_borrador = True
lapiz_generico.borrar()
