#ESERCIZIO 1 punto 1
def is_pari(n):
   '''controllo se il numero è pari'''

   if n%2 == 0:
      return True
   else:
      return False



#ESERCIZIO 1 punto 2
def chiedi_numero_positivo():
    while True:
        '''crea ciclo infinito che si interrompe con return'''
        try:
            numero = int(input("Inserire un numero intero positivo"))
            if numero > 0:
             '''verifico che il numero sia maggiore di 0'''
             return numero
            else:
                print("Errore : il numero deve essere maggiore di zero")
        except ValueError :
            print("Inserire un numero intero valido")
            
n = chiedi_numero_positivo()
print("Hai inserito:", n)

#ESERCIZIO 1 punto 3
def genera_lista(n):
    '''genera lista da n'''
    risultato = [n]
    while n != 1 and len(risultato) < 100:
         if n%2 == 0:
            n = n//2
         else:
            n = (n*3)+1
        
         risultato.append(n)
    return risultato

lista = genera_lista(n)
print('Sequenza:',lista)


# ESERCIZIO 1 punto 4

def analizza_sequenza(lista):
    risultato = genera_lista(n)
    massimo = max(risultato)
    lunghezza = len(risultato)
    somma = sum(risultato)
    return massimo, lunghezza, somma

max_val, lung, totale = analizza_sequenza(lista)

print(f"'Valore massimo:',{max_val}")
print(f"'Lunghezza lista:',{lung}")
print(f"'Somma dei valori nella lista:',{totale}")

def ricerca(lista):
    divisibili_per_5 = [x for x in lista if x % 5 == 0]
    if divisibili_per_5:
       print( f"{divisibili_per_5}")
    else:
        print('Nessun numero divisibile per 5')

ricerca(lista)
 