# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 19:20:41 2022

@author: Asadbek
"""

# =============================================================================
# def toliq_ism_yasa(ism, familiya):
#     """To'liq ism qaytaruvchi funksiya"""
#     toliq_ism = f"{ism} {familiya}"
#     return toliq_ism
# talaba1 = toliq_ism_yasa('asadbek', 'xolboyev')
# talaba2 = toliq_ism_yasa('sardor', 'sadullayev')
# print(f"Darsga kelmagan talabalar {talaba1.title()} va {talaba2.title()}")
# print(f"{talaba1.title()} darsga kechikib keldi.")
# =============================================================================
    

# =============================================================================
# def toliq_ism_yasa(ism, familiya, otasining_ismi=''):
#     """To'liq ism qaytaruvchi funksiya"""
#     if otasining_ismi:
#         toliq_ism = f"{ism.title()} {otasining_ismi.title()} {familiya.title()}"
#     else:
#         toliq_ism = f"{ism.title()} {familiya.title()}"
#     return toliq_ism
# talaba1 = toliq_ism_yasa('asadbek', 'xolboyev', 'bahodirovich')
# talaba2 = toliq_ism_yasa('sardor', 'sadullayev')
# print(f"Darsga kelmagan talabalar {talaba1.title()} va {talaba2.title()}")
# print(f"{talaba1.title()} darsga kechikib keldi.")
# =============================================================================


# =============================================================================
# def avto_info(kompaniya, model, rang, karobka, yili, narh=None):
#     """Avtomobil haqida ma'lumot beruvchi funksiya"""
#     avto = {
#         'kompaniya' : kompaniya,
#         'model' : model,
#         'rang' : rang,
#         'karobka' : karobka,
#         'yili' : yili,
#         'narh':narh
#         }
#     return avto
# avto1 = avto_info("GM", 'Malibu', 'qora', 'avtomat', 2020)
# avto2 = avto_info('Gm', 'Gentra', 'oq', 'avto', 2021, 15000)
# avtolar = [avto1, avto2]
# print('Online bozordagi mavjud avtomashinalar')
# for avto in avtolar:
#     if avto['narh']:
#         narh=avto['narh']
#     else:
#         narh = "Noma'lum"
#     print(f"{avto['rang'].capitalize()} {avto['model']}. Narhi:{avto['narh']}")
# 
# =============================================================================


# =============================================================================
# def oraliq(min, max, n = None):
#     sonlar = []
#     while min<max:
#         if n==None:
#             sonlar.append(min)
#             min += 1
#         if n==2:
#             sonlar.append(min)
#             min += n
#     return sonlar
# list_nubers = oraliq(1, 10, 2)
# print(list_nubers)
# =============================================================================


def avto_info(kompaniya, model, rang, korobka, yil, narh=None):
    avto = {
        'kompaniya': kompaniya,
        'model': model,
        'rang': rang,
        'korobka' : korobka,
        'yil' : yil, 
        'narh' : narh
        }
    return avto
print("Saytimizdagi avtolar ro'yhatini shakllantiramiz.")
avtolar = []
while True:
    print("\nQuyidagi ma'lumotlarni kiriting: ")
    kompaniya = input('Ishlab chiqaruvchi: ')
    model = input("Modeli: ")
    rang = input("Rangi: ")
    korobka = input("Korobka: ")
    yil = input("Ishlab chiqarilgan yili: ")
    narh = input("Narhi: ")
    
    avtolar.append(avto_info(kompaniya, model, rang, korobka, yil, narh))
    savol = input("\nYana avto qo'shasizmi? yes/no: ")
    
    if savol=='no':
        break
    
print("\nSalonimizdgi avtolar: ")
for avto in avtolar:
    if avto['narh']:
        narh = avto['narh']
    else:
        narh = "Noma'lum"
    print(f"{avto['rang'].capitalize()} {avto['model'].capitalize()}, narhi {avto['narh']}")
