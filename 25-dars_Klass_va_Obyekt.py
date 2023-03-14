# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 09:11:40 2023

@author: Asadbek
"""

# =============================================================================
# class Kompyuter:
#     def __init__(self, model, ram, hdd, gpu, cpu):
#         self.model = model
#         self.ram = ram
#         self.hdd = hdd
#         self.gpu = gpu
#         self.cpu = cpu
#         
#     def info(self):
#         inf = f"{self.model} RAM:{self.ram}, GPU:{self.gpu}, CPU:{self.cpu}"
#         return inf
# 
# macbook = Kompyuter('Apple Macbook', '8GB', '512GB', 'Nvidia', 'Intel core i5')
# =============================================================================


class Student():
    def __init__(self, name, surname, b_year):
        self.name = name
        self.surname = surname
        self.b_year = b_year
        self.bosqich = 1
        
    def set_bosqich(self,bosqich):
        """Talabaning kursini yangilsh"""
        self.bosqich = bosqich
        
    def update_bosqich(self):
        """Talabaning bosqichini 1 ga oshiradi"""
        self.bosqich += 1
        
    def get_name(self):
        """The function will return student's name."""
        return self.name
    
    def lastname(self):
        """The function will return student's surname."""
        return self.surname
    
    def get_age(self, this_year):
        """The function will return student's age."""
        return this_year - self.b_year
    
    def get_introduce(self):
        """The function will introduce to student"""
        result = (f"My name is {self.name} and my surname is {self.surname}."
                 f"I was born in {self.b_year}")
        return result
    
talaba1 = Student('Asadbek', 'Xolboyev', 2001)
talaba2 = Student('Sardor', 'Atajanov', 2000)
talaba3 = Student('Doniyor', 'Komilov', 2001)






