# -*- coding: utf-8 -*-
"""
Created on Thu Nov  6 10:17:07 2025

@author: adelu
"""

"""
En este programa, una vez hemos visto un poco cómo funciona la librería de 
cv2, vamos a intentar controlar la webcam del ordenador.
"""
#%%Importamos todo lo necesario

import numpy as np
import matplotlib.pyplot as plt
from time import sleep
import cv2

#%%Creamos nuestra cámara

cap= cv2.VideoCapture(0)

"""
#Tomamos un fotograma de nuestra cámara para ver si va bien
ret, frame= cap.read()

#Lo enseñamos
plt.imshow(frame)
"""

#%% Vamos a obtener un video y guardarlo

#%%% Parámetros necesarios

ret, frame= cap.read()#Para obtener las dimensiones de la imagen, así no habrá
#que hacerlo a cada paso del bucle
h,w,_= frame.shape #Dimensiones de la imagen

formato= cv2.VideoWriter_fourcc(*'mp4v') #Nuestro CODE

out= cv2.VideoWriter('output.mp4', formato, 30, (w,h)) #La salida del vídeo

#%%% El bucle que seguiremos

while cap.isOpened():
    ret, frame= cap.read()#Nos irá leyendo la cámara a cada paso
    
    if ret== False:#Si la cámara no está disponible cierra el bucle
        break
    
    cv2.imshow('imagen', frame)#Nos muestra lo que ve la cámara, no es importante
    #es sólo para saber que funciona, en el programa bueno se puede omitir
    
    out.write(frame)#Aquí grabamos el frame en la salida, esto es lo que queremos
    
    if cv2.waitKey(1)== 27:#si pulsamos la 'escape' se detiene la grabación
        break
    
    #sleep(1/30)#Supongo que para no sobrecargar y de tiempo a evaluar si la cámara
    #ha dejado de estar tisponible o ha habido algún fallo

#%% Liberar las cámaras y cerrar las ventanas 
   
cap.release()#Libero la cámara
out.release()#Libero el outpout
cv2.destroyAllWindows()#Cierro las ventanas
























