from control.control import *
from control.Camara import camara
from threading import Thread 
import time

"""
Grueso del programa principal
"""
def main():
	indices = listar_indices()
	cam1, cam2 = camara(indices[0]), camara(indices[1])
	# Activar cam2 para que sirva como detonante
	cam2.activar()
    
    # Creamos un hilo para poner las cámaras en paralelo creo qeu se
	t1 = Thread(target=cam1.grabar) # Ahora mismo la latencia es = la latencia del SO en abrir un hilo
	t2 = Thread(target=cam2.grabar) # He quitado el () a grabar() por eso ahora van a la vez

	t1.start()
	t2.start()

	while not cam2.get_preparada():
		print("Esperando a cámara 2")
	cam1.activar()
	#time.sleep(10) # Autocierre. Por la cara solo sale 1 abe ??¿???¿ pero lo de que la 0 no salga xd
	#cam1.cerrar()
	#cam2.cerrar()
	
	


if __name__ == "__main__":
	main()
