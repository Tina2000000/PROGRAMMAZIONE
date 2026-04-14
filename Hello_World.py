ora_attuale=int(input('Inserire ora attuale(0-23):'))
ore_attesa=int(input('Tra quante ore deve suonare la sveglia?'))
ora_sveglia=(ora_attuale + ore_attesa) % 24
print(f'La sveglia suonerà alle ore:{ora_sveglia}')