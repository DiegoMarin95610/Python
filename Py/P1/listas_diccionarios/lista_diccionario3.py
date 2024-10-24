# lista de contactos de personas
persona = {}

loop_activo = input('deseas agregar algun contacto? \n yes/no: ')
id_contacto = 0

if loop_activo == "yes":
    loop_activo = True
    
def guardar_contacto(nombre, id, telefono, direccion):
    try:
        persona[nombre] = {
            'id': id, 
            'telefono': telefono, 
            'direccion': direccion
            }
        print('usuario guardado')  
          
    except ValueError:
        print('Creo que algo ha salido mal')
        
while loop_activo:
    nombre = input('nombre del nuevo contacto: ')
    id = int(id_contacto)
    telefono = int(input('telefono: '))
    direccion = input('direccion: ')
    guardar_contacto(nombre, id, telefono, direccion)
    id_contacto += 1
    
    loop_activo = input('deseas agregar a una persona nueva? \n yes/no: ')
    if loop_activo.lower() == "yes":
        loop_activo = True
    else:
        loop_activo = False
        
print(persona)
    
    
    