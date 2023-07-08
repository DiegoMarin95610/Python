from io import open


#Crear archivos desde python modo escritura W = write
# text_file = open("textonew.txt","w")

# frase = "Hola, aqui estoy escribiendo \nhola de nuevo en una nueva linea"

# text_file.write(frase)

# text_file.close()

#Crear archivos desde python modo lectura R = Read o readlines

#Si adicionamos "r+" le damos a entender al programa que es de lectura y escritura
# .seek(#) reinicia el cursor para volver al principio de la lectura
# readlines() funcion que lee linea por linea y convierte en una lista que se puede recorrer
# writelines() funcion que recibe como parametro una lista de string, para poder manipularla o reescribirla.

text_file = open("textonew.txt","r")

text =  text_file.read()

text_file.close

print(text)