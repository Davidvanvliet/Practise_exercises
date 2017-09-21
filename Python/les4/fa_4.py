#1723682
#David van Vliet

def standaardprijs(afstandKM) :
    0.80 * afstandKM
    if afstandKM > 50 :
        0.60 * afstandKM + 15
    if afstandKM < 0 :
        0.00 * afstandKM

def ritprijs(leeftijd, weekendrit, afstandKM) :
    ritprijs == standaardprijs
    if leeftijd < 12 :
        ritprijs/100*70
    else :
        ritprijs == standaardprijs
    if leeftijd >= 65 :
        ritprijs/100*70
    else :
        ritprijs == standaardprijs
    if weekendrit is True :
        if leeftijd < 12 or leeftijd >= 65 :
            ritprijs/100*70
        else :
            ritprijs/100*70
    else :
        ritprijs == standaardprijs
    return ritprijs
print(ritprijs(20, False, 25))
