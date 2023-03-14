# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 10:08:23 2022

@author: Asadbek
"""

# =============================================================================
# car_0 = {'model':'ferrari','rang':'qizil'}
# print(car_0['model'])
# print(car_0['rang'])
# =============================================================================

# =============================================================================
# mevalar = {'olma':10000,'tarvuz':8000,'qovun':10000}
# print(f"Olma narhi {mevalar['olma']} so'm,\
#       qovunning narhi esa {mevalar['qovun']} so'm")
# =============================================================================

# =============================================================================
# talaba_0 = {'ism':'asadbek xolboyev', 'yosh':21, 't_yili':2001}
# print(f"{talaba_0['ism'].title()}, {talaba_0['t_yili']}-yilda tug'ilgan,\
#       {talaba_0['yosh']} yoshda")       
# talaba_0['kurs'] = 4
# talaba_0['fakultet'] = 'Kompyuter injiniringi'
# print(talaba_0)
# del talaba_0['yosh']
# =============================================================================


telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310',
    'anvar':'mi not8 pro'    
    }
#print(telefonlar['ali'])
#phone = telefonlar['ali']
#print(f"Alining telefoni {phone}")
#phone = telefonlar.get('hasan','Bunday ism yo\'q')
#print(phone)
phone = telefonlar.get('ali',)
print(phone)