pyt_dict = {"print":"matnni ekranga chiqaradi",
            "range":"0 dan boshlab belgilangan songacha list chiqaradi",
            "if, else, elif":"bular shart operatorlari",
            "integer":"butun son",
            "float":"onlik son",
            "string":"matnli uzgaruvchi",
            "upper, lower, capitalize, title":"bular harflarning registrlari",
            "del, append, insert, remove":"bular, listlar, uzgaruvchilar bilan ishlovchilar",
            "for":"bu takrorlanish operati",
            "input":"kiritish operatori",
            "%,//, **":"qoldiq, bulganda asosiy qism, daraja",
            "get":"kutubxonada bormi yoki yuqligini aniqlaydi",
            "boolean":"logik qiymat"}

word = input("Biror so\'z kiriting: ")
print({pyt_dict.get(word, "Bunday birikma mavjud emas!")})