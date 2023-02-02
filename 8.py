def palindrom(zbor):
    svrten = ''.join(reversed(zbor))
    if (zbor == svrten):
        return "Palindrom"
    return "Ne e palindrom"


ime = input("Vnesete go vaseto ime: ")
rezultat = palindrom(ime)
print("Zborot {} e {}".format(ime, rezultat))
