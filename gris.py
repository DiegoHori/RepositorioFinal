import cv2
import numpy as np

imagen=cv2.imread("imagen.jpg")
imagenA=imagen.shape[0]
imagenH=imagen.shape[1]
matriz=np.zeros((imagenA,imagenH),np.uint8)
img2=np.int16(imagen)
for i in range(imagenA):
    for j in range(imagenH):
        matriz[i,j]=(img2[i,j,0] + img2[i,j,1] + img2[i,j,2])/3


cv2.imwrite("imagengris.jpg",matriz)
import cv2
import numpy as np
def escala_grises(imagen):
    imagen=cv2.imread("imagen.jpg")
    imagenh=imagen.shape[0]
    imagenw=imagen.shape[1]
    Matriz=np.zeros((imagenh,imagenw),np.uint8)
    im2=np.int16(imagen)
    for i in range(imagenh):
        for j in range(imagenw):
            Matriz[i,j]=(im2[i,j,2]+im2[i,j,1]+im2[i,j,0])/3
    cv2.imshow("imagen",imagen)
    cv2.imshow("imagegn",Matriz)
    cv2.waitKey(0escala_grises("imagen.jpg")
escala_grises("imagen.jpg")
