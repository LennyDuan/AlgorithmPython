#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
from collections import defaultdict


def primality(n):
    if not n % 2 and n != 2 or n == 1: return "Not prime"
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if not n % i: return "Not prime"
    return "Prime"


n = 12
n = 13
# n = 1
print(primality(n))
