#1723682
#David van Vliet

#bereken de gemiddelde kosten per persoon
def kosten (personen):
    try:
        print(4356/personen)

    except ZeroDivisionError:
        print ('Delen door 0 kan niet')

    except ValueError:
        print ('Gebruik cijfers voor het invoeren van het aantal')

    except:
        print('Onjuiste invoer')


kosten (int(input('Aantal personen: ')))