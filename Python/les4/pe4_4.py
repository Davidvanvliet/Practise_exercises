#1723682
#David van Vliet

#Nieuw wachtwoord laten instellen met minimale eisen en mag niet gelijk zijn met het oude wachtwoord
def new_password(oldpassword, newpassword) :
    if oldpassword != newpassword \
        and len (newpassword) >= 6 :
        return True
    else :
        return False

res = new_password('vakProg17', 'python17')
print(res)

