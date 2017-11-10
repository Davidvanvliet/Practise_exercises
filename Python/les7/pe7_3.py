#1723682
#David van Vliet

#checken wie een cijfer heeft dat hoger of gelijk is aan 9
klas = {'piet': 6, 'henk': 7, 'sjors': 8, 'klaas': 9, 'kees': 10, 'gert': 4, 'gerard': 10, 'anton': 7}
klas = dict((k, v) for k, v in klas.items() if v >= 9)
print(klas)
