def solution(arr):
    # Type your solution here
    if not arr:
        return ''

    left_sum = 0
    right_sum = 0

    level = 0

    while arr:
        pop_total = 2 ** level
        if pop_total == 1:
            arr.pop(0)
        else:
            side_total = pop_total / 2
            level_start = 1
            while pop_total and arr:
                current_val = arr.pop(0)
                if current_val != -1:
                    if level_start <= side_total:
                        left_sum += current_val
                    else:
                        right_sum += current_val
                level_start += 1
                pop_total -= 1

        level += 1
    print(left_sum)
    print(right_sum)

    if left_sum < right_sum:
        return 'Right'
    if left_sum > right_sum:
        return 'Left'
    return ''


arr = [3, 6, 2, 9, -1, 10]
print(solution(arr))
