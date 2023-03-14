# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 09:19:55 2023

@author: Asadbek
"""

# =============================================================================
# def bahola(ismlar):
#     baholar = {}
#     while ismlar:
#         ism = ismlar.pop()
#         baho = int(input(f"Talaba {ism.title()}ning bahosini kiriting: "))
#         baholar[ism] = baho
#     return baholar
# talabalar = ['Doniyor', 'Sardor', 'Sanjar', 'Muxammad']
# baholar = bahola(talabalar[:]) # [:] --> asosiy ro'yxat qiymati o'zgarib ketmasligi uchun 
# print(baholar)
# =============================================================================


# =============================================================================
# def katta_harf(matnlar):
#     for i in range(len(matnlar)):
#         matnlar[i]=matnlar[i].title()
#     return matnlar
# ismlar = ['ali', 'vali', 'hasan', 'husan']
# katta_harf(ismlar)
# print(ismlar)
# =============================================================================


# =============================================================================
# def katta_harf(matnlar):
#     for i in range(len(matnlar)):
#         matnlar[i]=matnlar[i].title()
#     return matnlar
# ismlar = ['ali', 'vali', 'hasan', 'husan']
# yangi_ismlar = katta_harf(ismlar[:])
# print(yangi_ismlar)
# print(ismlar)
# 
# =============================================================================


def bahola(ismlar):
    baholar = {}
    for i in range(len(ismlar)):
        baho = int(input(f"Talaba {ismlar[i].title()}ning bahosini kiriting: "))
        baholar[ismlar[i]] = baho
    return baholar
talabalar = ['doniyor', 'sardor', 'sanjar', 'muxammad']
baholar = bahola(talabalar[:]) # [:] --> asosiy ro'yxat qiymati o'zgarib ketmasligi uchun 
print(baholar)
print(talabalar)
