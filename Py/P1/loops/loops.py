personas = []
start = True
print ('Bienvenido al sistema de registro de personas')

while start != False:
    
    num_personas_agregar = int(input('cuantas personas deseas agregar? \n ->')) 

    for num_persona in range(num_personas_agregar):
        print (f'Agregue a la persona numero {num_persona}')
        
        dni = input("digite el dni: ")
        nombre = input("digite el nombre: ")
        edad = input("digite el edad: ")
        pais = input("digite el pais: ")
        ciudad = input("digite el ciudad: ")
        persona = {
            'dni': dni,
            'nombre': nombre,
            'edad': edad,
            'pais': pais,
            'ciudad': ciudad
        }
        personas.append(persona)
        
    print(f'{personas} \n')
    
    print("Deseas agregar a otra persona? \n 1 - Si \n 2 - No")
    otra_persona_mas = int(input('-> '))
    
    if otra_persona_mas == 2:
        print('Gracias por visitar el registro de usuarios')
        start = False
        # tambien se puede usar Break para terminar el ciclo, para mas facilidad si hay menos complejidad.
    
    
