#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
from collections import defaultdict


def candies(n, arr):
    candies = [1] * n

    for i in range(n-1):
        if arr[i + 1] > arr[i]:
            candies[i + 1] = candies[i] + 1
    print(candies)

    for i in range(n-1, 0 ,-1):
        if arr[i - 1] > arr[i] and candies[i - 1] <= candies[i]:
            candies[i-1] = candies[i] + 1
    print(candies)
    # Write your code here
    return sum(candies)


n = 6
arr = [4, 6, 4, 5, 6, 2]

n = 8
arr = [4, 6, 4, 5, 6, 3, 2, 1]

print(candies(n, arr))
