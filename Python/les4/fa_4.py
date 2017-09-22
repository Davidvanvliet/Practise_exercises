#1723682
#David van Vliet

#deel 1: Iedere treinrit kost 80 cent per kilometer, maar als de rit langer is dan 50 kilometer betaal je
# een vast bedrag van €15,- plus 60 cent per kilometer. Ga bij invoer van negatieve afstanden uit van
# een afstand van 0 kilometer (prijs is dan dus 0 Euro).
def standaardprijs(afstandKM) :
    prijs = 0.80 * afstandKM
    if afstandKM > 50 :
        prijs = 0.60 * afstandKM + 15
    if afstandKM < 0 :
        prijs = 0.00
    return prijs

#deel 2: Op werkdagen reizen kinderen (onder 12 jaar) en ouderen (65 en ouder) met 30% korting. In het
# weekend reist deze groep met 35% korting. De overige leeftijdsgroepen reizen betalen de gewone
# prijs, behalve in het weekend, dan reist deze leeftijdsgroep met 40% korting.
def ritprijs(leeftijd, weekendrit, afstandKM) :
    ritprijs = standaardprijs(afstandKM)
    if weekendrit == 'ja' or weekendrit == 'Ja' :
        if leeftijd < 12 or leeftijd >= 65 :
           prijs = (ritprijs/100*65)
        else :
             prijs = (ritprijs/100*60)
    else :
        if leeftijd < 12 or leeftijd >= 65 :
             prijs = (ritprijs/100*70)
        else :
            prijs = standaardprijs(afstandKM)
    return prijs

#deel 3: Testen
print('11 jaar oud, wel weekend en 49 km, verwacht: 25.48', ritprijs(11, 'ja', 49))
print('12 jaar oud, wel weekend en 49 km, verwacht: 23.52', ritprijs(12, 'ja', 49))
print('64 jaar oud, wel weekend en 49 km, verwacht: 23.52', ritprijs(64, 'ja', 49))
print('65 jaar oud, wel weekend en 49 km, verwacht: 25.48', ritprijs(65, 'ja', 49))
print('11 jaar oud, geen weekend en 49 km, verwacht: 27.44', ritprijs(11, 'nee', 49))
print('12 jaar oud, geen weekend en 49 km, verwacht: 39.20', ritprijs(12, 'nee', 49))
print('64 jaar oud, geen weekend en 49 km, verwacht: 39.20', ritprijs(64, 'nee', 49))
print('65 jaar oud, geen weekend en 49 km, verwacht: 27.44', ritprijs(65, 'nee', 49))
print('11 jaar oud, geen weekend en -10 km, verwacht: 0.0', ritprijs(11, 'nee', -10))
print('11 jaar oud, geen weekend en 0 km, verwacht: 0.0', ritprijs(11, 'nee', 0))
print('11 jaar oud, geen weekend en 49 km, verwacht: 0.56', ritprijs(11, 'nee', 1))
print('11 jaar oud, geen weekend en 49 km, verwacht: 28.0', ritprijs(11, 'nee', 50))
print('12 jaar oud, geen weekend en 49 km, verwacht: 0.0', ritprijs(12, 'nee', -10))
print('12 jaar oud, geen weekend en 49 km, verwacht: 0.8', ritprijs(12, 'nee', 1))
print('12 jaar oud, geen weekend en 49 km, verwacht: 40.0', ritprijs(12, 'nee', 50))
print('12 jaar oud, wel weekend en 50 km, verwacht: 0.80', ritprijs(12, 'ja', 50))
print('12 jaar oud, wel weekend en -10 km, verwacht: 0.0', ritprijs(12, 'ja', -10))
print('12 jaar oud, wel weekend en 1 km, verwacht: 0.48', ritprijs(12, 'ja', 1))
print('64 jaar oud, wel weekend en 50 km, verwacht: 24.0', ritprijs(64, 'ja', 50))
print('65 jaar oud, wel weekend en 50 km, verwacht: 26.0', ritprijs(65, 'ja', 50))
print('64 jaar oud, wel weekend en -10 km, verwacht: 0.0', ritprijs(64, 'ja', -10))
print('64 jaar oud, wel weekend en 1 km, verwacht: 0.48', ritprijs(64, 'ja', 1))
print('65 jaar oud, wel weekend en -10 km, verwacht: 0.0', ritprijs(65, 'ja', -10))
print('65 jaar oud, wel weekend en 1 km, verwacht: 0.52', ritprijs(65, 'ja', 1))