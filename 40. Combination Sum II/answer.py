def combinationSum2(candidates: list(), target: int) -> list():
    results = []

    def findMatch(current_list, candidates, target, origin_index, index):
        if target == 0:
            if current_list not in results:
                results.append(current_list)
            return
        for current_index in range(index, len(candidates)):
            if target < 0:
                return

            current_num = candidates[current_index]
            findMatch(
                current_list + [current_num],
                candidates,
                target - current_num,
                origin_index + 1,
                current_index + 1,
            )

    candidates.sort()
    findMatch(list(), candidates, target, 0, 0)
    print(results)
    print('---')
    return results


# [[1,1,6],[1,2,5],[1,7],[2,6]]
combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)

combinationSum2([2, 5, 2, 1, 2], 5)

combinationSum2([1, 1], 2)

