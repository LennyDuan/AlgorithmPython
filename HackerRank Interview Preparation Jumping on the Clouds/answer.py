#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
from collections import defaultdict


def jumpingOnClouds(c):
    res = None
    dp = [0] * len(c)
    # Write your code here
    dp[0] = 0
    dp[1] = float('inf') if c[1] else 1
    for i in range(2, len(c)):
        if c[i]:
            dp[i] = float('inf')
        else:
            dp[i] = min(dp[i-1], dp[i-2]) + 1
    return dp[-1]


c = [0, 1, 0, 0, 0, 1, 0]

c = [0, 0, 1, 0, 0, 1, 0]
print(jumpingOnClouds(c))
