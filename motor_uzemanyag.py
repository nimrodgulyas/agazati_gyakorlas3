korok_szama = int(input("Adja meg a versenyen teljesítendő körök számát!: "))
atlag_fogyasztas_egykoron = float(input("Adja meg az egy körre eső átlagos fogyasztást literben!: "))
uzema_tartaly = float(input("Adja meg az üzemanyag-tarály méretét literben!: "))


szukseges = korok_szama * atlag_fogyasztas_egykoron
eleg_uzema = uzema_tartaly - szukseges

print(f"A versenyhez szükséges üzemanyag: {szukseges}")

if eleg_uzema > 0:
    print("A tartály elegendő a versenyhez!")
else:
    print(f"A tartály NEM elegendő! Még {-eleg_uzema} liter üzemanyag szükséges.")
