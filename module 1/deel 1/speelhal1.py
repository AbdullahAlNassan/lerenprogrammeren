ticket = 7.45
vip_minuten = 45
vip_kost_per_5_minuten = 0.37
aantal_personen = 4

totaal_ticket_kosten = ticket * aantal_personen

totaal_vip_game_seat_kosten = (vip_minuten / 5) * vip_kost_per_5_minuten * aantal_personen

totaal_kosten = totaal_ticket_kosten + totaal_vip_game_seat_kosten

print(f'Dit geweldige dagje-uit met {aantal_personen} mensen in de Speelhal met {vip_minuten} minuten VR kost je maar {totaal_kosten:.2f} euro')
