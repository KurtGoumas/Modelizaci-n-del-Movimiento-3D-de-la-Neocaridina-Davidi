import cv2
import time
import datetime as dt
import csv

def listar_indices(max=10):
    l = [i for i in range(max) if cv2.VideoCapture(i).isOpened() and cv2.VideoCapture(i).release() is None]
    return l

def tiempo_grabacion():
    horas= int(input('Horas: '))
    minutos= int(input('Minutos: '))
    segundos= int(input('Segundos: '))

    intervalos_minutos= int(input('Intervalos de grabación en minutos: '))
    intervalos_segundos= int(input('Intervalos de grabación en segundos: '))
    
    tiempo= horas*3600 + minutos*60 + segundos
    intervalo= intervalos_minutos*60 + intervalos_segundos
    return tiempo,intervalo

def MetadatosGlobales(Nombre, camara):
    with open(Nombre + '.csv', 'w', newline='') as file:
        formato = csv.writer(file, delimiter = ' ',dialect='excel', quotechar='|' ,quoting=csv.QUOTE_ALL)
        lista= [f'{camara.shape}',f'{camara.fourcc}']
        formato.writerow(lista)

    return True

def MetadatosIteracion(Nombre,camara,hilo):
    with open(Nombre + '.csv', 'a', newline='') as file:
        formato = csv.writer(file, delimiter = ' ',dialect='excel', quotechar='|' ,quoting=csv.QUOTE_ALL)
        lista= [f'{hilo.Contador_Frames}', 
                f'{dt.datetime.now().hour}-{dt.datetime.now().minute}-{dt.datetime.now().second}',
                'Tiempo desde que empezo el experimento', 
                f'{camara.fps}', f'{camara.exposicion}', f'{camara.ganancia}', 'bitrate', 'WB']
        formato.writerow(lista)
    return True
