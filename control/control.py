import cv2
import time

def listar_indices(max=10):
    l = [i for i in range(max) if cv2.VideoCapture(i).isOpened() and cv2.VideoCapture(i).release() is None]
    return l

def tiempo_grabacion():
    horas= int(input('Horas: '))
    minutos= int((input('Minutos: ')))
    segundos= int(input('Segundos: '))
    
    tiempo= horas*3600 + minutos*60 + segundos
    return tiempo 