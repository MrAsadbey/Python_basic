# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 20:30:52 2022

@author: Asadbek
"""

# =============================================================================
# ismlar = []
# n = 1
# while True:
#     savol = f"{n}-do'stingiz ismini kiriting:  "
#     ism = input(savol)
#     ismlar.append(ism)
#     takrorlash = input("Yana ism qo'shasizmi? ha/yo'q  ")
#     n+=1
#     if takrorlash != 'ha':
#         break
# print("Do'stlaringiz ro'yhati:")
# for ism in ismlar:
#     print(ism.title())
# =============================================================================


# =============================================================================
# dostlar = {}
# ishora = True
# while ishora:
#     ism = input("Do'stingiz ismini kiriting: ")
#     yosh = input(f"{ism.title()}ning yoshini kiriting: ")
#     dostlar[ism]=int(yosh)
#     
#     javob = input("Yana ma'lumot qo'shasizmi? ha/yo'q  ")
#     if javob == 'yo\'q':
#         ishora=False
# for ism, yosh in dostlar.items():
#     print(f"{ism.title()}ning yoshi {yosh} da")
# =============================================================================


# =============================================================================
# cars = ['lacetti','nexia','toyota','nexia','audi','malibu','nexia']
# while 'nexia' in cars: # toki nexia cars ro'yxati ichida ekan...
#     cars.remove('nexia') # nexia ni ro'yxatdan olib tashla
# print(cars)
# =============================================================================


talabalar = ['Salim', 'Olim', 'Nizom', 'Botir']
baholangan_talabalar = {}
while talabalar:
    talaba = talabalar.pop()
    baho = input(f"{talaba.title()}ning bahosini kiriting: ")
    print(f"{talaba.title()} baholandi\n")
    baholangan_talabalar[talaba] = int(baho)
    