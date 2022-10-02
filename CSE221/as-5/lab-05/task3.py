#!/usr/bin/env python3


def jackJill(sil, chars):

    sil.sort()
    stack = []
    index = 0
    sequence = ""
    jacks_hr = 0
    jills_hr = 0
    
    for c in chars:
        if c == "J":
            stack.append(index)
            sequence += str(sil[index])
            jacks_hr += sil[index]
            index += 1
    
        elif c == "j":
            val = stack.pop()
            sequence += str(sil[val])
            jills_hr += sil[val]

        else:
            pass

    return sequence, jacks_hr, jills_hr
    

if __name__ == "__main__":

    with open('./input3.txt', 'r') as fr:
        fr.readline()
        sil = list(map(int, fr.readline().split()))
        chars = fr.readline()

    sequence, jacks_hr, jills_hr = jackJill(sil, chars)

    with open('./output3.txt', 'w') as fw:
        fw.write(sequence)
        fw.write("\n")
        fw.write(f"Jack will work for {str(jacks_hr)} hours\n")
        fw.write(f"Jill will work for {str(jills_hr)} hours\n")
