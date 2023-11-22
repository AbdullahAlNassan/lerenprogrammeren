kleuren = ('oranje', 'blauw', 'groen', 'bruin')

aantal_MMs = int(input("Hoeveel M&M's wil je aan de zak toevoegen? "))

def vul_zak_met_MMs(aantal):
    index = 0
    zak = []
    for _ in range(aantal):
        zak.append(kleuren[index])
        index = (index + 1) % len(kleuren)
    return zak

zak_met_MMs = vul_zak_met_MMs(aantal_MMs)

print("Inhoud van de zak met M&M's:")
print(zak_met_MMs)
