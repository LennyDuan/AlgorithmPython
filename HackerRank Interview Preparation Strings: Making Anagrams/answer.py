#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
from collections import defaultdict

def makeAnagram(a, b):
    dic = defaultdict(int)
    for c in a:
        dic[c] += 1
    for c in b:
        dic[c] -= 1

    return sum([abs(v) for v in dic.values()])

