MIJN_NAAM = 'Abdullah'
SLB_NAAM = "jauke"

gastheer = input('Wie is de gastheer?')
gasten = 1
drank = 1
chips = 1
if gastheer == MIJN_NAAM or ((gasten and chips and drank) or (gastheer and drank)) and gastheer != SLB_NAAM:
    print('Start the Party')
else:
    print('No Party')

