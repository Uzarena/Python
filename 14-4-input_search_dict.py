dukon = {"olma":20000,
         "gilos":30000,
         "anor":15000,
         "banan":19000,
         "aplesin":50000,
         "nok":25000}

bozorlik = []

bor_tovar = []
yuq_tovar = []

money = int(input("Qancha mablag\'ingiz bor? "))
meva_soni = int(input("Necha turdagi meva xarid qilmoqchisiz? "))

for n in range(0,meva_soni):
    bozorlik.append(input(f"{n+1}-meva nomini kiriting: "))

for tovar in bozorlik:
    if tovar in dukon:
        bor_tovar.append({tovar})
        print(f"{tovar.title()}ning narxi {dukon[tovar]} so\'m")
    else:
        yuq_tovar.append({tovar})

print(f"Afsuski, do\'konimizda {(yuq_tovar)} tugab qolibdi.")