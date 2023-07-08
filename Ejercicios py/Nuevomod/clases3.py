class Usuario:
    #Verdadero constructor de la clase
    def __new__(cls):
        print("Este es el primero que se ejecuta")
        return super().__new__(cls)


    def __init__(self):
        print("Este es el segundo que se ejecuta")

    #Esto se imprime cuando intento mostrar el objeto, esto devuelve un string
    def __str__(self):
        pass

    def __getattr__(self, nombre):
        print("no se encontro el atributo")
        self.otro_metodo()

    def otro_metodo(self):
        print("Otro metodo")


usuario = Usuario()

print(usuario.apellido)