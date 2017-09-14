leeftijd = int(input('Wat is je leeftijd: '))
paspoort = input('Heb je een paspoort: ')
stemmen = 'ja'
if leeftijd >= 18 and paspoort <= stemmen :
    print('gefeliciteerd, U mag stemmen')
else :
    print('U mag helaas niet stemmen')
