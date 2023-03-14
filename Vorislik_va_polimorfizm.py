# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 16:09:01 2023

@author: Asadbek
"""

class Shaxs():
    """Data about persons"""
    def __init__(self, name, surname, passport, b_year):
        """Traits of person"""
        self.name = name
        self.surname = surname
        self.passport = passport
        self.b_year = b_year
        
    def get_info(self):
        """Information about person"""
        info = f"{self.name} {self.surname}. "
        info += f"Passport: {self.passport}, {self.b_year}-yilda tug'ilgan"
        return info
    def get_age(self, this_year):
        """The method will return person's age"""
        return this_year - self.b_year
    
    
inson = Shaxs('Akbar', 'Olimov', 'KA1122333', 1998)

class Student(Shaxs):
    """Talaba klassi"""
    def __init__(self, name, surname, passport, b_year, idnumber, address):
        """Traits of student"""
        super().__init__(name, surname, passport, b_year)
        self.idnumber = idnumber
        self.bosqich = 1
        self.address = address
        
    def get_id(self):
        """ID number of student"""
        return self.idnumber
    
    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich
    
    def get_info(self):
        """Information about person"""
        info = f"{self.name} {self.surname}. "
        info += f"{self.get_bosqich()} - bosqich talabasi, ID raqam: {self.get_id()}, {self.b_year}-yilda tug'ilgan"
        return info
    
class Address:
    """Class to store the address"""
    def __init__(self, home, street, district, province):
        """Manzil xususiyatlari"""
        self.home = home
        self.street = street
        self.district = district
        self.province = province
        
    def get_address(self):
        """Manzilni ko'rish"""
        address = f"{self.province} viloyati {self.district} tumani, "
        address += f"{self.street} ko'chasi {self.home} - uy."
        return address 
    
talaba1_address = Address(5, 'Bog\'bon', "Pop", 'Samarqand')
talaba1 = Student('Alijon', 'Valiyev', 'KA1112233', 1999, "M1000011", talaba1_address)
## talaba1.address.get_address()  # Address klassining get_address() metodiga murojaat.