def generador(*args):
    """Para que lo sepas, esta es una funcion documentada por Diego\nDocumentacion escrita en python\nque se imprimira en breve."""
    for valor in args:
        yield valor * 10 #example


docu = generador.__doc__
docu1 = generador.__name__

print(docu1, " : ")
print(docu)