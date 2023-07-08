def palindromo(palabra):
    palabra = palabra.replace(" ", "")
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False


def run():
    palabra =  input("ingresa una frase:")
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print("la frase/palabra ingresada es palindormo")
    else:
        print("la frase/palabra ingresada no es palindromo")


if __name__ == '__main__':
    run()

