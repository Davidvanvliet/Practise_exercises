#1723682
#David van Vliet

def code(invoerstring): #hier worden de normale letters gencrypted zodat
    encrypted = ""
    for i in invoerstring:
        if i == " ":
            encrypted += "#"
        else:
            encrypted += chr(ord(i)+3) #hier word geencrypted en doorgeteld met 3 letters erna
    return encrypted

print(code("RutteAlkmaarDen Helder"))