from tkinter import *
from tkinter.messagebox import *
import sqlite3
from os import *
import os.path

#---------------------Function--------------------#
def conexionDB():
    
    try:
        con = sqlite3.connect("ddbbp1")
        cur = con.cursor()
        cur.execute('''
            CREATE TABLE USER(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NAME VARCHAR(40),
                LAST_NAME VARCHAR(40),
                CITY VARCHAR(20),
                EMAIL VARCHAR(30),
                COMENT VARCHAR(80)
            )
        ''')
        showinfo(title="Succes", message="Base de datos creada correctamente")
        fileMenu.pack_forget()
        con.close
    except:
        showwarning(title="Atencion", message="La base de datos ya existe")

def salirApp():

    value = askquestion(title="Salir", message="Estas seguro que desar abandonar?")
    if value == "yes":
        root.destroy()

def borrarCampos():
    strId.set("")
    strName.set("")
    strLastName.set("")
    strCity.set("")
    strEmail.set("")
    txtboxComent.delete(1.0, END)

def acercaDe():
    showinfo(title="Info", message="Version del programa 1.0")

def Crear():
    con = sqlite3.connect("ddbbp1")
    cur = con.cursor()
    cur.execute("INSERT INTO USER VALUES (NULL,'"+txtboxName.get()+
    "','"+txtboxLastName.get()+
    "','"+txtboxCity.get()+
    "','"+txtboxEmail.get()+
    "','"+txtboxComent.get("1.0", END)+"')")

    con.commit()
    con.close()
    borrarCampos()
    showwarning(title="Exito", message="Los datos han sido guardados correctamente.")

def Leer():
    con = sqlite3.connect("ddbbp1")
    cur = con.cursor()
    cur.execute("SELECT * FROM USER WHERE ID = "+txtboxId.get())
    usuario = cur.fetchall()
    borrarCampos()

    for user in usuario:
        strId.set(user[0])
        strName.set(user[1])
        strLastName.set(user[2])
        strCity.set(user[3])
        strEmail.set(user[4])
        txtboxComent.insert(1.0, user[5])

    con.commit()
    con.close()
        
def Actualizar():
    con = sqlite3.connect("ddbbp1")
    cur = con.cursor()
    cur.execute("UPDATE USER SET NAME='"+txtboxName.get()+
    "', LAST_NAME='"+txtboxLastName.get()+
    "', CITY='"+txtboxCity.get()+
    "', EMAIL='"+txtboxEmail.get()+
    "', COMENT='"+txtboxComent.get("1.0", END)+
    "' WHERE ID="+txtboxId.get())

    con.commit()
    con.close()
    showwarning(title="Actualizado", message="Los registros han sido actualizados correctamente")

def Borrar():
    con = sqlite3.connect("ddbbp1")
    cur = con.cursor()
    
    question = askquestion("Borrar", "Estas seguro que deseas borrar el registro?")
    if question == "yes":
        cur.execute("DELETE FROM USER WHERE ID="+txtboxId.get())
        con.commit()
        con.close()
        showwarning("Borrado", "El registro ha sido eliminado exitosamente")
        borrarCampos()




#Raiz
root = Tk()

#VariablesRoot
strName = StringVar()
strLastName = StringVar()
strCity = StringVar()
strEmail = StringVar()
strId = StringVar()

#navBar
menuInicio = Menu(root)
root.config(menu=menuInicio, width="250", height="300")
root.propagate(False)

#Submenus
fileMenu = Menu(menuInicio, tearoff=0)
fileMenu.add_command(label="Conectar", command=conexionDB)
fileMenu.add_separator()
fileMenu.add_command(label="Salir", command=salirApp)

editMenu = Menu(menuInicio, tearoff=0)
editMenu.add_command(label="Borrar datos", command=borrarCampos)

CRUDMenu = Menu(menuInicio, tearoff=0)
CRUDMenu.add_command(label="Crear", command=Crear)
CRUDMenu.add_command(label="Leer", command=Leer)
CRUDMenu.add_command(label="Actualizar", command=Actualizar)
CRUDMenu.add_command(label="Eliminar", command=Borrar)

helpMenu = Menu(menuInicio, tearoff=0)
helpMenu.add_command(label="acerca de.", command=acercaDe)

#Menu
menuInicio.add_cascade(label="Archivo", menu=fileMenu)
menuInicio.add_cascade(label="Editar", menu=editMenu)
menuInicio.add_cascade(label="CRUD", menu=CRUDMenu)
menuInicio.add_cascade(label="Ayuda", menu=helpMenu)

#Frame 1
frm = Frame(root)
frm.propagate(False)
frm.pack()

Id = Label(frm, text="Id:")
Id.grid(padx=5, row=0, column=0)
txtboxId = Entry(frm, textvariable=strId)
txtboxId.grid(pady=5, row=0, column=2)


name = Label(frm, text="Nombre:")
name.grid(padx=5, row=1, column=0)
txtboxName = Entry(frm, textvariable=strName)
txtboxName.grid(pady=5, row=1, column=2)

lastName = Label(frm, text="Apellido:")
lastName.grid(padx=5, row=2, column=0)
txtboxLastName = Entry(frm, textvariable=strLastName)
txtboxLastName.grid(pady=5, row=2, column=2)

city = Label(frm, text="Ciudad:")
city.grid(padx=5, row=3, column=0)
txtboxCity = Entry(frm, textvariable=strCity)
txtboxCity.grid(pady=5, row=3, column=2)

email = Label(frm, text="Correo:")
email.grid(padx=5, row=4, column=0)
txtboxEmail = Entry(frm, textvariable=strEmail)
txtboxEmail.grid(pady=5, row=4, column=2)

coment = Label(frm, text="Comentario:")
coment.grid(padx=5, row=5, column=0)
txtboxComent = Text(frm, width=15, height=5)
txtboxComent.grid(pady=5, row=5, column=2)
scrollvet = Scrollbar(frm, command=txtboxComent.yview)
scrollvet.grid(row=5, column=3, sticky="nsew")
txtboxComent.config(yscrollcommand=scrollvet.set)

#Frame 2
frm2 = Frame(root)
frm2.pack()

button = Button(frm2, text="Crear", command=Crear)
button.grid(row=4, column=0, pady=5)

button = Button(frm2, text="Ver", command=Leer)
button.grid(row=4, column=1, pady=5)

button = Button(frm2, text="Actualizar", command=Actualizar)
button.grid(row=4, column=2, pady=5)

button = Button(frm2, text="Borrar", command=Borrar)
button.grid(row=4, column=3, pady=5)

root.mainloop()