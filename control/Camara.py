"""
Vamos a crear aquí la clase camara para poder, posterioremente, hacer uso de ella 
en el código principal.
"""

import numpy as np
import cv2
import matplotlib.pyplot as plt
import datetime as dt

class camara:
    #Atributos de la cámara
    
    #Ahora creamos algunos de los métodos 
    
    def __init__(self,indice):#Método constructor de la clase
    
        self.indice= indice
        self.cap = cv2.VideoCapture(self.indice)
    
    def grabar(self):#El método que vamos a usar para grabrar
        
        ret, frame= self.cap.read()
        
        h,w,_= frame.shape
        
        
        
        fecha, out = self.crear_salida()
        
        while self.cap.isOpened():
            
            ret, frame= self.cap.read()#Nos irá leyendo la cámara a cada paso
    
            if ret== False:#Si la cámara no está disponible cierra el bucle
                break
    
            cv2.imshow('imagen', frame)#Nos muestra lo que ve la cámara, no es importante
            #es sólo para saber que funciona, en el programa bueno se puede omitir
    
            out.write(frame)#Aquí grabamos el frame en la salida, esto es lo que queremos
    
            if cv2.waitKey(1)== 27:#si pulsamos la 'escape' se detiene la grabación
                break
            
        self.cerrar(out)          
        
    def crear_salida(self):
        
        fecha= dt.datetime.now()
        formato= cv2.VideoWriter_fourcc(*'mp4v')
        out= cv2.VideoWriter('{fecha[0]}/{fecha[1]}/{fecha[2]}_{indice}.mp4', formato, 30, (w,h))
        return fecha, out
    
    def cerrar(self, out):
        self.cap.release()
        out.release()
        cv2.destroyAllWindows()
        
        
    
        
    
        
        
    
    