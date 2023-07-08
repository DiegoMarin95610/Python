import re

# cadena = "Vamos a aprender de expresiones regulares, Python es un lenguaje de sintaxis sencilla"
# palabraBuscar = "aprender"

# # print(re.search(palabraBuscar, cadena))

# texto_encontrado = re.search(palabraBuscar, cadena)
# texto_buscado = "Python"

# print(re.findall(texto_buscado, cadena))

# print(texto_encontrado.start())

# print(texto_encontrado.end())

# print(texto_encontrado.span())


#--------------------Metacaracteres-----------------------#

# lista_nombres = [
#     'Ana Gomez',
#     'Maria Martin',
#     'Sandra lopez',
#     'Sandra Martinez',
#     'Sandra Gonzalez',
#     'Santiago Martin',
#     'Pablo Martin',
#     'Juan Martin'
# ]


# for elemento in lista_nombres:
#     #Este metacaracter devuelve todos los registros con la palabra inicial que se especifique
#     if re.search('^Sandra', elemento):
#         print(elemento)


# for elemento in lista_nombres:
# #     #Este metacaracter devuelve todos los registros con la palabra final que se especifique
#     if re.search('Martin$', elemento):
#         print(elemento)

# lista_nombres = [
#     'hombres',
#     'mujeres',
#     'niños',
#     'niñes',
#     'niñas'
# ]

# for elemento in lista_nombres:
#     #Busca todos los registros que contengan una combinacion diferente de caracteres como se muestra acontinuacion
#     #Esto tambien consigue busquedas con tildes o algun tipo de caracter especial
#     if re.findall('niñ[oae]s', elemento):
#         print(elemento)


# lista_nombres = [
#     'Glora',
#     'Pamela',
#     'Sofia',
#     'Paola',
#     'Celia',
#     'Rosa',
#     'Pedro',
#     'Carmen'
# ]

# for elemento in lista_nombres:
#     #Busca palabras que tengan un rango especial en el abecedario, como ejemplo colocamos que busque los nombres que contengan las lestras que van 
#     #desde la O hasta la T = (o, p, q, r, s, t)[o-t], cabe destacar que si ponemos las letras mayusculas, buscara letras mayusculas.
#     if re.findall('[o-t]', elemento):
#         print(elemento)


nombre1="Sandra lopez"
nombre2="Antonio Gomez"
nombre2="Maria López"



















