def divide(self, dividend: int, divisor: int) -> int:
    res = 0
    positive = (dividend > 0) is (divisor > 0)
    dividend_abs = abs(dividend)
    divisor_abs = abs(divisor)

    while dividend_abs >= divisor_abs:
        if dividend_abs - divisor_abs >= 0:
            res += 1
            dividend_abs -= divisor_abs

    return res if positive else -res


dividend = 10
divisor = 3

print(divide(None, dividend, divisor))