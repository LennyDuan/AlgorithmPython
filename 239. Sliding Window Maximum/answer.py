def maxSlidingWindow(self, nums, k):
    results = []

    for i, num in enumerate(nums):
        if i + k > len(nums):
            break
        res = max(nums[i:i + k])
        results.append(res)

    return results


def maxSlidingWindow2(self, nums, k):
    if len(nums) is 0:
        return []

    if k < 2:
        return nums

    result = list()
    deque = list()
    deque.append((nums[0], 0))

    def build_queue(queue, value, index):
        if index - k + 1 > queue[0][1]:
            queue.pop(0)

        while queue:
            if value > queue[-1][0]:
                queue.pop(-1)
            else:
                break
        queue.append((value, index))

    for i in range(1, k):
        build_queue(deque, nums[i], i)

    for index, val in enumerate(nums[k:]):
        result.append(deque[0][0])
        build_queue(deque, val, index + k)

    result.append(deque[0][0])

    return result


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
#
# nums = [7, 2, 4]
# k = 2
#
# nums = [1, 3, 1, 2, 0, 5]
# k = 3

# nums = [-6, -10, -7, -1, -9, 9, -8, -4, 10, -5, 2, 9, 0, -7, 7, 4, -2, -10, 8, 7]
# print([9, 9, 10, 10, 10, 10, 10, 10, 10, 9, 9, 9, 8, 8])
# k = 7

print(nums)
print(maxSlidingWindow2(None, nums, k))
#
# def maxSlidingWindow2(self, nums, k):
#     # Checking for base case
#     if not nums:
#         return []
#     if k == 0:
#         return nums
#     # Defining Deque and result list
#     deq = deque()
#     result = []
#
#     # First traversing through K in the nums and only adding maximum value's index to the deque.
#     # Note: We are olny storing the index and not the value.
#     # Now, Comparing the new value in the nums with the last index value from deque,
#     # and if new valus is less, we don't need it
#
#     for i in range(k):
#         while len(deq) != 0:
#             if nums[i] > nums[deq[-1]]:
#                 deq.pop()
#             else:
#                 break
#
#         deq.append(i)
#     print(deq)
#     print('---')
#
#     # Here we will have deque with index of maximum element for the first subsequence of length k.
#
#     # Now we will traverse from k to the end of array and do 4 things
#     # 1. Appending left most indexed value to the result
#     # 2. Checking if left most is still in the range of k (so it only allows valid sub sequence)
#     # 3. Checking if right most indexed element in deque is less than the new element found, if yes we will remove it
#     # 4. Append i at the end of the deque  (Not: 3rd and 4th steps are similar to previous for loop)
#
#     for i in range(k, len(nums)):
#
#         result.append(nums[deq[0]])
#
#         if deq[0] < i - k + 1:
#             deq.popleft()
#
#         while len(deq) != 0:
#             if nums[i] > nums[deq[-1]]:
#                 deq.pop()
#             else:
#                 break
#
#         deq.append(i)
#
#         print(deq)
#         print('-')
#     # Adding the maximum for last subsequence
#     print('---')
#     result.append(nums[deq[0]])
#
#     return result
