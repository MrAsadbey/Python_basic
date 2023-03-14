# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 16:25:03 2022

@author: Asadbek
"""

# =============================================================================
# def salom_ber():
#     """Salom beruvchi funksiya"""
#     print("Assalomu alekum!")
#     
# salom_ber()
# =============================================================================


# =============================================================================
# def salom_ber(ism):
#     """Foydalanuvchi ismini qabul qilib unga salom beruvchi funksiya"""
#     print(f"Assalomu alekum! Hurmatli {ism.title()}.")
#     
# salom_ber('hasan')    
# salom_ber('husan') 
# =============================================================================


# =============================================================================
# def toliq_ism(ism, familiya):
#     """Foydalanuvchi ism va familiyasini birgalikda chiqaruvchi funksiya"""
#     print(f"Foydalanuvchi ismi: {ism.title()}\n"
#           f"Foydalanuvchi familiyasi: {familiya.title()}")
# toliq_ism('asadbek', 'xolboyev')    
# =============================================================================


def yosh_hisobla(ism, t_yil):
    """Foydalanuvchi yoshini hisoblaydigan funksiya"""
    print(f"{ism.title()} {2022-t_yil} yoshda")
yosh_hisobla('asadbek', 2001) # parametrlarni kiritishda funksiyada berilgan
                               # parametr ketma-ketligiga e'tibor berish kerak!
