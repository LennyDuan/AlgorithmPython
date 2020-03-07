def combinationSum2(candidates: list(), target: int) -> list():
    results = []
    candidates.sort()
    table = [None] + [set() for i in range(target)]
    print(table)

    for i in candidates:
        if i > target:
            break;

        print('---')
        for j in range(target - i, 0, -1):
            table[i + j] |= {elt + (i,) for elt in table[j]}
        table[i].add((i,))

    return table


# [[1,1,6],[1,2,5],[1,7],[2,6]]
#combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)

combinationSum2([2, 5, 2, 1, 2], 5)

#combinationSum2([1, 1], 2)

