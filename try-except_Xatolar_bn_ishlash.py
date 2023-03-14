# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 12:42:21 2023

@author: Asadbek
"""

# =============================================================================
# yosh = input("Yoshingizni kiriting: ")
# try:   
#     yosh = int(yosh)
# except:
#     print("Siz butun son kiritmadingiz.")
# else:
#     print(f"Siz {2023-yosh}-yilda tug'ilgansiz.")
# =============================================================================


# =============================================================================
# # ZeroDivisionError
# x, y = 5, 10
# try:
#     y/(x-5)
# except ZeroDivisionError:
#     print("0 ga bolish mumkin emas")
# =============================================================================


# =============================================================================
# #IndexError
# mevalar = ['olma', 'anjir', 'anor', 'uzum']
# try:
#     print(mevalar[0]) # Index ni o'zgartirib qayta tekshirib ko'ring
# except IndexError:
#     print(f"Ro'yxatda faqat {len(mevalar)} ta meva bor")
# =============================================================================


import json
files = ['talaba1.json', 'talaba2.json', 'talaba3.json', 'talaba4.json']
for filename in files:
    try:
        with open(filename) as f:
            talaba = json.load(f)
    except FileNotFoundError:
        print(f"{filename} mavjud emas.")
    else:
        print(talaba['ism'])