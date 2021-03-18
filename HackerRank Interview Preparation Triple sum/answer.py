#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
from collections import defaultdict


def triplets(a, b, c):
    a = list(sorted(set(a)))
    b = list(sorted(set(b)))
    c = list(sorted(set(c)))

    ai = 0
    bi = 0
    ci = 0

    ans = 0

    while bi < len(b):
        while ai < len(a) and a[ai] <= b[bi]:
            ai += 1

        while ci < len(c) and c[ci] <= b[bi]:
            ci += 1

        ans += ai * ci
        bi += 1

    return ans


a = [3, 5, 7]
b = [3, 6]
c = [4, 6, 9]

a = [1, 4, 5]
b = [2, 3, 3]
c = [1, 2, 3]

print(triplets(a, b, c))
