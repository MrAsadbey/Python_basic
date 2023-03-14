# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 15:32:45 2022

@author: Asadbek
"""

# =============================================================================
# py_izohli_lug = {
#     'integer':"Butun son",
#     'float':"O'nlik son",
#     'string':"Matn",
#     'list':"Ro'yxat",
#     'tuple':"O'zgarmas ro'yxat",
#     'if':'shart operatori',
#     'boolen':'Mantiqiy qiymat',
#     'len':'uzunlik'
#     }
# for key in sorted(py_izohli_lug.keys()):
#     print(key)
# print('\n')
# for value in sorted(py_izohli_lug.values()):
#     print(value)
# =============================================================================


# =============================================================================
# dav_poytaxt = {
#     'uzbekistan':'toshkent',
#     'fransiya':'parij',
#     'ispaniya':'madrid',
#     'italiya':'rim',
#     'germaniya':'berlin',
#     'angliya':'london',
#     'rossiya':'moskva',
#     }
# for key in sorted(dav_poytaxt.keys()):
#     print(key.title())
# print('\n')
# for value in sorted(dav_poytaxt.values()):\
#     print(value.title())
# =============================================================================
    
    
# =============================================================================
# dav_poytaxt = {
#     'uzbekistan':'toshkent',
#     'fransiya':'parij',
#     'ispaniya':'madrid',
#     'italiya':'rim',
#     'germaniya':'berlin',
#     'angliya':'london',
#     'rossiya':'moskva',
#     } 
# country = input("Istalgan davlatingizni kiriting: >>> ")
# capital = dav_poytaxt.get(country)
# if capital == None:
#     print("Bunday malumot yo'q")
# else: 
#     print(f"{country.title()} ning poytaxti {capital.title()} shahri")
# =============================================================================


menyu = {
    'kabob':12000,
    'manti':15000,
    'lag\'mon':18000,
    "so'msa":6000,
    'tuxum barak':24000,
    'pelmin':20000,
    'qozon kabob':45000,
    'tabaqa':38000,
    'baliq':40000,
    'KFC':45000
    }
print("Kamida uchta ovqat buyurtma berishingiz kerak.")
buyurtma = []
for n in range(3):
    buyurtma.append(input(f"{n+1}-buyurtmangiz: >>>"))
for taom in buyurtma:
    if taom in menyu:
        print(f"Buyurtma bergan taomingiz {taom.title()} {menyu[taom]} so'm turadi.")
    else:
        print(f"Kechirasiz, bizda buyurtmalaringizdan {taom.title()} yo'q.")