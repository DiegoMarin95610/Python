personas = []

print ('Bienvenido al sistema de registro de personas')
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
    
print(personas)
    
    
