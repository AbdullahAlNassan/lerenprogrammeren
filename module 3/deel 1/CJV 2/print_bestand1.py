from bestand1 import verzamel_gegevens

gegevens_list = verzamel_gegevens()
for name, age, woonplaats in gegevens_list:
    print(f'{name} die in {woonplaats} woont is {age} jaar oud!')
