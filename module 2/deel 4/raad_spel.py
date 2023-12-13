import random

print("Welkom bij het raden van getallen spel!")

rounds = 0
score = 0

while rounds < 20:
    secret_number = random.randint(1, 1000)
    guess_attempts = 0

    while guess_attempts < 10:
        guess = input('Raad een getal tussen 1 en 1000: ')
        
        try:
            guess = int(guess)
        except ValueError:
            print('Ongeldige invoer. Voer een geldig getal in.')
            continue

        guess_attempts += 1

        if guess == secret_number:
            print(f'Gefeliciteerd! Je hebt het geheime getal {secret_number} geraden.')
            score += 1
            break
        else:
            difference = secret_number - guess
            if difference < 20:
                print('Je bent heel warm!')
            elif difference < 50:
                print('Je bent warm!')
            else:
                print('Koud!')

            print(f'Het geheime getal is {"hoger" if secret_number > guess else "lager"}.')

    rounds += 1
    print(f'Score: {score}/{rounds}')

    if rounds < 20:
        play_again = input('Nog een getal raden? (ja/nee): ')
        if play_again.lower() != 'ja':
            break

print(f'Eindscore: {score}/20')
