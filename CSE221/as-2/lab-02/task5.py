#!/usr/bin/env python3

# ==============================
# Title: CSE221 lab-02 task-05
# Author: Abir Ahammed Bhuiyan
# ID: 20101197
# ==============================


import time
import formatter


def partition(A, p, q):

    x = A[p]
    i = p

    for j in range(p+1, q+1):
        if A[j] <= x:
            i = i+1
            A[i], A[j] = A[j], A[i]

    A[p], A[i] = A[i], A[p]

    return i


def quickSort(A, p, r):

    if p < r:
        q = partition(A, p, r)
        quickSort(A, p, q-1)
        quickSort(A, q+1, r)


def findK(A, p, r, k):

    if (k > 0 and k <= r - p + 1):

        pos = partition(A, p, r)

        if (pos - p == k - 1):
            return A[pos]
        if (pos - p > k - 1):
            return findK(A, p, pos - 1, k)

        return findK(A, pos + 1, r, k - pos + p - 1)

    return "array index out of bound"



if __name__ == "__main__":

    with open('./input5.txt', 'r') as fr:
        arr = list(map(int, fr.readline().split()))
        ks = list(map(int, fr.readline().split()))
    
    # copying orginal array as arr_unsorted for future use
    arr_unsorted = arr

    # converting array to the valid output format
    arr_string = formatter.stringify(arr_unsorted)

    with open('./output5.txt', 'w') as fw:
        fw.write("============== 5.a ===================\n")
        fw.write("unsorted array: \n")
        fw.write(arr_string)
        fw.write("\n")

    stime = time.time()
    quickSort(arr, 0, len(arr)-1)
    etime = time.time()

    # converting array to the valid output format
    arr_string = formatter.stringify(arr)

    with open('./output5.txt', 'a') as fa:
        fa.write("sorted array:\n")
        fa.write(arr_string)
        fa.write("\n")
        fa.write("time took:\n")
        fa.write(str(etime-stime) + " seconds\n")

        fa.write("============== 5.b ===================\n")
        
        for k in ks:
            kth_elem = findK(arr_unsorted, 0, len(arr_unsorted)-1, k)
            fa.write(f"Kth(i.e {k}) smallest element is {kth_elem}\n")


