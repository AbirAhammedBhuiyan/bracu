#!/usr/bin/env python3


import math

def subtractReduceZero(num):

    sil = [math.inf for i in range(num+1)]

    sil[0] = 0

    for n in range(num+1):
        for char in str(n):
            
            charInNumber = ord(char)-48
            print(n, sil[n], sil[n-charInNumber]+1)
            sil[n] = min(sil[n], sil[n-charInNumber]+1)

    print(sil)
    return sil[num]



if __name__ == "__main__":

    with open('input1.txt', 'r') as fr:
        number = int(fr.readline())

    with open('output1.txt', 'w') as fw:
        fw.write(f"{subtractReduceZero(number)}\n")


