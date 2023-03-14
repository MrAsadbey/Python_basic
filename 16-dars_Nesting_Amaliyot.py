# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 21:24:30 2022

@author: Asadbek
"""

# =============================================================================
# buxoriy = {
#     'ism':'Abu Abdulloh Muhammad ibn Ismoil',
#     't_yil':810,
#     'v_yil':870,
#     't_joy':'buxoro'
#     }
# vohidov = {
#     'ism':'Erkin Vohidov',
#     't_yil':1936,
#     'v_yil':2016,
#     't_joy':'Farg\'ona'
#     }
# qodiriy = {
#     'ism':'Abdulla Qodiriy',
#     't_yil':1894,
#     'v_yil':1938,
#     't_joy':'toshkent'
#     }
# navoiy = {
#     'ism':'alisher navoiy',
#     't_yil':1441,
#     'v_yil':1501,
#     't_joy':'xirot'
#     }
# shaxslar = [buxoriy, vohidov, qodiriy, navoiy]
# for shaxs in shaxslar:
#     ism = shaxs['ism']
#     t_yil = shaxs['t_yil']
#     v_yil = shaxs['v_yil']
#     t_joy = shaxs['t_joy']
#     print(f"{ism.title()} {t_yil}-yilda {t_joy.title()}da tug'ilgan."
#           f"{v_yil-t_yil} yil umr ko'rgan."
#           )
# =============================================================================
    
    
# =============================================================================
# buxoriy = {
#     'ism':'Abu Abdulloh Muhammad ibn Ismoil',
#     't_yil':810,
#     'v_yil':870,
#     't_joy':'buxoro',
#     'asarlar':["Al-jome' as-sahih", "Al-adab al-mufrad", "At-tarix al-kabir"]
#     }
# vohidov = {
#     'ism':'Erkin Vohidov',
#     't_yil':1936,
#     'v_yil':2016,
#     't_joy':'Farg\'ona',
#     'asarlar':["Tong nafasi","Qo'shiqlarim sizga","O'zbegim","Qiziquvchan Matmusa"]
#     }
# qodiriy = {
#     'ism':'Abdulla Qodiriy',
#     't_yil':1894,
#     'v_yil':1938,
#     't_joy':'toshkent',
#     'asarlar':["O'tkan kunlar","Mehrobdan Chayon",'Obid ketmon']
#     }
# navoiy = {
#     'ism':'alisher navoiy',
#     't_yil':1441,
#     'v_yil':1501,
#     't_joy':'xirot',
#     'asarlar':["Xamsa","Lison ut-Tayr","Mahbub Al-Qulub",'Munojot']
#     }
# shaxslar = [buxoriy, vohidov, qodiriy, navoiy]
# for shaxs in shaxslar:
#     ism = shaxs['ism']
#     asarlar = shaxs['asarlar']
#     print(f"\n {ism.title()}ning mashxur asarlari: ")
#     for asar in asarlar:
#         print(asar)
# =============================================================================


# =============================================================================
# kinolar = {
#     'ali':['Terminator', 'Tor', 'Titanic'],
#     'vali':['Ipman', 'После', 'Chegarasizlar'],
#     'hasan':['Shaytanat', 'Osmondagi balalar'],
#     'husan':['Ajal o\'yini', 'Farsaj', 'Bo\'ysunmas']
#     }
# for ism, kinolar in kinolar.items():
#     print(f"\n {ism.title()}ning sevimli kinolari: ")
#     for kino in kinolar:
#         print(kino)
# =============================================================================


# =============================================================================
# davlatlar = {
#     'O\'zbakiston':{'poytaxt':'toshkent',
#                     'maydon':448978,
#                     'aholi':36_000_000,
#                     'pul birligi':'so\'m'
#                     },  
#     "rossiya":{'poytaxt':"moskva",
#                    'maydon':17_098_246,
#                    'aholi':144_000_000,
#                    'pul birligi':"rubl"
#                    },
#     "aqsh":{'poytaxt':"vashington",
#                    'maydon':9_631_418,
#                    'aholi':327_000_000,
#                    'pul birligi':"dollar"},
#     "malayziya":{'poytaxt':"kuala-lumpur",
#                    'maydon':329750,
#                    'aholi':25_000_000,
#                    'pul birligi':"rinngit"}
#     }
# for davlat, info in davlatlar.items():
#         if davlat.lower()=='aqsh':
#             davlat=davlat.upper()
#         else:
#             davlat=davlat.capitalize()
#         print(f"\n{davlat}ning poytaxti {info['poytaxt'].title()}"
#           f"\nHududi: {info['maydon']} kv.km"
#           f"\nAholisi: {info['aholi']}"
#           f"\nPul birligi: {info['pul birligi']}")
# =============================================================================


davlatlar = {
    'O\'zbakiston':{'poytaxt':'toshkent',
                    'maydon':448978,
                    'aholi':36_000_000,
                    'pul birligi':'so\'m'
                    },  
    "rossiya":{'poytaxt':"moskva",
                   'maydon':17_098_246,
                   'aholi':144_000_000,
                   'pul birligi':"rubl"
                   },
    "aqsh":{'poytaxt':"vashington",
                   'maydon':9_631_418,
                   'aholi':327_000_000,
                   'pul birligi':"dollar"},
    "malayziya":{'poytaxt':"kuala-lumpur",
                   'maydon':329750,
                   'aholi':25_000_000,
                   'pul birligi':"rinngit"}
    }
davlat = input("Qaysi davlat haqida ma'lumot olishni hohlaysiz? >>> ")
if davlat in davlatlar:
    info = davlatlar[davlat]
    print(f"\n{davlat.capitalize()}ning poytaxti {info['poytaxt'].title()}"
          f"\nHududi: {info['maydon']} kv.km"
          f"\nAholisi: {info['aholi']}"
          f"\nPul birligi: {info['pul birligi']}")
else:
    print("Bizda bu davlat haqida ma'lumot yo'q")