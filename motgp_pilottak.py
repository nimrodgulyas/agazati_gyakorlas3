class Pilota:
    def __init__(self, nev, csapat, nemzetiseg, rajtszam, osszpontszam):
        self.nev = nev
        self.csapat = csapat
        self.nemzetiseg = nemzetiseg
        self.rajtszam = int(rajtszam)
        self.osszpontszam = int(osszpontszam)

fajl = open("202__2/pilottak.txt" , "r", encoding="utf-8")

pilotak = []
for sor in fajl:
    adatok = sor.strip().split(";")
    hozzaad = Pilota(
        adatok[0],
        adatok[1],
        adatok[2],
        adatok[3],
        adatok[4]
    )
    pilotak.append(hozzaad)
    fajl.close


print(f"3.2 feladat: Az állományban {len(pilotak)} pilót adatai szerepelnek.")

legtobb_pont = pilotak[0]
for i in pilotak:
    if  i.osszpontszam > legtobb_pont.osszpontszam:
        legtobb_pont = i

print(f"3.3 feladat: A legtöbb pontot szerző pilóta: Név: {legtobb_pont.nev}\n Csapat: {legtobb_pont.csapat}\n Nemzetiség: {legtobb_pont.nemzetiseg}\n Rajtszám: {legtobb_pont.rajtszam}\n Összpontszám: {legtobb_pont.osszpontszam}")

print("3.4 feladat")
csapatnev = str(input("Írjon be egy csapatnevet: "))

van = False
for i in pilotak:
    if i.csapat == csapatnev:
        print(f"A {csapatnev} pilótái: {i.nev}")
        van = True

if van == False:
        print("Nem található a csapat!")

print("3.5 feladat")
osszpontszam = 0
darab = 0
for i in pilotak:
    if i.nemzetiseg == "spanyol":
        darab += 1
        osszpontszam += i.osszpontszam
atlag = osszpontszam / darab
print(f"A spanyol pilóták átlag pontszáma: {round(atlag, 2)}")