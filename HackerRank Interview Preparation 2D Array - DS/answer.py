#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    start_x, end_x = 1, 5
    start_y, end_y = 1, 5
    res = float('-inf')
    for y in range(start_y, end_y):
        for x in range(start_x, end_x):
            c_sum = arr[y][x] + arr[y-1][x] + arr[y-1][x-1] + arr[y-1][x+1] + arr[y+1][x]+ arr[y+1][x+1] + arr[y+1][x-1]
            res = max(c_sum, res)
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
