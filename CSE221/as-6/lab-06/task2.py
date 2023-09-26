#!/usr/bin/env python3


def LCS(X, Y):
    m = len(X) + 1
    n = len(Y) + 1

    table = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(m):
        for j in range(n):
            if i == 0 or j == 0:
                table[i][j] = 0
            elif X[i-1] == Y[j-1]:
                table[i][j] = table[i-1][j-1] + 1
            else:
                table[i][j] = max(table[i-1][j], table[i][j-1])


    m -= 1
    n -= 1

    lcs_len = table[m][n]
    lcs = ""

    while m>0 and n>0:
        if X[m-1] == Y[n-1]:
            lcs += X[m-1]
            m -= 1
            n -= 1
        elif table[m-1][n] > table[m][n-1]:
            m -= 1
        else:
            n -= 1

    return (lcs_len, lcs[::-1])


def constructName(lcs):

    zoneNames = {
            'Y': "Yasnaya",
            'P': "Pochinki",
            'S': "School",
            'R': "Rozhok",
            'F': "Farm",
            'M': "Mylta",
            'H': "Shelter",
            'I': "Prison"
            }

    res = ""

    for char in lcs:
        if zoneNames.get(char):
            res += zoneNames[char] + " "

    return res[:-1]


def correctnessOfPrediction(numberOfZones, lcs_len):

    return ((lcs_len*100)/numberOfZones)


if __name__ == "__main__":

    with open('./input2.txt', 'r') as fr:
        numberOfZones = int(fr.readline())

        actual = fr.readline().strip()
        prediction = fr.readline().strip()

        lcs_len, lcs = LCS(actual, prediction)

    fullNames = constructName(lcs)

    percentage = int(correctnessOfPrediction(numberOfZones, lcs_len))

    with open('./output2.txt', 'w') as fw:
        fw.write(f"{fullNames} \nCorrectness of prediction: {str(percentage)}%\n")


