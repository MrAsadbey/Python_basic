# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 11:25:23 2022

@author: Asadbek
"""

# =============================================================================
# mehmonlar = ['Ali', 'Vali', 'Sardor', 'Doniyor', 'Zafar']
# for mehmon in mehmonlar:
#     print("Salom ", mehmon)
#     print(f"Hurmatli {mehmon}, sizni Sanjar bilan Parizoda Usmono'vaning to'ylariga taklif qilamiz.")
#     print("Hurmat bilan Sancho jo'rooong\n")
# =============================================================================

# =============================================================================
# sonlar = list(range(1, 11))
# for son in sonlar:
#     print(f"{son} ning kvadrati {son**2} ga teng")
# =============================================================================

# =============================================================================
# sonlar = list(range(11))
# sonlar_kvadrati = []
# for son in sonlar:
#     sonlar_kvadrati.append(son**2) 
#     
# print(sonlar)
# print(sonlar_kvadrati)
# 
# =============================================================================

# =============================================================================
# dostlar = []
# print("5 ta eng yaqin do'stingizni kiriting:\n")
# for n in range(5):
#     dostlar.append(input(f"{n+1}- do'stingiz ismini kiriting: "))
# print(dostlar)    
# =============================================================================

# =============================================================================
# ismlar = ['Muhammad', 'Sardor', 'Doniyor', 'Ali', 'Vali']
# for ism in ismlar:
#     print('Salom ', ism)
#     print(f"{ism} jo'ro sani o'zimni to'yimo taklif ataman")
#     print("Hurmat bilan Sancho jo'rooong\n")
# u = len(ismlar) 
# print(f"Kod ekranga {u} marta chiqdi")   
# =============================================================================

# =============================================================================
# sonlar = list(range(11, 100, 2))
# print(sonlar)
# for son in sonlar:
#     print(f"{son} ning kubi {son**3} ga teng.\n")
# =============================================================================

# =============================================================================
# kinolar = []
# print("5 ta eng sevimli kinolaringiz nomini kiriting.")
# for n  in range(5):
#     kinolar.append(input(f"{n+1}-kino nomini kiriting: "))
# print(kinolar)    
# =============================================================================

odamlar_soni =int( input("Bugun nechta odam bn ko'rishdingiz?>>> "))
ismlar = []
print("Ko'rishgan odamlaringiz ismini kiriting:\n")
for n in range(odamlar_soni):
    ismlar.append(input(f"{n+1}-ko'rishgan insoningiz ismi: "))
print(ismlar)    