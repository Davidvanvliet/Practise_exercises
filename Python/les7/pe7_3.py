#1723682
#David van Vliet

klas = {'piet': 6, 'henk': 7, 'sjors': 8, 'klaas': 9, 'kees': 10, 'gert': 4, 'gerard': 10, 'anton': 7}
klas = dict((x, y) for x, y in klas.items() if y >= 9)
print(klas)