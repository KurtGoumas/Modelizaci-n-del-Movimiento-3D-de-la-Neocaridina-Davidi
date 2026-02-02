import cv2
import time

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