#1723682
#David van Vliet

def grootte(woorden, size):
    resultaat = []  #nieuwe list voor het resultaat
    for woord in woorden:
        if len(woord) == 4:
            resultaat.append(woord) #alle woorden met 4 letters worden toegevoegd aan deze list
    return resultaat
gewenst = grootte(["boter", "kaas", "bier", "pizza", "thee", "drop", "koek", "cola", "boterham", "stamppot"],4)
print (gewenst)
