#!/usr/bin/env python3


def parityChecker(number):

    number = float(number)

    if number%1 != 0:
        return "cannot have parity"
    elif number%2 == 0:
        return "has even parity"
    else:
        return "has odd parity"



def isPalindrome(word):

    if len(word) == 0:
        return "is not a palindrome"
    else:
        for i in range(int(len(word)/2)):
            if word[i] != word[len(word)-1-i]:
                return "is not a palindrome"
    return "is a palindrome"



def parityCount(data_input):

    parity_counts = {'even': 0, 'odd': 0, 'noparity': 0}

    for data in data_input:
        number = float(data.split()[0])
        if number%1 != 0:
            parity_counts['noparity'] += 1
        elif number%2 == 0:
            parity_counts['even'] += 1
        else:
            parity_counts['odd'] += 1

    return parity_counts



def palindromeCount(data_input):

    palindrome_counts = {'palindrome': 0, 'nonpalindrome': 0}

    for data in data_input:
        word = data.split()[1]
        if isPalindrome(word) == "is not a palindrome":
            palindrome_counts['nonpalindrome'] += 1
        else:
            palindrome_counts['palindrome'] += 1

    return palindrome_counts



def calculatePercentage(occurance,  total):

    return int((occurance/total)*100)


if __name__ == "__main__":

    with open('./input.txt', 'r') as fi:
        input_data = fi.read().splitlines()

    parity_counts = parityCount(input_data)
    palindrome_counts = palindromeCount(input_data)
    total = len(input_data)

    with open('./output.txt', 'w') as fo:
        for data in input_data:
            number, word  = data.split()
            fo.write(f"{number} {parityChecker(number)} and {word} {isPalindrome(word)} \n")

    with open('./record.txt', 'w') as fr:
        fr.write(f"Percentage of odd parity: {calculatePercentage(parity_counts['odd'], total)}% \n")
        fr.write(f"Percentage of even parity: {calculatePercentage(parity_counts['even'], total)}% \n")
        fr.write(f"Percentage of no parity: {calculatePercentage(parity_counts['noparity'], total)}% \n")
        fr.write(f"Percentage of palindrome: {calculatePercentage(palindrome_counts['palindrome'], total)}% \n")
        fr.write(f"Percentage of non-palindrome: {calculatePercentage(palindrome_counts['nonpalindrome'], total)}% \n")





