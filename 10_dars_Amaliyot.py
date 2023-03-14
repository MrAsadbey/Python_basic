# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 16:11:51 2022

@author: Asadbek
"""

# =============================================================================
# avtolar = ['audi', 'bmw', 'volvo', 'kia', 'hyundai']
# for avto in avtolar:
#     if avto == 'bmw':
#         print(avto.upper())
#     else:
#         print(avto.title())
# =============================================================================

# =============================================================================
# ism = input("Ismingiz nima? >>> ")
# if ism.lower() != 'ali' :
#     print(f'Uzr {ism.title()}, biz Alini kutyapmiz')
# else :
#     print("Salom Ali")
# =============================================================================

# =============================================================================
# yosh = int(input("Yoshingiz nechida? >>> "))
# if yosh>=18 :
#     print("Xush kelibsiz")
# else : 
#     print("Kirish mumkin emas")
# =============================================================================
    
# =============================================================================
# login = input("Yangi login yarating: >>>> ")
# if len(login)<=5 :
#     print("Login 5 harfdan ko'p bo'lishi kerak.")
# =============================================================================
    
# =============================================================================
# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#     if car == 'gm' :
#         print(car.upper())
#     else:
#         print(car.title())
# =============================================================================

# =============================================================================
# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#     if car != 'gm' :
#         print(car.title())
#     else:
#         print(car.upper())
# =============================================================================

# =============================================================================
# login = input("Loginingizni kiriting: >>>")
# if login.lower() == "admin" :
#     print(f"Xush kelibsiz {login.title()}. Foydalanuvchilar ro'yhatini ko'rasizmi?")
# else :
#     print(f"Xush kelibsiz {login.title()}!")
# =============================================================================

# =============================================================================
# print("Hohlagan ikkita sonni kiriting")
# a = int(input("Birinchi sonni kiriting: "))
# b = int(input("Ikkinchi sonni kiriting: "))
# if a==b :
#     print("Sonlar teng")
# =============================================================================


# =============================================================================
# a = int(input("Hohlagan sonni kiriting: >>> "))
# if a<0:
#     print("Manfiy son")
# else :
#     print("Musbat son")
#     
# =============================================================================


a = int(input("Hohlagan sonni kiriting: >>> "))
if a>=0:
    print(f"Sonning ildizi {a**(1/2)} ga teng")
else :
    print("Musbat son kiriting!")