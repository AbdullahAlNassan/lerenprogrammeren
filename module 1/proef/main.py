from gevangenis_1 import intro, make_decision

def main():
    intro()

    game_result, success = make_decision()

    if success:
        print("Gefeliciteerd! Je bent succesvol ontsnapt!")
    else:
        print(f"Jammer, je bent opgepakt. Je hebt het niet gehaald. Resultaat: {game_result}")


main()
