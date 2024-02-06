import random

deelnemers = []

while True:

    deelneemer = input("voer een naam in:")

    if deelneemer in deelnemers:
        print("waarde is niet uniek. probeer het opnieuw")
    
    else:
        deelnemers.append(deelneemer)
        print("naam scussesvol toegevoegd")

    if len(deelnemers) >= 3:
        meer_namen = input("wil je meer namen toevoegen? (ja of nee)")

        if meer_namen == 'nee':
            break

lootjes = deelnemers[1:] + deelnemers[:1]

for i in range(len(deelnemers)):
    print(f"{deelnemers[i]} koopt voor: {lootjes[i]}")