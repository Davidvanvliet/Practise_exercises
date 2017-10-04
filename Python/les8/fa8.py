#1723682
#David van Vliet

stations = ['schagen', 'heerhugowaard', 'alkmaar', 'castricum', 'zaandam', 'amsterdam sloterdijk', 'amsterdam centraal', 'amsterdam amstel', 'utrecht centraal', '’s-hertogenbosch', 'eindhoven', 'weert', 'roermond', 'sittard', 'maastricht']

def inlezen_beginstation(stations):
    beginstation = input("Wat is je begin station?")
    while beginstation not in stations:
        print("wrong station")
        beginstation = input("Wat is je begin station?")
    return beginstation

beginstation = inlezen_beginstation(stations)

def inlezen_eindstation(stations, beginstation):
    eindstation = input("Wat is je eind station?")
    while eindstation not in stations:
       print("wrong station")
       eindstation = input("Wat is je eind station?")
    while stations.index(eindstation) < stations.index(beginstation):
        print("Uw eindstation staat voor het beginstation. Dit kan niet!")
        eindstation = input("Wat is je eind station?")
    return eindstation

eindstation = inlezen_eindstation(stations, beginstation)

def omroepen_reis(stations, beginstation, eindstation):
    positie1 = stations.index(beginstation) +1
    positie2 = stations.index(eindstation) +1
    positie3 = stations.index(beginstation) +1
    print("Het beginstation ", beginstation, "is het ", positie1, "e station in het traject")
    print("Het eindstation ", eindstation, "is het ", positie2, "e station in het traject")
    afstand = positie2 - positie1
    print("De afstand bedraagt ", afstand, "station(s)")
    prijs = afstand * 5
    print("De prijs van het kaartje is ", prijs, "euro")
    print("Jij stapt in de trein in ", beginstation)
    print(stations[positie3:positie2 -1])
    print("Jij stapt uit in ", eindstation)

print(inlezen_beginstation(stations))
print(inlezen_eindstation(stations, beginstation))
print(omroepen_reis(stations, beginstation, eindstation))
