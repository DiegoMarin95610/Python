import math

def raizCuadrada(listaNumeros):
    """
    La funcion devuelve una lista con la raiz cuadrada
    de los elementos nuemricos pasados por parametros
    en otra lista, test:
    
    >>> lista = []
    >>> for i in [4, 9, 12]:
    ...     lista.append(i)
    >>> raizCuadrada(lista)
    [2.0, 3.0, 4.0]
    
    """
    
    return [math.sqrt(n) for n in listaNumeros]


import doctest

doctest.testmod()

