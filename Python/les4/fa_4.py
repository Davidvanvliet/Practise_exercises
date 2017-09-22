#1723682
#David van Vliet

#deel 1
def standaardprijs(afstandKM) :
    prijs = 0.80 * afstandKM
    if afstandKM > 50 :
        prijs = 0.60 * afstandKM + 15
    if afstandKM < 0 :
        prijs = 0.00 * afstandKM
    return prijs

#deel 2
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

#deel 3
print('11 jaar oud, geen weekend en 49 km, verwacht: 25.48', ritprijs(11, 'ja', 49))

