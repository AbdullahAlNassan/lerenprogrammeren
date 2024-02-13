def vraag_gegevens():
    name = input('Wat is je naam? ')
    age = input('Hoe oud ben je? ')
    return name, age

def verzamel_gegevens():
    gegevens_list = []
    while True:
        stoppen = input('klick enter om door te gaan of toets stop om te stoppen: ')
        if stoppen == 'stop':
            break
        name, age = vraag_gegevens()
        gegevens_list.append((name, age))
    return gegevens_list

gegevens_list = verzamel_gegevens()
for name, age in gegevens_list:
    print(f'{name} is {age} jaar oud!')
