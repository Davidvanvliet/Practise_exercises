#1723682
#David van Vliet

#Laten weten door de input of je mag stemmen of niet
leeftijd = int(input('Wat is je leeftijd: '))
paspoort = input('Heb je een paspoort: ')
stemmen = 'ja'
if leeftijd >= 18 and paspoort <= stemmen :
    print('gefeliciteerd, U mag stemmen')
else :
    print('U mag helaas niet stemmen')
