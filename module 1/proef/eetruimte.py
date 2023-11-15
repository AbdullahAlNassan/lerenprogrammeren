from gevangenis_1 import make_decision_1

def richting_ruimte():
    print("Je bent de eetruimte binnen gekomen.")
    print("Wat is je volgende stap??")
    print("1. onder de tafel gaan verstoppen.")
    print("2. blijven rennen naar een andere ruimte of kamer.")
    print("3. je zelf uit het dichtste raam gooien.")
    choice = input("Typ het nummer van je keuze: ")

    if choice == "1":
        return volg_de_tunnel()
    elif choice == "2":
        return blijven_rennen()
    elif choice == "3":
        return vanuit_raam()
    else:
        print("Ongeldige keuze. Het spel eindigt.")
        return "fail", False
    
def volg_de_tunnel():
    print("\Heyy!!, je hebt een tunnel gevonden. je gaan de tunnel volgen.")
    print("de put is blijkbaar lang en heeft 3 richtingen")
    print("welke richting kies jij?")
    print("1. Links.")
    print("2. Rechts.")
    print("3. Rechtdoor.")
    choice = input("Typ het nummer van je keuze: ")

    if choice == "1":
        return tunnel_links()
    elif choice == "2":
        return tunnel_rechts()
    elif choice == "3":
        return tunnel_rechtdoor()
    else:
        print("Ongeldige keuze. Het spel eindigt.")
        return "fail", False

def blijven_rennen():
    print("\Je komt twee deuren tegen.")
    print("welke deur kies jij?")
    print("1. Linker deur.")
    print("2. Rechter deur.")
    print("3. terug keren.")
    choice = input("Typ het nummer van je keuze: ")

    if choice == "1":
        return rennen_linker_deur()
    elif choice == "2":
        return rennen_rechter_deur()
    elif choice == "3":
        return richting_ruimte()
    else:
        print("Ongeldige keuze. Het spel eindigt.")
        return "fail", False

def vanuit_raam():
    print("\Je bent nu uit de gavangenis.")
    print("Het is 's nachts en er is overal bomen. je bent in een bos!")
    print("wat ga je doen?")
    print("1. In de top van een bomen gaan verstoppen.")
    print("2. Blijven weg rennen.")
    choice = input("Typ het nummer van je keuze: ")

    if choice == "1":
        return raam_top_boom()
    elif choice == "2":
        return raam_rennen()
    else:
        print("Ongeldige keuze. Het spel eindigt.")
        return "fail", False



def tunnel_links():
    print("\nJe komt weer 3 richtingen tegen.")
    print("Welke richting kies jij?")
    print("1. Links.")
    print("2. Rechts.")
    print("3. Rechtdoor.")
    choice = input("Typ het nummer van je keuze: ")

    if choice == "1":
        print("Helaas is de tunnel vanuit dit richting afgesloten! en je werdt opgepakt door de politie achter jouw!")
        return make_decision_1()
    elif choice == "2":
        print("Helaas is de tunnel vanuit dit richting afgesloten! en je werdt opgepakt door de politie achter jouw!")
        return make_decision_1()
    elif choice == "3":
        print("Helaas is de tunnel vanuit dit richting afgesloten! en je werdt opgepakt door de politie achter jouw!")
        return make_decision_1()
    else:
        print("Ongeldige keuze. Het spel eindigt.")
        return "fail", False

def tunnel_rechts():
    print("\nJe komt weer 2 richtingen tegen.")
    print("Welke richting kies jij?")
    print("1. Links.")
    print("2. Rechts.")
    choice = input("Typ het nummer van je keuze: ")

    if choice == "1":
        print("Helaas is de tunnel vanuit dit richting afgesloten! en je werdt opgepakt door de politie achter jouw!")
        return make_decision_1()
    elif choice == "2":
        print("Helaas is de tunnel vanuit dit richting afgesloten! en je werdt opgepakt door de politie achter jouw!")
        return make_decision_1()
    else:
        print("Ongeldige keuze. Het spel eindigt.")
        return "fail", False

def tunnel_rechtdoor():
    print("\nJe komt weer 3 richtingen tegen.")
    print("Welke richting kies jij?")
    print("1. Links.")
    print("2. Rechts.")
    print("3. Rechtdoor.")
    choice = input("Typ het nummer van je keuze: ")

    if choice == "1":
        print("Helaas is de tunnel vanuit dit richting afgesloten! en je werdt opgepakt door de politie achter jouw!")
        return make_decision_1()
    elif choice == "2":
        print("Helaas is de tunnel vanuit dit richting afgesloten! en je werdt opgepakt door de politie achter jouw!")
        return make_decision_1()
    elif choice == "3":
        print("Helaas is de tunnel vanuit dit richting afgesloten! en je werdt opgepakt door de politie achter jouw!")
        return make_decision_1()
    else:
        print("Ongeldige keuze. Het spel eindigt.")
        return "fail", False



def rennen_linker_deur():
    print("\nJe komt weer 2 deuren tegen.")
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

def rennen_rechter_deur():
    print("\nJe komt weer 2 deuren tegen.")
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



def raam_top_boom():
    print("\nje zit geen poltie meer om je heen.")
    print("Wat doe je?")
    print("1. van de boom uit springen en door met wegrennen.")
    print("2. Blijven nog langer zitten.")
    choice = input("Typ het nummer van je keuze: ")

    if choice == "1":
        print("Helaas je hebt je he voet gebroken tijdens springen! en je werdt opgepakt door de politie")
        return make_decision_1()
    elif choice == "2":
        print("Helaas de politie heeft jouw kunnen vinden! en je werdt opgepakt!")
        return make_decision_1()
    else:
        print("Ongeldige keuze. Het spel eindigt.")
        return "fail", False

def raam_rennen():
    print("\nJe komt twee winkels tegen.")
    print("Welke winkel kies jij?")
    print("1. Linker winkel.")
    print("2. Rechter winkel.")
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