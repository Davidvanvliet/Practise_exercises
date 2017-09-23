#1723682
#David van Vliet

invoer = "5-9-7-1-7-8-3-2-4-8-7-9"
x = invoer.split('-')   #een lijst maken die de variabelen splitst bij een -
print (sorted(x))   #sorteren

print('Het grootste getal is', max(x), 'en kleinste is', min(x))
print('De lengte van de lijst is', len(x), 'en de som is')
# print('Het gemiddelde is:', (sum(x) / float(len(x))))
