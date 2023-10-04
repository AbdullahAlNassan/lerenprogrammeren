croissant = 0.39
stokbrood = 2.78
kortingsbon = 0.50

AANTAL_CROISSANT = 17
AANTAL_STOKBROOD = 2
AANTAL_KORTINGSBON = 3

croissant_kost = croissant * AANTAL_CROISSANT
stokbrood_kost = stokbrood * AANTAL_STOKBROOD
kortingsbon_kost = kortingsbon * AANTAL_KORTINGSBON

totaal = croissant_kost + stokbrood_kost - kortingsbon_kost

print(totaal)


