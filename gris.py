import cv2
import numpy as np

imagen=cv2.imread("imagen.jpg")
imagenA=imagen.shape[0]
imagenH=imagen.shape[1]
matriz=np.zeros((imagenA,imagenH),np.uint8)
img2=np.int16(imagen)
for i in range(imagenA):
    for j in range(imagenH):
        matriz[i,j]=(img2[i,j,0]+img2[i,j,1]+img2[i,j,2])/3


cv2.imwrite("imagengris.jpg",matriz)
