#1723682
#David van Vliet



lijst = input('Schrijf uw zin: ')
woorden = lijst.split()
lengte = sum(len(woord) for woord in woorden) / len(woorden)
print (lengte)
