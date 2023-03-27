davlatlar = {
    'uzbekistan':{'Poytaxti':'Tashkent',
                  'Hududi':'448 978 kv.km',
                  'Aholisi':'38 mln.',
                  'Pul birligi':'so\'m'
                  },
    'russia':{'Poytaxti':'Moskva',
                  'Hududi':'17 098 246 kv.km',
                  'Aholisi':'144 mln.',
                  'Pul birligi':'rubl'
                  },
    'aqsh':{'Poytaxti':'Washington',
                  'Hududi':'9 631 418 kv.km',
                  'Aholisi':'327 mln.',
                  'Pul birligi':'dollar'
                  },
    'malayziya':{'Poytaxti':'Kuala-Lumpur',
                  'Hududi':'329 750 kv.km',
                  'Aholisi':'25 mln.',
                  'Pul birligi':'ringgit'
                  }
}

davlat = input("Davlat nomini kiriting: ").lower()

if davlat in davlatlar:
    info = davlatlar[davlat]
    print(
        f"\n{davlat.title()} to\'g\'risida ma\'lumotlar:"
        f"\nPoytaxti: {info['Poytaxti']}"
        f"\nHududi: {info['Hududi']}"
        f"\nAholisi: {info['Aholisi']}"
        f"\nPul birligi: {info['Pul birligi']}")
else:
    print("Bunday ma\'lumot mavjud emas!")