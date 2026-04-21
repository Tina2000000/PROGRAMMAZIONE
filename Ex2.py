testo = '''
Day after day, day after day,
We stuck, nor breath nor motion;
As idle as a painted ship
Upon a painted ocean.

Water, water, every where,
And all the boards did shrink;
Water, water, every where,
Nor any drop to drink.

The very deep did rot: O Christ!
That ever this should be!
Yea, slimy things did crawl with legs
Upon the slimy sea.

About, about, in reel and rout
The death-fires danced at night;
The water, like a witch's oils,
Burnt green, and blue and white.
'''
# Risolvendo parte 1 esercizio 2:
lista_righe = testo.split('\n')

contatore_0 = 0
for riga in lista_righe:
    if len(riga) > 0:
        contatore_0 = contatore_0 + 1

print(contatore_0)

# Risolvendo parte 2 esercizio 2

lista_parole = testo.split()

contatore_1= 0
for parola in lista_parole:
    if len(parola) > 0:
        contatore_1= contatore_1 + 1

print(contatore_1)



# Risolvendo parte 3 esercizio 2



alfabeto_numeri = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

contatore_2 = 0
for carattere in testo:
    if carattere in alfabeto_numeri:
       contatore_2 = contatore_2 + 1

print(contatore_2)

# Risolvendo parte 4 esercizio 2

def chiedi_lettera()
    while True:
    "Crea ciclo infinito che si interrompe con return"
          try lettera = str(input("Quale lettera vuoi contare?")):
            if len(lettera) = 1:
               if lettera in testo:
                  contatore_3 = 0
                  for lettera in testo:
                  contatore_3 = contatore_3 + 1
                  return contatore_3
                else:
                    print("La lettera non compare nel testo")
            else:
                print("")




