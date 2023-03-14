# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 21:31:16 2022

@author: Asadbek
"""
# =============================================================================
# 
# cars = ['bmw', 'mercedez benez', 'volvo', 'general motors', 'tesla', 'audi']
# #cars.sort()
# cars.reverse()
# #print(cars)
# print(sorted(cars))
# print(sorted(cars, reverse=True))
# 
# =============================================================================

# =============================================================================
# sonlar = [5, 26,33, -54, -5.2, -9]
# print(sorted(sonlar))
# print(sorted(sonlar, reverse=True))
# 
# =============================================================================

# =============================================================================
# sonlar = list(range(0,10))
# print(sonlar)
# toq_sonlar = list(range(1,20,2))
# print(toq_sonlar)
# juft_sonlar = list(range(0,30,2))
# print(juft_sonlar)
# onliklar = list(range(0,101,10))
# print(onliklar)
# max_qiymat = max(toq_sonlar)
# print(max_qiymat)
# min_qiymat = min(juft_sonlar)
# print(min_qiymat)
# =============================================================================

# =============================================================================
# countries = ['Uzbekistan', 'Russian', 'England', 'Egypt', 'China', 'France']
# print(countries)
# # =============================================================================
# # print(len(countries))
# # print(sorted(countries))
# # print(sorted(countries, reverse=True))
# # =============================================================================
# countries.sort()
# print(countries)
# countries.sort(reverse=True)
# print(countries)
# =============================================================================

sonlar = list(range(120,1200,2))
print(sonlar)
max_qiymat = max(sonlar)
print(max_qiymat)
min_qiymat = min(sonlar)
print(min_qiymat)
uzunlik = len(sonlar)
print(uzunlik)
jami = sum(sonlar)
print(jami)
copy_sonlar = sonlar[0:21]
print(copy_sonlar)