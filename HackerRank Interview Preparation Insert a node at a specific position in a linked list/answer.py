#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
from collections import defaultdict
def insertNodeAtPosition(head, data, position):
    root = head
    position -= 1
    while position and head:
        head = head.next
        position -= 1
    tmp = head.next
    node = SinglyLinkedListNode(data)
    node.next = tmp
    head.next = node
    return root