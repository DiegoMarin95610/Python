import json
from get_number import *

def get_stored_number() -> int:
    try:
        with open(FILENAME) as f:
            favorite_number = json.load(f)
        return favorite_number
    except FileNotFoundError:
        return None

def get_stored_user() -> str:
    try:
        with open(FILEUSER) as f:
            username = json.load(f)
        return username
    except FileNotFoundError:
        return None
    