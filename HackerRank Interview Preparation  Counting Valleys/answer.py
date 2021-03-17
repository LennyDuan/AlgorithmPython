#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
from collections import defaultdict

D = 'D'
U = 'U'


def countingValleys(steps, path):
    c_level = res = 0
    find_one = False

    for pa in path:
        if pa == 'D':
            c_level -= 1
        if pa == 'U':
            c_level += 1
        if c_level < 0 and not find_one:
            find_one = True
            res += 1
        if c_level >= 0:
            find_one = False
        print(pa, c_level, find_one)
    return res


path = [D, D, U, U, U, U, D, D]
path = [D, D, U, U, D, D, U, D, U, U, U, D]

print(countingValleys(8, path))
