# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 21:22:46 2016

@author: mac
"""

import urllib.request
site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1709168&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('temperature_15_10_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1709167&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('temperature_14_10_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1709166&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('temperature_13_10_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1709165&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('temperature_12_10_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1709164&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('temperature_11_10_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1709163&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('temperature_10_10_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1709162&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('temperature_09_10_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1708858&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('temperature_08_10_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1708857&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('temperature_07_10_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1708856&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('temperature_06_10_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1708855&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('temperature_05_10_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1708854&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('temperature_04_10_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1708853&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('temperature_03_10_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1708852&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('temperature_02_10_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1708851&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('temperature_01_10_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1708457&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('temperature_30_09_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1708456&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('temperature_29_09_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1708455&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('temperature_28_09_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1708454&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('temperature_27_09_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1708453&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('temperature_26_09_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1708452&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('temperature_25_09_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1708451&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('temperature_24_09_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1708450&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('temperature_23_09_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1708275&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('temperature_22_09_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1708274&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('temperature_21_09_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1708273&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('temperature_20_09_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1708272&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('temperature_19_09_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1708271&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('temperature_18_09_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1708270&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('temperature_17_09_global.csv',"wb")
file.write(data)
file.close()

import csv
with open('temperature_15_10_global.csv', 'r') as inp:
#with open('first_edit.csv', 'w') as out:
#    inp = csv.reader(open('MOD11C1_D_LSTDA_2016-10-14_rgb_360x180 copy.csv'))
    
    list1 = ['Longitude']
    list2 = ['latitude']
    list3 = ['Temperature_15_10']
#    建立三个list
    

    j = 90
#    j是经度
    
    for row in csv.reader(inp):
        for i in range(360):
#            i是纬度
            if row[i] == '99999.0':
                i += 1
                
            elif row[i] == '-25.0':
                i += 1
                
            else:
                if i <= 180:
                    list1.append(i)
                    list2.append(j)
                    list3.append(row[i])
                    i += 1
                else:
                    list1.append(i-360)
                    
                    list2.append(j)
                    list3.append(row[i])
                    i += 1
                
        j -= 1
        
with open('temperature_14_10_global.csv', 'r') as inp:

    list4 = ['Temperature_14_10']
#    建立list 
    
    for row in csv.reader(inp):
        for i in range(360):
#            i是纬度
            if row[i] == '99999.0':
                i += 1
                
            elif row[i] == '-25.0':
                i += 1
                
            else:
                if i <= 180:
                    
                    list4.append(row[i])
                    i += 1
                else:
                    list4.append(row[i])
                    i += 1
    
with open('temperature_13_10_global.csv', 'r') as inp:

    list5 = ['Temperature_13_10']
#    建立list 
    
    for row in csv.reader(inp):
        for i in range(360):
#            i是纬度
            if row[i] == '99999.0':
                i += 1
                
            elif row[i] == '-25.0':
                i += 1
                
            else:
                if i <= 180:
                    
                    list5.append(row[i])
                    i += 1
                else:
                    list5.append(row[i])
                    i += 1
                    
with open('temperature_13_10_global.csv', 'r') as inp:

    list6 = ['Temperature_12_10']
#    建立list 
    
    for row in csv.reader(inp):
        for i in range(360):
#            i是纬度
            if row[i] == '99999.0':
                i += 1
                
            elif row[i] == '-25.0':
                i += 1
                
            else:
                if i <= 180:
                    
                    list6.append(row[i])
                    i += 1
                else:
                    list6.append(row[i])
                    i += 1
                    
with open('temperature_12_10_global.csv', 'r') as inp:

    list7 = ['Temperature_12_10']
#    建立list 
    
    for row in csv.reader(inp):
        for i in range(360):
#            i是纬度
            if row[i] == '99999.0':
                i += 1
                
            elif row[i] == '-25.0':
                i += 1
                
            else:
                if i <= 180:
                    
                    list7.append(row[i])
                    i += 1
                else:
                    list7.append(row[i])
                    i += 1
                    
with open('temperature_11_10_global.csv', 'r') as inp:

    list8 = ['Temperature_11_10']
#    建立list 
    
    for row in csv.reader(inp):
        for i in range(360):
#            i是纬度
            if row[i] == '99999.0':
                i += 1
                
            elif row[i] == '-25.0':
                i += 1
                
            else:
                if i <= 180:
                    
                    list8.append(row[i])
                    i += 1
                else:
                    list8.append(row[i])
                    i += 1
                    
with open('temperature_10_10_global.csv', 'r') as inp:

    list9 = ['Temperature_10_10']
#    建立list 
    
    for row in csv.reader(inp):
        for i in range(360):
#            i是纬度
            if row[i] == '99999.0':
                i += 1
                
            elif row[i] == '-25.0':
                i += 1
                
            else:
                if i <= 180:
                    
                    list9.append(row[i])
                    i += 1
                else:
                    list9.append(row[i])
                    i += 1
                    
with open('temperature_09_10_global.csv', 'r') as inp:

    list10 = ['Temperature_09_10']
#    建立list 
    
    for row in csv.reader(inp):
        for i in range(360):
#            i是纬度
            if row[i] == '99999.0':
                i += 1
                
            elif row[i] == '-25.0':
                i += 1
                
            else:
                if i <= 180:
                    
                    list10.append(row[i])
                    i += 1
                else:
                    list10.append(row[i])
                    i += 1
                    
with open('temperature_08_10_global.csv', 'r') as inp:

    list11 = ['Temperature_08_10']
#    建立list 
    
    for row in csv.reader(inp):
        for i in range(360):
#            i是纬度
            if row[i] == '99999.0':
                i += 1
                
            elif row[i] == '-25.0':
                i += 1
                
            else:
                if i <= 180:
                    
                    list11.append(row[i])
                    i += 1
                else:
                    list11.append(row[i])
                    i += 1
                    
with open('temperature_07_10_global.csv', 'r') as inp:

    list12 = ['Temperature_07_10']
#    建立list 
    
    for row in csv.reader(inp):
        for i in range(360):
#            i是纬度
            if row[i] == '99999.0':
                i += 1
                
            elif row[i] == '-25.0':
                i += 1
                
            else:
                if i <= 180:
                    
                    list12.append(row[i])
                    i += 1
                else:
                    list12.append(row[i])
                    i += 1
                    
with open('temperature_06_10_global.csv', 'r') as inp:

    list13 = ['Temperature_06_10']
#    建立list 
    
    for row in csv.reader(inp):
        for i in range(360):
#            i是纬度
            if row[i] == '99999.0':
                i += 1
                
            elif row[i] == '-25.0':
                i += 1
                
            else:
                if i <= 180:
                    
                    list13.append(row[i])
                    i += 1
                else:
                    list13.append(row[i])
                    i += 1
                    
with open('temperature_05_10_global.csv', 'r') as inp:

    list14 = ['Temperature_05_10']
#    建立list 
    
    for row in csv.reader(inp):
        for i in range(360):
#            i是纬度
            if row[i] == '99999.0':
                i += 1
                
            elif row[i] == '-25.0':
                i += 1
                
            else:
                if i <= 180:
                    
                    list14.append(row[i])
                    i += 1
                else:
                    list14.append(row[i])
                    i += 1
                    
with open('temperature_04_10_global.csv', 'r') as inp:

    list15 = ['Temperature_04_10']
#    建立list 
    
    for row in csv.reader(inp):
        for i in range(360):
#            i是纬度
            if row[i] == '99999.0':
                i += 1
                
            elif row[i] == '-25.0':
                i += 1
                
            else:
                if i <= 180:
                    
                    list15.append(row[i])
                    i += 1
                else:
                    list15.append(row[i])
                    i += 1
            
with open('temperature_03_10_global.csv', 'r') as inp:

    list16 = ['Temperature_03_10']
#    建立list 
    
    for row in csv.reader(inp):
        for i in range(360):
#            i是纬度
            if row[i] == '99999.0':
                i += 1
                
            elif row[i] == '-25.0':
                i += 1
                
            else:
                if i <= 180:
                    
                    list16.append(row[i])
                    i += 1
                else:
                    list16.append(row[i])
                    i += 1
                    
with open('temperature_02_10_global.csv', 'r') as inp:

    list17 = ['Temperature_02_10']
#    建立list 
    
    for row in csv.reader(inp):
        for i in range(360):
#            i是纬度
            if row[i] == '99999.0':
                i += 1
                
            elif row[i] == '-25.0':
                i += 1
                
            else:
                if i <= 180:
                    
                    list17.append(row[i])
                    i += 1
                else:
                    list17.append(row[i])
                    i += 1
                    
with open('temperature_01_10_global.csv', 'r') as inp:

    list18 = ['Temperature_01_10']
#    建立list 
    
    for row in csv.reader(inp):
        for i in range(360):
#            i是纬度
            if row[i] == '99999.0':
                i += 1
                
            elif row[i] == '-25.0':
                i += 1
                
            else:
                if i <= 180:
                    
                    list18.append(row[i])
                    i += 1
                else:
                    list18.append(row[i])
                    i += 1
                    
with open('temperature_30_09_global.csv', 'r') as inp:

    list19 = ['Temperature_30_09']
#    建立list 
    
    for row in csv.reader(inp):
        for i in range(360):
#            i是纬度
            if row[i] == '99999.0':
                i += 1
                
            elif row[i] == '-25.0':
                i += 1
                
            else:
                if i <= 180:
                    
                    list19.append(row[i])
                    i += 1
                else:
                    list19.append(row[i])
                    i += 1
                    
with open('temperature_29_09_global.csv', 'r') as inp:

    list20 = ['Temperature_29_09']
#    建立list 
    
    for row in csv.reader(inp):
        for i in range(360):
#            i是纬度
            if row[i] == '99999.0':
                i += 1
                
            elif row[i] == '-25.0':
                i += 1
                
            else:
                if i <= 180:
                    
                    list20.append(row[i])
                    i += 1
                else:
                    list20.append(row[i])
                    i += 1
                    
with open('temperature_28_09_global.csv', 'r') as inp:

    list21 = ['Temperature_28_09']
#    建立list 
    
    for row in csv.reader(inp):
        for i in range(360):
#            i是纬度
            if row[i] == '99999.0':
                i += 1
                
            elif row[i] == '-25.0':
                i += 1
                
            else:
                if i <= 180:
                    
                    list21.append(row[i])
                    i += 1
                else:
                    list21.append(row[i])
                    i += 1
                    
with open('temperature_28_09_global.csv', 'r') as inp:

    list22 = ['Temperature_28_09']
#    建立list 
    
    for row in csv.reader(inp):
        for i in range(360):
#            i是纬度
            if row[i] == '99999.0':
                i += 1
                
            elif row[i] == '-25.0':
                i += 1
                
            else:
                if i <= 180:
                    
                    list22.append(row[i])
                    i += 1
                else:
                    list22.append(row[i])
                    i += 1
                    
with open('temperature_28_09_global.csv', 'r') as inp:

    list23 = ['Temperature_28_09']
#    建立list 
    
    for row in csv.reader(inp):
        for i in range(360):
#            i是纬度
            if row[i] == '99999.0':
                i += 1
                
            elif row[i] == '-25.0':
                i += 1
                
            else:
                if i <= 180:
                    
                    list23.append(row[i])
                    i += 1
                else:
                    list23.append(row[i])
                    i += 1
                    
with open('temperature_27_09_global.csv', 'r') as inp:

    list24 = ['Temperature_27_09']
#    建立list 
    
    for row in csv.reader(inp):
        for i in range(360):
#            i是纬度
            if row[i] == '99999.0':
                i += 1
                
            elif row[i] == '-25.0':
                i += 1
                
            else:
                if i <= 180:
                    
                    list24.append(row[i])
                    i += 1
                else:
                    list24.append(row[i])
                    i += 1
                    
with open('temperature_26_09_global.csv', 'r') as inp:

    list25 = ['Temperature_26_09']
#    建立list 
    
    for row in csv.reader(inp):
        for i in range(360):
#            i是纬度
            if row[i] == '99999.0':
                i += 1
                
            elif row[i] == '-25.0':
                i += 1
                
            else:
                if i <= 180:
                    
                    list25.append(row[i])
                    i += 1
                else:
                    list25.append(row[i])
                    i += 1
                    
with open('temperature_25_09_global.csv', 'r') as inp:

    list26 = ['Temperature_25_09']
#    建立list 
    
    for row in csv.reader(inp):
        for i in range(360):
#            i是纬度
            if row[i] == '99999.0':
                i += 1
                
            elif row[i] == '-25.0':
                i += 1
                
            else:
                if i <= 180:
                    
                    list26.append(row[i])
                    i += 1
                else:
                    list26.append(row[i])
                    i += 1
                    
with open('temperature_24_09_global.csv', 'r') as inp:

    list27 = ['Temperature_24_09']
#    建立list 
    
    for row in csv.reader(inp):
        for i in range(360):
#            i是纬度
            if row[i] == '99999.0':
                i += 1
                
            elif row[i] == '-25.0':
                i += 1
                
            else:
                if i <= 180:
                    
                    list27.append(row[i])
                    i += 1
                else:
                    list27.append(row[i])
                    i += 1
                    
with open('temperature_23_09_global.csv', 'r') as inp:

    list28 = ['Temperature_23_09']
#    建立list 
    
    for row in csv.reader(inp):
        for i in range(360):
#            i是纬度
            if row[i] == '99999.0':
                i += 1
                
            elif row[i] == '-25.0':
                i += 1
                
            else:
                if i <= 180:
                    
                    list28.append(row[i])
                    i += 1
                else:
                    list28.append(row[i])
                    i += 1
                    
with open('temperature_22_09_global.csv', 'r') as inp:

    list29 = ['Temperature_22_09']
#    建立list 
    
    for row in csv.reader(inp):
        for i in range(360):
#            i是纬度
            if row[i] == '99999.0':
                i += 1
                
            elif row[i] == '-25.0':
                i += 1
                
            else:
                if i <= 180:
                    
                    list29.append(row[i])
                    i += 1
                else:
                    list29.append(row[i])
                    i += 1
                    
with open('temperature_21_09_global.csv', 'r') as inp:

    list30 = ['Temperature_21_09']
#    建立list 
    
    for row in csv.reader(inp):
        for i in range(360):
#            i是纬度
            if row[i] == '99999.0':
                i += 1
                
            elif row[i] == '-25.0':
                i += 1
                
            else:
                if i <= 180:
                    
                    list30.append(row[i])
                    i += 1
                else:
                    list30.append(row[i])
                    i += 1
                    
with open('temperature_20_09_global.csv', 'r') as inp:

    list31 = ['Temperature_20_09']
#    建立list 
    
    for row in csv.reader(inp):
        for i in range(360):
#            i是纬度
            if row[i] == '99999.0':
                i += 1
                
            elif row[i] == '-25.0':
                i += 1
                
            else:
                if i <= 180:
                    
                    list31.append(row[i])
                    i += 1
                else:
                    list31.append(row[i])
                    i += 1
                    
with open('temperature_19_09_global.csv', 'r') as inp:

    list32 = ['Temperature_19_09']
#    建立list 
    
    for row in csv.reader(inp):
        for i in range(360):
#            i是纬度
            if row[i] == '99999.0':
                i += 1
                
            elif row[i] == '-25.0':
                i += 1
                
            else:
                if i <= 180:
                    
                    list32.append(row[i])
                    i += 1
                else:
                    list32.append(row[i])
                    i += 1
                    
with open('temperature_18_09_global.csv', 'r') as inp:

    list33 = ['Temperature_18_09']
#    建立list 
    
    for row in csv.reader(inp):
        for i in range(360):
#            i是纬度
            if row[i] == '99999.0':
                i += 1
                
            elif row[i] == '-25.0':
                i += 1
                
            else:
                if i <= 180:
                    
                    list33.append(row[i])
                    i += 1
                else:
                    list33.append(row[i])
                    i += 1
                    
with open('temperature_17_09_global.csv', 'r') as inp:

    list34 = ['Temperature_17_09']
#    建立list 
    
    for row in csv.reader(inp):
        for i in range(360):
#            i是纬度
            if row[i] == '99999.0':
                i += 1
                
            elif row[i] == '-25.0':
                i += 1
                
            else:
                if i <= 180:
                    
                    list34.append(row[i])
                    i += 1
                else:
                    list34.append(row[i])
                    i += 1
        
    y = zip(list1,list2,list34,list33,list32,list31,list29,list28,list27,list26,list25,list24,list23,list22,list21,list20,list19,list18,list17,list16,list15,list14,list13,list12,list11,list10,list9,list8,list7,list6,list5,list4,list3)
    x = list(y)

    with open("temperature_30days_land.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerows(x)