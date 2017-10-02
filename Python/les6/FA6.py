#1723682
#David van Vliet

def toon_aantal_kluizen_vrij():
    bestand = open('kluizen.txt', 'r')
    inhoud = bestand.readlines()
    bestand.close()

    beschikbaar = 12 - len(inhoud)  #Lijnen tellen door 12 min het aantal lijnen
    return beschikbaar

def nieuwe_kluis():
    beschikbarekluizen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    bestand = open('kluizen.txt', 'r')
    regels = bestand.readlines()
    for regel in regels:            #kluisnummer kiezen welke als eerste beschikbaar is. Vervolgens de kluis aanmaken met in het bestand splitsen met ;
        kluisinfo = regel.split(';')
        kluisnummer = int(kluisinfo[0].strip())

        if kluisnummer in beschikbarekluizen:
            beschikbarekluizen.remove(kluisnummer)

    bestand.close()

    if len(beschikbarekluizen) > 0:     #Alleen als er nog kluizen beschikbaar zijn een kluis aanmaken
        kluiscode = input('Voer uw nieuwe wachtwoord in: ')
        print('U krijgt kluis met nummer {} en code {}'.format(beschikbarekluizen[0], kluiscode))

        bestand = open('kluizen.txt', 'a')
        bestand.write('{};{}\n'.format(beschikbarekluizen[0], kluiscode))
        bestand.close()

def kluis_openen():
    nummer = input('Wat is uw kluisnummer? ')   #Vragen naar het kluisnummer en wachtwoord om de kluis te openen
    code = input('Wat is uw wachtwoord? ')

    bestand = open('kluizen.txt', 'r')
    regels = bestand.readlines()
    geopend = False
    for regel in regels:    #Bestand lezen en de ingevoerde kluisnummer en code vergelijken voor het openen van de kluis
        kluisinfo = regel.split(';')
        kluisnummer = kluisinfo[0].strip()
        kluiscode = kluisinfo[1].strip()

        geopend = (kluisnummer == nummer and kluiscode == code)
        if geopend:
            print('U heeft zojuist kluis {} geopend!'.format(kluisnummer))
            exit()

    if not geopend:
        print('Deze combinatie is niet correct!')

def menu():
    print('1: Ik wil weten hoeveel kluizen nog vrij zijn \n 2: Ik wil een nieuwe kluis \n 3: Ik wil even iets uit mijn kluis halen \n 5: Afbreken')
    keuze = int(input("Uw keuze: "))

    if keuze == 1:
        vrij = toon_aantal_kluizen_vrij()
        print("Er zijn ", vrij, "kluizen vrij")
        menu()

    elif keuze == 2:
        print(nieuwe_kluis())
        menu()

    elif keuze == 3:
        print(kluis_openen())
        menu()

    elif keuze == 5:
        exit()

    else :
        print('Verkeerde invoer')

menu()
