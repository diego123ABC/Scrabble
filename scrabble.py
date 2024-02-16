'''
Implementare una prima versione testuale del gioco Scrabble: vengono assegnate all'utente 8 lettere scelte casualmente dal "sacchetto" virtuale che
le contiene nella quantità specificata nella tabella allegata.
L'utente deve proporre una parola con le lettere a disposizione. Il programma verificherà che la parola possa essere composta con le lettere a
disposizione dell'utente e che questa sia presente all'interno del file dizionario con le parole della lingua italiana. In caso affermativo,
si calcolerà il punteggio ottenuto dall'utente sempre in base alla tabella allegata.
'''

import random

# Definizione del dizionario delle lettere con quantità e punteggio
lettere = {
    'A': {'quantità': 14, 'punteggio': 1},
    'B': {'quantità': 3, 'punteggio': 5},
    'C': {'quantità': 6, 'punteggio': 2},
    'D': {'quantità': 3, 'punteggio': 5},
    'E': {'quantità': 11, 'punteggio': 1},
    'F': {'quantità': 3, 'punteggio': 5},
    'G': {'quantità': 2, 'punteggio': 8},
    'H': {'quantità': 2, 'punteggio': 8},
    'I': {'quantità': 12, 'punteggio': 1},
    'L': {'quantità': 5, 'punteggio': 3},
    'M': {'quantità': 5, 'punteggio': 3},
    'N': {'quantità': 5, 'punteggio': 3},
    'O': {'quantità': 5, 'punteggio': 1},
    'P': {'quantità': 3, 'punteggio': 5},
    'Q': {'quantità': 1, 'punteggio': 10},
    'R': {'quantità': 6, 'punteggio': 2},
    'S': {'quantità': 6, 'punteggio': 2},
    'T': {'quantità': 6, 'punteggio': 2},
    'U': {'quantità': 5, 'punteggio': 3},
    'V': {'quantità': 3, 'punteggio': 5},
    'Z': {'quantità': 2, 'punteggio': 8}
}

def estrazione_lettere():
    lista_lettere = [] #lista con tutte lettere nella relativa quantità
    lettere_estratte = [] #8 lettere estratte

    for lettera, info in lettere.items():
        lista_lettere.extend([lettera] * info['quantità'])
    random.shuffle(lista_lettere)

    while len(lettere_estratte) < 8:
        lettera_estratta = random.choice(lista_lettere) #estraggo una lettera casuale
        if lettere[lettera_estratta]['quantità'] > 0:
            lettere_estratte.append(lettera_estratta)
            lettere[lettera_estratta]['quantità'] -= 1
    return lettere_estratte


def verifica_parola(parola, lettere_estratte):
    for lett in parola:
        if lett not in lettere_estratte:
            return False

    for lett in parola: #controllo per le doppie lettere non valide nonostante la lettera sia estratta
        if parola.count(lett) > lettere_estratte.count(lett):
            return False
    return True

def verifica_italiana(parola):
    with open("60000_parole_italiane.txt", "r") as file: #chiude automaticamente il file
        for linea in file:
            if parola.strip().lower() == linea.strip().lower(): #strip rimuove tutti gli eventuali spazi
                return True
    return False

def calcola_punteggio(parola):
    punteggio=0
    for lett in parola:
        punteggio+=lettere[lett]['punteggio']
    return punteggio

def fine_gioco():
    fine = True

    for lett in lettere:
        if lettere[lett]['quantità'] != 0:
            fine = False

    return fine



punteggio_totale = 0
valida = True

while True:
    if(valida):
        lettere_estratte = estrazione_lettere() #aggiorno le lettere estratte solo se precedentemente è stata inserito una parola valida

    print(lettere_estratte)

    parola = input("Inserisci una parola: ").upper()
    if (verifica_parola(parola, lettere_estratte) and verifica_italiana(
            parola)):
        punteggio_totale += calcola_punteggio(parola)
        print("Il tuo punteggio è:", punteggio_totale)
        valida = True
    else:
        print("Parola non valida")
        valida = False

    if(fine_gioco()): #esco se sono finite tutte le lettere nel sacchetto
        break




