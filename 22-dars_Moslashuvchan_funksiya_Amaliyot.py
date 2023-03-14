# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 21:32:38 2023

@author: Asadbek
"""

# =============================================================================
# def summa(*sonlar):
#     """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
#     yigindi = 0
#     for son in sonlar:
#         yigindi += son
#     return yigindi
# print(summa(1, 2, 5, 6, 8))
# print(summa(1, 2))
# print(summa(5, 8, 9, 4))
# =============================================================================


# =============================================================================
# def summa(x, y, *sonlar):
#     """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
#     return x+y+sum(sonlar)
# print(summa(1, 2, 5, 6, 8))
# print(summa(5, 8, 9, 4))
# print(summa(1, 2))
# =============================================================================


# =============================================================================
# def avto_info(kompaniya, model, **malumotlar):
#     #  **kwargs --> keyword arguments(kalit so'z argumentlar)
#     """Avtomobil haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
#     malumotlar['kompaniya']=kompaniya
#     malumotlar['model']=model
#     return malumotlar
# avto1 = avto_info('Hyundai', 'sanata', rangi="silver", yili= 2022, narhi=30_000)
# avto2 = avto_info('Mercedez', 'AMG', rangi="Qora", narhi=40_000)
# print(avto1)
# =============================================================================



# =============================================================================
# def kopaytma(*sonlar):
#     """Kiritilgan sonlarni ko'paytmasini hisoblaydigan funksiya"""
#     natija = 1
#     for son in sonlar:
#         natija *= son
#     return natija
# print(kopaytma(2, 6, 3, 5))
# print(kopaytma(2, 6, 3, 5, 6, 9, 8 ,5, 7))
# =============================================================================


def talaba_info(ism, familiya, **kwargs):
    """Talaba haqida ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
    kwargs['ism']= ism
    kwargs['familiya']=familiya
    return kwargs
talaba = talaba_info('Asadbek', 'Xolboyev', t_yili=2001, t_joy='Ellikqala', tel=None, email="")
print(talaba)