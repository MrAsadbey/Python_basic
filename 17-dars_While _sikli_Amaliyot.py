# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 19:38:10 2022

@author: Asadbek
"""

# =============================================================================
# savol = "Yaxshi ko'rgan kitoblaringizni kiriting"
# savol += "(Sevimli kitoblaringizni kiritib bo'lganingizdan keyin 'stop' deb yozing). >>> "
# 
# while True:
#     kitob = input(savol)
#     if kitob == 'stop':
#         break
#     else:
#         print(kitob)
# print("Raxmat")     
# =============================================================================


# =============================================================================
# quesion = "How old are you? "
# while True:
#     value = input(quesion)
#     if value == 'exit' or value == 'quit':
#         break
#     age = int(value)
#     if age<7:
#         narh=2000
#     elif 7<=age<18:
#         narh=3000
#     elif 18<=age<65:
#         narh=10000
#     else: narh=0
#     
#     if narh == 0:
#         print("Sizga chipta bepul")
#     else:
#         print(f"Sizga chipa narhi {narh} so'm.")
# print("Tashrifingiz uchun raxmat!")
# =============================================================================


savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if  qiymat=='exit':
        break
    elif float(qiymat)<0:
        continue
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")