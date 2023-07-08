class Animal():
    volador = True

class cocodrilo():
    def __init__(self, nombre):
        self.nombre = nombre


    @classmethod
    def new(cls, nombre):
        cls.volador = False
        return cocodrilo(nombre)


cocodrilo = cocodrilo.new("coco")
print(cocodrilo)