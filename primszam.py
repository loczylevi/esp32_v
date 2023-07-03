osztok = 0
bekeres = int(input("kérek számot "))
szam= 0
while szam <= 10000000:
    try:
        if bekeres % szam == 0:
            osztok = osztok + 1
        szam = szam + 1
    except:
        print("0-val nem osztunk gec")
        szam=+1
if osztok == 2:
    print(f"ez a szám {bekeres} primszám")
else:
    print(f"ez a szám {bekeres} NEM primszám")

print(f"ennek a számnak ennyi ósztója van: {osztok}")
