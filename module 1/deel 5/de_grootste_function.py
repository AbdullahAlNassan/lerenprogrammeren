from test_lib import test, report

def numbers(nr1: int, nr2: int) -> str:
    if nr1 > nr2:
        return f'Maximum: {nr1} en minimum: {nr2}'
    elif nr1 < nr2:
        return f'Maximum: {nr2} en minimum: {nr1}'
    else:
        return 'Beide getallen zijn even groot'

nr1 = 5
nr2 = 10
result = numbers(nr1, nr2)
test("Test 1", "Maximum: 10 en minimum: 5", result)

nr1 = 15
nr2 = 8
result = numbers(nr1, nr2)
test("Test 2", "Maximum: 15 en minimum: 8", result)

nr1 = 3
nr2 = 3
result = numbers(nr1, nr2)
test("Test 3", "Beide getallen zijn even groot", result)


report()
