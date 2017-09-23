#1723682
#David van Vliet

infile = open('kaartnummers.txt', 'r')
lijst = infile.readlines()
kaartnummer_lijst = []

for nummer in lijst:
    getal = nummer.split(',')
    kaartnummer_lijst.append(int(getal[0]))

hoogste = max(kaartnummer_lijst)

regels = len(lijst)


print("Deze file telt", regels, "regels.")
print("Het grootste kaartnummer is:", hoogste, "en dat staat op regel", kaartnummer_lijst.index(hoogste) + 1)

