def run(valid = True):
    def _run(func):
        def before_action():
            print("hola inicial")

        
        def after_action():
            print("adios final")
            

        def deco1(*arg, **kwargs):
            if valid:
                before_action()

            result = func(*arg, **kwargs)

            if result:
                after_action()
            return result
        return deco1
    return _run

@run()
def suma(n1, n2):
    return n1 + n2

result = suma(2, 6)
print (result)
