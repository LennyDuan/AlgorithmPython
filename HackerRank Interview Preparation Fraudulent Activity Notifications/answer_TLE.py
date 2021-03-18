#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
from collections import defaultdict


def activityNotifications(expenditure, d):
    res = 0
    for i in range(d, len(expenditure)):
        t_d = expenditure[i]
        t_prevs = sorted(expenditure[i - d:i])
        t_mid = t_prevs[d // 2]
        print(i, t_prevs, t_d, t_mid)
        if t_d >= t_mid * 2:
            res += 1
    # Write your code here
    return res


expenditure = [2, 3, 4, 2, 3, 6, 8, 4, 5]
d = 5
print(activityNotifications(expenditure, d))
