#1723682
#David van Vliet

invoer = "5-9-7-1-7-8-3-2-4-8-7-9"
getallen = invoer.split('-')   #een lijst maken die de variabelen splitst bij een -
getallen = [int(y) for y in getallen]   #int ervan maken
print (sorted(getallen))   #sorteren

#printen met max, min, len en sum
print('Het grootste getal is', max(getallen), 'en kleinste is', min(getallen))
print('De lengte van de lijst is', len(getallen), 'en de som is', (sum(getallen)))
print('Het gemiddelde is:', (sum(getallen) / float(len(getallen))))
