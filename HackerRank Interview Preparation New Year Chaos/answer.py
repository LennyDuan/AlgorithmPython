#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
from collections import defaultdict


def minimumBribes(Q):
    moves = 0
    Q = [P - 1 for P in Q]
    print(Q)
    for i, P in enumerate(Q):
        if P - i > 2:
            print("Too chaotic")
            return
        for j in range(max(P - 1, 0), i):
            if Q[j] > P:
                moves += 1
    print(moves)


q = [2, 1, 5, 3, 4]
# q = [2, 5, 1, 3, 4]

print(minimumBribes(q))
