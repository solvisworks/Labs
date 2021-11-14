# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import time
import random
import numpy as np
#Cw1
list = []
list2 = []
list3 = []
#Cw2
for i in range (100,201,1):
    list.append(i)
    list2.append(i)
    list3.append(i)
print()
print('Cw2: ----')
print(list)
#Cw3
for i in range(len(list)):
    list[i] = list[i]+8
    list3[i] = list[i]
print()
print('Cw3: ----')
print(list)
#Cw4
random.shuffle(list)
print()
print('Cw4: ----')
print(list)
#Cw5
n = random.randint(1, 100)
m = 100 - n
print()
print('Liczba jedynek: ', n, 'Liczba zer: ', m)
tab = np.array([1]*n + [0]*m)
random.shuffle(tab)
print('Cw5: ----')
print(tab)
#Cw6
list_25_el = []
list_75_el = []
for i in range(len(list2)):
    if (i < len(list2)/4):
        list_25_el.append(list2[i])
    else:
        list_75_el.append(list2[i])
print()
print('Cw7: ----')
print('Lista 25 elementow:')
print(list_25_el)
print('Lista 75 elementow:')
print(list_75_el)
#Cw8 do poprawy losowanie
list_los_1 = []
list_los_2 = []
for i in range(len(list2)):
    #switch
    a = random.randint(0, 1)
    if (a == 0):
        list_los_1.append(list2[i])
    else:
        list_los_2.append(list2[i])
random.shuffle(list_los_1)
random.shuffle(list_los_2)
print()
print('Cw8: ----')
print('Lista los 1 - ilosc: ', len(list_los_1))
print(list_los_1)
print('Lista los 2 - ilosc: ', len(list_los_2))
print(list_los_2)
#Cw9
print()
print('Cw9: ----')
print('Srednia tablic')
for i in range(10):
    list_los_1 = []
    list_los_2 = []
    for j in range(len(list2)):
        #switch
        a = random.randint(0, 1)
        if (a == 0):
            list_los_1.append(list2[j])
        else:
            list_los_2.append(list2[j])
    random.shuffle(list_los_1)
    random.shuffle(list_los_2)
    sr1 = np.sum(list_los_1) / len(list_los_1)
    sr2 = np.sum(list_los_2) / len(list_los_2)
    print('1 : ', format(sr1, ".2f"), '2 : ', format(sr2, ".2f"))
#Cw10
def pary(li,t):
    for i,j in zip(li,t):
        print('{0}'.format(i), ' {0}'.format(j))
print()
print('Cw10: ---- Pary Cw 3 i 6')
pary(list3, tab)
#Cw11

#Cw12
