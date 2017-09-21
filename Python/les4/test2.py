#accumulator loop
def f2 (sequence) :
    getal = 1000000
    for item in sequence :
        if item < getal :
            getal = item
    return getal

s=[500000]
print (f2(s))
