import cv2
import numpy as np
def escala_grises(imagen):
    imagen=cv2.imread("imagen.jpg")
    imagenA=imagen.shape[0]
    imagenH=imagen.shape[1]
    matriz=np.zeros((imagenA,imagenH),np.uint8)
    for i in range(imagenA):
        for j in range(imagenH):
            matriz[i,j]=(imagen[i,j,2] + imagen[i,j,1] + imagen[i,j,0])/3
    cv2.imwrite("imagengris.jpg",matriz)
escala_grises("imagen.jpg")
#
