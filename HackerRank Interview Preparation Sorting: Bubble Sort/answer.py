#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    count = 0
    for i in range(len(a)):
        for j in range(0, len(a) - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                count += 1
    print('Array is sorted in {} swaps.  \nFirst Element: {}  \nLast Element: {}'.format(count, a[0], a[-1]))



if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)


a = [6,4,1]
countSwaps(a)
