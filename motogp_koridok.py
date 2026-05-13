import random

def gyors_kor(korido):
    if korido < 105:
        return True
    else:
        return False

hany_volt = 0
for i in range(120):
    szam = random.randint(95, 120)
    if gyors_kor(szam) == True:
        hany_volt += 1

print(f"A 120 körből {hany_volt} volt 105 másodpercnél gyorsabb")
print(f"Ez az összes kör: {round(hany_volt / 120 * 100, 2)}%-a.")