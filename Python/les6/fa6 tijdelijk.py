#1723682
#David van Vliet

bestand = open('kluizen.txt', 'r')
inhoud = bestand.readlines()
print(inhoud)

def toon_aantal_kluizen_vrij():
    infile = open('kluizen.txt', 'r')
    inhoud = infile.readlines()
    infile.close()

    beschikbaar = 12 - len(inhoud)
    return beschikbaar

# def nieuwe_kluis():
#     kluisnummers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

def menu():
    print('1: Ik wil weten hoeveel kluizen nog vrij zijn \n 2: Ik wil een nieuwe kluis \n 3: Ik wil even iets uit mijn kluis halen')
    keuze = int(input("Uw keuze: "))

    if keuze == '1':
        vrij = toon_aantal_kluizen_vrij()
        print("Er zijn ", vrij, "kluizen vrij")

    elif keuze == '2':
        print('Uw nieuwe kluisnummer is: 1')

    elif keuze == '3':
        print('Kluisnummer: ')
        input()
        print('Wachtwoord: ')
        input()

menu()
