# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 14:09:14 2022

@author: Asadbek
"""

# =============================================================================
# yosh = int(input("Yoshingiz nechida? >>> "))
# if yosh<=4 :
#     narh=0
# elif yosh<=12:
#     narh=5000
# else:
#     narh=10000
# print(f"Sizga kirish {narh} so'm")
# =============================================================================


# =============================================================================
# kun = input("Bugun nima kun? >>> ")
# if kun.lower() == 'shanba' or kun.lower() == 'yakshanba' :
#     print("Bugun dam olish kuni\n")
# else:
#     print("Bugun ish kuni\n")
# 
# =============================================================================

# =============================================================================
# kun = input("Bugun nima kun? >>> ")
# harorat = float(input("Havo harorati qanday? >>> "))
# if (kun.lower() == 'yakshanba' or kun.lower() == 'shanba') and harorat >= 30 :
#     print("Cho'milgani kettik")
# elif kun.lower() == 'yakshanba' and harorat < 30 :
#     print("Bugun uyda dam olamiz.")
# =============================================================================


# =============================================================================
# a = int(input("Juft son kiriting: >>> "))
# if a%2==0 :
#     print("Raxmat")
# elif a%2!=0:
#     print("Bu juft son emas.")
# =============================================================================


# =============================================================================
# yosh = int(input("Yoshingiz nechchida: "))
# if yosh<=4 or yosh>=60 :
#     narh = 0
# elif yosh<18 :
#     narh = 10000
# else:
#     narh = 20000
# print(f"Siz uchun kirish {narh} so'm.")
# =============================================================================


# =============================================================================
# print("Hohlagan ikkita soningizni kiriting:")
# a = int(input("1-sonni kiriting: "))
# b = int(input("2-sonni kiriting: "))
# if a==b : 
#     print("Sonlar teng")
# elif a>b :
#     print(a,">",b)
# else : 
#     print(a,"<",b)
# =============================================================================


# =============================================================================
# mahsulotlar = ['tuxum','shakar','qaymoq','sut','olma','banan','uzum','to\'rt','pecheniya','kampot']
# print("Kamida 5 ta mahsulot kiriting.")
# savat = []
# savat.append(input("1-mahsulot: "))
# savat.append(input("2-mahsulot: "))
# savat.append(input("3-mahsulot: "))
# savat.append(input("4-mahsulot: "))
# savat.append(input("5-mahsulot: "))
# print(savat)
# if savat:
#     for mahsulot in savat:
#         if mahsulot in mahsulotlar:
#             print(f"{mahsulot} do'konimizda bor.")
#         else:
#             print(f"{mahsulot} do'konimizda yo'q")
# =============================================================================
        

# =============================================================================
# mahsulotlar = ['tuxum','shakar','qaymoq','sut', 'olma' ,'banan','uzum','to\'rt','pecheniya','kampot']
# print("Kamida 5 ta mahsulot kiriting.")
# savat = []
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}- mahsulotni qo'shing: "))
# 
# bor_mahsulot = []
# mavjud_emas = []
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulot.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)
#         
# if mavjud_emas :
#     print(f"Quyidagi mahsulotlar do'konimizda yo'q:")
#     for mahsulot in mavjud_emas:
#         print(mahsulot)
# else:
#     print("Siz so'ragan barcha mahsulotlar do'konimizda bor.")
# =============================================================================


# =============================================================================
# users = ['admin','adminka', 'coder','akmal','anvar']
# login = input("O'z loginingizni kiriting: ")
# if login.lower() in users:
#     print("Bu login band, iltimos yangi login kiriting: ")
# else:
#     print(f"Xush kelibsiz {login}")
# =============================================================================


a = int(input("Istalgan butun sonni kiriting: "))
for n in range(2,11):
    if not (a%n):
        print(f"{a} soni {n} ga qoldiqsiz bo'linadi")
        