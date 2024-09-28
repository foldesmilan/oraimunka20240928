def szog():
    # Szögtípus A program  kérjen be a konzolról egy valós számot! Ha ez a szám 0 és 360 közé esik, akkor legyen egy szög mértéke (pl. 60 fok), egyébként a program adjon hibaüzenetet! Ha lehet, a program írja ki a szög mértéke alapján a szög típusát (pl.: 60 -> hegyesszög)!
vSzam = float(input("kérem adjon meg egy valós számot"))
if (vSzam >= 0) and (vSzam <= 360):
    if vSzam == 0:
        print(str=(vSzam)+" -> nullszög"
    elif (vszam>0) and (vSzam<90):
        print(str=(vSzam)+" -> hegyesszög"
    elif VSZam ==90:
        print(str=(vSzam)+" -> tompaszög"
    elif VSZam>90:
        print(str=(vSzam) + " -> egyenesszög"
        elif (VSZam > 90) and (vSzam < 360)):

    else:
        print("HIBA: Nem megfelelő szögérték!")