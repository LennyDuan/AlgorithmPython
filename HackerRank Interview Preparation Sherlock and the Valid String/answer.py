#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
from collections import defaultdict, Counter


def isValid(s):
    counter = Counter(s)
    # Write your code here
    print(counter)
    counter_val = Counter(counter.values())
    print(counter_val)
    most_count = counter_val.most_common(1)[0][0]
    print(most_count)
    all_count_1 = all_count_2  = list(counter.values())
    print(all_count_1)

    step = list(map(lambda x: abs(x - most_count), all_count_1))
    print(step)
    part_1 = sum(step) <= 1
    print('---')

    if 1 in all_count_2:
        all_count_2.remove(1)
        print(all_count_2)
        return 'YES' if len(set(all_count_2)) == 1 or len(set(all_count_2)) == 0 else 'NO'

    return 'YES' if part_1 else 'NO'


s = 'aabbccddeefghi'
s = 'aabbcd'
s = 'ibfdgaeadiaefgbhbdghhhbgdfgeiccbiehhfcggchgghadhdhagfbahhddgghbdehidbibaeaagaeeigffcebfbaieggabcfbiiedcabfihchdfabifahcbhagccbdfifhghcadfiadeeaheeddddiecaicbgigccageicehfdhdgafaddhffadigfhhcaedcedecafeacbdacgfgfeeibgaiffdehigebhhehiaahfidibccdcdagifgaihacihadecgifihbebffebdfbchbgigeccahgihbcbcaggebaaafgfedbfgagfediddghdgbgehhhifhgcedechahidcbchebheihaadbbbiaiccededchdagfhccfdefigfibifabeiaccghcegfbcghaefifbachebaacbhbfgfddeceababbacgffbagidebeadfihaefefegbghgddbbgddeehgfbhafbccidebgehifafgbghafacgfdccgifdcbbbidfifhdaibgigebigaedeaaiadegfefbhacgddhchgcbgcaeaieiegiffchbgbebgbehbbfcebciiagacaiechdigbgbghefcahgbhfibhedaeeiffebdiabcifgccdefabccdghehfibfiifdaicfedagahhdcbhbicdgibgcedieihcichadgchgbdcdagaihebbabhibcihicadgadfcihdheefbhffiageddhgahaidfdhhdbgciiaciegchiiebfbcbhaeagccfhbfhaddagnfieihghfbaggiffbbfbecgaiiidccdceadbbdfgigibgcgchafccdchgifdeieicbaididhfcfdedbhaadedfageigfdehgcdaecaebebebfcieaecfagfdieaefdiedbcadchabhebgehiidfcgahcdhcdhgchhiiheffiifeegcfdgbdeffhgeghdfhbfbifgidcafbfcd'
s = 'abcdefghhgfedecba'
s = 'a'

print(isValid(s))


#     counter = Counter(s)
#     # Write your code here
#     counter_val = Counter(counter.values())
#     most_count = counter_val.most_common(1)[0][0]
#     all_count = list(counter.values())
#     step = list(map(lambda x: abs(x - most_count), all_count))
#     return 'YES' if sum(step) <= 1 else 'NO'