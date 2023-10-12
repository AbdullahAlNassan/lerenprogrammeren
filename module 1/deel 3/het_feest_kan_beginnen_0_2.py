MIJN_NAAM = 'Abdullah'
SLB_NAAM = "jouke"

gastheer = input('Wie is de gastheer? ')
gasten = int(input('Hoeveel gasten zijn er? '))
drank = 1
chips = 1

if gastheer == MIJN_NAAM or ((4 <= gasten <= 20 and chips and drank) or (gastheer and drank)) and gastheer != SLB_NAAM:
    print('Start the Party')
else:
    print('No Party')





