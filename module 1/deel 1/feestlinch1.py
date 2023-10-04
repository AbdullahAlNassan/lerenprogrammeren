croissant = 0.39
stokbrood = 2.78
kortingsbon = 0.50

aantal_croissant = 17
aantal_stokbrood = 2
aantal_kortingsbon = 3

croissant_kost = croissant * aantal_croissant
stokbrood_kost = stokbrood * aantal_stokbrood
kortingsbon_kost = kortingsbon * aantal_kortingsbon

totaal = croissant_kost + stokbrood_kost - kortingsbon_kost

print(f'De feestlunch kost je bij de bakker {totaal} euro voor de {aantal_croissant} croissantjes en de {aantal_stokbrood} stokbroden als de {aantal_kortingsbon} kortingsbonnen nog geldig zijn!')
