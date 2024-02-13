# Deze functie gemiddelde neemt twee parameters, som en aantal, en retourneert het gemiddelde door som te delen door aantal.
def gemiddelde(som, aantal): 
    return som / aantal

# Deze functie neemt een lijst van getallen en retourneert het eerste getal in de lijst.
def haal_eerste_getal_op(getallen):
    return getallen[0]

# Deze functie delen neemt twee parameters, kleinste_getal en controlegetal1, en retourneert het resultaat van kleinste_getal gedeeld door controlegetal1
def delen(kleinste_getal, controlegetal1):
    return kleinste_getal / controlegetal1

# Deze functie delen neemt twee parameters, grootste_getal en controlegetal2, en retourneert het resultaat van grootste_getal gedeeld door controlegetal2.
def delen(grootste_getal, controlegetal2):
    return grootste_getal / controlegetal2

# Deze functie neemt een lijst van getallen. Het telt het aantal keer dat elk getal voorkomt in de lijst en retourneert een woordenboek waarin de getallen de sleutels zijn en hun tellingen de waarden.
def tel_elementen(getallen):
    telling_elementen = {}
    for getal in getallen:
        aantalkeer = telling_elementen.get(getal, 0) + 1
        telling_elementen[getal] = aantalkeer
    return telling_elementen

# Deze functie neemt een lijst van getallen en een controlegetal als invoer.
def vind_deelbare_getallen(getallen, controlegetal):
    deelbaar = [getal for getal in getallen if getal % controlegetal == 0]
    return sorted(deelbaar)

# Deze functie neemt getallen en een controlegetal als invoer.
def vind_deelbare_getallen(getallen, controlegetal):
    deelbaar = [getal for getal in getallen if getal % controlegetal == 0]
    return sorted(deelbaar)

# Deze functie neemt getallen en twee controlegetallen als invoer.
def controleer_voorkomen(getallen, controlegetal1, controlegetal2):
    komtvoor = controlegetal1 in getallen and controlegetal2 in getallen
    return komtvoor

# Deze functie neemt getallen en een controlegetal als invoer.
def vind_posities(getallen, controlegetal):
    posities = [index for index, num in enumerate(getallen) if num == controlegetal]
    return posities

# Deze functie variantie neemt twee parameters, verschil_kwadraat en aantal, en retourneert de variantie door verschil_kwadraat te delen door aantal.
def variantie(verschil_kwadraat, aantal):
    return verschil_kwadraat / aantal


