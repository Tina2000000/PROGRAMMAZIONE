# Esercizio 8
#Autore:
#Data:



import random

def gioco_impiccato():
    # Lista di parole possibili
    lista_parole = ["python", "programmazione", "computer", "sviluppatore", "algoritmo", "funzione"]
    
    # Scelta casuale della parola segreta
    parola_segreta = random.choice(lista_parole).lower()
    
    # Set per tenere traccia delle lettere indovinate e di quelle tentate
    lettere_indovinate = set()
    lettere_tentate = set()
    
    # Numero massimo di errori consentiti
    tentativi_rimasti = 6
    
    print("--- BENVENUTO AL GIOCO DELL'IMPICCATO! ---")
    
    while tentativi_rimasti > 0:
        # Mostra lo stato corrente della parola (es. p _ t h o _ )
        parola_visualizzata = [lettera if lettera in lettere_indovinate else "_" for lettera in parola_segreta]
        print("\nParola da indovinare: " + " ".join(parola_visualizzata))
        print(f"Tentativi rimasti: {tentativi_rimasti}")
        if lettere_tentate:
            print(f"Lettere già provate: {', '.join(sorted(lettere_tentate))}")
        
        # Controllo vittoria: se non ci sono più "_" la parola è stata indovinata
        if "_" not in parola_visualizzata:
            print(f"\nComplimenti! Hai indovinato la parola: '{parola_segreta}'! 🎉")
            return

        # Input dell'utente
        tentativo = input("Inserisci una lettera: ").lower().strip()
        
        # Validazione dell'input
        if len(tentativo) != 1 or not tentativo.isalpha():
            print("Per favore, inserisci una sola lettera valida.")
            continue
            
        if tentativo in lettere_tentate:
            print("Hai già provato questa lettera. Scegline un'altra!")
            continue
            
        # Aggiunge la lettera all'elenco delle provate
        lettere_tentate.add(tentativo)
        
        # Verifica se la lettera è nella parola
        if tentativo in parola_segreta:
            print(f"Ottimo! La lettera '{tentativo}' è presente.")
            lettere_indovinate.add(tentativo)
        else:
            print(f"Peccato! La lettera '{tentativo}' non è presente.")
            tentativi_rimasti -= 1
        
        try:
        indice = lettere_indovinate.index(tentativo)
        except ValueError:
            print(f"Hai giè provato la lettera"(tentativo)".")
            
    # Se i tentativi finiscono, il giocatore perde
    print(f"\nGame Over! Hai esaurito i tentativi. La parola era: '{parola_segreta}'. 😢")


print(gioco_impiccato())