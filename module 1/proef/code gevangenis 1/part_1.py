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
    


    def richting_achtertuin():
    print("\n je hebt achtertuib bereikt en ziet bewakers.")
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