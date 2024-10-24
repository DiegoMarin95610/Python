import json

def get_stored_user() -> str:
    filename = "name.json"
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_user() -> str:
    filename = "name.json"
    username = input("Agregar usuario... -> ")
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username   

def get_user():
    username = get_stored_user()
    if username:
        print(f"Hola de nuevo {username}!")
    else:
        username = get_new_user()
        print(f"Te recordaremos para futuras consultas {username}")
    
get_user()