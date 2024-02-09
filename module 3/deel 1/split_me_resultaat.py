from collections import Counter
import math, random

def controleer_getallen(getallen:list) -> dict:
    if not getallen:
        return {"Lijst is leeg, voer getallen in.":getallen}
    return {}

def controleer_controlegetal(controlegetal:int) -> dict:
    if not str(controlegetal).isnumeric():
        return {f"Controlegetal {controlegetal} incorrect.":controlegetal}
    return {}

def bereken_gemiddelde(getallen:list) -> float:
    return sum(getallen) / len(getallen)

def bereken_deelbaar(getallen:list, controlegetal:int) -> list:
    return sorted([getal for getal in getallen if getal % controlegetal == 0])

def bereken_posities(getallen:list, controlegetal:int) -> list:
    return [index for index, num in enumerate(getallen) if num == controlegetal]

def bereken_standaardafwijking(getallen:list, gemiddelde:float) -> float:
    verschil_kwadraat = sum((x - gemiddelde) ** 2 for x in getallen)
    variantie = verschil_kwadraat / len(getallen)
    return math.sqrt(variantie)

def kies_random_getal(getallen:list) -> int:
    random.shuffle(getallen)
    return getallen[random.randint(0, len(getallen)-1)]

def analyseer_getallenlijst(getallen:list, controlegetal1:int, controlegetal2:int) -> dict:
    resultaten = controleer_getallen(getallen)
    if resultaten:
        return resultaten

    resultaten = controleer_controlegetal(controlegetal1)
    if resultaten:
        return resultaten

    resultaten = controleer_controlegetal(controlegetal2)
    if resultaten:
        return resultaten

    aantal = len(getallen)
    som = sum(getallen)
    gemiddelde = bereken_gemiddelde(getallen)
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
    telling_elementen = Counter(getallen)
    deelbaar1 = bereken_deelbaar(unieke_getallen, controlegetal1)
    deelbaar2 = bereken_deelbaar(unieke_getallen, controlegetal2)
    komtvoor = controlegetal1 in getallen and controlegetal2 in getallen
    posities = bereken_posities(getallen, controlegetal1)
    standaardafwijking = bereken_standaardafwijking(getallen, gemiddelde)
    geshufflede_lijst = random.sample(getallen, len(getallen))
    random_getal = kies_random_getal(getallen)
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
        "Geshufflede lijst": geshufflede_lijst,
        "Willekeurige getal uit de lijst": random_getal,
        f"Het verschil tussen {random_getal} & {controlegetal2}": verschil2,
    }

    return resultaten
