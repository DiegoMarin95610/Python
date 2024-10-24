class Perro:
    """Simple comportamiento de un perro"""
    
    def __init__(self, nombre, edad):
        """Se inicializan los atributos"""
        self.nombre = nombre
        self.edad = edad
        
    def sentarse(self):
        """perro se sienta"""
        print(f"{self.nombre} esta sentado ahora")
        
    def rodar(self):
        """Perro rueda"""
        print(f"{self.nombre} da un giro")

perros =[]

for i in range(3):
    nombre = input("nombre del tu can \n- ")
    edad = int(input("edad de tu can \n- "))
    crear_perro = Perro(nombre, edad)
    perros.append
    print(f"{nombre} guardado correctamente \n")
    

for perro in perros:
    print(perro.nombre)
        

        