#1723682
#David van Vliet

import random

#Monopoly spel door met random dobbelstenen te gooien
def monopolyworp():
    def worp_werpen():
        return [random.randrange(1,7),random.randrange(1,7)]
    worp = worp_werpen()
    if worp[0] == worp[1]:
        print("{} + {} = {} (Dubbel!)".format(worp[0],worp[1],worp[0]+worp[1]))#hier word gezegd wanneer er dubbel gegooit wrod in de eerste beurt
        worp = worp_werpen()
        if worp[0] == worp[1]:
            print("{} + {} = {} (Dubbel!)".format(worp[0],worp[1],worp[0]+worp[1])) #dit isde eventuele tweede beurt ie dubbel kan zijn
            worp = worp_werpen()
            if worp[0] == worp[1]:
                print("{} + {} = (Direct naar de gevangenis!)".format(worp[0], worp[1]))  # bij de derde keer gooien word er na de beurt de aangegeven tekst weergegeven
            else: print("{} + {} = {}".format(worp[0], worp[1], worp[0] + worp[1]))
        else: print("{} + {} = {}".format(worp[0],worp[1],worp[0]+worp[1]))
    else: print("{} + {} = {}".format(worp[0], worp[1], worp[0] + worp[1]))


print(monopolyworp())