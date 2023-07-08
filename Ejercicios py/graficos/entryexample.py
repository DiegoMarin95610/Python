from tkinter import *

root = Tk()

frm = Frame(root, width="1200", height="600")
frm.pack()

myName = StringVar()

lbl = Label(frm, text="Nombre:")
lbl.grid(padx=5, row=0, column=0)
txtboxname = Entry(frm, textvariable=myName)
txtboxname.grid(pady=5, row=0, column=1)


lbl1 = Label(frm, text="Apellido:")
lbl1.grid(padx=5, row=1, column=0)
txtboxlastname = Entry(frm)
txtboxlastname.grid(pady=5, row=1, column=1)  


lbl1 = Label(frm, text="Direccion:")
lbl1.grid(padx=5, row=1, column=0)
txtboxaddress = Entry(frm)
txtboxaddress.grid(pady=5, row=2, column=1)


lbl2 = Label(frm, text="Contraseña:")
lbl2.grid(padx=5, row=3, column=0)
txtboxpass = Entry(frm)
txtboxpass.grid(pady=5, row=3, column=1)
txtboxpass.config(show="*")


lbl3 = Label(frm, text="Comentarios label:")
lbl3.grid(padx=5, row=4, column=0)
txtboxcaja = Text(frm, width=16, height=8)
txtboxcaja.grid(pady=5, row=4, column=1)
scrolbar = Scrollbar(frm, command=txtboxcaja.yview)
scrolbar.grid(pady=5, row=4, column=2, sticky="nsew")
txtboxcaja.config(yscrollcommand=scrolbar.set)

def codigoBoton():
    
    myName.set("Perico quitate de la via")

button = Button(root, text="Ingresar", command=codigoBoton)
button.pack()



root.mainloop()