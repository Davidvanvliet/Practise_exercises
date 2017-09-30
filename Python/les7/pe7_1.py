#1723682
#David van Vliet

getallen = []   #nieuwe list maken van de inputs
inp = (int(input("Geef een getal: ")))
while inp != 0:
    getallen.append(inp)    #inputs in de list zetten
    inp = (int(input("Geef een getal: ")))

x = len(getallen)
y = sum(getallen)
print("Er zijn", x, "getallen ingevoerd, de som is: ", y)
