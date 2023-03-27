countries = {"uzbekistan":"tashkent","tadjikistan":"dushanbe","kyrgzstan":"bishkek","kazakhstan":"nursultan","afghanistan":"kabul","turkmenistan":"ashghabat"}
davlat = input("O\'zbekistonga chegaradosh bo\'lgan davlat nomini kiriting: ").lower()
if davlat in countries:
    print(f"{davlat.title()} davlati poytaxti {countries[davlat]} shahri!")
else:
    print(countries.get(davlat, "Siz davlat nomini xato kiritdingiz!"))