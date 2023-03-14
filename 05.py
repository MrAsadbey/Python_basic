# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 06:24:48 2022

@author: Asadbek
"""

#ism = "asadbek"
#familya = "xolboyev"
#print(ism.upper())
#print(familya.capitalize())
#ism_sharif = f"{ism} {familya}"
#print(ism_sharif.title())

#kocha = "Bog'bon"
#mahalla = "Sog'bon"
#tuman = "Bodomzor"
#viloyat = "samarqand"
#address = f"{kocha} ko\'chasi, {mahalla} mahallas, {tuman} tumani, {viloyat.capitalize()} viloyati"
#print(address)

kocha = input("Iltimos ko'changiz nomini kiriting\n>>>")
mahalla = input("Iltimos mahallangiz nomini kiriting\n>>>")
tuman = input("Iltimos tumaningiz nomini kiriting\n>>>")
viloyat = input("Iltimos viloyatingiz nomini kiriting\n>>>")
address = f"{kocha} ko\'chasi, \n{mahalla} mahallasi, \n{tuman} tumani, \n{viloyat.capitalize()} viloyati."
print(address)
