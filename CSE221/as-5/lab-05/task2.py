#!/usr/bin/env python3


def activityComplete(arr, m):
    
    arr.sort(key=lambda x: (x[1], x[0]))

    next_free = [ 0 for _ in range(m) ]

    count = 0

    for i in range(len(sil)):

        select = -1

        for j in range(m):

            if next_free[j] <= arr[i][0]:
                if select == -1:
                    select = j
                if next_free[j] > next_free[select]:
                    select = j

        if select != -1:
            count += 1
            next_free[select] = arr[i][1]


    return count


if __name__ == "__main__":

    with open('./input2.txt', 'r') as fr:
        n, m = list(map(int, fr.readline().split()))

        sil = []

        for i in range(n):
            sil.append(tuple(map(int, fr.readline().split())))

    count = activityComplete(sil, m)
    
    with open('./output2.txt', 'w') as fw:
        fw.write(str(count) + "\n")

