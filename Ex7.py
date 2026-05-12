#ESERCIZIO 7, creare un programma per giocare con le tabelline
#Punto 1: creare un generatore che generi una tabellina
def generatore_tabellina(numero):
    
    n = 0
    # loop infinitino per non fermarmi al 10
    while True:
        
        yield n*numero
        n = n + 1
num = int(input('Con che numero desideri giocare?'))
numero_intero=int(num)

print(f'Giocheremo con il numero' (numero_intero))
g = generatore_tabellina(numero_intero)
numero_tabellina = next(g)

continua = True
while continua:
    
    guess = input(f'Il numero attuale è' (numero_tabellina). 'Qual è il prossimo numero?')
    numero_tabellina = next(g)

    if guess = 'FINE':
        continua = False
numero_tabellina = next(g)

if numero_tabellina = next(g):
   print('Hai indovinato!')
else:
    print(riprova)
     





print('Esci dal gioco')

