import random

class Dice():
    def __init__(self, size: int) -> None:
        self.size = size        
         
    def roll_dice(self) -> None:
        print(random.randint(1,self.size))


class Lotery():
    def __init__(self) -> None:
        self.letras: list = ['A','B', 'C', 'D']
        self.lista: list = []
        
    def full_list(self) -> None:
        for i in range(10):
            self.lista.append(i)
        for i in range(4):
            self.lista.append(self.letras[i])
            

mi_boleto: list = []
lotery = Lotery()
lotery.full_list()
random.shuffle(lotery.lista)

"""mi boleto al azar"""
for select in range(4):
    mi_boleto.append(random.choice(lotery.lista))

random.shuffle(lotery.lista)


cont = 0
loop = True

while loop:
    ganador: list = []
    """Boleto ganador"""  
    for select in range(4):
        ganador.append(random.choice(lotery.lista))
        
    if ganador == mi_boleto:
        print("Has ganado el premio")
        loop = False
    else:
        cont += 1
        continue

print(f"para ganar tomaron {cont} intento/s")
print(ganador)
print(mi_boleto)
