#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
from collections import defaultdict


def maximumToys(prices, k):
    sorted_price = sorted(prices)
    res = 0
    total = 0
    for price in sorted_price:
        total += price
        res += 1

        if total >= k:
            return res - 1
    return len(prices)


prices = [1, 2, 3, 4]
k = 7
print(maximumToys(prices, k))
