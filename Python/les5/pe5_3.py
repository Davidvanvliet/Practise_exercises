#1723682
#David van Vliet

#Het textbestand openen in leesmodus en alle regels lezen
infile = open('kaartnummers.txt', 'r')
lijst = infile.readlines()
kaartnummer_lijst = []

#De getallen splitsen met een , om hier aparte nummers van te maken
for nummer in lijst:
    getal = nummer.split(',')
    kaartnummer_lijst.append(int(getal[0]))

#De hoogste en lengte uitrekenen
hoogste = max(kaartnummer_lijst)

regels = len(lijst)


print("Deze file telt", regels, "regels.")
print("Het grootste kaartnummer is:", hoogste, "en dat staat op regel", kaartnummer_lijst.index(hoogste) + 1)

