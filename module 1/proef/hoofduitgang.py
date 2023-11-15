
from gevangenis_1 import make_decision_1

def richting_hoofduitgang():
    print("\nJe staat voor het hoofduitgang.")
    print("hij is dicht gesloten.")
    print("Wat ga je doen?")
    print("1. De sleutels gaan zoeken.")
    print("2. De deur proberen te breken.")
    print("3. Keer om en ga een andere uitgangzoeken.")
    choice = input("Typ het nummer van je keuze: ")

    if choice == "1":
        return zoek_sleutels()
    elif choice == "2":
        return deur_breken()
    elif choice == "3":
        return zoek_andere_uigang()
    else:
        print("Ongeldige keuze. Het spel eindigt.")
        return "fail", False
    
def zoek_sleutels():
    print("\je gaat nu de sleutels zoeken.")
    print("Er zijn 3 mogelijke plekken waar de sleutel kan zijn")
    print("waar ga je zoeken?")
    print("1. Het monitor kamer.")
    print("2. Wachters kamer.")
    print("3. om de uitgang.")
    choice = input("Typ het nummer van je keuze: ")

    if choice == "1":
        return monitor_kamer()
    elif choice == "2":
        return wachters_kamer()
    elif choice == "3":
        return om_de_uitgang()
    else:
        print("Ongeldige keuze. Het spel eindigt.")
        return "fail", False

def deur_breken():
    print("Je kon helaas de deur niet breken.")
    print("Er zijn twee kamers naast de uitgang")
    print("welke kamer kies jij?")
    print("1. Linker kamer.")
    print("2. Rechter kamer.")
    print("3. blijven proberen.")
    choice = input("Typ het nummer van je keuze: ")

    if choice == "1":
        return breken_linker_kamer()
    elif choice == "2":
        return breken_rechter_kamer()
    elif choice == "3":
        print("Je kon helaas de deur niet breken.")
        return richting_hoofduitgang()
    else:
        print("Ongeldige keuze. Het spel eindigt.")
        return "fail", False

def zoek_andere_uigang():
    print("\Je bent nu andere uitgang aan het zoeken.")
    print("Er is een aan de achter kan van het gebouw en een in de keuken!")
    print("welke kies je?")
    print("1. uitgang achterkant.")
    print("2. uitgang keuken.")
    choice = input("Typ het nummer van je keuze: ")

    if choice == "1":
        return uitgang_achter()
    elif choice == "2":
        return uitgang_keuken()
    else:
        print("Ongeldige keuze. Het spel eindigt.")
        return "fail", False



def monitor_kamer():
    print("\nEr zijn 3 monitor kamers.")
    print("In welke kamer ga je zoeken?")
    print("1. kamer 1.")
    print("2. kamer 2.")
    print("3. kamer 3.")
    choice = input("Typ het nummer van je keuze: ")

    if choice == "1":
        print("Helaas is de deur van het kamer afgesloten! en je werdt opgepakt door de politie achter jouw!")
        return make_decision_1()
    elif choice == "2":
        print("Helaas is de deur van het kamer afgesloten! en je werdt opgepakt door de politie achter jouw!")
        return make_decision_1()
    elif choice == "3":
        print("Helaas is de deur van het kamer afgesloten! en je werdt opgepakt door de politie achter jouw!")
        return make_decision_1()
    else:
        print("Ongeldige keuze. Het spel eindigt.")
        return "fail", False

def wachters_kamer():
    print("\nEr zijn 2 wachter kamers .")
    print("In welke kamer ga je zoeken?")
    print("1. kamer 1.")
    print("2. kamer 2.")
    choice = input("Typ het nummer van je keuze: ")

    if choice == "1":
        print("Helaas is de deur van het kamer afgesloten! en je werdt opgepakt door de politie achter jouw!")
        return make_decision_1()
    elif choice == "2":
        print("Helaas is de deur van het kamer afgesloten! en je werdt opgepakt door de politie achter jouw!")
        return make_decision_1()
    else:
        print("Ongeldige keuze. Het spel eindigt.")
        return "fail", False

def om_de_uitgang():
    print("\nEr zijn twee kastjes naast de uitgang.")
    print("Welke kastje kies jij?")
    print("1. kastje 1.")
    print("2. kastje 2.")
    choice = input("Typ het nummer van je keuze: ")

    if choice == "1":
        print("Helaas de sleutels zaten niet in! en je werdt opgepakt door de politie achter jouw!")
        return make_decision_1()
    elif choice == "2":
        print("Helaas de sleutels zaten niet in! en je werdt opgepakt door de politie achter jouw!")
        return make_decision_1()
    else:
        print("Ongeldige keuze. Het spel eindigt.")
        return "fail", False



def breken_linker_kamer():
    print("\n je komt 2 deuren tegen.")
    print("Welke deur kies jij?")
    print("1. Linker deur.")
    print("2. Rechter deur.")
    choice = input("Typ het nummer van je keuze: ")

    if choice == "1":
        print("Helaas is de deur afgesloten! en je werdt opgepakt door de politie achter jouw!")
        return make_decision_1()
    elif choice == "2":
        print("Helaas is de deur afgesloten! en je werdt opgepakt door de politie achter jouw!")
        return make_decision_1()
    else:
        print("Ongeldige keuze. Het spel eindigt.")
        return "fail", False

def breken_rechter_kamer():
    print("\nJe komt 2 deuren tegen.")
    print("Welke deur kies jij?")
    print("1. Linker deur.")
    print("2. Rechter deur.")
    choice = input("Typ het nummer van je keuze: ")

    if choice == "1":
        print("Helaas is de deur afgesloten! en je werdt opgepakt door de politie achter jouw!")
        return make_decision_1()
    
    elif choice == "2":
        print("Helaas is de deur afgesloten! en je werdt opgepakt door de politie achter jouw!")
        return make_decision_1()
    else:
        print("Ongeldige keuze. Het spel eindigt.")
        return "fail", False



def uitgang_achter():
    print("\nom naar achter het gebouw te kunnen komen moet je via links of rechts langes het gebouw.")
    print("welke kan kies jij?")
    print("1. lienker kant.")
    print("2. rechter kant.")
    choice = input("Typ het nummer van je keuze: ")

    if choice == "1":
        print("Helaas De politie heeft jouw kunnen vinden en je werdt opgepakt")
        return make_decision_1()
    elif choice == "2":
        print("Helaas de politie heeft jouw kunnen vinden! en je werdt opgepakt!")
        return make_decision_1()
    else:
        print("Ongeldige keuze. Het spel eindigt.")
        return "fail", False

def uitgang_keuken():
    print("\nom naar de keuken te kunnen komen moet via gang nummer 4 of gang nummer 6 .")
    print("Welke gang kies jij?")
    print("1. gang 4.")
    print("2. gang 6.")
    choice = input("Typ het nummer van je keuze: ")

    if choice == "1":
        print("Helaas er was een agent in de winkel! en je werdt opgepakt door hem!")
        return make_decision_1()
    elif choice == "2":
        print("Helaas is de deur afgesloten! en je werd opgepakt door de politie achter jouw!")
        return make_decision_1()
    else:
        print("Ongeldige keuze. Het spel eindigt.")
        return "fail", False