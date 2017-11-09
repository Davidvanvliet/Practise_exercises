#1723682
#David van Vliet

#het bestand kaartnummers.txt wijzigen
bestand = open ('kaartnummers.txt', 'r')
inhoud = bestand.readlines()
print(inhoud)
bestand.close()

for file in inhoud:
    kaartinfo = file.split(', ')
    print('{} heeft kaartnummer:{}'.format (kaartinfo[1].strip(), kaartinfo[0]))
