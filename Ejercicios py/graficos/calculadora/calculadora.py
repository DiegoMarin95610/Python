from cgitb import text
from multiprocessing.sharedctypes import Value
from tkinter import *

#Variables
operacion = ""
result = 0

#Raiz
root = Tk()
root.config(bg="blue", relief=SUNKEN, bd=12)
root.resizable(0, 0)

#Frame
frm = Frame(root, bg="blue")
frm.pack()

#Caja donde aparecen los numero de la calculadora
numerosPantalla = StringVar()
cajanumero = Entry(frm, width=35, textvariable=numerosPantalla)
cajanumero.grid(pady=5, padx=5, row=0, columnspan=4)


#--------------------Funciones---------------------------------#
def pulsaBoton(num):

    global operacion

    if operacion!="":
        numerosPantalla.set(num)
        operacion = ""
    else:
        numerosPantalla.set(numerosPantalla.get()+num)

def Suma(num):

    global operacion
    global result

    result+=int(num)

    operacion = "suma"
     
    numerosPantalla.set(result)

def Resta(num):

    global operacion
    global result

    result+=int(num)

    operacion = "resta"
     
    numerosPantalla.set(result)

def Resultado():

    global result

    numerosPantalla.set(result+int(numerosPantalla.get()))
    numerosPantalla.delete()

    result = 0


#Botones de la calculadora
#--------------------Fila 1 ---------------------------------#
button1 = Button(frm, text="1", command=lambda:pulsaBoton("1"))
button1.grid(pady=5, padx=5, row=1,column=0)
button1.config(width=5, height=2)
button2 = Button(frm, text="2", command=lambda:pulsaBoton("2"))
button2.grid(pady=5, padx=5, row=1,column=1)
button2.config(width=5, height=2)
button3 = Button(frm, text="3", command=lambda:pulsaBoton("3"))
button3.grid(pady=5, padx=5, row=1,column=2)
button3.config(width=5, height=2)
#Suma
suma = Button(frm, text="+", command=lambda:Suma(numerosPantalla.get()))
suma.grid(pady=5, padx=5, row=1,column=3)
suma.config(width=5, height=2)

#--------------------Fila 2 ---------------------------------#
button4 = Button(frm, text="4", command=lambda:pulsaBoton("4"))
button4.grid(pady=5, padx=5, row=2,column=0)
button4.config(width=5, height=2)
button5 = Button(frm, text="5", command=lambda:pulsaBoton("5"))
button5.grid(pady=5, padx=5, row=2,column=1)
button5.config(width=5, height=2)
button6 = Button(frm, text="6", command=lambda:pulsaBoton("6"))
button6.grid(pady=5, padx=5, row=2,column=2)
button6.config(width=5, height=2)
#Resta
resta = Button(frm, text="-", command=lambda:Resta(numerosPantalla.get()))
resta.grid(pady=5, padx=5, row=2,column=3)
resta.config(width=5, height=2)

#--------------------Fila 3 ---------------------------------#
button7 = Button(frm, text="7", command=lambda:pulsaBoton("7"))
button7.grid(pady=5, padx=5, row=3,column=0)
button7.config(width=5, height=2)
button8 = Button(frm, text="8", command=lambda:pulsaBoton("8"))
button8.grid(pady=5, padx=5, row=3,column=1)
button8.config(width=5, height=2)
button9 = Button(frm, text="9", command=lambda:pulsaBoton("9"))
button9.grid(pady=5, padx=5, row=3,column=2)
button9.config(width=5, height=2)
#Multiplicacion
multiplicacion = Button(frm, text="*")
multiplicacion.grid(pady=5, padx=5, row=3,column=3)
multiplicacion.config(width=5, height=2)

#--------------------Fila 4 ---------------------------------#
button0 = Button(frm, text="0", command=lambda:pulsaBoton("0"))
button0.grid(pady=5, padx=5, row=4,column=1)
button0.config(width=5, height=2)
#Resultado
resultado = Button(frm, text="=", command=lambda:Resultado())
resultado.grid(pady=5, padx=5, row=4,column=2)
resultado.config(width=5, height=2)
#Coma
coma = Button(frm, text=",", command=lambda:pulsaBoton("."))
coma.grid(pady=5, padx=5, row=4,column=0)
coma.config(width=5, height=2)
#division
divicion = Button(frm, text="/")
divicion.grid(pady=5, padx=5, row=4,column=3)
divicion.config(width=5, height=2)

root.mainloop()