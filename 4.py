def plostina(strana1, strana2):
    return strana1 * strana2


def perimetar(strana1, strana2):
    return 2 * (strana1 + strana2)


strana1 = int(input("Vnesi ja stranata 1 : "))
strana2 = int(input("Vnesi ja stranata 2 : "))

odberi = input("Dali sakate da presmetate (plostina/perimetar) ")

if (odberi == "plostina"):
    plostina_pravoagolnik = plostina(strana1, strana2)
    print("Plostinata na pravoagolnik so strani {} i {} iznesuva {}".format(strana1, strana2, plostina_pravoagolnik))
elif (odberi == "perimetar"):
    perimetar_pravoagolnik = perimetar(strana1, strana2)
    print("Perimetarot na pravoagolnik so strani {} i {} iznesuva {}".format(strana1, strana2, perimetar_pravoagolnik))

