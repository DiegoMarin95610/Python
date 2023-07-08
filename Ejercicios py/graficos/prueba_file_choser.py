from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

root = Tk()

def abrirFichero():

    fichero =  filedialog.askopenfilename(title="Abir", initialdir="C:", filetypes=(("ficheros excel", "*.xlsx"), 
    ("ficheros de texto", "*.txt")))
    print(fichero)


Button(root, text="Open file", command=abrirFichero).pack()












root.mainloop()
