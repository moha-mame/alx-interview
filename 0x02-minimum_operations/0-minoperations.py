#!/usr/bin/python3
''' Module for 0-minoperations
'''


def minOperations(n):
    '''
    method that calculates the fewest number of operations needed to result
    '''
    if n == 1:
        return 0

    operations = 0
    current = 1  # Number of characters currently in the file
    clipboard = 1  # Number of characters in the clipboard

    while current < n:
        if n % current == 0:
            clipboard = current
            operations += 1
        current += clipboard
        operations += 1

    return operations if current == n else 0
