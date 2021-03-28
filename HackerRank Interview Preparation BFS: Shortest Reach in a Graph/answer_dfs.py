#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
from collections import defaultdict


def build_graph(s, edges, n):
    nodes = [i + 1 for i in range(n)]
    print(nodes)
    res = {k: 0 for k in nodes}
    adjance = defaultdict(list)
    for pair in edges:
        n_1, n_2 = pair[0], pair[1]
        adjance[n_1].append(n_2)
        adjance[n_2].append(n_1)
    print(adjance)
    print(res)
    visited = set()

    def build(key, val):
        if not key:
            return
        if key in visited:
            return
        visited.add(key)
        res[key] = val
        for next_key in adjance[key]:
            build(next_key, val + 6)

    build(s, 0)
    print(res)
    ans = []
    for k, v in res.items():
        if k == s:
            continue
        ans.append(v if v else -1)

    # Write your code here
    return ans


n = 6
s = 1
edges = [[1, 2], [2, 3], [3, 4], [1, 5], ]
print(build_graph(s, edges, n))
