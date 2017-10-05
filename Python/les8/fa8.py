#1723682
#David van Vliet

stations = ['schagen', 'heerhugowaard', 'alkmaar', 'castricum', 'zaandam', 'amsterdam sloterdijk', 'amsterdam centraal', 'amsterdam amstel', 'utrecht centraal', '’s-hertogenbosch', 'eindhoven', 'weert', 'roermond', 'sittard', 'maastricht']

def inlezen_beginstation(stations):     #input krijgen voor het beginstation. Als het een foute invoer heeft, opnieuw vragen
    beginstation = input("Wat is je begin station?")
    while beginstation not in stations:
        print("wrong station")
        beginstation = input("Wat is je begin station?")
    return beginstation

beginstation = inlezen_beginstation(stations)

def inlezen_eindstation(stations, beginstation):    #input krijgen voor het eindstation. Als het een foute invoer heeft, opnieuw vragen.
    while True:
        eindstation = input("Wat is je eind station?")
        if eindstation in stations:
            if stations.index(eindstation) < stations.index(beginstation):       #Als het eindstation voor het beginstation staat opnieuw vragen
                print("Uw eindstation staat voor het beginstation. Dit kan niet!")
            else:
                return eindstation
        else:
            print("Wrong station")

eindstation = inlezen_eindstation(stations, beginstation)

def omroepen_reis(stations, beginstation, eindstation):
    positie1 = stations.index(beginstation) +1      #Beginstation index
    positie2 = stations.index(eindstation) +1       #Eindstation index
    print("Het beginstation ", beginstation, "is het ", positie1, "e station in het traject")
    print("Het eindstation ", eindstation, "is het ", positie2, "e station in het traject")
    afstand = positie2 - positie1       #afstand berekenen door het eindstation index - beginstation index te berekenen
    print("De afstand bedraagt ", afstand, "station(s)")
    prijs = afstand * 5     #Prijs van het ticket berekenen door de afstand (index) * 5 uit te rekenen
    print("De prijs van het kaartje is ", prijs, "euro")
    print("Jij stapt in de trein in ", beginstation)
    print(*stations[positie1:positie2 -1], sep='\n - ')     #tussenstations printen
    print("Jij stapt uit in ", eindstation)

print(omroepen_reis(stations, beginstation, eindstation))
