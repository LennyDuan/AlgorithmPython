#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
from collections import defaultdict


def minimumSwaps(arr):
    a = dict(enumerate(arr, 1))
    b = {v: k for k, v in a.items()}
    print(a)
    print(b)

    count = 0

    for i in a:
        x = a[i]
        if x != i:
            y = b[i]
            print(i, x, y)
            a[y] = x
            b[x] = y
            count += 1
        print('----')
    return count


arr = [7, 1, 3, 2, 4, 5, 6]
print(minimumSwaps(arr))
