# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 18:39:00 2022

@author: Asadbek
"""

# =============================================================================
# otam = {'ism':'Baxodir', 't_yili':1972, 'viloyat':'Qoraqalpog\'iston Respublikasi\
#         ', 'manzil':'Ellikqal\'a tumani'}
# onam = {'ism':'Fazilat','t_yili':1974,'viloyat':'Qoraqalpog\'iston Respublikasi\
#         ', 'manzil':'Ellikqal\'a tumani'}
# print(f"Otamning ismi {otam['ism'].title()}, {otam['t_yili']}-yilda \
#       {otam['viloyat'].title()} {otam['manzil']}da tug'ilgan.")
# =============================================================================
      
      
# =============================================================================
# taomlar = {'ali':'osh',
#         'vali':'manti',
#         'hasan':'shashlik',
#         'husan':'so\'msa',
#         'olim':'lag\'mon'
#         }
# taom1 = taomlar['ali']
# taom2 = taomlar['vali']
# taom3 = taomlar['hasan']
# taom4 = taomlar['husan']
# print(f"Alining sevimli taomi {taom1}")
# print(f"Valining sevimli taomi {taom2}")
# print(f"Hasanining sevimli taomi {taom3}")
# =============================================================================


py_izohli_lug = {
    'integer':"Butun son",
    'float':"O'nlik son",
    'string':"Matn",
    'list':"Ro'yxat",
    'tuple':"O'zgarmas ro'yxat",
    'if':'shart operatori',
    'boolen':'Mantiqiy qiymat'
    }
#kalit = input("Kalit so'z kiriting: ").lower()
#print(py_izohli_lug.get(kalit,"Bunday so'z mavjud emas"))

kalit = input("Kalit so'z kiriting: ").lower()
tarjima = py_izohli_lug.get(kalit)
if tarjima == None:
    print("Bunday so'z mavjud emas.")
else:
    print(f"{kalit.title()} so'zi {tarjima} deb tarjima qilinadi")