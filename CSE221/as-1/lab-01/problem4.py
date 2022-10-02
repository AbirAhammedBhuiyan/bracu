#!/usr/bin/env python3


def printMatrix(matrix):
    print("--------------------\n")
    for row in matrix:
        for column in row:
            print(column, end="  ")
        print("\n")
    print("--------------------")


def inputMatrix(fileName):
    with open(f"./{fileName}") as fp:
        n = int(fp.readline())
        
        matA = []
        matB = []

        for i in range(n):
            matA.append(list(map(int, fp.readline().split())))

        for i in range(n):
            matB.append(list(map(int, fp.readline().split())))
        

    return [matA, matB]



def createZeroMatrix(size):
    return [[0 for x in range(size)] for y in range(size)]



def multiplyMatrix(matA, matB, matC):

    n = len(matC)

    for i in range(n):
        for j in range(n):
            for k in range(n):
                matC[i][j] += matA[i][k] * matB[k][j]
    return matC



if __name__ == "__main__":

    matA, matB = inputMatrix("./matrix_input.txt")

    matC = createZeroMatrix(len(matA))

    matC = multiplyMatrix(matA, matB, matC)

    printMatrix(matC)











