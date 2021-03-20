#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
from collections import defaultdict


def flippingBits(n):
    res_2 = str(bin(n))
    res_10 = ['1'] * 32
    for c in res_2:
        if c == '0':
            res_10.append('1')
            res_10.pop(0)
        if c == '1':
            res_10.append('0')
            res_10.pop(0)
    res = int(''.join(res_10), 2)
    print(n, res_2, res_10, res)
    print('---')
    return res


n = 2147483647

# n = 1

print(flippingBits(n))
