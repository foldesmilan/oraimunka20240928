def kocka():
    # feladat leírás

    el = int(input("Kérem adjon meg egy él értéket!"))
    if el<=0:
        print("")
    else:
        felszin = 6 * el**2
        terfogat = pow(el, 3)

        print("A kocka felszíne: "+str(felszin)+", térfogata: "+str(terfogat)+".")