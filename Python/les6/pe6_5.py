#1723682
#David van Vliet

#Tafels berekenen van 1 tot en met 10
for i in range(1, 11):
    for j in range(1, 11):
        print ('{:02}'.format(i),'X','{:02}'.format(j),'=','{:02}'.format(i*j))
