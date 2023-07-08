# biblioteca Pickle

import pickle

#Con este codigo estamos cifrando nuestro archivo a codigo binario
# list_name = ["pedro", "ana", "maria", "isabel"]

# bin_fich = open("lista_nombres", "wb")

# pickle.dump(list_name, bin_fich)

# bin_fich.close()

# del (bin_fich)


#Con este codigo estamos descifrando nuestro archivo convertido en binario
memory_fich = open("lista_nombres", "rb")

list = pickle.load(memory_fich)

print(list)