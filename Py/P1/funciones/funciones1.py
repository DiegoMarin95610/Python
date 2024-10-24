# def make_shirt (talla='M', mensaje='Me encanta python'):
#     print(f'talla de camiseta {talla}')
#     print(f'mensajes: {mensaje} \n')
    
# make_shirt ('XL')

# def describe_city (ciudad, pais='Unknown'): 
#     if pais == 'Unknown':
#         print(f'la ciudad es {ciudad} pero el pais es desconocido')
#     else:    
#         print(f'la ciudad {ciudad} esta en {pais}')
    
    
# describe_city ('Cali', 'Colombia')
# describe_city ('Cali')

def nombre_formateado (nombre, apellido, segundo_nombre=''):
    if segundo_nombre:
        nombre_completo = f'{nombre} {segundo_nombre} {apellido}'
    else:
        nombre_completo = f'{nombre} {apellido}'
        
    return nombre_completo.title()

nombre = nombre_formateado ('DIego', 'gOnZalez', 'armANDo')
print(nombre)
    
    