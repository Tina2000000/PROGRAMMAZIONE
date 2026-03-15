'''import turtle

def draw_square(tartaruga, pippo):
  for i in range(4):
   tartaruga.forward(pippo)                  # movimenti per disegnare quadrato
   tartaruga.left(90)                     # con raffaello
def draw_triangle(tartaruga):
  for i in range(3):
   tartaruga.forward(80)                  # movimenti per disegnare un triangolo
   tartaruga.left(120)                    # con donatello
   
def somma (a,b):
   risultato = a + b
   return risultato
#######################################
 
result = somma (3,4)
print(result)

window = turtle.Screen()               # istanza "window" di Screen
window.bgcolor("lightgreen")           # imposto lo stato della "window"
# window.title("Raffaello & Donatello")

raffaello = turtle.Turtle()            # Istanza di Turtle chiamata raffaello
raffaello.color("red")                 # attributi per lo stato di raffaello    
raffaello.pensize(5)

draw_square(raffaello, 50)
  
raffaello.right(180)                   # giro e sposto dall'origine raffaello
raffaello.forward(80)                  # 


donatello = turtle.Turtle()            # Istanza di Turtle chiamata donatello
donatello.color("violet")              # attributi per lo stato di donatello

draw_triangle(donatello)
donatello.forward(80)                  # movimenti per disegnare un triangolo
donatello.left(120)                    # con donatello

draw_square(donatello, 20)
            

#draw_square(donatello)

window.mainloop()                      # Attendo chiusura finestra di gioco o stop del programma
'''