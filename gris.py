import cv2
import numpy as np

imagen=cv2.imread("imagen.jpg")
imagen=cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)

cv2.imwrite("imagengris.jpg",imagen)
