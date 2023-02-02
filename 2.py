def zbir(broj1, broj2):
    zbir = broj1 + broj2
    if (zbir % 2 == 0):
        print("{} + {} = {} , brojot e paren".format(broj1, broj2, zbir))
    else:
        print("{} + {} = {} , brojot e neparen".format(broj1, broj2, zbir))


broj1 = int(input("Vnesi broj 1 : "))
broj2 = int(input("Vnesi broj 2 : "))

zbir(broj1, broj2)
