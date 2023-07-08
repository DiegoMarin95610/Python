from ast import If
from traitlets import Int

#pido al usuario que ingrese su edad, indicando que no se admiten menores de edad
edad = int(input("Recuerda que no dejamos entrar a menores de edad. Escribe tu edad: "))

#evaluo si la edad es mayor o menor de 18 años
if edad < 18:
    #si la edad es menor de 18 años, se indica que no puede ingresar
    print("Eres menor de 18 años, no puedes ingresar")
else:
    #si es mayor de edad, da la bienvenida
    print("Bienvenido") 