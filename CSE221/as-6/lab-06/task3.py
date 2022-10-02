#!/usr/bin/env python3


def LCS(X, Y, Z):

    m = len(X) + 1
    n = len(Y) + 1
    o = len(Z) + 1

    table = [[[0 for _ in range(o)] for _ in range(n)] for _ in range(m)]

    for i in range(m):
        for j in range(n):
            for k in range(o):
                if i == 0 or j == 0 or k == 0:
                    table[i][j][k] = 0
                elif X[i-1] == Y[j-1] and X[i-1] == Z[k-1]:
                    table[i][j][k] = table[i-1][j-1][k-1] + 1
                else:
                    table[i][j][k] = max(table[i-1][j][k], table[i][j-1][k], table[i][j][k-1])

    return table[m-1][n-1][o-1]


if __name__ == "__main__":
    
    with open('./input3.txt', 'r') as fr:
        X = fr.readline().strip()
        Y = fr.readline().strip()
        Z = fr.readline().strip()

    lcs_len = LCS(X, Y, Z)

    with open('./output3.txt', 'w') as fw:
        fw.write(f"{str(lcs_len)}\n")

