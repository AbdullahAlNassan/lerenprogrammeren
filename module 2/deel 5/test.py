from fruitmand import fruitmand

rounds = 0

for fruit in fruitmand:
    gekozen_kleur = input(f"Choose a color for {fruit}: ")
    if gekozen_kleur in fruit["color"]:
        rounds += 1

print(f"Total rounds with matching colors: {rounds}")