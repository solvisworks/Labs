# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random
import numpy as np
import matplotlib.pyplot as plt
import math
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
print()

#Cw6
tabbool = np.array(tab, dtype = bool)
print()
print('Cw6: ----')
print(tabbool)

#Cw7
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

#Cw8 
list_los_1 = []
list_los_2 = []
def los_list_del(l1, l2, l3):
    for i in range(len(l1)):
        a = random.randrange(0,len(l1))
        b = random.randint(0,1)
        if (len(l1) > 0):
            if (b == 0):
                l2.append(l1[a])
                del l1[a]
            else:
                l3.append(l1[a])
                del l1[a]
        else:
            print('lista pusta')

los_list_del(list2,list_los_1,list_los_2)
print()
print('Cw8: ----')
print('Lista los 1 - ilosc: ', len(list_los_1))
print(list_los_1)
print('Lista los 2 - ilosc: ', len(list_los_2))
print(list_los_2)


for i in range (100,201,1):
    list2.append(i)


#Cw9 

print()
print('Cw9: ----')
print('Srednia tablic')
for i in range(10):
    list_los_1 = []
    list_los_2 = []
    los_list_del(list2,list_los_1,list_los_2)
    for i in range (100,201,1):
        list2.append(i)
    sr1 = np.sum(list_los_1) / len(list_los_1)
    sr2 = np.sum(list_los_2) / len(list_los_2)
    print('1 : ', format(sr1, ".2f"), '2 : ', format(sr2, ".2f"))
    
#Cw10
def pary(li,t):
    for i,j in zip(li,t):
        print('{0}'.format(i), ' {0}'.format(j))
print()
print('Cw10: ---- Pary Cw 3 i 6')
pary(list3, tabbool)

#Cw12
tab_0_1f = np.empty(1000)
for i in range(len(tab_0_1f)):
    tab_0_1f[i] = random.uniform(0,1)
print()
print('Cw12: ----')
print(tab_0_1f)

#Cw14
def licz_Eltab(l,a):
    if (len(l) > a):
        print(len(l))
print()
print('Cw14: ---- Liczba elementow tablicy')
licz_Eltab(tab_0_1f, 100)

#Cw15
def zmien_Wartosc_0(l,a):
    for i in range(len(l)):
        if (l[i] < a):
            l[i] = 0
    return l
a = 150
tab_wartosc_0 = np.array(list_los_1)
zmien_Wartosc_0(tab_wartosc_0, a)
print()
print('Cw15: ---- Zamiana na 0 liczb ponizej',a)
print(tab_wartosc_0)

#Cw16
# class klasa:
#     def __init__(self, wagi, bias):
#         self.wagi = wagi
#         self.bias = bias
    
#     def sum(self):
#         print()
    
#     def signum(self):
        
        
# p1 = Klasa()
# p1.fun()
#Cw16
x = np.linspace(-5,5,100)
y = x**3
# setting the axes at the centre
f = plt.figure()
ax = f.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

plt.title('Zad.16 Funkcja f(x) = x^3')
plt.plot(x,y)
plt.savefig('f1.png')
plt.show()
#Cw17
x = np.linspace(0,20,100)
y1 = np.log10(x)
y2 = np.log2(x)
# setting the axes at the centre
f2 = plt.figure()

plt.title('Zad.17 Funkcja f(x) = log_10(x) & g(x) = log_2(x)')
plt.plot(x,y1,x,y2)
plt.legend(["log10(X)", "log2(x)"], loc ="lower right")
plt.show()
#Cw18
x = np.linspace(-3,3,100)
ynorm = (math.e**((-x**2)/2))/(math.sqrt(2*math.pi))
fnorm = plt.figure()
plt.title('Zad.18')
plt.plot(x,ynorm)
plt.show()
#Cw19