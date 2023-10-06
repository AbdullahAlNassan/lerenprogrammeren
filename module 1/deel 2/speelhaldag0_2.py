aantal_mensen = int(input("hoeveel mensen gaan mee?"))

TOEGANG_TICKET_PRIJS = 7.45
gameseat_per_5_minuut = float(input("Hoeveel kost per 5 minuut?"))
tijd_gameseat_minuut = int(input("Hoeveel minuten willen jullie spelen?"))
PERIODE = 5

totaal_kosten_gameseat = ((tijd_gameseat_minuut / PERIODE) * gameseat_per_5_minuut) * aantal_mensen
totaal_toegangtickets = aantal_mensen * TOEGANG_TICKET_PRIJS 

totaat_bedrag = totaal_kosten_gameseat + totaal_toegangtickets
print(f"Dit is geweldige dagje uit met {aantal_mensen} mensen in de speelhal met {tijd_gameseat_minuut} minuten VR kost maar {totaat_bedrag} euro")