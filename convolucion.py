import numpy as np

#Función que calcula la matriz resultante de la convolución de A * B
def convolucion(A,B):
    C=np.zeros((len(A)-2,len(A[0])-2))
    n=0
    for ren in range(len(C)):
        for col in range(len(C[0])):
            res=0
            for i in range (len(B)):
                for j in range (len(B[0])):
                    res +=A[ren+i][col+j]*B[i][j]
                C[ren][col]=res
    return C
MatrizImg= [[6,9,0,3],[8,4,9,1],[4,1,3,12],[3,2,1,100]]
Filtro=[[1,0,2],[5,0,9],[6,2,1]]
