# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 14:17:58 2022

@author: Asadbek
"""

# =============================================================================
# menu = {
#         "so'msa":6000, 
#         "shashlik":12000, 
#         "lag'mon":18000,
#         "manti":15000,
#         "cola":12000,
#         "fanta":12000
#         }
# buyurtmalar = []
# while True:
#     buyurtma = input("Nima buyurtma qilasiz? ")
#     buyurtmalar.append(buyurtma)
#     javob = input("Yana mahsulot qo'shasizmi? ha/yo'q  ")
#     if javob != "ha":
#         break
# print(buyurtmalar)
# =============================================================================




# =============================================================================
# mahsulotlar = {}
# ishora = True
# while ishora:
#     mahsulot = input("Mahsulot nomini kiriting:  ")
#     narh = input(f"{mahsulot.capitalize()}ning narhini kiriting:  ")
#     mahsulotlar[mahsulot]=int(narh)
#     
#     savol = input("Yana mahsulot qo'shasizmi? ha/yo'q  ")
#     if savol == 'yo\'q':
#         ishora = False
# for mahsulot, narh in mahsulotlar.items():
#     print(f"{mahsulot.capitalize()}ning narhi {narh} so'm.")
# print(mahsulotlar)
# =============================================================================


menu = {
        "so'msa":6000, 
        "shashlik":12000, 
        "lag'mon":18000,
        "manti":15000,
        "cola":12000,
        "fanta":12000
        }
buyurtmalar = []
u_narh = 0
while True :
    buyurtma = input("Nima buyurtma qilasiz? ")
    buyurtmalar.append(buyurtma)
    savol = input("Yana mahsulot qo'shasizmi? ha/yo'q   ")
    if savol != "ha":
        break
while buyurtmalar:
        buyurtma = buyurtmalar.pop()
        if buyurtma in menu.keys():
            narh = menu[buyurtma] 
            print(f"{buyurtma.title()} {narh} so'm turadi.")
            u_narh += narh
        else:
            print(f"Kechirasiz bizda buyurtmalaringiz orasidagi quydagi mahsulotlar yo'q: {buyurtma.title()}")

savol = input("Hisobni bilishni istaysizmi? ha/yo'q   ")
if savol == 'ha':
    while buyurtmalar:
            mahsulot = buyurtmalar.pop()
            if mahsulot in menu.keys():
                narh = menu[mahsulot] 
                print(f"{mahsulot.title()} {narh} so'm turadi.")
    print(f"Umumiy hisob: {u_narh} so'm")