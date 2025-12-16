import cv2
import datetime as dt
import time
import os

class Camara:
    def __init__(self, indice):
        self.indice = indice
        self.winname = f'Imagen cámara [{self.indice}]'
        self.cap = cv2.VideoCapture(self.indice)
        self.out = None
        self.preparada = False
        self.activa = False
        self.shape = None

    def preparar(self):
        """Captura un primer frame válido y prepara el VideoWriter."""
        if not self.cap.isOpened():
            raise RuntimeError(f"No se pudo abrir cámara {self.indice+1}")

        ret, frame = self.cap.read()
        while not ret:
            time.sleep(0.05)
            ret, frame = self.cap.read()

        self.shape = frame.shape
        self.out = self.crear_salida()
        self.preparada = True
        print(f"Cámara {self.indice+1} preparada")

    def crear_salida(self):
        h, w, _ = self.shape
        if not os.path.exists('./videos'):
            os.makedirs('./videos')
        fecha = dt.datetime.now()
        filename = f'videos/{fecha.day}-{fecha.month}-{fecha.year}_{self.indice}.mp4'
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        return cv2.VideoWriter(filename, fourcc, 30, (w, h))

    def activar(self):
        self.activa = True

    def grabar_frame(self):
        """Captura y guarda un frame, muestra ventana si se desea."""
        ret, frame = self.cap.read()
        if not ret:
            return False
        self.out.write(frame)
        cv2.imshow(self.winname, frame)
        if cv2.waitKey(1) & 0xFF == 27:  # ESC para cerrar
            self.activa = False
        return True

    def cerrar(self):
        print("Cerrando cámara")
        if self.out:
            self.out.release()
        if self.cap:
            self.cap.release()
        cv2.destroyAllWindows()