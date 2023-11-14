from gevangenis_1 import intro, make_decision

def main():
    intro()

    actions = 0
    win = False

    while actions < 10 and not win:
        decision, win = make_decision()
        actions += 1

    if win:
        print("Gefeliciteerd, je hebt het spel gewonnen!")
    else:
        print("Bedankt voor het spelen!")

if __name__ == "__main__":
    main()
