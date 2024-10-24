class Carro():
    
    def __init__(self, fabricante, modelo, año):
        self.fabricante = fabricante
        self.modelo = modelo
        self.año = año
        
    def datos(self):
        datos = f'{self.fabricante} {self.modelo} {self.año}'
        return datos.title()
    
    def mostrar_datos(self):
        print(self.datos())
    
    
class CarroElectrico(Carro):
    
    def __init__(self, fabricante, modelo, año, bateria):
        super().__init__(fabricante, modelo, año)
        self.bateria = bateria
    
    def mostrar_datos(self):
        print(f'{super().datos()} {self.bateria.title()}')
        
    def cambiar_bateria(self, bateria):
        self.bateria = bateria
        
        