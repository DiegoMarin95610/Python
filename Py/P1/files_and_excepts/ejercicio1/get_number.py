import json

FILENAME = "number.json"
FILEUSER = "user.json"

def get_number(mensaje):
    while True:     
        try:
            favorite_number = int(input(mensaje))
            with open(FILENAME, "w") as f:
                json.dump(favorite_number, f)
                break         
        except ValueError:        
            print ("El valor ingresado no es un numero.")
            
def get_username(mensaje):
    while True:     
        try:
            username = str(input(mensaje))
            with open(FILEUSER, "w") as f:
                json.dump(username, f)
                break         
        except ValueError:        
            print ("Ingresa un nombre de usuario válido.")
            