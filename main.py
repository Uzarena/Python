car1 = {'model':'lacetti',
       'rang':'oq',
       'yil':2018,
       'narx':13000,
       'probeg':50000,
       'uzatma':'avtomat'}

car2 = {'model':'nexia_3',
       'rang':'qora',
       'yil':2015,
       'narx':9000,
       'probeg':89000,
       'uzatma':'mexanik'}

car3 = {'model':'gentra',
       'rang':'qizil',
       'yil':2019,
       'narx':15000,
       'probeg':20000,
       'uzatma':'mexanik'}

cars = [car1, car2, car3]
for car in cars:
    print(f'{car}')