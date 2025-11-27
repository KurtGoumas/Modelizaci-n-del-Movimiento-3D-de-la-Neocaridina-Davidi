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
from time import sleep #Para llevar recuento del tiempo
import datetime as dt #Para llevar recuento del tiempo
import os #Para guardar los videos en la carpeta que queramos
import cv2 #Para procesado de video

#%%Creamos nuestra cámara
def crear_camara(numero_camara=0):
    """
    Crea y retorna un objeto de captura de video desde la cámara especificada.
    
    Args:
        numero_camara (int): Número de la cámara a utilizar (por defecto 0)
    
    Returns:
        cv2.VideoCapture: Objeto de captura de video
    """
    return cv2.VideoCapture(numero_camara)

"""
#Tomamos un fotograma de nuestra cámara para ver si va bien
ret, frame= cap.read()

#Lo enseñamos
plt.imshow(frame)
"""

#%% Vamos a obtener un video y guardarlo
def listar_camaras(max_camaras=10):
    """
    Lista las cámaras disponibles en el sistema.
    
    Args:
        max_camaras (int): Número máximo de cámaras a verificar (por defecto 10)
    
    Returns:
        list: Lista de índices de cámaras disponibles
    """
    camaras_disponibles = [i for i in range(max_camaras) if cv2.VideoCapture(i).isOpened() and cv2.VideoCapture(i).release() is None]
    return camaras_disponibles
#%%% Parámetros necesarios

def parametros_necesarios(cap):
    ret, frame= cap.read()#Para obtener las dimensiones de la imagen, así no habrá
    #que hacerlo a cada paso del bucle
    h,w,_= frame.shape #Dimensiones de la imagen

    path= r'C:\Users\adelu\OneDrive\Escritorio\FisicaAlicante\Año_V\Gambas_con_Alzheimer\Camaras\videos'
    #En path es donde ponemos la ruta de la carpeta en la que vamos a guardar los videos

    formato= cv2.VideoWriter_fourcc(*'mp4v') #Nuestro CODE

    out= cv2.VideoWriter(path + 'output.mp4', formato, 30, (w,h)) #La salida del vídeo
    return h, w, path, formato, out, ret, frame
def bucle_grabacion(cap, out, h, w):
    video= []#Aquí es donde vamos a guardar todos los fotogramas

    while cap.isOpened():
        ret, frame= cap.read()#Nos irá leyendo la cámara a cada paso
        
        if ret== False:#Si la cámara no está disponible cierra el bucle
            VideoMatriz= np.zeros([len(video),h,w,3])
            VideoMatriz[:]+= video[:]
            #V= VideoMatriz.reshape(len(video*h*w),3)
            break
        
        cv2.imshow('imagen', frame)#Nos muestra lo que ve la cámara, no es importante
        #es sólo para saber que funciona, en el programa bueno se puede omitir
        
        video.append(frame)#Intentamos meter todos los frames en la lista, video
        #out.write(frame)#Aquí grabamos el frame en la salida, esto es lo que queremos
        
        if cv2.waitKey(1)== 27:#si pulsamos la 'escape' se detiene la grabación
            VideoMatriz= np.zeros([len(video),h,w,3])
            VideoMatriz[:]+= video[:]
            #out.write(VideoMatriz[:])
            break
        
        #sleep(1/30)#Supongo que para no sobrecargar y de tiempo a evaluar si la cámara
        #ha dejado de estar disponible o ha habido algún fallo

   
def liberar_camaras(cap, out):
    cap.release()#Libero la cámara
    out.release()#Libero el outpout
    cv2.destroyAllWindows()#Cierro las ventanas


