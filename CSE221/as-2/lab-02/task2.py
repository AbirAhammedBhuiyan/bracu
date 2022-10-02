#!/usr/bin/env python3

# ==============================
# Title: CSE221 lab-02 task-02
# Author: Abir Ahammed Bhuiyan
# ID: 20101197
# ==============================


import formatter


def selectionSort(arr, endPoint):
    
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
            
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

        if i == endPoint-1:
            break;

    return arr[:endPoint]



if __name__ == "__main__":

    with open('./input2.txt', 'r') as fr:
        size, endPoint = list(map(int, fr.readline().split()))
        arr = list(map(int, fr.readline().split()))

    arr = selectionSort(arr, endPoint)

    # converting array to the valid output format
    arr = formatter.stringify(arr)

    with open('./output2.txt', 'w') as fw:
        fw.write(arr)
        fw.write("\n")


