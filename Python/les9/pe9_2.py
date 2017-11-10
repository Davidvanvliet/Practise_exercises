#1723682
#David van Vliet

import datetime
import csv

bestand = 'inloggers.csv'

#In een csv bestand schrijven met de inputs die je geeft
with open (bestand, 'w', newline='') as CSVfile:
    schrijven = csv.writer(CSVfile, delimiter = ';')

    while True:
        naam = input("Wat is je achternaam? ")
        if naam == 'einde':
            break
        voorl = input("Wat zijn je voorletters? ")
        gbdatum = input("Wat is je geboortedatum? ")
        email = input("Wat is je e-mail adres? ")
        schrijven.writerow ((naam, voorl, gbdatum, email))
