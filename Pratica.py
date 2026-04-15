def fattoriale(n):
    if n < 0:
        return 'Insert n > 0'
    if n == 0 or n == 1:
        return 1
    else:
        t = n * fattoriale(n-1)
        return t

risultato = fattoriale(3)
print(risultato)

