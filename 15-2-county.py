countries = {"uzbekistan":"tashkent","tadjikistan":"dushanbe","kyrgzstan":"bishkek","kazakhstan":"nursultan","afghanistan":"kabul","turkmenistan":"ashghabat"}
print("Davlatlar:")
for davlat in sorted(countries):
    print(davlat.upper())

print(" \nPoytaxtlar:")
for poytaxt in sorted(countries.values()):
    print(poytaxt.title())