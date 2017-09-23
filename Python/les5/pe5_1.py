#1723682
#David van Vliet

#convereerd van Celsius naar Fahrenheit
def convert(Celsius) :
    Fahrenheit = convert(Celsius)*1.8+32
    return (Fahrenheit)

#Geformatteerd printen
def table() :
    print('(0) (1)'.format('  F  ', '  C'))
    for Celsius in range(-30, 50, 10):
        Fahrenheit = convert(Celsius)
        print('[0:5]  {1:5.1f}'.format(Fahrenheit, Celsius))

