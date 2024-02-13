def vraag_gegevens():
    name = input('Wat is je naam? ')
    age = input('Hoe oud ben je? ')
    return name, age

name, age = vraag_gegevens()
print(f'{name} is {age} jaar')
