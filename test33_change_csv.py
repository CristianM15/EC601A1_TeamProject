# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 22:23:08 2016

@author: mac
"""

import csv
with open('MOD11C1_D_LSTDA_2016-10-14_rgb_360x180 copy.csv', 'r') as inp, open('first_edit.csv', 'w') as out:
#with open('first_edit.csv', 'w') as out:
#    inp = csv.reader(open('MOD11C1_D_LSTDA_2016-10-14_rgb_360x180 copy.csv'))
    
    list1 = []
    list2 = []
    list3 = []
    
    writer = csv.writer(out)
    j = 0
    for row in csv.reader(inp):
        for i in range(360):
            if row[i] == '99999.0':
#                list1.append(i)
#                list2.append(j)
#                list3.append(row[i])
                i += 1
            elif row[i] == '-25.0':
                i += 1
            else:
                list1.append(i)
                list2.append(j)
                list3.append(row[i])
                i += 1
        j += 1
        
    y = zip(list1,list2,list3)
    x = list(y)
#    print(x)
    
    with open("output.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerows(x)
                
#                print(i)
#        j += 1
#        print(j)
                
#        print(row[1])
#        for i in range(361):
#            if row[1] = 
#        for i in range():
#            #for j in range():
#                if row[i] != '99999':
#                    row[i] == '0'
#        writer.writerow(row)
#    lines = [l for l in inp]
#    for i in range(91):
#        for j in range(91):
#            if lines[i][j] == '99999':
#                lines[i][j] = '0'
#    writer.writerow(lines)
