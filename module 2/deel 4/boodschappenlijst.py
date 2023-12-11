# Importeer de nodige modules
import re

# Definieer een functie om een item toe te voegen aan de lijst
def voeg_item_toe(lijst, item):
    # Splits het item op in zijn twee delen
    wat, hoeveel = item.strip().split("x")

    # Vervang alle hoofdletters door kleine letters
    wat = wat.lower()

    # Controleer of het item al in de lijst staat
    if wat in lijst:
        # Zoek het item in de lijst
        voorkomen = lijst.index(wat)

        # Tel de hoeveelheid bij
        lijst[voorkomen] = str(int(lijst[voorkomen]) + int(hoeveel))

    # Voeg het item toe aan de lijst
    else:
        lijst.append(item)

# Start het programma
lijst = []

# Vraag de gebruiker om items toe te voegen
while True:
    item = input("Wat wil je toevoegen aan je boodschappenlijst? ('Stop' om te stoppen): ")

    # Controleer of de gebruiker wil stoppen
    if item.lower() == "stop":
        break


    voeg_item_toe(lijst, item)

# Toon de lijst
print("[BOODSCHAPPENLIJST]")

if not lijst:
    print("Je boodschappenlijst is leeg.")
else:
    for item in lijst:
        print(item)

