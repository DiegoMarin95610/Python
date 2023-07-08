# def imprimir_mensaje():
#     print("mensaje especial.")
#     print("mensaje especial.")

# imprimir_mensaje()
# imprimir_mensaje()
# imprimir_mensaje()

# def conversacion(mensaje):
#     print("Hola")
#     print("Como estas")
#     print(mensaje)
#     print("Adios")


# opcion = int(input("Elige una opcion: (1,2,3)"))

# if opcion == 1:
#     conversacion("esta es la opcion 1")
# elif opcion == 2:
#     conversacion("esta es la opcion 2")
# elif opcion == 3:
#     conversacion("esta es la opcion 3")
# else:
#     print("No es un numero valido")

def suma(a, b):
    print("la suam es: ")
    resultado = a + b
    return resultado

n1 = int(input("numero 1: "))
n2 = int(input("numero 2: "))


sumatoria = suma(n1, n2)
print(sumatoria)