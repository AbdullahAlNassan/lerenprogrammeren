import random
from gevangenis_2 import make_decision_1

def intro():
    print("Welkom in BE FREE!")
    print("Je Ontsnapte uit de gevangenis. Ren nu weg van de de politie. Als je wordt opgepakt word je in een andere gevangenis opgesloten en moet je weer proberen te ontsnappen.")

def make_decision():
    print("Je ontsnapte uit de cel.")
    print("Welke richting ga je?")
    print("1. Richting de eetruimte.")
    print("2. Richting de Hoofduitgang.")
    print("3. Richting de achtertuin.")
    return input("Typ het nummer van je keuze: ")

def process_action(decision):
    if decision == "1":
        return richting_ruimte()
    elif decision == "2":
        return richting_hoofduitgang()
    elif decision == "3":
        return richting_achtertuin()
    else:
        print("Ongeldige keuze. Het spel eindigt.")
        return "fail", False

def richting_ruimte():
    print("\nJe bent de eetruimte binnen gekomen.")
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























def richting_hoofduitgang():
    print("\nJe staat voor het hoofduitgang.")
    print("hij is dicht gesloten.")
    print("Wat ga je doen?")
    print("1. De sleutels gaan zoeken.")
    print("2. De deur proberen te breken.")
    print("3. Keer om en ga een andere uitgangzoeken.")
    choice = input("Typ het nummer van je keuze: ")

    if choice == "1":
        return follow_left_path()
    elif choice == "2":
        return follow_right_path()
    elif choice == "3":
        return return_to_temple()
    else:
        print("Ongeldige keuze. Het spel eindigt.")
        return "fail", False

def follow_left_path():
    print("\nJe volgt het pad naar links en komt bij een rivier.")
    print("Wat ga je doen?")
    print("1. Bouw een vlot om de rivier over te steken.")
    print("2. Zoek naar een brug in de buurt.")
    print("3. Keer terug naar het kruispunt.")
    choice = input("Typ het nummer van je keuze: ")

    if choice == "1":
        return build_raft()
    elif choice == "2":
        return search_for_bridge()
    elif choice == "3":
        print("Je keert terug naar het kruispunt en kiest een andere route.")
        return "continue", False
    else:
        print("Ongeldige keuze. Het spel eindigt.")
        return "fail", False

def build_raft():
    print("\nGefeliciteerd, je bouwt een vlot en steekt veilig de rivier over. Ga verder.")
    return "continue", False

def search_for_bridge():
    print("\nHelaas, er is geen brug in de buurt. Je hebt het spel verloren.")
    return "fail", False

def follow_right_path():
    print("\nJe volgt het pad naar rechts en komt bij een verlaten dorp.")
    print("Wat ga je doen?")
    print("1. Doorzoek de huizen op aanwijzingen.")
    print("2. Rust uit in het dorp.")
    print("3. Ga verder naar de heuvels achter het dorp.")
    choice = input("Typ het nummer van je keuze: ")

    if choice == "1":
        return search_houses()
    elif choice == "2":
        return rest_in_village()
    elif choice == "3":
        return hills_behind_village()
    else:
        print("Ongeldige keuze. Het spel eindigt.")
        return "fail", False

def search_houses():
    print("\nGefeliciteerd, je vindt een kaart met de locatie van de verloren stad. Ga verder.")
    return "continue", False

def rest_in_village():
    print("\nHelaas, je wordt overvallen door bandieten terwijl je rust. Je hebt het spel verloren.")
    return "fail", False

def hills_behind_village():
    print("\nJe gaat verder naar de heuvels en ontdekt een geheime doorgang. Ga verder.")
    return "continue", False

def return_to_temple():
    print("\nJe keert terug naar de tempel en kiest een andere route.")
    return "continue", False

def richting_achtertuin():
    print("\nJe besluit een andere route te zoeken rondom de tempel.")
    print("Je komt een oude brug tegen.")
    print("Wat ga je doen?")
    print("1. Steek de brug over.")
    print("2. Zoek een andere route langs de rivier.")
    choice = input("Typ het nummer van je keuze: ")

    if choice == "1":
        print("Gefeliciteerd, je steekt de brug over en vindt een verloren schat. Je wint!")
        return "win", True
    elif choice == "2":
        print("Helaas, de rivier is te wild en gevaarlijk om langs te gaan. Je hebt het spel verloren.")
        return "fail", False
    else:
        print("Ongeldige keuze. Het spel eindigt.")
        return "fail", False