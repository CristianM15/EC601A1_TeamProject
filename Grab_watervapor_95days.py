# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 01:31:24 2016

@author: mac
"""

import urllib.request

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1709031&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_15_10_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1709030&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_14_10_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1709029&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_13_10_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1709028&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_12_10_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1709027&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_11_10_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1709026&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_10_10_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1709025&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_09_10_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1708745&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_08_10_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1708742&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_07_10_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1708739&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_06_10_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1708735&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_05_10_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1708732&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_04_10_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1708729&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_03_10_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1708726&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_02_10_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1708723&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_01_10_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1708554&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_30_09_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1708553&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_29_09_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1708552&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_28_09_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1708551&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_27_09_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1708550&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_26_09_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1708549&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_25_09_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1708548&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_24_09_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1708547&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_23_09_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1708146&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_22_09_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1708145&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_21_09_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1708144&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_20_09_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1708143&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_19_09_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1708142&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_18_09_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1708141&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_17_09_global.csv',"wb")
file.write(data)
file.close()

#site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1708140&cs=rgb&format=CSV&width=360&height=180')
#data = site.read()
#file = open('watervapor_16_09_global.csv',"wb")
#file.write(data)
#file.close()
#
#site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1708139&cs=rgb&format=CSV&width=360&height=180')
#data = site.read()
#file = open('watervapor_15_09_global.csv',"wb")
#file.write(data)
#file.close()
#
#site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1708138&cs=rgb&format=CSV&width=360&height=180')
#data = site.read()
#file = open('watervapor_14_09_global.csv',"wb")
#file.write(data)
#file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1708137&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_13_09_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1708136&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_12_09_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1708135&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_11_09_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1707857&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_10_09_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1707854&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_09_09_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1707851&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_08_09_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1707848&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_07_09_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1707494&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_06_09_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1707493&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_05_09_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1707492&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_04_09_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1707491&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_03_09_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1707490&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_02_09_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1707489&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_01_09_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1707488&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_31_08_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1707487&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_30_08_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1707164&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_29_08_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1707161&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_28_08_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1707158&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_27_08_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1707190&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_26_08_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1707189&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_25_08_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1707188&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_24_08_global.csv',"wb")
file.write(data)
file.close()

#site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1707187&cs=rgb&format=CSV&width=360&height=180')
#data = site.read()
#file = open('watervapor_23_08_global.csv',"wb")
#file.write(data)
#file.close()
#
#site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1707186&cs=rgb&format=CSV&width=360&height=180')
#data = site.read()
#file = open('watervapor_22_08_global.csv',"wb")
#file.write(data)
#file.close()
#
#site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1708143&cs=rgb&format=CSV&width=360&height=180')
#data = site.read()
#file = open('watervapor_21_08_global.csv',"wb")
#file.write(data)
#file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1706781&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_20_08_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1707187&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_19_08_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1707186&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_18_08_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1706782&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_17_08_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1706782&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_16_08_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1707186&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_15_08_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1706781&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_14_08_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1707188&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_13_08_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1707190&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_12_08_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1707164&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_11_08_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1707487&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_10_08_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1706742&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_09_08_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1706777&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_08_08_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1706774&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_07_08_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1706771&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_06_08_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1706229&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_05_08_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1706296&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_04_08_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1706293&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_03_08_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1706290&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_02_08_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1706286&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_01_08_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1706284&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_31_07_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1706283&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_30_07_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1706280&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_29_07_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1706280&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_28_07_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1706280&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_27_07_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1706115&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_26_07_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1705546&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_19_07_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1705543&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_18_07_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1705540&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_17_07_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1705537&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_16_07_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1705534&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_15_07_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1705531&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_14_07_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1705528&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_13_07_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1705339&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_12_07_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1705338&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_11_07_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1705337&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_10_07_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1705336&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_09_07_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1705335&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_08_07_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1705334&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_07_07_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1705333&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_06_07_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1705332&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_05_07_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1705013&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_04_07_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1705012&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_03_07_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1705011&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_02_07_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1705009&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('watervapor_01_07_global.csv',"wb")
file.write(data)
file.close()