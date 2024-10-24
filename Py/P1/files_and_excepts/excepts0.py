def suma(a: int, b: int):
    print(a + b)

def obtener_numero(mensaje: str) -> int:
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print('Error: ingrese un número entero')
        

numero1 = obtener_numero("digite primer numero -> ")
numero2 = obtener_numero("digite segundo numero -> ")

suma(numero1, numero2)