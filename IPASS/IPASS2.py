#David van Vliet
#IPASS script

import os
import re
from collections import Counter

def open_bestand(): #Opent het opgegeven bestand
    global inhoud   #inhoud wordt in meerdere defenities gebruikt dus is het een global
    try:
        lezen = os.path.abspath(input('padnaam ingeven van het logbestand:'))
        bestand = open(lezen, 'r')
        inhoud = bestand.readlines()
    except:
        print("Fout pad")
        exit()

def gefaalde_downloads():   #laat alle downloads zien die gefaald zijn
    gefaald = []            #lijst waar alle gefaalde downloads in komen te staan
    for regel in inhoud:
        fout = re.search("FAIL.+\"", regel)
        if fout is not None:
            gefaald.append(fout.group())
            output = ("\n".join(gefaald))
            print(output)
            file = open("output.txt","a")
            file.write(output)          #De output wordt in output.txt geschreven
            file.close()

def aantal_gefaalde_downloads():    #Laat een lijst zien van alle gefaalde downloads met de hoeveelheden per bestand
    lijst = []              #Maakt een lijst met de gefaalde downloads
    hoeveel = Counter()     #Hier komen de hoeveelheden te staan voor elke gefaalde download die in de lijst staat

    for regel in inhoud:
        if "FAIL DOWNLOAD" in regel:
            split = regel.split()
            lijst.append(split[12].strip(',').strip('""'))
    for aantal in lijst:
        hoeveel[aantal] += 1
    for waarde, getal in hoeveel.most_common():
        output = ("Bestand: {} Gefaalde downloads: {}".format(waarde, getal))
        print(output)
        file = open("output.txt", "a")
        file.write(output)          #De output wordt in output.txt geschreven
        file.close()

def top_tien_downloads():   #Laat de 10 meest gedownloade bestanden zien met daarachter de hoeveelheid
    top_tien = []           #Een lijst waar de top 10 gedownloade bestanden worden geplaatst
    hoeveel = Counter()     #Een counter die telt hoeveel keer een zelfde bestand is gedownload
    for regel in inhoud:
        if "OK DOWNLOAD" in regel:
            split = regel.split()
            top_tien.append(split[12].strip(',').strip('""'))
    for aantal in top_tien:
        hoeveel[aantal] += 1
    top_tien.clear()
    for waarde, getal in hoeveel.most_common(10):
        output = ("bestand: {} Downloads: {}".format(waarde, getal))
        print(output)
        file = open("output.txt", "a")
        file.write(output)          #De output wordt in output.txt geschreven
        file.close()

def menu():                 #Een menu met alle keuzes
    print('\n---------------------menu---------------------')
    print(' 1: Laat gefaalde downloads zien \n 2: Laat aantal gefaalde downloads per bestand zien \n 3: Laat een top 10 gedownloade bestanden zien \n 5: Afbreken')
    keuze = str(input("Uw keuze: "))
    if str(keuze) == '1':
        gefaalde_downloads()
        menu()
    elif str(keuze) == '2':
        aantal_gefaalde_downloads()
        menu()
    elif str(keuze) == '3':
        top_tien_downloads()
        menu()
    elif str(keuze) == '5':
        exit()
    else :
        print('Verkeerde invoer')
        menu()

open_bestand()
menu()

