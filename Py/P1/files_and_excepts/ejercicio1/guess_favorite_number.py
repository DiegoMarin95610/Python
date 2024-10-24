import json
from get_stored_number import *
from get_number import *

def validate_user(user) -> bool:
    stored_user = get_stored_user()
    user = str(user).lower()
    if user == stored_user.lower():
        return True 
    
def get_current_user(message) -> str:
    try:
        get_user = input(message)
        return get_user
    except ValueError:
        print("ingresa un nombre de usuario valido.\n -> ")
    

def guess_favorite_number():   
    while True:
        get_user = get_current_user("Ingresa nombre de usuario.\n -> ")
        if validate_user(get_user):
            favorite_number = get_stored_number()
            print(f"tu numero favorito es {favorite_number}")
            break
        else:
            print("Usuario NO registrado, deseas registrar un nuevo usuario? S/N")
            new = input("-> ")
            if new.lower() == "s":
                get_username("Ingresa al nuevo usuario.\n -> ")
                get_number("Ahora ingresa tu numero favorito\n -> ")
            else:
                break
        
