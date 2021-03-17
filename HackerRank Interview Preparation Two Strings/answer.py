#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
from collections import defaultdict


def twoStrings(s1, s2):
    for c in s1:
        if c in s2:
            return 'YES'
    return 'NO'
