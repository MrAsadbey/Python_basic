# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 14:27:11 2023

@author: Asadbek
"""

import datetime as dt


# =============================================================================
# hozir = dt.datetime.now()
# print(hozir)
# 
# ## sanani ajratib olish
# print(hozir.date())
# 
# ## vaqtni ajratib olish
# print(hozir.time())
# 
# ## soatni ajratib olish
# print(hozir.hour)
# =============================================================================

# =============================================================================
# from datetime import timedelta
# #delta = timedelta(weeks=2)
# bugun = dt.date.today()
# print(f"Bugungi sana: {bugun}")
# print("2 hafta bilan farq qiluvchi keyingi 10 ta sana.")
# for i in range(10):
#     bugun += timedelta(weeks=2)
#     print(bugun)
# =============================================================================


# =============================================================================
# today = dt.date.today()
# ramadan = dt.date(2023, 3, 23)
# eid_al_adha = dt.date(2023, 6, 28)
# distance1 = ramadan-today
# distance2 = eid_al_adha - today
# print(f"{distance1.days} days left for Ramadan")
# print(f"{distance2} days left for Eid al-Adha")
# =============================================================================

# =============================================================================
# def get_info():
#     """Tug'ilgan kuningizdan bugungacha qancha yil, oy, kun o'tganini qaytaruvchi funksiya"""
#     today = dt.date.today()
#     my_birthday = dt.date(2001, 2, 11)
#     
#     return (f"Tug'ilgan kuningizdan bugungacha {today.year-my_birthday.year} yil "
#           f"{today.month-my_birthday.month} oy {today.day-my_birthday.day} kun o'tdi")
# =============================================================================


# =============================================================================
# import re
# 
# andoza = "^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"
# phone_number = input("Iltimos telefon nomeringizni kiriting: ")
# print(re.match(andoza, phone_number))
# =============================================================================


# =============================================================================
# import re
# 
# text = """Assalom alaykum hurmatli do'stlar. Navbatdagi darsimiz YouTubega yuklandi: https://youtu.be/vsxJPRLXpgI Ushbu darsimizda unittest moduli yordamida klasslarning xususiyatlar va metodlarini tekshiruvchi dastur yozishni o'rganamiz. Bugungi dars manzili: https://python.sariq.dev/testing/37-klass-test"""
# andoza = "https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*)"
# url_address = re.findall(andoza, text)
# print(url_address)
# =============================================================================


import random as r

a = list(range(100))
print(a)
b = r.sample(a, k=10)
print(b)

