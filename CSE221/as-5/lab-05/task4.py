#!/usr/bin/env python3


def squareCount(a, b):

    count = 0

    for i in range (a, b + 1):

        j = 1;

        while j * j <= i:

            if j * j == i:
                 count += 1

            j = j + 1

    return count


if __name__ == "__main__":
    
    with open('./input4.txt', 'r') as fr:
        sil = fr.readlines()

    res = ""

    for elem in sil:
        a, b = list(map(int, elem.split()))

        if a == 0 and b == 0:
            break
        else:
            res += str(squareCount(a, b)) + "\n"

    with open('./output4.txt', 'w') as fw:
        fw.write(res)


