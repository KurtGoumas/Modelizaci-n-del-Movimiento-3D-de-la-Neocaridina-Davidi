from threading import Thread
from control.control import *
from control.Camara_arreglo import Camara
from control.Camara import camara
import cv2   
import time


class CamThread(Thread):
    def __init__(self, camara):
        super().__init__()
        self.cam = camara
        self.frame = None
        self.running = True

    def run(self):
        while self.running:
            ret, frame = self.cam.cap.read()
            if ret:
                self.frame = frame
                self.cam.out.write(frame)

    def stop(self):
        self.running = False

def main():

    indices= listar_indices()
    tiempo= tiempo_grabacion()
    cam1 = Camara(indices[0])
    cam2 = Camara(indices[1])

    cam1.preparar()
    cam2.preparar()

    cam1.activar()
    cam2.activar()

    t1 = CamThread(cam1)
    t2 = CamThread(cam2)

    t1.start()
    t2.start()

    start_time = time.time()
    while time.time() - start_time < tiempo:
        if t1.frame is not None:
            cv2.imshow("Camara 1", t1.frame)
        if t2.frame is not None:
            cv2.imshow("Camara 2", t2.frame)
        if cv2.waitKey(1) == 27:
            break

    t1.stop()
    t2.stop()
    t1.join()
    t2.join()

    cam1.cerrar()
    cam2.cerrar()
    cv2.destroyAllWindows()
    print("Programa finalizado")

if __name__ == "__main__":
    main()