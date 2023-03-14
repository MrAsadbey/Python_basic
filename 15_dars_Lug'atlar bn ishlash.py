# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 20:05:44 2022

@author: Asadbek
"""

# =============================================================================
# talaba = {
#     'ism':'ali',
#     'familiya':'shamsiyev',
#     'yosh':22,
#     'fakultet':'matematika',
#     'kurs':4
#     }
# print(talaba.items())
# 
# for kalit, qiymat in talaba.items():
#     print(f"Kalit: {kalit}")
#     print(f"Qiymat: {qiymat} \n")
# =============================================================================
    

# =============================================================================
# telefonlar = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10pro',
#     'orif':'nokia 3310'
#     }
# for key, value in telefonlar.items():
#     print(f"{key.title()}ning telefoni {value}")
# =============================================================================


# =============================================================================
# mahsulotlar = {
#     'olma':10000,
#     'behi':15000,
#     'banan':25000,
#     'uzum':5000,
#     'shaftoli':8000
#     }
# #print(mahsulotlar.keys())
# # =============================================================================
# # print("do'kondagi mahsulotlar: ")
# # for mahsulot in mahsulotlar.keys():
# #     print(mahsulot.title())
# # =============================================================================
# bozorlik = ['olma', 'uzum','anor', 'hurmo']
# for mahsulot in mahsulotlar:
#     if mahsulot in bozorlik:
#         print(f"{mahsulot.title()}ning narhi {mahsulotlar[mahsulot]} so'm") 
#         
# for buyum in bozorlik:
#     if buyum not in mahsulotlar:
#         print(f"Iltimos, do'koningizga {buyum}ni ham olib keling.")
# =============================================================================
    
telefonlar = {
     'ali':'iphone x',
     'vali':'galaxy s9',
     'olim':'mi 10pro',
     'orif':'nokia 3310',
     'sanjar':'iphone x',
     'holiq':'galaxy s9',
     'samad':'galaxy s9',
     'halima':'huawei p30'
     }
# =============================================================================
# print("Foydalanuvchilar quydagi telefonlarni ishlatishadi: \n")
# for tel in telefonlar.values():
#     print(tel)
# =============================================================================
print("Foydalanuvchilar quydagi telefonlarni ishlatishadi: \n")
for tel in set(telefonlar.values()):
    print(tel)