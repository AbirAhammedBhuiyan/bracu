#!/usr/bin/env python3

# ==============================
# Title: CSE221 lab-02 task-04
# Author: Abir Ahammed Bhuiyan
# ID: 20101197
# ==============================


import formatter


def merge(arr, l, mid, r):

    n1 = mid - l + 1 
    n2 = r - mid

    L = [0]*n1
    R = [0]*n2

    for i in range(n1):
        L[i] = arr[l+i]

    for j in range(n2):
        R[j] = arr[mid+j+1]

    i = j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
    


def mergeSort(arr, l, r):

    if l < r:
        mid = l + (r-l)//2

        mergeSort(arr, l, mid)
        mergeSort(arr, mid+1, r)
        
        merge(arr, l, mid, r)



if __name__ == "__main__":
    
    with open('./input4.txt', 'r') as fr:
        size = int(fr.readline())
        arr = list(map(int, fr.readline().split()))

    mergeSort(arr, 0, len(arr)-1)

    # converting array to the valid output format
    arr = formatter.stringify(arr)

    with open('./output4.txt', 'w') as fw:
        fw.write(arr)
        fw.write("\n")





