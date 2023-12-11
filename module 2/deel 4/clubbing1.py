# Constantes
PRIJS_COLA = 1.80
PRIJS_BIER = 2.40
PRIJS_CHAMPAGNE = 12.30

DRANKJES = ('cola', 'bier', 'champagne')
VIP_LIST = ('jeroen', 'jouke', 'rudi')

KLEUR_BANDJE = 'Je krijgt van mij een {kleur} bandje'
STEMPEL = 'Je krijgt van mij een stempel'
COMPLIMENTEN = 'Alsjeblieft complimenten van het huis'
DRANKJE_PRIJS = 'Alsjeblieft, je {drankje}, dat is dan €{prijs}'
LATER_PROBEREN = 'Probeer het over {0} jaar nog eens'
GEEN_ALCOHOL = 'Sorry, je mag geen alcohol bestellen onder de 21'

# Start programma
print('Welkom in de kroeg!')

# Vraag naar leeftijd
leeftijd = int(input('Hoe oud ben je? '))

# Controleer leeftijd
if leeftijd < 18:
    print('Sorry, je mag niet naar binnen.')
    print(LATER_PROBEREN.format(18 - leeftijd))
    exit()

# Vraag naar naam
naam = input('Wat is je naam? ')

# Controleer of het een vip is
if naam in VIP_LIST and leeftijd >= 21:
    kleur = 'blauw'
    print(KLEUR_BANDJE.format(kleur=kleur))
else:
    kleur = 'rood'
    print(KLEUR_BANDJE.format(kleur=kleur))

# Vraag naar drankje
drankje = input('Wat wil je drinken? ')

# Controleer drankje
if drankje not in DRANKJES:
    print('Sorry, ik weet niet wat je bedoelt. Hier is een glaasje water.')
else:
    # Controleer leeftijd en vip-status
    if drankje == 'bier' and leeftijd < 21:
        print(GEEN_ALCOHOL.format(21 - leeftijd))
        print(LATER_PROBEREN.format(21 - leeftijd))
    elif drankje == 'bier' and leeftijd < 21 and naam not in VIP_LIST:
        print(DRANKJE_PRIJS.format(drankje=drankje, prijs=PRIJS_BIER))
    elif drankje == 'bier' and naam in VIP_LIST and kleur == 'blauw':
        print(COMPLIMENTEN)
    elif drankje == 'champagne' and naam not in VIP_LIST:
        print('Sorry, alleen vips mogen champagne bestellen.')
    elif drankje == 'champagne' and naam in VIP_LIST and kleur != 'blauw':
        print(GEEN_ALCOHOL.format(21 - leeftijd))
        print(LATER_PROBEREN.format(21 - leeftijd))
    elif drankje == 'champagne' and naam in VIP_LIST and kleur == 'blauw':
        print(DRANKJE_PRIJS.format(drankje=drankje, prijs=PRIJS_CHAMPAGNE))
    else:
        # Bereken prijs
        prijs = PRIJS_COLA if drankje == 'cola' else PRIJS_BIER if drankje == 'bier' else PRIJS_CHAMPAGNE

        # Print bevestiging
        print(DRANKJE_PRIJS.format(drankje=drankje, prijs=prijs))

# Einde programma
print('Tot ziens!')
