def richting_achtertuin():
    print("\n je hebt achtertuin bereikt en ziet bewakers.")
    print("Wat ga je doen?")
    print("1. in de schaduwen verbergen en wachten to de bewakers weg zijn.")
    print("2. een steen gooien om de bewakers af te leiden.")
    choice = input("Typ het nummer van je keuze: ")

    if choice == "1":
        return achtertuin_in_schaduwen()
    elif choice == "2":
        return achtertuin_steen_gooien()
    else:
        print("Ongeldige keuze. Het spel eindigt.")
        return "fail", False
    
def achtertuin_in_schaduwen():
    print("\De bewakers zijn weg.")
    print("bent nu bij het hek van de achtertuin ")
    print("wat ga je doen?")
    print("1. Klim over het hek.")
    print("2. Zoek naar een zwakke plek in het hek om doorheen te kruipen.")
    choice = input("Typ het nummer van je keuze: ")

    if choice == "1":
        return schaduw_klimen()
    elif choice == "2":
        return schaduw_zwakplek()
    else:
        print("Ongeldige keuze. Het spel eindigt.")
        return "fail", False

def achtertuin_steen_gooien():
    print("Je bent buiten de gevangenismuren, maar er is een bos dat je moet doorkruisen.")
    print("Wat ga je doen?")
    print("1. Volg het pad door het bos om snelheid te behouden.")
    print("2. Baan je een weg door het dichte bos om uit het zicht te blijven.")
    choice = input("Typ het nummer van je keuze: ")

    if choice == "1":
        return steen_honden()
    elif choice == "2":
        return steen_honden()
    else:
        print("Ongeldige keuze. Het spel eindigt.")
        return "fail", False


def schaduw_klimen():
    print("\nJe bent buiten de gevangenismuren, maar er is een bos dat je moet doorkruisen.")
    print("wat ga je doen?")
    print("1. Volg het pad door het bos om snelheid te behouden.")
    print("2. Baan je een weg door het dichte bos om uit het zicht te blijven.")
    choice = input("Typ het nummer van je keuze: ")

    if choice == "1":
        return steen_honden()
    elif choice == "2":
        return steen_honden()
    else:
        print("Ongeldige keuze. Het spel eindigt.")
        return "fail", False

def schaduw_zwakplek():
    print("\nJe bent buiten de gevangenismuren, maar er is een bos dat je moet doorkruisen.")
    print("wat ga je doen?")
    print("1. Volg het pad door het bos om snelheid te behouden.")
    print("2. Baan je een weg door het dichte bos om uit het zicht te blijven.")
    choice = input("Typ het nummer van je keuze: ")

    if choice == "1":
        return steen_honden()
    elif choice == "2":
        return steen_honden()
    else:
        print("Ongeldige keuze. Het spel eindigt.")
        return "fail", False




def steen_honden():
    print("\n Je hoort het geluid van honden in de verte en realiseert je dat je gevolgd wordt.")
    print("Wat doe je?")
    print("1. Versnel je tempo om de afstand te vergroten..")
    print("2. Zoek naar een rivier om je geurspoor te verbergen.")
    choice = input("Typ het nummer van je keuze: ")

    if choice == "1":
        return verlaten_hut()
    elif choice == "2":
        return verlaten_hut()
    else:
        print("Ongeldige keuze. Het spel eindigt.")
        return "fail", False


def verlaten_hut():
    print("\n Je hebt de honden afgeleidt en komt aan bij een verlaten hut.")
    print("Wat doe je?")
    print("1. Doorzoek de hut op zoek naar voedsel en een schuilplaats.")
    print("2. Ga snel voorbij de hut om geen risico te nemen.")
    choice = input("Typ het nummer van je keuze: ")

    if choice == "1":
        return gevonden_kaart()
    elif choice == "2":
        return gevonden_stad()
    else:
        print("Ongeldige keuze. Het spel eindigt.")
        return "fail", False

def gevonden_kaart():
    print("\n Je hebt nu een kaart gevonden in de hut en ziet dat er een stad in de buurt is.")
    print("Wat doe je?")
    print("1. Volg de kaart en ga naar de stad.")
    print("2. Blijf in de wildernis en vermijd de stad om niet opgemerkt te worden.")
    choice = input("Typ het nummer van je keuze: ")

    if choice == "1":
        return gevonden_stad()
    elif choice == "2":
        return gevonden_stad()
    else:
        print("Ongeldige keuze. Het spel eindigt.")
        return "fail", False
    
def gevonden_stad():
    print("\n Je bent nu in stad en moet nu een manier vinden om onder de radar te blijven.")
    print("Wat doe je?")
    print("1. Zoek een vermomming om niet op te vallen.")
    print("2. Ga undercover en meng je met de lokale bevolking.")
    choice = input("Typ het nummer van je keuze: ")

    if choice == "1":
        return gevonden_stad()
    elif choice == "2":
        return gevonden_stad()
    else:
        print("Ongeldige keuze. Het spel eindigt.")
        return "fail", False
    
def politie_controle():
    print("\n  Je bevindt je nu in de stad en ziet een politiecontrole op de hoofdweg.")
    print("Wat doe je?")
    print("1. Loop rustig door en probeer niet op te vallen.")
    print("2. Zoek een alternatieve route om de politiecontrole te vermijden.")
    choice = input("Typ het nummer van je keuze: ")

    if choice == "1":
        return opzoek_naar_jouw()
    elif choice == "2":
        return opzoek_naar_jouw()
    else:
        print("Ongeldige keuze. Het spel eindigt.")
        return "fail", False

