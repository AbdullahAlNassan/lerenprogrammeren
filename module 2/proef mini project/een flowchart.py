import random

unique_values = set()

while True:
    user_input = input("Voer een naam in: ")

    if user_input in unique_values:
        print("Waarde is niet uniek. Probeer het opnieuw.")
    else:
        unique_values.add(user_input)
    
    if user_input < 3:
        meer_namen = input("Wil je meer namen toevoegen? (ja of nee) ")
        if meer_namen.lower() == "nee":
            break

deelnemers = list(unique_values)  # Maak een lijst van unieke waarden
random.shuffle(deelnemers)  # Schud de lijst met deelnemers

lootjes = list(deelnemers)  # Maak een kopie van de deelnemerslijst voor lootjes
random.shuffle(lootjes)  # Schud de lijst met lootjes

niemand_heeft_zijn_eigen_lootje = True
for i in range(len(deelnemers)):
    if deelnemers[i] == lootjes[i]:
        niemand_heeft_zijn_eigen_lootje = False
        break

if niemand_heeft_zijn_eigen_lootje:
    for i in range(len(deelnemers)):
        print(f"{deelnemers[i]} koopt voor: {lootjes[i]}")
else:
    print("Er is een probleem met het verdelen van de lootjes. Probeer het opnieuw.")
