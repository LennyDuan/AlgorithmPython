#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
from collections import defaultdict, Counter


def checkMagazine(magazine, note):
    m_d = Counter(magazine)
    n_d = Counter(note)

    for k, v in n_d.items():
        if not m_d.get(k) or m_d.get(k) < v:
            print('No')
            return
    print('Yes')
    return


magazine = 'give me one grand today night'
note = 'give one grand today'
print(checkMagazine(magazine, note))
