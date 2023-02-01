def najdolgo_ime(lista):
    najd_ime = max(lista, key=len)
    vkupno = len(lista)
    print("Najdolgoto ime e {}, ima vkupno {} parametri.Listata e {}".format(najd_ime,vkupno,lista))

lista = []
while True:
    zbor = input("Vnesi nekoj zbor: ")
    lista.append(zbor)
    da_ne = input("Dali ke prodolzite (da/ne) ")
    if(da_ne=="ne"):
        break

najdolgo_ime(lista)