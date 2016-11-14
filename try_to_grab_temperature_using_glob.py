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
            list1.append(row[215])
        
        lista.append(list1[50])
        
for i in range(1,30):
    if lista[i] == '99999.0':
        lista[i] = ' '

        
Trials2 = glob.glob('activefire*global.csv')

listb = ['Fire']

for file_name in Trials2:
    with open(file_name, 'r') as inp:
        list1 = []
        for row in csv.reader(inp):
            list1.append(row[215])
        
        listb.append(list1[50])
    
for i in range(1,30):
    if listb[i] == '99999.0':
        listb[i] = 0
    elif listb[i] == '0.1':
        listb[i] = 0
    else:
        listb[i] = 1
        
y = zip(lista,listb)
x = list(y)

#print(x)
with open("temperature_and_fire_15_10-19_09_35_40.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerows(x)