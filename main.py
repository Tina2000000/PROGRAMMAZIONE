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
    lista = [n]
    while n != 1 and len(lista) < 100:
         if n%2 == 0:
            n = n//2
         else:
            n = (n*3)+1
        
         lista.append(n)
    return lista

risultato = genera_lista(n)
print('Sequenza:',risultato)


# ESERCIZIO 1 punto 4

def analizza_sequenza(lista)

     