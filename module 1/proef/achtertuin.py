from gevangenis_1 import make_decision

def make_decision_1():
    print("Helaas, je hebt het spel verloren!")
    print("Wil je het verlies accepteren of opnieuw beginnen?.")
    print("1. Accepteren.")
    print("2. opnieuw beginnen.")
    choice = input("Typ het nummer van je keuze: ")

    if choice == "1":
        return make_decision()
    elif choice == "2":
        return make_decision()
    elif choice == "3":
        return make_decision()
    else:
        print("Ongeldige keuze. Het spel eindigt.")
        return "fail", False



