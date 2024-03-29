from collections import Counter
import math, random

def analyseer_getallenlijst(getallen:list, controlegetal1:int, controlegetal2:int) -> dict:
    if not getallen:
        return {"Lijst is leeg, voer getallen in.":getallen}

    if not str(controlegetal1).isnumeric():
        return {"Eerste controlle getal incorrect.":controlegetal1}

    if not str(controlegetal2).isnumeric():
        return {"Tweede controlle getal incorrect.":controlegetal2}


    aantal = len(getallen)


    som = sum(getallen)


    gemiddelde = som / aantal


    grootste_getal = max(getallen)
    

    kleinste_getal = min(getallen)
    

    eerste_getal = getallen[0]
    

    delen1 = kleinste_getal / controlegetal1


    delen2 = grootste_getal / controlegetal2


    unieke_getallen = list(set(getallen))


    aantal_unieke_elementen = len(unieke_getallen)


    verschil1 = abs(aantal_unieke_elementen - controlegetal1)


    gesorteerde_lijst = sorted(getallen)


    gesorteerde_lijst_uniek = sorted(unieke_getallen)


    telling_elementen = {}
    for getal in getallen:
        aantalkeer = telling_elementen[getal]+1 if getal in telling_elementen else 1
        telling_elementen[getal] = aantalkeer


    deelbaar1 = []
    for getal in unieke_getallen:
        if getal % controlegetal1 == 0:
            deelbaar1.append(getal)
    deelbaar1 = sorted(deelbaar1)


    deelbaar2 = []
    for getal in unieke_getallen:
        if getal % controlegetal2 == 0:
            deelbaar2.append(getal)
    deelbaar2 = sorted(deelbaar2)


    komtvoor = controlegetal1 in getallen and controlegetal2 in getallen


    posities = []
    for index, num in enumerate(getallen):
        if num == controlegetal1:
            posities.append(index)


    verschil_kwadraat = sum((x - gemiddelde) ** 2 for x in getallen)
    variantie = verschil_kwadraat / aantal
    standaardafwijking = math.sqrt(variantie)


    random.shuffle(getallen)


    random_getal = getallen[random.randint(0,aantal-1)]


    verschil2 = abs(random_getal - controlegetal2)

    resultaten = {
        "Aantal getallen": aantal,
        "Gemiddelde": gemiddelde,
        "Som": som,
        "Grootste getal": grootste_getal,
        "Kleinste getal": kleinste_getal,
        "Eerste getal": eerste_getal,
        f"{kleinste_getal} / {controlegetal1}": delen1,
        f"{grootste_getal} / {controlegetal2}": delen2,
        "Aantal unieke elementen": aantal_unieke_elementen,
        f"Het verschil tussen {aantal_unieke_elementen} & {controlegetal1}": verschil1,
        "Gesorteerde lijst getallen": gesorteerde_lijst,
        "Gesorteerde lijst unieke getallen": gesorteerde_lijst_uniek,
        "Telling van elementen": telling_elementen,
        f"Deelbaar door {controlegetal1} (op volgorde)": deelbaar1,
        f"Deelbaar door {controlegetal2} (op volgorde)": deelbaar2,
        f"{controlegetal1} & {controlegetal2} komt wel voor in de lijst": komtvoor,
        f"{controlegetal1} komt voor op positie(s)": posities,
        "Standaardafwijking": standaardafwijking,
        "Geshufflede lijst": getallen,
        "Willekeurige getal uit de lijst": random_getal,
        f"Het verschil tussen {random_getal} & {controlegetal2}": verschil2,
    }

    return resultaten



getallenlijst = [16, 2, 5, 8, 12, 3, 9, 16, 5, 8, 64, 33]
controlegetal1 = 8
controlegetal2 = 3
analyse_resultaat = analyseer_getallenlijst(getallenlijst, controlegetal1, controlegetal2)
print("Analyse resultaten:")
for key, value in analyse_resultaat.items():
    print(f"{key}: {value}")




































#     # Deze functie gemiddelde neemt twee parameters, som en aantal, en retourneert het gemiddelde door som te delen door aantal.
# def gemiddelde(som, aantal): 
#     return som / aantal

# # Deze functie neemt een lijst van getallen als invoer en retourneert het eerste getal in de lijst.
# def haal_eerste_getal_op(getallen:list) -> int:
#     if not getallen:
#         return None
#     return getallen[0]

# # Deze functie delen neemt twee parameters, kleinste_getal en controlegetal1, en retourneert het resultaat van kleinste_getal gedeeld door controlegetal1
# def delen(kleinste_getal, controlegetal1):
#     return kleinste_getal / controlegetal1

# # Deze functie delen neemt twee parameters, grootste_getal en controlegetal2, en retourneert het resultaat van grootste_getal gedeeld door controlegetal2.
# def delen(grootste_getal, controlegetal2):
#     return grootste_getal / controlegetal2

# # Deze functie neemt een lijst van getallen als invoer. Het telt het aantal keer dat elk getal voorkomt in de lijst en retourneert een woordenboek waarin de getallen de sleutels zijn en hun tellingen de waarden.
# def tel_elementen(getallen:list) -> dict:
#     telling_elementen = {}
#     for getal in getallen:
#         aantalkeer = telling_elementen.get(getal, 0) + 1
#         telling_elementen[getal] = aantalkeer
#     return telling_elementen

# # Deze functie neemt een lijst van getallen en een controlegetal als invoer.
# def vind_deelbare_getallen(getallen:list, controlegetal:int) -> list:
#     deelbaar = [getal for getal in getallen if getal % controlegetal == 0]
#     return sorted(deelbaar)

# # Deze functie neemt een lijst van getallen en een controlegetal als invoer.
# def vind_deelbare_getallen(getallen:list, controlegetal:int) -> list:
#     deelbaar = [getal for getal in getallen if getal % controlegetal == 0]
#     return sorted(deelbaar)

# # Deze functie neemt een lijst van getallen en twee controlegetallen als invoer.
# def controleer_voorkomen(getallen:list, controlegetal1:int, controlegetal2:int) -> bool:
#     komtvoor = controlegetal1 in getallen and controlegetal2 in getallen
#     return komtvoor

# # Deze functie neemt een lijst van getallen en een controlegetal als invoer.
# def vind_posities(getallen:list, controlegetal:int) -> list:
#     posities = [index for index, num in enumerate(getallen) if num == controlegetal]
#     return posities


# def variantie(verschil_kwadraat, aantal):
#     return verschil_kwadraat / aantal
