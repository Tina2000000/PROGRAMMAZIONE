'''
a=input('qualcosa?)
print(a)
'''
'''


#
# File: HelloWorld.py
#
# Author: V.Zanotto
#
# Date: 2026/03/03
#
# Version: 1.0
#
# Description: My First Project Program to print "Hello, World!".
#


print('Hello, World')
'''
import turtle               # Importo modulo turtle

window = turtle.Screen()    # Creo una finestra dove lavorare
raffaello = turtle.Turtle() # Creo una tartaruga e la assegno alla variabile "raffaello"


#for i in range(4):

for i in ['red', 'blue', 'violet', 'orange']:
               raffaello.color(i)      #Assegno un colore a raffaello  
               raffaello.forward(50)       # Dico a "raffaello" di andare avanti di 50 passi
               raffaello.left(90)          # Dico a "raffaello" di girare a sinistra di 90 gradi

leonardo = turtle.Turtle()
leonardo.color('blue')
leonardo.forward(50)
leonardo.left(120)         #Non 60, ma 120 poichè per la tartaruga andare avanti in orizzontale è uguale a 0 gradi
leonardo.forward(50)
leonardo.left(120)
leonardo.forward(50)
leonardo.left(60)

window.mainloop()           # Attende che l'utente chiuda la finestra di gioco o fermi il programma