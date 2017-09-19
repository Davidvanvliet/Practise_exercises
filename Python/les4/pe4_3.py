def lang_genoeg(hoogte) :
    if (hoogte) >= 120 :
        return "Je bent lang genoeg voor de attractie"
    else :
        return "Sorry, je bent te klein"

res = lang_genoeg(130)
print(res)
