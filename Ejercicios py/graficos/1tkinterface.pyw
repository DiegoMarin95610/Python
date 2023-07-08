from tkinter import *
from tkinter import ttk

#Para crear la raiz o el lienzo
root = Tk()
root.title("Main")
root.resizable(1, 1)
root.iconbitmap("pc.ico")
root.geometry("480x350")
root.config(cursor="pirate",
            relief=SUNKEN,
            bd=12)
root.config(bg="blue")

#Para crear un frame
frm = Frame()
frm.pack(fill="both", expand="True")
frm.config(bg="red", 
           width="400", 
           height="300",
           relief=SUNKEN,
           bd=12,
           cursor="hand1")


#Para ejecutar la aplicacion
root.mainloop()

