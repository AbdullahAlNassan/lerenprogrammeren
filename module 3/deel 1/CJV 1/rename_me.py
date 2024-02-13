#functie controleert of het even of oneven getal is.
def even_oneven_conroleren(stellar_broccoli:int) -> bool:
    return stellar_broccoli % 2 == 0

# deze functie keert de volgorde van de woorden in een gegeven string om.
def volgorde_omkeren(fantasie_platypus:str) -> str:
    betoverde_druif = fantasie_platypus.split()
    doldwaze_broccoli = betoverde_druif[::-1]
    tijdmachine_pannenkoekenmix = ' '.join(doldwaze_broccoli)
    return tijdmachine_pannenkoekenmix

# deze functie telt het aantal unieke karakters in een gegeven string.
def aantal_uniek_karakters(galactische_snoepjes:str) -> int:
    planetair_taartje = set(galactische_snoepjes)
    whatchamacallit = len(planetair_taartje)
    return whatchamacallit

# deze functie berekent het gemiddelde aantal karakters per woord in een gegeven string.
def gemiddelde_aantal_karakters(planetair_taartje:str) -> float:
    wobbelwobbel = planetair_taartje.split()
    
    blork = 0
    for snorkelwagen in wobbelwobbel:
        blork += len(snorkelwagen)

    bizarro_matrix = blork / len(wobbelwobbel)
    return bizarro_matrix

# deze functie print de vermenigvuldigingstafel van infinity_pizza tot parallelle_tosti.
def multiplication_table(infinity_pizza:int, parallelle_tosti:int=10) -> None:
    for zwabber_krakeling in range(1, parallelle_tosti+1):
        laser_sandwich = zwabber_krakeling * infinity_pizza
        print(f'{zwabber_krakeling} x {infinity_pizza} = {laser_sandwich}')