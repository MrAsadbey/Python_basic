# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 12:53:29 2023

@author: Asadbek
"""

class Student():
    """A class that callects informations about a student."""
    def __init__(self, name, surname, b_year, idnumber):
        """Traits of student"""
        self.name = name
        self.surname = surname
        self.b_year = b_year
        self.idnumber = idnumber
        self.fanlar = []
        
    def fanga_yozil(self, student):
        """Add to the science"""
        self.fanlar.append(student)
        
    def get_students(self):
        """Fanga yozilgan talabalar haqida ma'lumot"""
        return [ student for student in self.students]
    
student1 = Student('Asadbek', 'Xolboyev', 2001, "N1000111")
student2 = Student('Sardor', 'Atajanov', 2000, "N1000112")
student3 = Student('Doniyor', 'Komilov', 2001, "N1000113")   

class Fan(Student):
    """Fan klassi"""
    def __init__(self, name):
        self.name = name
    
    def get_info(self):
        return self.name

fan1 = Fan('Oliy matematika')
fan2 = Fan('Psixologiya')
fan3 = Fan('Fizika')
fan4 = Fan('Ingliz tili')
fan1.fanga_yozil(student1)

    