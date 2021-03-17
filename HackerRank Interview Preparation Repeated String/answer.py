#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
from collections import defaultdict


def repeatedString(s, n):
    res = 0
    a_in_s = s.count('a')
    s_len = len(s)
    print(a_in_s)
    multi_s = n // s_len
    remain_s = n % s_len
    res += a_in_s * multi_s
    res += s[:remain_s].count('a')
    # Write your code here
    return res


s = 'aba'
n = 10
print(repeatedString(s, n))
