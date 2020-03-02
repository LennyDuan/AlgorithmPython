def letterCombinations(digits: str) -> list():
    two = ['a', 'b', 'c']
    three = ['d', 'e', 'f']
    four = ['g', 'h', 'i']
    five = ['j', 'k', 'l']
    six = ['m', 'n', 'o']
    seven = ['p', 'q', 'r', 's']
    eight = ['t', 'u', 'v']
    nine = ['w', 'x', 'y', 'z']
    map = {
        "2": two,
        "3": three,
        "4": four,
        "5": five,
        "6": six,
        "7": seven,
        "8": eight,
        "9": nine,
    }

    results = []

    def buildList(combination, nexts):
        if len(nexts) == 0:
            results.append(combination)
        else:
            for letter in map[nexts[0]]:
                buildList(combination + letter, nexts[1:])

    if digits:
        buildList("", digits)

    print(results)
    return results


letterCombinations("23")
