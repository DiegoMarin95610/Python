def run():
    lista = [5, 10, 3, 12, 10, 6, 0]

    for i in range(1, len(lista)):
        temp =  lista[i]
        j = i - 1 
        while j >= 0 and temp < lista[j]:
            lista[j+1] = lista[j]
            lista[j] = temp
            j -= 1 

    print(lista)

if __name__ == "__main__":
    run()