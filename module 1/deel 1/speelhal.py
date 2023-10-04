ticket = 1

vip_minuten = 5

vip_kost_per_5_minuten = 0.37

aantal_personen = 1

totaal_ticket_kosten = ticket * aantal_personen

totaal_vip_game_seat_kosten = (vip_minuten / 5) * vip_kost_per_5_minuten * aantal_personen

totaal_kosten = totaal_ticket_kosten + totaal_vip_game_seat_kosten

print(totaal_kosten)

