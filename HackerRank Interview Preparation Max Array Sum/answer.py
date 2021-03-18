#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
from collections import defaultdict


def maxSubsetSum(arr):
    dp = [0] * len(arr)
    dp[0] = arr[0]
    dp[1] = max(arr[0], arr[1])
    for i in range(2, len(arr)):
        cur = arr[i]
        dp[i] = max(dp[i-1], dp[i-2]+cur, dp[i-2], cur)

    return max(dp)


arr = [3, 7, 4, 6, 5]
print(maxSubsetSum(arr))
