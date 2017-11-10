#1723682
#David van Vliet

#Als je te klein bent zeggen dat ze niet in de attractie mag. Ben je groter of even groot als 120cm, dan mag je wel
def lang_genoeg(hoogte) :
    if (hoogte) >= 120 :
        return "Je bent lang genoeg voor de attractie"
    else :
        return "Sorry, je bent te klein"

res = lang_genoeg(130)
print(res)
