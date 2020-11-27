def numPairsDivisibleBy60(time) -> int:
    sum = 0

    for i in range(len(time)):
        for j in range(i + 1, len(time)):
            if (time[i] + time[j]) % 60 == 0:
                sum += 1

    return sum


def numPairsDivisibleBy602(time) -> int:
    ret = 0
    from collections import defaultdict

    remainders = defaultdict(int)

    for t in time:
        if t % 60 == 0:  # check if a%60==0 && b%60==0
            ret += remainders[0]
        else:  # check if a%60+b%60==60
            ret += remainders[60 - t % 60]
        remainders[t % 60] += 1  # remember to
    return ret


def numPairsDivisibleBy603(time) -> int:
    ret = 0
    from collections import defaultdict
    remainders = defaultdict(int)

    for t in time:
        remainders[t % 60] += 1

    for n in range(31):
        if n == 0 or n == 30:
            c_n = remainders[n]
            ret += c_n * (c_n - 1) / 2
        else:
            ret += remainders[c_n] * remainders[60 - c_n]

    return ret


time1 = [30, 20, 150, 100, 40]
time2 = [60, 60, 60, 60]
print(numPairsDivisibleBy603(time2))
