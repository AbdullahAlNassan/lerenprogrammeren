def vraag_gegevens():
    name = input('Wat is je naam? ')
    age = input('Hoe oud ben je? ')
    woonplaats = input('waar woon je?')
    return name, age, woonplaats

def verzamel_gegevens():
    gegevens_list = []
    while True:
        stoppen = input('klick enter om door te gaan of toets stop om te stoppen: ')
        if stoppen == 'stop':
            break
        name, age, woonplaats = vraag_gegevens()
        gegevens_list.append((name, age, woonplaats))
    return gegevens_list

gegevens_list = verzamel_gegevens()
for name, age, woonplaats in gegevens_list:
    print(f'{name} die in {woonplaats} woont is {age} jaar')