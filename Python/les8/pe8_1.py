#1723682
#David van Vliet

bruin = {'boxtel', 'best', 'beukenlaan', 'eindhoven', "helmond 't hout", 'helmond', "helmond brouwhuis", 'deurne'}
groen = {'boxtel', 'best', 'beukenlaan', 'eindhoven', 'geldrop', 'heeze', 'weert'}

#print de overeenkomsten, verschillen, en samengevoegd maar 1 keer als die dubbel is
print(bruin & groen)
print(bruin - groen)
print(bruin | groen)
