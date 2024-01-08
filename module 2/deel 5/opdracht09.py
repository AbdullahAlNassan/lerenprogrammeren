from fruitmand import fruitmand

fruitmand = [fruit for fruit in fruitmand
             if fruit['name'] != 'druif']

uniek_kleur = set(fruit['color'] for fruit in fruitmand)

for color in uniek_kleur:
    print(color)