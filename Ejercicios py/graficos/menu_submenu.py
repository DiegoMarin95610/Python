from tkinter import *
from tkinter import messagebox

#-----------------------Funciones-----------------------------#
def infoAdicional():
    messagebox.showinfo("Aceca de.", "Version de Diego")

def avisoLicecia():
    messagebox.showwarning("Licencia", "Producto bajo licencia GNU")

def salirApp():
    # valor = messagebox.askquestion("Cerrar", "Realamente te vas?") #Devuelve Yes y No
    valor = messagebox.askokcancel("Cerrar", "Realamente te vas?") #Devuelve True o False

    if valor == "yes":
        root.destroy()

def abrirDoc():
    
    valor = messagebox.askretrycancel("Reintentar", "Error al cargar")
    cont = 1

    while valor==1:
        cont+=valor
        valor = messagebox.askretrycancel("Reintentar", "Error al cargar")
        print(cont)

        if cont == 3:
                messagebox.showwarning("Error", "Error al intentar abrir archivo")
                valor = 0
                root.destroy()



#-----------------------Raiz-----------------------------#
root = Tk()
root.config(width=600, height=300)
root.resizable(0,0)

navBar = Menu(root)
root.config(menu=navBar)

fileMenu = Menu(navBar, tearoff=0)  #Menu
fileMenu.add_command(label="Nuevo")   #Sub menu
fileMenu.add_command(label="Abrir", command=abrirDoc)   #Sub menu
fileMenu.add_separator()   #Separador
fileMenu.add_command(label="Guardar")   #Sub menu
fileMenu.add_command(label="Guardar como...")   #Sub menu
fileMenu.add_separator()   #Separador
fileMenu.add_command(label="Cerrar", command=salirApp)   #Sub menu


editMenu = Menu(navBar, tearoff=0)
editMenu.add_command(label="Copiar")   #Sub menu
editMenu.add_command(label="Cortar")   #Sub menu
editMenu.add_command(label="Pegar")   #Sub menu


toolMenu = Menu(navBar, tearoff=0)

helpMenu = Menu(navBar, tearoff=0)
helpMenu.add_command(label="Acerca de", command=infoAdicional)   #Sub menu
helpMenu.add_command(label="Licencia", command=avisoLicecia)   #Sub menu


navBar.add_cascade(label="Archivo", menu=fileMenu)
navBar.add_cascade(label="Editar", menu=editMenu)
navBar.add_cascade(label="Herramientas", menu=toolMenu)
navBar.add_cascade(label="Ayuda", menu=helpMenu)

root.mainloop()