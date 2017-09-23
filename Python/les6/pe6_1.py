#1723682
#David van Vliet

#maandnummers koppelen aan de seizoen namen
def seizoen(maand):
    if maand in ('12', '1', '2'):
        return ('Winter')
    elif maand in ('3', '4', '5'):
        return ('Lente')
    elif maand in ('6', '7', '8'):
        return ('Zomer')
    elif maand in ('9', '10', '11'):
        return ('Herfst')

print(seizoen('9'))