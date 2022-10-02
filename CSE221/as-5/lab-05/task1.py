#!/usr/bin/env python3


def assignmentSelection(arr, n):

    arr.sort(key=lambda y: y[1])
    selected = [arr[0]]
    count = 1
    curr_f = arr[0][1]

    for c in range(1, n):

        if arr[c][0] >= curr_f:
            count += 1
            curr_f = arr[c][1]
            selected.append(arr[c])

    return count, selected


def stringify(arrs):

    res = ""
    for arr in arrs: 
        res += f"{arr[0]} {arr[1]}\n"

    return res


if __name__ == "__main__":

    with open('./input1.txt', 'r') as fr:
        n = int(fr.readline())

        arr = []

        for i in range(n):
            start, end = list(map(int, fr.readline().split()))

            arr.append([start, end])

    count, selected = assignmentSelection(arr, n)
    res = stringify(selected)

    with open('./output1.txt', 'w') as fw:
        fw.write(str(count))
        fw.write("\n")
        fw.write(res)


