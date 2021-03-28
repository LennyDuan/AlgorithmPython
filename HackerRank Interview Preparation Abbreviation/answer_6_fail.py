#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
from collections import defaultdict

def abbreviation(a, b):
    a = list(a)
    b = list(b)
    res = True
    while b:
        first_b = b[0]
        print(first_b)
        while a:
            first_a = a.pop(0)
            if first_b == first_a or first_a.upper() == first_b:
                b.pop(0)
                break
        if b and not a:
            res = False
            break

    a_remain_upper = any(x in 'ABCDEFGHIJKLMNOPQRESUVWXYZ' for x in a)
    # Write your code here
    return 'YES' if res and not a_remain_upper else 'NO'



a = 'AbcDE'
b = 'ABDE'

# a = 'beFgH'
# b = 'EFG'
#
# a = 'sYOCa'
# b = 'YOCN'
print(abbreviation(a, b))
