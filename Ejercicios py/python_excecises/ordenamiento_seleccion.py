def run():
    lista = [7,6,4,5,1,2,3,11,11,98,46,745,37,84]
    print(lista)  

    for i in range(len(lista)):
        min = i  
        for j in range(i+1, len(lista)):
            if lista[j] < lista[min]:
                min = j 
        temp = lista[i]
        lista[i] =  lista[min]
        lista[min] = temp

    print(lista)



if __name__ == "__main__":
    run()