#1723682
#David van Vliet

#Alleen de klinkers printen
s = ("Guido van Rossum heeft programmeertaal Python bedacht.")
for letter in s:
    if letter in 'aeiou':
        print(letter)
