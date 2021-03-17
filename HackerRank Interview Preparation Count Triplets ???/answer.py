#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
from collections import defaultdict


def countTriplets(arr, r):
    if len(arr) <= 2:
        return 0
    map_arr = {}
    map_doubles = {}
    count = 0
    print(arr[::-1])
    # Traversing the array from rear, helps avoid division
    for x in arr[::-1]:
        print(map_arr, map_doubles)
        r_x = r * x
        r_r_x = r * r_x

        # case: x is the first element (x, x*r, x*r*r)
        count += map_doubles.get((r_x, r_r_x), 0)

        # case: x is the second element (x/r, x, x*r)
        map_doubles[(x, r_x)] = map_doubles.get((x, r_x), 0) + map_arr.get(r_x, 0)

        # case: x is the third element (x/(r*r), x/r, x)
        map_arr[x] = map_arr.get(x, 0) + 1

    return count


arr = [1, 2, 2, 4]
r = 2

arr = [1, 3, 9, 9, 27, 81]
r = 3


arr = [1, 2, 1, 2, 4]
r = 2
print(countTriplets(arr, r))


def countTripletsWithRightOrder(arr, r):
    res = 0
    dic = defaultdict(int)
    for ar in arr:
        dic[ar] += 1
    print(dic)

    for k, v in dic.items():
        k_nd = k * r
        k_rd = k_nd * r
        val_nd = dic.get(k_nd) or 0
        val_rd = dic.get(k_rd) or 0
        res += v * val_nd * val_rd
        # Write your code here
    return res