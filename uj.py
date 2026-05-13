class Pilotak:
    def __init__(self, nev, csapat, nemzetiseg, rajtszam, osszpontszam):
        self.nev = nev
        self.csapat = csapat
        self.nemzetiseg = nemzetiseg
        self.rajtszam = int(rajtszam)
        self.osszpontszam = int(osszpontszam)
fajl = open("202__2/pilottak.txt" , "r", encoding="utf-8")

pilota = []
for sor in fajl:
    adatok = sor.strip().split(";")
    hozzaad = Pilotak(
        adatok[0],
        adatok[1],
        adatok[2],
        adatok[3],
        adatok[4]
    )
    pilota.append(hozzaad)
fajl.close()


legtobb_pont = 0
legtobb_pontupilota = None
for i in pilota:
    if i.osszpontszam > legtobb_pont:
        legtobb_pont = i.osszpontszam
        legtobb_pontupilota = i.nev

print(legtobb_pontupilota)

asdad = str(input("random:"))
print(asdad)