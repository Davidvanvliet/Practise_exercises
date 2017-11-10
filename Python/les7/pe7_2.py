#1723682
#David van Vliet

#Checken of de string 4 letters heeft
str = ()
inp = input("Geef een string van vier letters: ")
while len(inp) != 4:
    print(inp, "heeft", len(inp), "letters")
    inp = input("Geef een string van vier letters: ")
while len(inp) == 4:
    print("Inlezen van correcte string: ", inp, "is geslaagd")
    break
