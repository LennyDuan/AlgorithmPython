#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
from collections import defaultdict

def sherlockAndAnagrams(s):
    dic = defaultdict(int)
    print(s)
    res = 0
    for i in range(len(s) + 1):
        for j in range(i, len(s) + 1):
            sub_s = sorted(s[i:j])
            print(sub_s)
            if sub_s:
                dic[''.join(sub_s)] += 1
    print(dic)
    for pair in dic.values():
        res += (pair - 1) * pair // 2
    return res

s = 'abba'
s = 'ifailuhkqq'
s = 'kkkk'
print(sherlockAndAnagrams(s))
