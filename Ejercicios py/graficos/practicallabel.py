from tkinter import *
from tkinter import ttk
from tkinter.font import BOLD

root = Tk()
root.title("Label practice")
frm = Frame(root, width="500", height="400")
frm.pack()

#Si reutilizaremos esta variable declarada
# label1 =    Label(frm, text="Hola mundo!")
# label1.place(x=100, y=100)

#Para agregar una images
img = PhotoImage(file="goku.gif")
Label(frm, image=img).grid()

# Si no vamos a utilizar de nuevo esta declaracion
Label(frm, text="Hola mundo!", bg=None, fg="red", font=("Comic Sans MS", 22, BOLD)).place(x=100, y=100)


root.mainloop()

