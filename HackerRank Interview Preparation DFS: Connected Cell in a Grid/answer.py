#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
from collections import defaultdict


def maxRegion(grid):
    res = float('-inf')
    y = len(grid)
    x = len(grid[0])
    x_max, y_max = x - 1, y - 1
    print(x, y, x_max, y_max)
    visited = set()
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]

    def can_move(x, y):
        return 0 <= x <= x_max and 0 <= y <= y_max and grid[y][x]

    def check_max(x, y, nodes):
        if (x, y) in visited:
            return
        if grid[y][x] == 0:
            return
        visited.add((x, y))
        nodes.append((x, y))
        for direction in directions:
            next_x, next_y = direction[0] + x, direction[1] + y
            if can_move(next_x, next_y):
                check_max(next_x, next_y, nodes)

    for y_index in range(y):
        for x_index in range(x):
            if grid[y_index][x_index] and (x_index, y_index) not in visited:
                nodes = []
                check_max(x_index, y_index, nodes)
                print(nodes)
                res = max(res, len(nodes))
            else:
                continue

    # Write your code here
    return res


grid = [
    [1, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 0],
]
print(maxRegion(grid))
