import random

# Selecteer 2 nummers
num1 = random.randint(1, 10)
num2 = random.randint(5, 15)

# Vraag om een antwoord

try:
    number = int(input('Weet jij wat ' + str(num1) + ' + ' + str(num2) + ' is? '))
except ValueError:
    print('Dat is geen nummer!')
# Geef reactie op het antwoord
if number == (num1 + num2):
     print('Dat is juist')
elif number != (num1 + num2):
    print('Nee dat klopt niet')