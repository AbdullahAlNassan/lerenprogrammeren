#to do specefiek fout

PIZZA_GROOT = 12.50
PIZZA_MEDIUM = 10.50
PIZZA_KLEIN = 8.50

aantal_klein = 0
aantal_medium = 0
aantal_groot = 0

try:
    aantal_groot = int(input("Hoeveel groot pizza's wilt u bestellen?"))
except ValueError:
    print("Ongeldige invoer. Voer a.u.b. geldige gehele getallen in voor het aantal pizza's.")

try:
    aantal_medium = int(input("Hoeveel medium pizza's wilt u bestellen?"))
except ValueError:
    print("Ongeldige invoer. Voer a.u.b. geldige gehele getallen in voor het aantal pizza's.")
    
try:
    aantal_klein = int(input("Hoeveel klein pizza's wilt u bestellen?"))
except ValueError:
    print("Ongeldige invoer. Voer a.u.b. geldige gehele getallen in voor het aantal pizza's.")
    
kosten_groot = aantal_groot * PIZZA_GROOT
kosten_medium = aantal_medium * PIZZA_MEDIUM
kosten_klein = aantal_klein * PIZZA_KLEIN
totaal_kosten = kosten_groot + kosten_medium + kosten_klein

print("-----uw bestelling-----")
print(f"{aantal_groot} x groot pizza's: € {kosten_groot}")
print(f"{aantal_medium} x medium pizza's: € {kosten_medium}")
print(f"{aantal_klein} x klein pizza's: € {kosten_klein}")
print('-----------------------')
print(f"totaal prijs: € {totaal_kosten}")
