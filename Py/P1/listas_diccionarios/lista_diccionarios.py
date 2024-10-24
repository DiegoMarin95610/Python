lista = [
    {
        'firs_name': 'Anoa',
        'last_name': 'Pestoso',
        'age': '28',
        'city': 'Chernobyl' 
    },
    {
        'firs_name': 'Pardo',
        'last_name': 'Posilga',
        'age': '33',
        'city': 'Mongomeri' 
    },
    {
        'firs_name': 'Costi',
        'last_name': 'Marongo',
        'age': '41',
        'city': 'Bangladesh' 
    }
]

busca_usuario = 'Pelica'
usuario_encontrado = False

for item in lista:
    for key, value in item.items():
        if busca_usuario in item.values():
            print(f'usuario encontrado {value}')
            usuario_encontrado = True
            break
        
if not usuario_encontrado:
    print('usuario no encontrado')