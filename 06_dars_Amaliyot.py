# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 07:15:40 2022

@author: Asadbek
"""
#Foydalanuvchi kiritgan sonning kvadrati va kubini konsolga chiqaruvchi dastur
a =int( input("Istalgan sonni kiriting: "))
print(a," ning kvadrati ", a**2,"\n",a," ning kubi", a**3)

#Foydalanuvchining yoshini so'rab, uning tug'ilgan yilini hisoblab, konsolga chiqaruvchi dastur
b = int(input("Yoshingizni kiriting: "))
print("Siz", 2022-b, " yilda tug'ilgansiz")    

#Foydalanuvchidan ikki son kiritshni so'rab, kiritilgan sonlarning yig'indisi, ayirmasi, ko'paytmasi va bo'linmasini chiqaruvchi dastur
print("Hoxlagan ikkita soningizni kiriting: ")
x = int(input("1-son :  "))
y = int(input("2-son :  "))
#print(str(x) + "+" + str( y) + "=" +str(int(x+y)))
#print(str(x) + "-" + str( y) + "=" +str(int(x-y)))
#print(str(x) + "*" + str( y) + "=" +str(int(x*y)))
#print(str(x) + "/" + str( y) + "=" +str(int(x/y)))
print(f"{x}+{y} = ",x+y)
print(f"{x}-{y} = ",x-y)
print(f"{x}*{y} = ",x*y)
print(f"{x}/{y} = ",x/y)