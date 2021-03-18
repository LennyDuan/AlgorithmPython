#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
from collections import defaultdict


def triplets(a, b, c):
    res = 0
    combile = defaultdict(list)
    l = list()
    for p in set(a):
        for q in set(b):
            if p <= q:
                combile[p].append(q)
                l.append(q)
    print(l)
    for r in set(c):
        for q in l:
            if q >= r:
                res += 1

    # Write your code here
    return res


a = [3, 5, 7]
b = [3, 6]
c = [4, 6, 9]

a = [1, 4, 5]
b = [2, 3, 3]
c = [1, 2, 3]

print(triplets(a, b, c))
