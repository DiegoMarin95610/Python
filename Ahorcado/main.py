from tkinter import *
from random import randint
from tkinter.messagebox import *

life = 7
correctLetters = 0

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

#-----------------Variables-----------------#
triedLetter = []


#-----------------Function-----------------#
def catchLetterFunction():

  global life
  global correctLetters

  #valida que el campo no este vacio
  if len(catchLetter.get()) >= 2:

    print ("Solo se perimite 1 letra")
    catchLetter.set("")

  else: 

    life-=1

    if life == 0:

      showwarning(title="has perdido", message="Se te han acabado los intentos") 

    alphabet[ord(catchLetter.get())-97].config(text="")

  if catchLetter.get() == "" or catchLetter.get()==" ":
      print("Solo se permiten letras")
      #Reinica el campo
      catchLetter.set("")
      life-=1
      if life == 0:
        showwarning(title="has perdido", message="Se te han acabado los intentos") 
  else:
      #Agregamos las letras usadas a nuestra lista
      triedLetter.append(catchLetter.get())
      #Validamos que nuestras letras esten dentro de la palabra
      if catchLetter.get() in wordSelected:
        #Recorremos la palabra seleccionada letra por letra para comparar con la letra ingresada
        for i in range(len(wordSelected)):
            

            #Comparamos cada letra de la palabra, con la letra ingresada
            if wordSelected[i] == catchLetter.get():
                #Reemplazamos el _ con la letra que corresponde a ese lugar
                screenPlay[i].config(text=catchLetter.get())
                #Prueba de ingreso al condicional
                # print("cambio")
        #Reinica el campo
        catchLetter.set("")
        if correctLetters == len(wordSelected):
          showwarning(title="Felicidades", message="Felicidades has ganado.")
      #Si la letra ingresada no esta, reinicia el campo
      else:
          #Reinica el campo
          catchLetter.set("")

def putLetter():
  x = 50
  y = 180
  count = 0 
  Label(frm, text="Letras sin usar", font=("sans", 20)).place(x=50,y=140)

  
  for i in range(26):
    count+=1
    alphabet[i].place(x=x, y=y)
    x+=30
    if count == 5:
      y+=35
      count = 0
      x = 50
    
    

#Abrimos el archivo txt, y lo listamos en una variable, dandole un salto de liena con \n y 
#converimos todo en minusculas
file = open("palabras.txt", "r")
allWords = list(file.read().split("\n"))
wordSelected = allWords[randint(0, len(allWords)-1)].lower()

#Raiz
root = Tk()
root.config(width=800, height=500, bg="yellow", relief=GROOVE, bd=10)
catchLetter = StringVar()

#Frame
frm = Frame(root)
frm.config(width=800, height=550, relief=SUNKEN, bd=15)
frm.grid_propagate(False)
frm.pack()

#Label
Label(frm, text="Ingresa la letra", font=("verdana", 24)
).grid(row=0, column=0, padx=10, pady=10)
letter = Entry(frm, width=1, font=("verdana", 24), textvariable=catchLetter
).grid(row=0, column=1)

#Button
letterTry = Button(frm, text="Probas", font=("verdana"), bg="yellow", command=catchLetterFunction
).grid(row=1, column=0, padx=10, pady=10)

#Alfabeto imprimido
alphabet = [Label(frm, text=chr(j+97), font=("verdana", 20)) for j in range(26)]
putLetter()

#Dibujo hangman

#Por cada letra en la palabra, crea un _ 
screenPlay = [Label(frm, text="_", font=("verdana",30)) for _ in wordSelected]
initialX=50
for i in range(len(wordSelected)):
    screenPlay[i].place(x=initialX, y=440)
    initialX+=50

root.mainloop()