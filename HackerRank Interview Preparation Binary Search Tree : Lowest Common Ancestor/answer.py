#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
from collections import defaultdict


def lca(root, v1, v2):
    # Enter your code here
    def find_node(node, p, q):
        parent_val = node.info
        if p < parent_val and q < parent_val:
            return find_node(node.left, p, q)
        if p > parent_val and q > parent_val:
            return find_node(node.right, p, q)
        return node

    return find_node(root, v1, v2)