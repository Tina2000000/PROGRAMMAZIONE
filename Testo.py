testo = '''
Day after day, day after day,
We stuck, nor breath nor motion;
As idle as a painted ship
Upon a painted ocean.
'''

'''file_testo = open('testo.txt', 'w')

# Loop sulle righe che compongono la stringa multilinea
for riga in testo.split('\n'):     
    # Scrivo la riga nel file (ricordandomi di andare a capo con \n)
    file_testo.write(f'{riga}\n')   

# chiudo il file a fine operazioni
file_testo.close()

# Apro file in lettura
file_testo = open('testo.txt', 'r')   

# Leggo l'intero contenuto del file
contenuto = file_testo.readlines()                   

# Chiudo il file
file_testo.close()                              

# visualizzo il contenuto letto dal file
print(contenuto)

# visualizzo il tipo del contenuto letto
print(type(contenuto))'''
# oggetto da scrvere, ad esempio le soluzioni del problema regine
lista_numeri = [3, 6, 2, 7, 1, 4, 0]

# Apro un file binario in scrittura
binary_file = open('lista_numeri.bin', 'w') 

# Converto l'oggetto da scrivere in un gruppo di bytes
lista_numeri_bytes = bytearray(lista_numeri)

# Scrivo il gruppo di bytes nel file
binary_file.write(lista_numeri_bytes)           

# Chiudo il file
binary_file.close()