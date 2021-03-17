#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
from collections import defaultdict


def sockMerchant(n, ar):
    D = defaultdict(int)
    for sock in ar:
        D[sock] += 1
    print(D)
    res = 0
    for num in D.values():
        res += num // 2

    return res


print(sockMerchant(7, [1, 2, 1, 2, 1, 3, 2]))
