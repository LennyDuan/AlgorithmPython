#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
from collections import defaultdict


def whatFlavors(cost, money):
    res = []
    # Write your code here
    dic = {}
    for i, c in enumerate(cost):
        if dic.get(c) is not None:
            res.append(str(dic.get(c) + 1))
            res.append(str(i + 1))
            break

        dic[money - c] = i
    print(res)
    print(' '.join(res))


cost = [2, 1, 3, 5, 6]
money = 5
print(whatFlavors(cost, money))
