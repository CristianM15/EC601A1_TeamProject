# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 21:32:43 2016

@author: mac
"""

import urllib.request
site = urllib.request.urlopen('https://firms.modaps.eosdis.nasa.gov/active_fire/c6/text/MODIS_C6_Global_24h.csv')
data = site.read()
file = open("file.text","wb")
file.write(data)
file.close()