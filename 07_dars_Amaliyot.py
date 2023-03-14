# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 21:46:34 2022

@author: Asadbek
"""

"""
ismlar = []
ismlar.append('Sardor')
ismlar.append('Doniyor')
ismlar.append('Muhammad')
ismlar.insert(0, 'Zafar')
ismlar.insert(3, 'Islom')
print(ismlar[0], ' nichiksan yoxshison,hormo ishla bilan.')
print(ismlar[1], ' na gap kurso borib yuribsanmi?')
print(ismlar[2], ' nishatdi ishni boshlodingmi?')
print(ismlar[3], ' nichiksan sog\'liqlo yoxshimi, to\'y qochon?')
print(ismlar[-1], ' qanday ey makkammi?')'
"""
"""
sonlar = [5, 78, -85, 96, 10.25, 86.7, -5.2]
sonlar[2] = sonlar[2]+100
print(sonlar)
sonlar.remove(-5.2)
print(sonlar)
"""
"""
t_shaxslar = ['Islom_Karimov', 'Stiv_Jobs', 'Imom_Buxoriy', 'Amir_Temur', 'Z.M.Bobur']
z_shaxslar = ['Bill Gates', 'Alisher_Sadullayev', 'Muhammadali_Eshonqulov', 'Sardor_Rahimxon']
suhbatdosh1= t_shaxslar.pop(0)
suhbatdosh2 = z_shaxslar.pop(2)
print('Men tarixiy shaxslardan', suhbatdosh1,'  bilan, zamonaviy shaxslardan ',suhbatdosh2, ' bilan suhbatlashgim keladi')
"""

friends = []
friends.append('Sardor')
friends.append('Zafar')
friends.append('Sanjar')
friends.append('Shoxzod')
friends.append('Doniyor')
friends.append('Islom')
print(friends)
friends.remove('Zafar')
friends.remove('Islom')
print(friends)
friends.insert(0, 'Muhammad')
friends.insert(3, 'Baxrom')
friends.insert(-1, 'Sarvar')
print(friends)
mehmonlar = []
mehmonlar.append(friends.pop(0))
mehmonlar.append(friends.pop(1))
mehmonlar.append(friends.pop(2))
mehmonlar.append(friends.pop(-1))
print('Kelgan mehmonlar ',mehmonlar)