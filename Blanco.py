import cv2
import numpy as np

def escala_grises(A):
    B = np.zeros([A.shape[0], A.shape[1]])
    for i in range(0, len(A)):
        for j in range(0, len(A[0])):
            res = 0
            for x in range(0, len(A[0][0])):
                res += A[i][j][x]
            res = int(res/len(A[0][0]))
            B[i][j] = res
    return B


def convolucion(A, B):
    C = np.zeros([A.shape[0]-2, A.shape[1]-2])
    for i in range(0, len(A)-2):
        for j in range(0, len(A[0])-2):
            res = 0
            for x in range(0, len(B)):
                for y in range(0, len(B[0])):
                    res += A[i+x][j+y]*B[x][y]
            if res > 255:
                res = 255
            C[i][j] = res
    return C


def blanco_negro(A):
    B = np.zeros([A.shape[0], A.shape[1]])
    for i in range(0, len(A)):
        for j in range(0, len(A[0])):
            if A[i][j] > 128:
                B[i][j] = 255
            if A[i][j] <= 128:
                B[i][j] = 0
    return B

def padding(A):
    B = np.zeros((len(A)+2, len(A[0])+2))
    for i in range(0, len(A)):
        for j in range(0, len(A[0])):
            B[i+1][j+1] = A[i][j]
    return B

F = [[1, 1, 1],[1, 0, 1],[1, 1, 1]]
img = cv2.imread("imagen2.jpg")
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img2 = escala_grises(img)
cv2.imwrite("imagengris.jpg", img2)

img_padding = padding(img2)
img_padding = convolucion(img_padding, F)
cv2.imwrite("padding.jpg", img_padding)

img_spad = convolucion(img2, F)
cv2.imwrite("sinpad.jpg", img_spad)

img_blanconegro = blanco_negro(img2)
cv2.imwrite("blancoYNegro.jpg", img_blanconegro)