def opzoek_naar_jouw():
    print("\n  Terwijl je door de stad sluipt, hoor je dat de politie op zoek is naar een ontsnapte gevangene.")
    print("Wat doe je?")
    print("1. Verander eerst je uiterlijk om minder herkenbaar te zijn en verlaat de stad.")
    print("2. Versnel je pas en probeer de stad zo snel mogelijk te verlaten.")
    choice = input("Typ het nummer van je keuze: ")

    if choice == "1":
        return treinstation_in_buurt()
    elif choice == "2":
        return treinstation_in_buurt()
    else:
        print("Ongeldige keuze. Het spel eindigt.")
        return "fail", False
    
def treinstation_in_buurt():
    print("\n  Je hebt gehoord dat er een treinstation in de buurt is dat je uit de stad kan brengen.")
    print("Wat doe je?")
    print("1. Ga direct naar het treinstation en probeer een ticket te kopen.")
    print("2. Zoek een verborgen plek in de stad om te schuilen tot het veilig is en daarna ga je naar het treinstation.")
    choice = input("Typ het nummer van je keuze: ")

    if choice == "1":
        return treinstation_in_buurt()
    elif choice == "2":
        return treinstation_in_buurt()
    else:
        print("Ongeldige keuze. Het spel eindigt.")
        return "fail", False

def treinstation_agenten():
    print("\n Je bent bij het treinstation, maar er zijn politieagenten in de buurt.")
    print("Wat doe je?")
    print("1. Sluip langs de agenten om onopgemerkt het station binnen te gaan.")
    print("2. Wacht tot de agenten weg zijn voordat je het station betreedt.")
    choice = input("Typ het nummer van je keuze: ")

    if choice == "1":
        return aan_boord_trein()
    elif choice == "2":
        return aan_boord_trein()
    else:
        print("Ongeldige keuze. Het spel eindigt.")
        return "fail", False
    
def aan_boord_trein():
    print("\n Je bent aan boord van de trein, maar de conducteur vraagt om een identificatie.")
    print("Wat doe je?")
    print("1. Probeer de conducteur om te kopen met het geld dat je hebt gevonden.")
    print("2. ga in de wc verstoppen tot hij weg is.")
    choice = input("Typ het nummer van je keuze: ")

    if choice == "1":
        return stad_verlaten()
    elif choice == "2":
        return stad_verlaten()
    else:
        print("Ongeldige keuze. Het spel eindigt.")
        return "fail", False
    
def stad_verlaten():
    print("\n Je hebt de stad verlaten en bent nu op zoek naar een veilige schuilplaats.")
    print("Wat doe je?")
    print("1. Ga naar een afgelegen gebied om te voorkomen dat je wordt gevonden.")
    print("2. Zoek onderdak bij lokale bewoners en vraag om hulp.")
    choice = input("Typ het nummer van je keuze: ")

    if choice == "1":
        return schuilplaats_vinden()
    elif choice == "2":
        return schuilplaats_vinden()
    else:
        print("Ongeldige keuze. Het spel eindigt.")
        return "fail", False

def schuilplaats_vinden():
    print("\n Je hebt een tijdelijke schuilplaats gevonden, maar je hebt nog steeds geen idee hoe je volledig off the grid kunt blijven.")
    print("Wat doe je?")
    print("1. Contacteer een oude vriend die je kan helpen.")
    print("2. Leer meer over technieken voor ondergronds leven om onopgemerkt te blijven.")
    choice = input("Typ het nummer van je keuze: ")

    if choice == "1":
        print("Helaas je vrienden kunnen jouw niet helpen.")
        return treinstation_in_buurt()
    elif choice == "2":
        return treinstation_in_buurt()
    else:
        print("Ongeldige keuze. Het spel eindigt.")
        return "fail", False
    
def technieken_leren():
    print("\n Je hebt besloten om meer te leren over technieken voor ondergronds leven en begint je onderzoek.")
    print("Wat doe je?")
    print("1. Volg online cursussen over survival en onzichtbaarheidstechnieken.")
    print("2. Zoek een ervaren mentor die je de fijne kneepjes van het vak kan leren.")
    choice = input("Typ het nummer van je keuze: ")

    if choice == "1":
        print("Helaas je vrienden kunnen jouw niet helpen.")
        return door_gaan_met_leven()
    elif choice == "2":
        return door_gaan_met_leven()
    else:
        print("Ongeldige keuze. Het spel eindigt.")
        return "fail", False
    
def door_gaan_met_leven():
    print("\n Je hebt nu de keuze om een nieuw leven op te bouwen of door te gaan met een leven in de schaduwen.")
    print("Wat doe je?")
    print("1. Probeer een eerlijk leven op te bouwen en je verleden achter je te laten.")
    print("2. Blijf in de schaduwen en blijf leven als een ongrijpbare figuur.")
    choice = input("Typ het nummer van je keuze: ")

    if choice == "1":
        print("Gefeliciteerd, Je hebt het spel gewonnen!")
        return "win", False
    elif choice == "2":
        print("Gefeliciteerd, Je hebt het spel gewonnen!")
        return "win", False
    else:
        print("Ongeldige keuze. Het spel eindigt.")
        return "fail", False



