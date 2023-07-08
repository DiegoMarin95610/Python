import re
from .felinos import Gato
from .felinos import Leon
from .perro import Perro

def creador_gato(nombre):
    return Gato(nombre)