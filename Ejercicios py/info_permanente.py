import pickle

class Usuario:
    
    def __init__(self, nombre, genero, edad) -> None:
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        print("Se ha creado una persona nueva con el nombre de: {}".format(self.nombre))

    def __str__(self) -> str:
        return "{} {} {}".format(self.nombre, self.genero, self.edad)
    

class listaUsuarios:

    usuarios = []

    def __init__(self) -> None:
        
        binUsuarios =  open("lista_usuarios", "ab+")
        binUsuarios.seek(0)

        try:
            self.usuarios = pickle.load(binUsuarios)
            print("se cargaron {} personas del fichero externo".format(len(self.usuarios)))
        except:
            print("El fichero esta vacio") 
        finally:
            binUsuarios.close()
            del (binUsuarios)


    def agregarUsuarios(self, user):
        self.usuarios.append(user)
        self.guardarUsuariosEnFicheroExterno()

    def mostrarUsuarios(self):
        for user in self.usuarios:
            print(user)

    def guardarUsuariosEnFicheroExterno(self):
        listaUsuarios = open("lista_usuarios", "wb")
        pickle.dump(self.usuarios, listaUsuarios)
        listaUsuarios.close()
        del (listaUsuarios)

    def mostrarInfoFicheroExterno(self):
        print("la informaccion del archivo externo es la siguiente: ")
        for user in self.usuarios:
            print(user,"\n")
        


miLista = listaUsuarios()
user = Usuario("Carlos", "Masculino", 27)
miLista.agregarUsuarios(user)
miLista.mostrarInfoFicheroExterno()

