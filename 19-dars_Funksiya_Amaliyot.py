# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 17:34:52 2022

@author: Asadbek
"""

# =============================================================================
# def yosh_hisobla(ism, familiya, t_yil):
#     """Foydalanuvchi ism sharifini so'rab, 
#     uning tug'ilga yilini hisoblaydigan funksiya"""
#     print(f"Foydalanuvchi ismi: {ism.title()}\n"
#           f"Foydalanuvchi familiyasi: {familiya.title()}\n"
#           f"{ism.title()} {2022-t_yil} yoshda\n")
# yosh_hisobla('asadbek', 'xolboyev', 2001)    
# =============================================================================

# =============================================================================
# def darajani_hisobla(son):
#     """Foydalanuvchidan son olib, 
#     uning kvadrati va kubini konsolga chiqaruvchi funksiya"""
#     print(f"{son} ning kvadrati {son**2}, kubi {son**3} ga teng.")
# darajani_hisobla(-9)
# =============================================================================


# =============================================================================
# def son_juftmi(son):
#     """Foydalanuvchidan son olib, 
#     son juft yoki toqligini konsolga chiqaruvchi funksiya"""
#     if son%2 == 0:
#         print(f"{son} soni juft son")
#     else:
#         print(f"{son} soni toq son")
# son_juftmi(68)
# =============================================================================


# =============================================================================
# def sonni_tekshir(son1, son2):
#     """Sonni katta kichikka tekshiruvchi funksiya"""
#     if son1>son2:
#         print(f"{son1}>{son2}")
#     elif son1 == son2:
#         print("Sonlar teng")
#     else:
#         print(f"{son1}<{son2}")
# sonni_tekshir(23, 20)
# =============================================================================


# =============================================================================
# def darajani_hisobla(x, y):
#     """Foydalanuvchidan x va y sonlarini olib,
#     x^y ni konsolga chiqaruvchi funksiya"""
#     print(f"{x} ning {y}-darajasi {x**y} ga teng.")
# darajani_hisobla(5, 2)
# =============================================================================


def bolinish_alomatlari(son):
    """Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan sonlarga
    qoldiqsiz bo'linishini tekshiruvchi funksiya"""
    for n in range(2,11):
        if son%n == 0:
            print(f"{son} {n} ga qoldiqsiz bo'linadi.")
        
bolinish_alomatlari(25)
        