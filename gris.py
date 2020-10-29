import numpy as np
import cv2

imagen =cv2.imread("imagen.jpg")
imagenh=imagen.shape[0]
imagenw=imagen.shape[1]
matriz=np.zeros((imagenh,imagenw),np.uint8)
im2=np.int16(imagen)
for i in range(imagenh):
    for j in range(imagenw):
        matriz[i,j]=(im2[i,j,2]+im2[i,j,1]+im2[i,j,0])/3
imagen=cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
cv2.imwrite("imagengris.jpg",imagen)
