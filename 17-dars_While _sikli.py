# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 14:08:37 2022

@author: Asadbek
"""

# =============================================================================
# son = 1
# while son<=5:
#     print(son, end=' ')
#     son+=1
# =============================================================================


# =============================================================================
# savol = "Istalgan sonni kiriting"
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): >>> "
# qiymat = ''
# while qiymat != 'exit':
#     qiymat=input(savol)
#     if qiymat != 'exit':
#         print(float(qiymat)**2)
# print("Dastur tugadi!")
# =============================================================================


# =============================================================================
# savol = "Istalgan sonni kiriting"
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): >>> "
# ishora=True
# while ishora:
#     qiymat=input(savol)
#     if qiymat == 'exit':
#        ishora=False
#     else:
#        print(float(qiymat)**2)
# print("Dastur tugadi!")
# =============================================================================


# =============================================================================
# savol = "Istalgan sonni kiriting"
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): >>> "
# while True:
#     qiymat=input(savol)
#     if qiymat == 'exit':
#         break
#     else:
#         print(float(qiymat)**2)
# print("Dastur tugadi!")
# =============================================================================


# =============================================================================
# sonlar = list(range(1,11))
# for son in sonlar:
#     if son == 5:
#         break
#     print(f"{son} ning kvadrati {son**2} ga teng.")
# # =======================================================    
# sonlar = list(range(1,11))
# for son in sonlar:
#     if son == 5:
#         continue
#     print(f"{son} ning kvadrati {son**2} ga teng.")
# =============================================================================


son = 0
while son<10:
    son += 1
    if son%2 != 0:
        continue
    else:
        print(son)