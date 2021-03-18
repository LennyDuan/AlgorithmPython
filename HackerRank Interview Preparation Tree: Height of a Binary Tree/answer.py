#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
from collections import defaultdict


def height(root):
    def find_max(node):
        if not node:
            return 0

        return max(find_max(node.left), find_max(node.right)) + 1

    res = find_max(root) - 1
    return res

