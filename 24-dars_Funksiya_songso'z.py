# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 16:59:18 2023

@author: Asadbek
"""

import math

# =============================================================================
# uzunlik = lambda pi, r : 2*pi*r
# print(uzunlik(math.pi, 10))
# =============================================================================

# =============================================================================
# kvadrat = lambda x, y : x**y
# print(kvadrat(3, 3))
# =============================================================================


# =============================================================================
# def daraja(n):
#     return lambda x : x**n
# 
# kvadrat = daraja(2)
# kub = daraja(3)
# =============================================================================


# =============================================================================
# # =============================================================================
# # from math import sqrt
# # 
# # sonlar = list(range(11))
# # print(sonlar)
# # ildizlar = list(map(sqrt, sonlar))
# # print(ildizlar)
# # =============================================================================
# 
# # =============================================================================
# # def daraja2(x):
# #     """Berilgan sonni kvadratini aniqlaydigan funksiya"""
# #     return x*x
# # print(list(map(daraja2, sonlar)))
# # 
# # =============================================================================
# 
# kvadratlar = list(map(lambda x : x*x, sonlar))
# print(kvadratlar)
# =============================================================================


# =============================================================================
# a = [4, 5, 6]
# b = [7, 8, 9]
# a_plus_b = list(map(lambda x, y : x+y, a, b,))
# print(a_plus_b)
# =============================================================================



# =============================================================================
# import random as r
# 
# sonlar = r.sample(range(100),10)
# print(sonlar)
# # def juftmi(x):
# #     """x juft bo'lsa True, aks holda False qaytaradigan funksiya"""
# #     return x%2==0
# # juft_sonlar = list(filter(juftmi, sonlar))
# # print(juft_sonlar)
# 
# 
# juft_sonlar = list(filter(lambda son : son%2==0, sonlar))
# print(juft_sonlar)
# =============================================================================


mevalar = ['anor', 'anjir', 'banan', 'behi', 'shaftoli', 'o\'rik', 'uzum', 'nok']
harf = 'a'
mevalar_b = list(filter(lambda meva : meva.startswith(harf), mevalar))
print(mevalar_b)