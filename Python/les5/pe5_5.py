#1723682
#David van Vliet

#berekend het gemiddelde van de lengte van de woorden in de input
lijst = input('Schrijf uw zin: ')
woorden = lijst.split()
lengte = sum(len(woord) for woord in woorden) / len(woorden)
print (lengte)
