#counter loop
def f3 (maxVal) :
    getal = 1
    for item in range(1,maxVal +1) :
        getal = getal * item
    return getal

s=(1,2,3)
print(f3(s))
