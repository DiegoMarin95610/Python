filenames: list = ['cats.txt', 'dogs.txt']

for filename in filenames:
    try: 
        with open(filename, 'r') as f:
            contents = f.readlines()
            print(contents)
    except FileNotFoundError:
        pass
        # print(f'El archivo {filename} no existe.')
            