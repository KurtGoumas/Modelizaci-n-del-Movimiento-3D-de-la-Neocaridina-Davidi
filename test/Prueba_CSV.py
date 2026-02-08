# -*- coding: utf-8 -*-
"""
Created on Tue Feb  3 17:15:09 2026

@author: User
"""

import csv
import numpy as np
import os 
with open('PruebaCSV.csv', 'w', newline = '') as file:
    formato = csv.writer(file, delimiter = ' ',dialect='excel', quotechar='|' ,quoting=csv.QUOTE_ALL)
    
    lista = ["Tipo de archivo","Fecha","Hora","Minuto", "Segundo", 
             "Tiempo desde que comenzo el experimento", "Codec", "Bitrate", 
             "Exposicion","Ganancia", "White Balance"]
    formato.writerow(lista)

print("Terminado. El archivo se ha cerrado solo")