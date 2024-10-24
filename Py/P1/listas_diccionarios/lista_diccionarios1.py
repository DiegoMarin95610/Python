# Generando creepers de diferentes colores, y la cantidad de spawn depende de la dificultad que se elija.
 
import random

color = ['azul', 'amarillo', 'verde', 'naranja', 'morado']


spawn_creepers = []
dificult = int(input('Elige la dificultad: \n 1 - facil \n 2 - medio \n 3 - dificil \n --> '))

if dificult == 1:
    random_spawn = random.randint(2, 7)
elif dificult == 2:
    random_spawn = random.randint(5, 14)
elif dificult == 3:
    random_spawn = random.randint(10, 30)

for spawn_creeper in range(random_spawn):
    creeper = {
    'vida': '120',
    'ataque': '10',
    'color': color[random.randint(0, 4)]
    }
    spawn_creepers.append(creeper)
    
print (f'Se han generado {random_spawn} creepers')

for creeeper in spawn_creepers:
    print (f'{creeeper}')



    
    

    


