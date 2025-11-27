'''
Vamos a crear aquí la clase camara para poder, posterioremente, hacer uso de ella 
en el codigo principal.
'''

import numpy as np
import cv2
import matplotlib.pyplot as plt
import datetime as dt

class camara:
    #Atributos de la camara
    
    #Ahora creamos algunos de los metodos 
    
    def __init__(self,indice):#Metodo constructor de la clase
    
        self.indice= indice
        self.winname = f'Imagen camara [{self.indice+1}]'
        self.cap = cv2.VideoCapture(self.indice)
        self.out = None
        self.cerrando = False
        self.shape = None
        self.activa = False
        self.preparada = False
    
    def grabar(self):#El metodo que vamos a usar para grabrar
        
        ret, frame= self.cap.read()
        self.shape = frame.shape
         
        out = self.crear_salida() #No necesitamos la fecha mas que para la out
        self.out = out
        self.preparada = True
        print(f"Cámara {self.indice+1} preparada")
        while self.preparada and not self.activa:
            print("Esperando a activar")
            if self.activa:
                break
        while self.cap.isOpened() and self.activa and not self.cerrando:
            
            ret, frame= self.cap.read()#Nos ira leyendo la camara a cada paso
    
            if ret== False:#Si la camara no esta disponible cierra el bucle
                break
    
            cv2.imshow(self.winname, frame)#Nos muestra lo que ve la camara, no es importante
            #es solo para saber que funciona, en el programa bueno se puede omitir
    
            self.out.write(frame)#Aqui grabamos el frame en la salida, esto es lo que queremos
    
            if cv2.waitKey(1)== 27 or self.cerrando:#si pulsamos la 'escape' se detiene la grabacion
                break
            
        if not self.cerrando:
            self.cerrar()       
        
    def crear_salida(self):
        h,w,_ = self.shape
        fecha= dt.datetime.now()
        path = '../videos/'
        file = f'{fecha.day}-{fecha.month}-{fecha.year}_{self.indice}.mp4'
        formato= cv2.VideoWriter_fourcc(*'mp4v')
        
        out= cv2.VideoWriter(path + file, formato, 30, (w,h))
        return out

    def activar(self):
        self.activa = not self.activa
        return self.activa
    
    
    def get_preparada(self):
        return self.preparada

    def cerrar(self, out=None):
        self.cerrando = True
        self.activa = False
        print("Cerrando camara")

        if out is None:
            self.out.release()
        else:
            out.release()
        self.cap.release()
        cv2.destroyWindow(self.winname)
        return True
        
        
    
        
    
        
        
    
    