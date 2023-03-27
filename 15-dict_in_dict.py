hamkasblar = {
    'ali':{'familiya':'valiyev',
           'tyil':1997,
           'malumot':'oliy',
           'tillar':['python','c++']},
    'vali':{'familiya':'aliyev',
            'tyil':1999,
            'malumot':'oliy',
            'tillar':['java','kotlin']},
    'hasan':{'familiya':'husanov',
             'tyil':2005,
             'malumot':'orta-maxsus',
             'tillar':['html','css']}
}
for ism, info in hamkasblar.items():
    print(f"\n{ism.title()} {info['familiya'].title()}, "
          f"{info['tyil']}-yilda tug\'ilgan. "
          f"Ma\'lumoti: {info['malumot']}. \n"
          "Quyidagi dasturlash tillarini biladi:")
    for til in info['tillar']:
        print(til.upper())