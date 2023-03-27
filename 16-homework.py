ronaldo = {'familiya': 'Cristiano',
           'ism': 'Ronaldo',
           'kasbi': 'futbolchi',
           'yili': 1985,
           'yoshi': 38,
           'davlati': 'Portugaliya',
           'boshqa': ['Sporting','Manutd','Real','Juventus','Annasr']}

ozodbek = {'familiya': 'Nazarbekov',
           'ism': 'Ozodbek',
           'kasbi': 'qo\'shiqchi',
           'yili': 1974,
           'yoshi': 48,
           'davlati': 'O\'zbekiston',
           'boshqa': ['Bedor','Anjancha','Binafsha','Ayirma','Lola']}

nadal = {'familiya': 'Rafael',
         'ism': 'Nadal',
         'kasbi': 'tennischi',
         'yili': 1986,
         'yoshi': 36,
         'davlati': 'Ispaniya',
         'boshqa': ['Novak Djokovich','Rodjer Federer','Karlos Alkaras','Mariya Sharapova']}

abror = {'familiya': 'Turgunboyev',
         'ism': 'Abrorjon',
         'kasbi': 'founder',
         'yili': 1997,
         'yoshi': 25,
         'davlati': 'O\'zbekiston',
         'boshqa': ['Kvartapp','Smartarena','Puzzle_15','Checkers_AI']}

shaxslar = [ronaldo, ozodbek, nadal, abror]

for shaxs in shaxslar:
    familiya = shaxs["familiya"]
    ism = shaxs['ism']
    kasbi = shaxs['kasbi']
    yili = shaxs['yili']
    yoshi = shaxs['yoshi']
    davlati = shaxs['davlati']
    boshqa = shaxs['boshqa']

#    print(
#        f"{familiya} {ism} {yili}-yilda {davlati} davlatida tug\'ilgan. U hozirda {yoshi} yoshli professional {kasbi}. Teglar {boshqa}"
#    )

    print(f"{familiya} {ism} ning asarlari")
    for bosh in boshqa:
        print(f"{bosh}")