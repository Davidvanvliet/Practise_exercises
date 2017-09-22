#1723682
#David van Vliet

def standaardprijs(afstandKM) :
    prijs = 0.80 * afstandKM
    if afstandKM > 50 :
        prijs = 0.60 * afstandKM + 15
    if afstandKM < 0 :
        prijs = 0.00 * afstandKM
    return prijs

def ritprijs(leeftijd, weekendrit, afstandKM) :
    ritprijs = standaardprijs(afstandKM)
    if weekendrit == 'ja' or weekendrit == 'Ja' :
        if leeftijd < 12 or leeftijd >= 65 :
           prijs =  (ritprijs/100*65)
        else :
             prijs = (ritprijs/100*60)
    else :
        if leeftijd < 12 or leeftijd >= 65 :
             prijs = (ritprijs/100*70)
        else :
            prijs = standaardprijs(afstandKM)
    return print(prijs)

leeftijd = 11
weekendrit = 'ja'
afstandKM = 60

ritprijs(leeftijd, weekendrit, afstandKM)

print (ritprijs)