# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 11:17:30 2022

@author: Asadbek
"""

# =============================================================================
# def malumot_topla(name, surname, b_year, age, where_born, tel_number = None, email = ''):
#     full_data = {
#         'name' : name,
#         'surname' : surname,
#         'b_year' : b_year,
#         'age' : 2023-b_year,
#         'where_born' : where_born, 
#         'tel_number' : tel_number,
#         'email' : email
#         }
#     return full_data
# 
# print("\n Foydalanuvchi haqidagi ma'lumotlarni shakllantiramiz!")
# data = []
# while True:
#     name = input("Ismi: ")
#     surname = input("Familiyasi: ")
#     b_year = int(input("Tug'ilgan yili: "))
#     where_born = input("Tug'ilgan joyi: ")
#     email = input("Email: ")
#     tel_number = input("Telefon raqami: ")
#     data.append(malumot_topla(name, surname, b_year, where_born, email, tel_number))
#     savol = input("Yana ma'lumot qo'shasizmi? ha/yo'q  ")
#     if savol == "yo'q":
#         break
# 
# print("Foydalanuvchi ma'lumotlari:")
# for full_data in data:
#     print(f"{full_data['name'].title()} {full_data['surname'].title()}," 
#           f"{full_data['age']} yoshda, telefoni: {full_data['tel_number']}")
# =============================================================================



# =============================================================================
# def sonlarni_taqqosla(x, y, z):
#     max = x
#     if y>max:
#         max = y
#     if z>max:
#         max = z
#     return max
# 
# print(sonlarni_taqqosla(25, -42, -12))
# =============================================================================


# =============================================================================
# def doira_info(radius, pi = 3.14159):
#     doira = {
#         'radius': radius,
#         'diametr' : 2*radius,
#         'perimetr' : 2*pi*radius,
#         'yuza' : pi*radius**2
#         }
#     return doira
# 
# print(doira_info(5))
# =============================================================================


# =============================================================================
# def tub_sonlarni_top(min,max):
#     tub_sonlar = []
#     for n in range(min, max+1):
#         tub = True
#         if (n==1):
#             tub = False
#         elif (n==2):
#             tub = True
#         else:
#             for x in range(2, n):
#                 if (n%x==0):
#                     tub = False
#         if tub:
#             tub_sonlar.append(n)
#             
#     return tub_sonlar
# print(tub_sonlarni_top(20, 40))
# =============================================================================


def fibonacci(n):
    sonlar = []
    for x in range(n):
        if x==0 or x==1:
            sonlar.append(1)        
        else:
            sonlar.append(sonlar[x-1]+sonlar[x-2])
    return sonlar

print(fibonacci(15))