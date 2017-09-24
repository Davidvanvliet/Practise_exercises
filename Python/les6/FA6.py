#1723682
#David van Vliet

def menu():
    print('1: Ik wil weten hoeveel kluizen nog vrij zijn \n 2: Ik wil een nieuwe kluis \n 3: Ik wil even iets uit mijn kluis halen')
    keuze = input()

    if keuze == '1':
        print('er zijn 12 kluizen over')
        menu()

    if keuze == '2':
        print('Uw nieuwe kluisnummer is: 1')
        menu()

    if keuze == '3':
        print('Kluisnummer: ')
        input()
        print('Wachtwoord: ')
        input()
        menu()

print(menu())


