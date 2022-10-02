#!/usr/bin/env python3

# ==============================
# Title: CSE221 lab-02 task-03
# Author: Abir Ahammed Bhuiyan
# ID: 20101197
# ==============================


import formatter


def insertionSort(arr):

    for i in range(1, len(arr)):

        key = arr[i]
        j = i-1

        while j >= 0 and key > arr[j] :

                arr[j + 1] = arr[j]
                j -= 1

        arr[j + 1] = key

    return arr



def get_key(dic, value):

    for ID, mark in dic.items():

        if  mark == value:
            return ID
    
    

if __name__ == "__main__":

    with open('./input3.txt', 'r') as fr:
        size = int(fr.readline())
        IDs = list(map(int, fr.readline().split()))
        marks = list(map(int, fr.readline().split()))

    IDs_marks = dict(zip(IDs, marks))

    marks_sorted = insertionSort(marks)

    IDs_sorted = []

    for mark in marks_sorted:
        ID = get_key(IDs_marks, mark)
        IDs_sorted.append(ID)
        del IDs_marks[ID] 
        
    # converting array to the valid output format
    IDs_sorted = formatter.stringify(IDs_sorted)

    with open('./output3.txt', 'w') as fw:
        fw.write(IDs_sorted)
        fw.write("\n")

