malibus = []
for n in range(10):
    new_car = {
        'model':'malibu',
        'rang':'oq',
        'yil':2018,
        'narx':13000,
        'probeg':50000,
        'uzatma':'avtomat'
    }
    malibus.append(new_car)

for malibu in malibus[:2]:
    malibu['rang']='mokriy'

for malibu in malibus[2:6]:
    malibu['rang']='qora'

for malibu in malibus[2:6]:
    malibu['yil']=2022

for malibu in malibus[2:6]:
    malibu['narx']=15000
    malibu['uzatma']='mexanika'

for malibu in malibus:
    if malibu['uzatma']=='avtomat':
        malibu['narx']='20000'
    else:
        malibu['narx'] = '18000'

for malibu in malibus:
    print(malibu)