def prosek(lista):
    return sum(lista) / len(lista)

lista = [1,2,3,4,5,6,7,8,9,100]
prosek_lista = prosek(lista)
print("Prosekot na listata {} e {}".format(lista,prosek_lista))