# def return_val():
    # print("retorna valores")
    # print("retorna valores")
    # print("retorna valores")
    # return True #despues de aqui no sigue ejecutando valores
    # print("retorna valores")
    # print("retorna valores")


def generador(*args):
    for valor in args:
        yield valor * 10 #example

for valor in generador(1,2,3,4,5,6,7,8,9):
    print(valor)