# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 22:29:44 2023

@author: Asadbek
"""

class Student():
    def __init__(self, name, surname, b_year):
        self.name = name
        self.surname = surname
        self.b_year = b_year
        self.bosqich = 1
        
    def set_bosqich(self, bosqich):
        """Talaba kursini yangilovchi metod"""
        self.bosqich = bosqich
        
    def update_bosqich(self):
        """Talabaning bosqichini 1 taga ko'paytiruvchi metod"""
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
    
    def get_info(self):
        """The function will give info about student"""
        result = (f"{self.name.capitalize()} {self.surname.capitalize()}."
                 f"He is a {self.bosqich} year student")
        return result
    
student1 = Student('Asadbek', 'Xolboyev', 2001)
student2 = Student('Sardor', 'Atajanov', 2000)
student3 = Student('Doniyor', 'Komilov', 2001)



class Fan():
    """class named science"""
    def __init__(self, name):
        self.name = name
        self.number_of_students = 0
        self.students = []
        
    def add_students(self, student):
        """Add to the science"""
        self.students.append(student)
        self.number_of_students += 1
        
    def get_students(self):
        """Fanga yozilgan talabalar haqida ma'lumot"""
        return [ student.get_info() for student in self.students]
    
    def get_students_num(self):
        """Fanga yozilgan talabalar soni"""
        return self.number_of_students
    
def see_methods(klass):
    return [method for method in dir(klass) if method.startswith('__')]
    
matematika = Fan("Oliy matematika")
matematika.add_students(student1)
matematika.add_students(student2)
matematika.add_students(student3)
