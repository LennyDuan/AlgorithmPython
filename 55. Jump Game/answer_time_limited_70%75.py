def canJump(self, nums) -> bool:
    res = [False]

    def canJump(remain, res):
        print('----')
        if not remain or len(remain) == 1:
            res[0] = True
            return
        step = remain[0]
        if step >= 1:
            for next_step in range(1, step + 1):
                current_remain = [] + remain
                print(current_remain, next_step)
                canJump(current_remain[next_step:], res)
        else:
            return

    canJump(nums, res)
    return res[0]


nums = [2, 3, 1, 1, 4]
nums = [3, 2, 1, 0, 4]
print(canJump(None, nums))
