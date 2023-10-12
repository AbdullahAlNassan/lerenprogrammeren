
MIN_GEWICHT = 90  
MAX_GEWICHT = 120 
MIN_LENGTE = 150 
MAX_LENGTE = 220 
MIN_DIEREN_ERVARING = 4  
MIN_JONGLEREN_ERVARING = 5  
MIN_ACROBATIEK_ERVARING = 3  



vrachtwagen_rijbewijs = input('Heeft u een geldig Vrachtwagen rijbewijs? (J/N): ')

hoge_hoed = input('Heeft u een hoge hoed? (J/N): ')

gewicht = int(input('Wat is uw lichaamsgewicht in kg?: '))

lengte = int(input('Wat is uw lengte in cm?: '))

overleven_certificaat = input('Heeft u het Certificaat “Overleven met gevaarlijk personeel”? (J/N): ')

dieren_ervaring = int(input('Hoeveel jaar praktijkervaring heeft u met dieren-dressuur?: '))

jongleren_ervaring = int(input('Hoeveel jaar ervaring heeft u met jongleren?: '))

acrobatiek_ervaring = int(input('Hoeveel jaar praktijkervaring heeft u met acrobatiek?: '))


if (
    vrachtwagen_rijbewijs == 'J' and
    hoge_hoed == 'J' and
    MIN_GEWICHT <= gewicht <= MAX_GEWICHT and
    MIN_LENGTE <= lengte <= MAX_LENGTE and
    overleven_certificaat == 'J' and
    (dieren_ervaring >= MIN_DIEREN_ERVARING or jongleren_ervaring >= MIN_JONGLEREN_ERVARING or acrobatiek_ervaring >= MIN_ACROBATIEK_ERVARING)
):

    print('Gefeliciteerd! U mag solliciteren naar de functie van Circusdirecteur voor Circus HotelDeBotel.')


else:
    print('Helaas, u voldoet niet aan alle criteria en komt niet in aanmerking voor de functie.')
