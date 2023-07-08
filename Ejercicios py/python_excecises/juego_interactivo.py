import random


def run():
    vidajuego = 6
    randomnum = random.randint(1, 100)
    print("solos tienes "+str(vidajuego)+" intentos") 
    numero = int(input("Escoge un numero del 1 al 100: "))
    
    print(randomnum)
    while randomnum != numero: 
        
        vidajuego -= 1
        print("te quedan "+str(vidajuego)+" intentos")

        if randomnum > numero:
            numero = int(input("Escoge un numero mas grande: "))
        elif randomnum < numero:
            numero = int(input("Escoge un numero mas pequeño: "))
            
        if vidajuego == 0:
            print("Has perdido el juego") 
            print("te quedan "+str(vidajuego)+" intentos")  
            break 
        
    if randomnum == numero:
        print("Ganaste")  

if __name__ == "__main__":
    run()