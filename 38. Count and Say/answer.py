def countAndSay(n: int) -> str:
    results = ["0"] * (n + 1)

    def readResult(number):
        nextStr = ""
        count = 0
        current = number[0]
        for j in range(len(number)):
            if number[j] == current:
                count += 1
            else:
                nextStr += (str(count) + current)
                count = 1
                current = number[j]
        nextStr += str(count) + current
        return nextStr

    for i in range(1, n + 1):
        print("Current i: " + str(i))
        if i == 1:
            results[i] = "1"
        else:
            results[i] = readResult(results[i - 1])
    print(results)
    return results[n]


# countAndSay(1)
# countAndSay(4)
countAndSay(10)
