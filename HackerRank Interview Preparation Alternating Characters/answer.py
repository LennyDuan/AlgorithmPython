#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
from collections import defaultdict


def alternatingCharacters(a):
    s = ''
    for i in range(1, len(a)):
        if a[i] != a[i-1]:
            s += a[i]
    # Write your code here
    return len(a) - len(s) - 1


s = 'ABABABAB'
print(alternatingCharacters(s))
