from threading import Thread
from control.control import *
from control.Camara_arreglo import Camara
from control.Camara import camara
import cv2   
import time


class CamThread(Thread):
    def __init__(self, camara, start):
        super().__init__()
        self.cam = camara
        self.comienzo= start
        self.frame = None
        self.running = True
        self.Contador_Frames= 0
        self.Prom_fps= 0

    def run(self):
        while self.running:
            ret, frame = self.cam.cap.read()
            if ret:
                self.frame = frame
                self.cam.out.write(frame)
                MetadatosIteracionCamara= MetadatosIteracion(self.cam.filename,self.cam,self)
                self.Prom_fps+= self.cam.fps 
                self.Contador_Frames += 1           

    def stop(self):
        self.running = False

def main():

    indices= listar_indices()
    tiempo, intervalo_grabacion= tiempo_grabacion()
    
    cam1 = Camara(indices[0])#Esto lo abrimos inicialmente para obtener los metadatos globales
    #cam2 = Camara(indices[1])
    cam1.preparar()
    #cam2.preparar()

    cam1.activar()
    #cam2.activar()

    #t1 = CamThread(cam1)
    #t2 = CamThread(cam2)

    MetadatosGLobalesCamara1= MetadatosGlobalesIniciales(cam1.filename, cam1)
    #MetadatosGLobalesCamara2= MetadatosGlobalesIniciales(cam2.filename, cam2)

    Promedio_fps1= 0
    #Promedio_fps2= 0
    Frames1= 0
    #Frames2= 0

    start_time = time.time()
    while time.time() - start_time < tiempo:
        cam1 = Camara(indices[0])
        #cam2 = Camara(indices[1])

        cam1.preparar()
        #cam2.preparar()

        cam1.activar()
        #cam2.activar()

        t1 = CamThread(cam1,start_time)
        #t2 = CamThread(cam2,start_time)

        t1.start()
        #t2.start()

        start_ciclo = time.time()
    
        while time.time() - start_ciclo < intervalo_grabacion:
    
            grab= time.time()- start_time
            h= int(grab/3600) 
            m= int(grab/60) - h*60 
            s= int(grab)-h*3600-m*60

            print(f'{h}:{m}:{s}')
            if t1.frame is not None:
                cv2.imshow("Camara 1", t1.frame)
            #if t2.frame is not None:
                #cv2.imshow("Camara 2", t2.frame)
            if cv2.waitKey(1) == 27:
                break
            if cv2.waitKey(1)== ord('e'):
                cam1.exp_up()
                #cam2.exp_up()
            if cv2.waitKey(1)== ord('q'):
                cam1.exp_down()
                #cam2.exp_down()
            if cv2.waitKey(1)== ord('a'):
                cam1.gain_up()
                #cam2.gain_up()
            if cv2.waitKey(1)== ord('d'):
                cam1.gain_down()
                #cam2.gain_down()

        MetadatosFinalesCamara1= MetadatosGlobalesFinales(t1)
        #MetadatosFinalesCamara2= MetadatosGlobalesFinales(t2)

        Promedio_fps1+= MetadatosFinalesCamara1[0]
        #Promedio_fps2+=MetadatosFinalesCamara2[0]

        Frames1+= MetadatosFinalesCamara1[1]
        #Frames2+= MetadatosFinalesCamara2[1]

        t1.stop()
        #t2.stop()
        t1.join()
        #t2.join()

        cam1.cerrar_salida()
        #cam2.cerrar_salida()
        cv2.destroyAllWindows()
    cam1.cerrar()
    #cam2.cerrar()

    Promedio_fps1= Promedio_fps1/Frames1
    #Promedio_fps2= Promedio_fps2/Frames2

    Resumen1= Resumen_final(MetadatosGLobalesCamara1 ,Promedio_fps1,Frames1)
    #Resumen2= Resumen_final(MetadatosGLobalesCamara2 ,Promedio_fps2,Frames2)
    print("Programa finalizado")

if __name__ == "__main__":
    main()