#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
from collections import defaultdict


def minimumAbsoluteDifference(arr):
    sorted_arr = sorted(arr)
    print(sorted_arr)
    diff = float('inf')
    for i in range(1, len(arr)):
        pre = sorted_arr[i - 1]
        cur = sorted_arr[i]
        print(abs(pre - cur))
        diff = min(diff, abs(pre - cur))
        print('---')
    return diff


arr = [3, -7, 0]
print(minimumAbsoluteDifference(arr))
