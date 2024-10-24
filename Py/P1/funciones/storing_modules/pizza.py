def making_pizza (size, *ingredientes):
    print (f'\nsaliendo pizza de tamaño {size}inch con los siguientes ingredientes:')
    for ingrediente in ingredientes:
        print (f'- {ingrediente}')