#!/bin/python3

import math
import os
import random
import re
import sys

from collections import defaultdict


# Complete the freqQuery function below.
def freqQuery(queries):
    dic = defaultdict(int)
    res = []
    for query in queries:
        key, val = query[0], query[1]
        if key == 1:
            dic[val] += 1
        if key == 2:
            if dic.get(val) and dic[val]> 0:
                dic[val] -= 1
        if key == 3:
            res.append(1 if val in dic.values() else 0)
    return res

    # res = []
    # fre = defaultdict(int)
    # for x in queries:
    #     if x[0] == 1:
    #         fre[x[1]] += 1
    #     elif x[0] == 2:
    #         if x[1] in fre and fre[x[1]] > 0:
    #             fre[x[1]] -= 1
    #     else:
    #         res.append(1 if x[1] in set(fre.values()) else 0)
    #
    #
    # return res


queries = [(3, 4),
           (2, 1003),
           (1, 16),
           (3, 1)]

ans = freqQuery(queries)
