import math

def negyzetgyok():
    # feladatleírás

    szam = float(input("Adjon meg egy számot!"))
    if szam >= 0:
        gyok = math.sqrt(szam)
        pprint(gyok)
    else:
        print("HIBA: negatív szám gyökét akarja számolni!")

