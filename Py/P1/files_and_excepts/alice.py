def count_words(filename):
    try:
        with open(filename, 'rb') as f:
            contents = f.read()
    except FileNotFoundError:
        # print(f'El archivo {filename} no existe.')
        # return None
        pass
    # except UnicodeError:
    #     print(f'El archivo {filename} contiene caracteres no compatibles.')
    #     return None
    else:
        words = contents.split()
        num_words = len(words)
        print(f"el archivo {filename} contiene {num_words} palabras.")


filenames = ['mytextfile.txt', 'proximab', 'mytextfile1.txt', 'mytextfile2.txt']  

for file in filenames:  
    count_words(file)

