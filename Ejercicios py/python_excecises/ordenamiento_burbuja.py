def run():
    lista = [2,9,5,3,5,1,0]
    print(lista)
    for i in range(len(lista)):
        for x in range(len(lista)-1):
            # Solo si le cambiamos el operador logico (>) , se podria invertir el ordenamiento
            if lista[x] > lista[x+1]:
                temp = lista[x]
                lista[x] = lista[x+1]
                lista[x+1] = temp
    print(lista)


if __name__ == "__main__":
    run()