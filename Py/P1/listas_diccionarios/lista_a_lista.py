usuarios_sin_confirmar = [
    {
        'first_name': 'Lona',
        'last_name': 'Pestoso',
        'age': '15',
        'city': 'Chernobyl' 
    },
    {
        'first_name': 'Pardo',
        'last_name': 'Posilga',
        'age': '23',
        'city': 'Mongomeri' 
    }, 
    {
        'first_name': 'Marcuz',
        'last_name': 'Diamond',
        'age': '13',
        'city': 'Mongomeri' 
    },
    {
        'first_name': 'Costi',
        'last_name': 'Marongo',
        'age': '41',
        'city': 'Bangladesh' 
    },
    {
        'first_name': 'Lina',
        'last_name': 'Tabares',
        'age': '18',
        'city': 'Germany' 
    }
]

usuarios_confirmados = []

while usuarios_sin_confirmar:
    usuario_actual = usuarios_sin_confirmar.pop()
    edad_usuario_actual = int(usuario_actual['age'])
    if edad_usuario_actual > 18:
        print(f'lo sentimos {usuario_actual['first_name']} solo se admiten mayores de 18 años')
    else:
        usuarios_confirmados.append(usuario_actual)
        print(f'hola {usuario_actual['first_name']} {usuario_actual['last_name']}! tu si puedes ingresar')

print('bienvenidos al sistema!!')
for usuario_confirmado in usuarios_confirmados:
    print (usuario_confirmado)    
    
