def hacer_pizza(tamaño, *ingredientes):
    print(f'\nhaciendo una pizza de {tamaño} con los siguietes ingredientes:')
    for ingrediente in ingredientes:
        print(f'- {ingrediente}')
    
    
hacer_pizza(16, 'peperoni')
hacer_pizza(12, 'jamon', 'queso', 'bacon')
    