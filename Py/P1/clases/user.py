class User():
    
    def __init__(self, first_name, last_name) -> None:
        self.first_name = first_name
        self.last_name = last_name
    
    def describe_user(self):
        print(f"Nombre: {self.first_name}")
        print(f"Apellido: {self.last_name}")
        
    def greet_user(self):
        print(f"bienvenido al sistema {self.first_name} {self.last_name}")
        
        
class Admin(User):
    
    def __init__(self):
        self.privileges = Privileges()

    
class Privileges():
    
    def __init__(self) -> None:
        self.privileges = [ "can add post", "can delete post", "can ban user"]
    
    def show_privileges(self):
        print("tienes los siguientes privilegios: ")
        
        for privilege in self.privileges:
            print(f"- {privilege}")
            
 