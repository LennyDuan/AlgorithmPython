def romanToInt(s: str) -> int:
    roman = ["I", "V", "X", "L", "C", "D", "M"]
    integer = [1, 5, 10, 50, 100, 500, 1000]
    array = s
    print(array)
    totalValue = 0
    for index in range(len(array)):
        curRomanIndex = roman.index(array[index])
        curInteger = integer[curRomanIndex]
        if index + 1 < len(array):
            nextRomanIndex = roman.index(array[index + 1])
            totalValue = totalValue - curInteger if nextRomanIndex > curRomanIndex else totalValue + curInteger
        else:
            totalValue += curInteger
    print(totalValue)
    print('---')

    return totalValue


romanToInt("III")
romanToInt("IV")
romanToInt("IX")
romanToInt("LVIII")
romanToInt("MCMXCIV")