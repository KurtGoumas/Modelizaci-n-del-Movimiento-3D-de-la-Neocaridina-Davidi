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

cap1= cv2.VideoCapture(0)
cap2= cv2.VideoCapture(1)

"""
#Tomamos un fotograma de nuestra cámara para ver si va bien
ret, frame= cap.read()

#Lo enseñamos
plt.imshow(frame)
"""

#%% Vamos a obtener un video y guardarlo

#%%% Parámetros necesarios

ret1, frame1= cap1.read()#Para obtener las dimensiones de la imagen, así no habrá
#que hacerlo a cada paso del bucle
h1,w1,_= frame1.shape #Dimensiones de la imagen

ret2, frame2= cap2.read()#Para obtener las dimensiones de la imagen, así no habrá
#que hacerlo a cada paso del bucle
h2,w2,_= frame2.shape

formato= cv2.VideoWriter_fourcc(*'mp4v') #Nuestro CODE

out1= cv2.VideoWriter('output1.mp4', formato, 30, (w1,h1)) #La salida del vídeo

out2= cv2.VideoWriter('output2.mp4', formato, 30, (w2,h2))

out3= cv2.VideoWriter('output3.mp4', formato, 30, (w2,h2+h1))

#%%% El bucle que seguiremos
video1=[]
video2= []
while cap1.isOpened() and cap2.isOpened():
    ret1, frame1= cap1.read()#Nos irá leyendo la cámara a cada paso
    ret2, frame2= cap2.read()
    if ret1== False or ret2== False:#Si la cámara no está disponible cierra el bucle
        break
    
    cv2.imshow('imagen', frame1)#Nos muestra lo que ve la cámara, no es importante
    #es sólo para saber que funciona, en el programa bueno se puede omitir
    video1.append(frame1)
    
    cv2.imshow('imagen2', frame2)
    video2.append(frame2)
    
    #out1.write(frame1)#Aquí grabamos el frame en la salida, esto es lo que queremos
    
    #out2.write(frame2)
    
    out3.write(frame1)
    if cv2.waitKey(1)== 27:#si pulsamos la 'escape' se detiene la grabación
        break
    
    #sleep(1/30)#Supongo que para no sobrecargar y de tiempo a evaluar si la cámara
    #ha dejado de estar tisponible o ha habido algún fallo

#%% Liberar las cámaras y cerrar las ventanas 
   
cap1.release()#Libero la cámara
cap2.release()

out1.release()#Libero el outpout
out2.release()

cv2.destroyAllWindows()#Cierro las ventanas
























