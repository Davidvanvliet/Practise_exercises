prijzen = [12.50, 9.99, 7.75, 6.00, 1.89, 25.00]
def kleinste_en_grootste():
    mini = min(prijzen)
    maxi = max(prijzen)
    antw = [mini, maxi]
    return tuple(antw)
print(kleinste_en_grootste())