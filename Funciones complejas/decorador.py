def mi_decorador(funcion):
    def nueva_funcion(*args, **kwargs):
        print("Se va a llamar")
        c = funcion(*args, **kwargs)
        print("Se ha llamado")
        return c
    return nueva_funcion

@mi_decorador
def suma(a, b):
    print("Entra en funcion suma")
    return a + b

suma(5,8)
