#ESERCIZIO 1 punto 1
def is_pari(n):
   '''controllo se il numero è pari'''

   if n%2 == 0:
      return True
   else:
      return False


result = is_pari(4)
print(result)
result = is_pari(5)
print(result)