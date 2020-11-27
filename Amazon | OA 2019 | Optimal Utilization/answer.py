def find_sum(a, b, target):
    sorted_a = sorted(a, key=lambda a: a[1])
    sorted_b = sorted(b, key=lambda b: b[1])
    print(sorted_a)
    print(sorted_b)

    a_l  = 0
    b_r = len(sorted_b) - 1
    results = list()
    max = float('-inf')
    max_ids = list()
    while a_l < len(sorted_a) and b_r >= 0:
        print('--')
        print(a_l, b_r)

        a_id, a_val = sorted_a[a_l]
        b_id, b_val = sorted_b[b_r]
        sum = a_val + b_val

        print(sum)
        if target > sum > max:
            max = sum
            max_ids = [a_id, b_id]

        if target is sum:
            results.append([a_id, b_id])
            a_l += 1
        if target < sum:
            b_r -= 1
        if target > sum:
            a_l += 1

    if len(results) is 0:
        results.append(max_ids)

    return results


# a = [[1, 2], [2, 4], [3, 6]]
# b = [[1, 2]]
# target = 7

# a = [[1, 8], [2, 15], [3, 9]]
# b = [[1, 8], [2, 11], [3, 12]]
# target = 20

# a = [[1, 8], [2, 7], [3, 14]]
# b = [[1, 5], [2, 10], [3, 14]]
# target = 20

a = [[1, 3], [2, 5], [3, 7], [4, 10]]
b = [[1, 2], [2, 3], [3, 4], [4, 5]]
target = 10
print(find_sum(a,b,target))
