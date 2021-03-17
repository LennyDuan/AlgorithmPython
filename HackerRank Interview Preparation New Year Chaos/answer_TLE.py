#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
from collections import defaultdict


def minimumBribes(q):
    res = 0
    normal_q = [i + 1 for i in range(len(q))]
    target_q = q

    while normal_q:
        last = normal_q[-1]
        loc_ti = target_q.index(last) + 1
        if abs(len(normal_q) - loc_ti) > 2:
            print('Too chaotic')
            return
        else:
            res += abs(len(normal_q) - loc_ti)
        normal_q.pop(-1)
        target_q.remove(last)

    if res:
        print(res)


q = [2, 1, 5, 3, 4]
# q = [2, 5, 1, 3, 4]

print(minimumBribes(q))
