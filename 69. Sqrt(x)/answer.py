def mySqrt(self, x: int) -> int:
    if x <= 1:
        return 0
    res = 1
    for i in range(res, x):
        if i * i <= x:
            res = i
        else:
            break
    return res
