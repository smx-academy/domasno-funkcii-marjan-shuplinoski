def prosek(lista):
    return sum(lista) / len(lista)


def pecati_ime_prosek(ime, prosek):
    if (prosek >= 2 and prosek <= 3):
        print("Ucenikot {} ima dovolen uspeh so {}.".format(ime, prosek))
    elif (prosek > 3 and prosek <= 4):
        print("Ucenikot {} ima sreden uspeh so {}.".format(ime, prosek))
    elif (prosek > 4 and prosek <= 5):
        print("Ucenikot {} ima odlicen uspeh so {}.".format(ime, prosek))


ime = input("Vnesete go vaseto ime: ")
lista_oceni = list()
while True:
    ocena = int(input("Vnesi ocena: (1-5): "))
    lista_oceni.append(ocena)
    da_ne = input("Da prodolzime? (da/ne) ")
    if (da_ne == "ne"):
        break
prosek_oceni = prosek(lista_oceni)
pecati_ime_prosek(ime, prosek_oceni)
