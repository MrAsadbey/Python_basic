# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 14:00:23 2022

@author: Asadbek
"""

# =============================================================================
# car0 = {
#         'model':'lacetti',
#         'rang':'oq',
#         'yil':2013,
#         'km':50000,
#         'karobka':'mehanik',
#         'narh':13000
#         }
# car1 = {
#         'model':'nexia 3',
#         'rang':'qizil',
#         'yil':2020,
#         'km':35000,
#         'karobka':'avtomat',
#         'narh':12000
#         }
# car2 = {
#         'model':'gentra',
#         'rang':'qora',
#         'yil':2022,
#         'km':0,
#         'karobka':'avtomat',
#         'narh':15000
#         }
# # =============================================================================
# # car = car0 
# # print(f"{car['model'].title()}, {car['rang']} rang, "  
# #       f"{car['yil']}-yil, {car['narh']}$")
# # =============================================================================
# 
# cars = [car0, car1, car2]
# print(cars[0]['model'])
# for car in cars:
#     print(f"{car['model'].title()}, {car['rang']} rang, "  
#           f"{car['yil']}-yil, {car['narh']}$\n")
# =============================================================================
    

# =============================================================================
# cars = []
# for n in range(10):
#     new_car = {
#         'model':None,
#         'rang':None,
#         'yil':2021,
#         'km':0,
#         'karobka':'avto'
#         }
#     cars.append(new_car)
# for car in cars[:3]:
#     car['model']='spark'
#     car['rang']='oq'
#     car['karobka']='mexanika'
# for car in cars[3:6]:
#     car['model']='gentra'
#     car['rang']='qora'
# for car in cars[6:]:
#     car['model']='onix'
#     car['rang']='mokri asfalt'
# for car in cars:
#     if (car['model']=='gentra' and car['karobka']=='avto'):
#         car['narh']=15000
#     elif (car['model']=='spark' and car['karobka']=='mexanika'):
#         car['narh']=8500
#     else:
#         car['narh']=14000
# for car in cars:
#     print(car)        
# =============================================================================


dasturchilar = {
    'ali':['python', 'c++'],
    'vali':['html', 'css', 'js'],
    'hasan':['php', 'sql'],
    'husan':['python', 'php'],
    'maryam':['c++', 'c#']
    }
for ism, tillar in  dasturchilar.items():
    print(f"\n{ism.title()} quydagi tillarni biladi: ")
    for til in tillar:
        print(til.upper())