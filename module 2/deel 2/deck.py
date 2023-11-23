import random

deck = []
suits = ['Harten', 'klaveren', 'schoppen', 'ruiten']
card_values = ["2", "3", "4", "5", "6", "7", "8"]

for suit in suits:
    for value in card_values:
        deck.append(f"{suit} {value}")

deck.extend(["joker1", "joker2"])
random.shuffle(deck)

for i in range(7):
    print(f"Kaart {i+1}: {deck[i]}")

remaining_cards = deck[7:]
print(f"Deck ({len(remaining_cards)} kaarten): {remaining_cards}")

