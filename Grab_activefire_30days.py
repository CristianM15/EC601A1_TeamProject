# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 02:54:07 2016

@author: mac
"""

import urllib.request
site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1709188&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('activefire_15_10_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1709187&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('activefire_14_10_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1709186&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('activefire_13_10_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1709185&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('activefire_12_10_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1709184&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('activefire_11_10_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1709183&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('activefire_10_10_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1709182&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('activefire_09_10_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1708876&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('activefire_08_10_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1708875&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('activefire_07_10_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1708874&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('activefire_06_10_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1708873&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('activefire_05_10_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1708872&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('activefire_04_10_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1708871&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('activefire_03_10_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1708870&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('activefire_02_10_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1708869&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('activefire_01_10_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1708631&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('activefire_30_09_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1708630&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('activefire_29_09_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1708629&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('activefire_28_09_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1708628&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('activefire_27_09_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1708627&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('activefire_26_09_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1708626&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('activefire_25_09_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1708625&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('activefire_24_09_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1708624&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('activefire_23_09_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1708326&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('activefire_22_09_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1708325&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('activefire_21_09_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1708324&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('activefire_20_09_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1708323&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('activefire_19_09_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1708322&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('activefire_18_09_global.csv',"wb")
file.write(data)
file.close()

site = urllib.request.urlopen('http://neo.sci.gsfc.nasa.gov/servlet/RenderData?si=1708321&cs=rgb&format=CSV&width=360&height=180')
data = site.read()
file = open('activefire_17_09_global.csv',"wb")
file.write(data)
file.close()