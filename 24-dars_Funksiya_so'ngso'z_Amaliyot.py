# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 10:29:46 2023

@author: Asadbek
"""

import random as r, math


# =============================================================================
# natija  = lambda son : son*10
# print(natija(365))
# =============================================================================


# =============================================================================
# yigindi = lambda x, y : x+y
# print(yigindi(256, 226))
# =============================================================================


# =============================================================================
# sonlar = r.sample(range(1000), 10)
# print(sonlar)
# kvadratlar = list(map(lambda son: son**2, sonlar))
# print(kvadratlar)
# toq_sonlar = list(filter(lambda son : son%2!=0, sonlar))
# print(toq_sonlar)
# =============================================================================


def tub_son(son):
    """Berilgan sonni tub yoki tub emasligini tekshiradigan funksiya"""
    if son%2==0 or son<2:
        return False
    if son == 2 or son == 3:
        return True
    for i in range(3, son, 2):
        if son%i == 0:
            return False
    return True
tub_son(17)        


tub_sonlar = list(filter(tub_son, range(1, 10000)))
print(tub_sonlar)