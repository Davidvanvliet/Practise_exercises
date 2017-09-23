#1723682
#David van Vliet

#het bestand kaartnummers.txt wijzigen
outfile = open('kaartnummers.txt', 'w')
outfile.write('Jan Jansen heeft kaartnummer: 325255\n')
outfile.write('Erik Materus heeft kaartnummer: 334343\n')
outfile.write('Ali Ahson heeft kaartnummer: 235434\n')
outfile.write('Eva Versteeg heeft kaartnummer: 645345\n')
outfile.write('Jan de Wilde heeft kaartnummer: 534545\n')
outfile.write('Henk de Vrie heeft kaartnummer: 345355\n')
outfile.close()

#Het bestand kaartnummers.txt lezen
infile = open('kaartnummers.txt', 'r')
inhoud = infile.read()
print(inhoud)
