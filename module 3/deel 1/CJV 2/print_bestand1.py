from bestand1 import verzamel_gegevens

gegevens_list = verzamel_gegevens()
for gegevens in gegevens_list:
    print(f'{gegevens["naam"]} die in {gegevens["kleur"]} woont, is {gegevens["leeftijd"]} jaar')
