#!/usr/bin/env python3

'''
list of elements to space seperated or arrow seperated string

@param {list} -> list that should be converted into string
@param {bool} [useDir=False] -> True means use arrow seperated, False means space seperated
@returns {str} -> the constructed string
'''

def stringify(arr, useDir=False):

    if not useDir:
        return " ".join(map(str, arr))

    return " -> ".join(map(str, arr))
