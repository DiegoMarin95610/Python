class Restaurant():
    
    def __init__(self, restaurant_name, cuisine_type) -> None:
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        print(f"restaurante: {self.restaurant_name}")
        print(f"tipo de cocina: {self.cuisine_type}")
        
    def open_restaurant(self):
        print(f"El restaurante '{self.restaurant_name}' esta abierto al publico")


class IceCreamStand(Restaurant):
    
    def __init__(self) -> None:
        self.flavor = ['vanila', 'chocolat', 'strawberry', 'apple', 'pineapple']
        
    def show_flavors(self):
        print("Helados disponibles")
        for flavor in self.flavor:
            print(f"- {flavor}")
            
