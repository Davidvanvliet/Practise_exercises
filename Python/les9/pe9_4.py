#1723682
#David van Vliet

import csv

prijs = ''
naam = ''
artikelnummer = ''
voorraad = ''
totaal_producten = 0

with open ('pe9_4.csv', 'w')as pe9_4: # Maakt het bestand aan met de volgende regels en kolommen
    schrijven_bestand = csv.writer(pe9_4, delimiter = ';')
    schrijven_bestand.writerow (('Artikelnummer', 'Artikelcode', 'Naam', 'Voorraad', 'Prijs'))
    schrijven_bestand.writerow (('121', 'ABC123', 'Highlight pen', '231', '0.56'))
    schrijven_bestand.writerow (('123', 'PQR678', 'Nietmachine', '587', '9.99'))
    schrijven_bestand.writerow (('128', 'ZYX163', 'Bureaulamp', '34', '19.95'))
    schrijven_bestand.writerow (('137', 'MLK709', 'Monitorstandaard', '66', '32.50'))
    schrijven_bestand.writerow (('271', 'TRS665', 'Ipad hoes', '155', '19.01'))

with open ('pe9_4.csv', 'r') as PE9_4csv: # Opend het bestand
    lees_bestand = csv.DictReader (PE9_4csv, delimiter = ';')

    prijs_teller = 0 # telt uiteindelij wat de hoogste prijs is en vind het bijpassende product bij de prijs
    for regel in lees_bestand:
        if float(regel['Prijs']) > float(prijs_teller):
            prijs_teller = float(regel['Prijs'])
            prijs = prijs_teller
            naam = regel['Naam']

    print ('Het duurste artikel is {} en die kost {} euro'.format(naam, prijs))

with open('pe9_4.csv', 'r') as PE9_4csv: # opend het bestand
    lees_bestand = csv.DictReader(PE9_4csv, delimiter=';')

    voorraad_teller = 100000 # een hoog getal dat nooit bereikt kan worden met voorraad
    totaal_producten = 0 # de aantal prodcuten dat begint met 0

    for regel in lees_bestand: # berekend welk product het minst op voorraad is
        if int(regel['Voorraad']) < voorraad_teller:
            voorraad_teller = int(regel['Voorraad'])
            artikelnummer = int(regel['Artikelnummer'])


        totaal_producten += int(regel['Voorraad']) # berekend de totaal aantal producten

    print('Er zijn slechts {} exemplaren in voorraad van het product met nummer {}'.format(voorraad_teller, artikelnummer))
    print ('In totaal hebben wij {} producten in ons magazijn liggen'.format(totaal_producten))