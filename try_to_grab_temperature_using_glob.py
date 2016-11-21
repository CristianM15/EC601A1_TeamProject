# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 05:29:48 2016

@author: mac
"""

import csv
import glob

Trials1 = glob.glob('temperature*global.csv')

lista = ['Temperature']

for file_name in Trials1:
    with open(file_name, 'r') as inp:
        list1 = []
        for row in csv.reader(inp):
            list1.append(row[202])
        
        lista.append(list1[98])

valid_temperature = 0
number_of_average = 0

for k in range(1,96):
    if (lista[k] != '99999.0' and lista[k] != '45.0'):
        valid_temperature +=  float(lista[k])
        number_of_average += 1

average_temperature = valid_temperature/number_of_average

for r in range(1,96):
    if lista[r] == '99999.0':
        lista[r] = average_temperature
    elif lista[r] == '45.0':
        lista[r] = average_temperature
        
#list6 = []
#        
#for i in range(1,96):
#    if lista[i] == '99999.0':
#        list6.append(i)
#    elif lista[i] == '45.0':
#        list6.append(i)

        
Trials2 = glob.glob('activefire*global.csv')

listb = ['Fire']


for file_name in Trials2:
    with open(file_name, 'r') as inp:
        list1 = []
        for row in csv.reader(inp):
            list1.append(row[202])
        
        listb.append(list1[98])

#for i in range(1,96):
#    if listb[i] == '99999.0':
#        listb[i] = 0
#    elif listb[i] == '0.1':
#        listb[i] = 0
#    else:
#        listb[i] = 1

Trials3 = glob.glob('watervapor*global.csv')

listc = ['Watervapor']


for file_name in Trials3:
    with open(file_name, 'r') as inp:
        list1 = []
        for row in csv.reader(inp):
            list1.append(row[202])
        
        listc.append(list1[98])
        
valid_watervapor = 0
number_of_average1 = 0

for k in range(1,96):
    if (float(listc[k]) < 10 and listc[k] != '0'):
        valid_watervapor +=  float(listc[k])
        number_of_average1 += 1

average_watervapor = valid_watervapor/number_of_average1

for r in range(1,96):
    if float(listc[r]) >= 10:
        listc[r] = average_watervapor
    elif listc[r] == '0':
        listc[r] = average_watervapor       
#p = 0 
#for j in list6:
#    j = j-p
#    lista.remove(lista[j])
#    listb.remove(listb[j])
#    listc.remove(listc[j])
#    p += 1
#        
y = zip(lista,listb,listc)
x = list(y)

#print(x)
with open("temperature&fire&watervapor_01_07-15_10_22_-8.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerows(x)