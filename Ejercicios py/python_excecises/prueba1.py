from operator import truediv


def es_primo(numero):
    cont = 0

    for i in range(1, numero + 1):
        print(cont)
        if i == 1 or i == numero:
            continue
        if numero % i == 0:
            cont += 1 
    if cont == 0:
        return True
    else:
        return False         


def run():
    numero = int(input("Escribe un numero: "))

    if es_primo(numero):
        print("El numero es primo")
    else:
        print("El numero no es primo")


    pass


if __name__ == "__main__":
    run()