menu = {"osh":20000,
         "shavla":30000,
         "norin":15000,
         "baliq":19000,
         "ikra":50000,
         "shashlik":25000,
         "beshmarmoq":75000,
         "tort":50000,
         "kapriz":26000,
         "bahor":7000,
         "mangal":200000}

buyurtmalar = []
print("3 ta taom bering: ")
for n in range(1, 4):
    buyurtmalar.append(input(f"{n}-taomingizni kiriting: ").lower())
for taom in buyurtmalar:
    if taom in menu:
        print(f"{taom.title()}ning narxi {menu[taom]} so\'m!")
    else:
        print(f"Bizda {taom.title()} nomli taom mavjud emas!")