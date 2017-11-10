#1723682
#David van Vliet

#iets in het bestand er bij zetten met de a van append
infile = open('hardlopers.txt', 'r')
with open('hardlopers.txt', 'a') as f:
    f.write(input('hardlopers.txt: '))
