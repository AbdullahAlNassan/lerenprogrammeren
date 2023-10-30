from test_lib import test, report

def numbers(nr1: int, nr2: int) -> str:
    if nr1 > nr2:
        return f'Maximum: {nr1} en minimum: {nr2}'
    elif nr1 < nr2:
        return f'Maximum: {nr2} en minimum: {nr1}'
    else:
        return 'Beide getallen zijn even groot'

nr1 = int(input('Voer nr1 in: '))
nr2 = int(input('Voer nr2 in: '))

result = numbers(nr1, nr2)
print(result)

report()