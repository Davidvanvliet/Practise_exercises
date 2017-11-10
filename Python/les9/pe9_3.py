#1723682
#David van Vliet

import csv

waarde = 0
naam = ''
datum = ''

#De hoogste score uitlezen en de bijbehorende datum en naam hiervan printen
with open ('lees_bestand.csv', 'r') as LeesBestand:
    lees = csv.reader (LeesBestand, delimiter = ';')

    for regel in lees:
        if int(regel[2]) > waarde:
            waarde = int(regel[2])
            naam = regel[0]
            datum = regel[1]

    print ('De hoogste score is: {} op {} behaald door {}'.format(waarde, datum, naam))



