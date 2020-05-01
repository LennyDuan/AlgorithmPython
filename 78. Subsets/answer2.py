import copy

def subsets(nums: list()) -> list():
    results = [[]]

    for num in nums:
        new_list = []
        origin_result = copy.deepcopy(results)
        for curr in origin_result:
            curr.append(num)
            new_list.append(curr)
        results += origin_result

    # for num in nums:
    #     results += [curr + [num] for curr in results]

    print(results)
    return results


subsets([1, 2, 3])
