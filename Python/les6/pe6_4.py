#1723682
#David van Vliet

studentencijfers = [ [95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0] ]
def gemiddelde_per_student(studentencijfers):
    antw = [sum(b) for b in studentencijfers]   #cijfers per student optellen
    antw = [i / 3 for i in antw]    #cijfers delen door 3 voor een gemiddelde er student
    return antw

def gemiddelde_van_alle_studenten(studentencijfers):
    antw = [sum(e) / len(e) for e in zip(*studentencijfers)]    #gemiddelde per lengte in de string
    return antw

print(gemiddelde_per_student(studentencijfers))
print(gemiddelde_van_alle_studenten(studentencijfers))
