#1723682
#David van Vliet

invoerstring = input('')

def code(invoerstring):
    invoerstring = [ord(c) for c in invoerstring]
    invoerstring = ''.join(chr(i) for i in invoerstring)
    return invoerstring
print(code(invoerstring))



# + 3 doet het nog niet