def divide(self, dividend: int, divisor: int) -> int:
    res = 0
    positive = (dividend > 0) is (divisor > 0)
    dividend_abs = abs(dividend)
    divisor_abs = abs(divisor)

    while dividend_abs >= divisor_abs:
        print('---')

        if dividend_abs - divisor_abs >= 0:
            tmp_res = 1
            tmp_div = divisor_abs
            print(dividend_abs)
            while dividend_abs >= tmp_div:
                print(dividend_abs, tmp_div, tmp_res)
                dividend_abs -= tmp_div
                res += tmp_res
                tmp_div += tmp_div
                tmp_res += tmp_res

    print('---end---')
    res = min(res, 2 ** 31 - 1) if positive else max(-res, -2**31)
    return res


# dividend = 10
# divisor = 3

dividend = -2147483648
divisor = -1

print(divide(None, dividend, divisor))