#1723682
#David van Vliet

import time
b = 7

#verdubbeld b
def verdubbelB():
    global b
    b = b + b


verdubbelB()

print(b)


#zet de tijd in een mooie layout met uur:minuten:seconden
print(time.strftime(("%H:%M:%S")))




def f(y):
    return 2 * y + 1

def g(x):
    return 5 + x + 10

#2 def uitkomsten bij elkaar optellen
print(f(3) + g(3))