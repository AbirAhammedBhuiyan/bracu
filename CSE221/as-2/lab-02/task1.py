#!/usr/bin/env python3

# ==============================
# Title: CSE221 lab-02 task-01
# Author: Abir Ahammed Bhuiyan
# ID: 20101197
# ==============================


import formatter


def bubbleSort(arr):
    
    flag = True
    
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                flag = False
                arr[j+1], arr[j] = arr[j], arr[j+1]
        if flag:
            break

    return arr



if __name__ == "__main__":

    with open('./input1.txt', 'r') as fr:
        size = int(fr.readline())
        arr = list(map(int, fr.readline().split()))

    arr = bubbleSort(arr)

    # converting array to the valid output format
    arr = formatter.stringify(arr)

    with open('./output1.txt', 'w') as fw:
        fw.write(arr)
        fw.write("\n")


# Explanation:

'''
We have intialized a flag variable as True. In the first iteration of i-loop,
we checked if all the elements are already in the ascending order or not, 
if all are already in the ascending order then flag will still be True,
then after the j-loop breaks we checked if flag is still True or not if 
True then we just break all the loops and return.
Hence, this produce θ(n).
'''
