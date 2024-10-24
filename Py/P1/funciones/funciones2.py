pokemon_disponibles = ['charizard', 'piplup', 'pikachu', 'gengar', 'treecko', 'darkray', 'torchic']
busqueda = True
pokenames = []

def buscar_pokemons (names):    
    pkmn_en_inventario = []
    pkmn_sin_capturar = []
    
    for name in names:
        if name in pokemon_disponibles:
            pkmn_en_inventario.append(name)
            continue
        else:
            pkmn_sin_capturar.append(name)
            continue
        
    print(pkmn_en_inventario)
    print(pkmn_sin_capturar)
    
    
while busqueda:
    cuantos_pokemon = int(input('Cuantos pokemon deseas buscar? \n= '))
    for pokemon in range(cuantos_pokemon):
        pkmn = input('ingresa el nombre del pokemon \n=')
        pokenames.append(pkmn.lower())
        
    busqueda = input('deseas buscar mas pokemon? \n si/no = ')
    if busqueda == "no":
        print('falso')
        busqueda = False        
    elif busqueda == "si" or "yes":
        print('verdadero')
        busqueda = True
    
buscar_pokemons(pokenames)