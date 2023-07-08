from asyncio import proactor_events
from re import A


class Usuario():
    def __init__(self, usuraio, contraseña, correo):
        self.usuario = usuraio
        #atributo privado, las instancias no podran acceder a este atributo __contraseña
        self.__contraseña = self.__encriptar_contraseña(contraseña)
        self.correo = correo

    def __encriptar_contraseña(self, contraseña):
        return contraseña.upper()

    @property
    def set_contraseña(self):
        return self.__contraseña

    @set_contraseña.setter
    def set_contraseña(self, valor):
        self.__contraseña = self.__encriptar_contraseña(valor)



Eduardo = Usuario("edu24", "holapablo", "edu@gmail.com")
print(Eduardo.usuario)
print(Eduardo.set_contraseña)
print(Eduardo.correo)

        