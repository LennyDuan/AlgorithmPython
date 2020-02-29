def leastInterval(tasks: [str], n: int) -> int:
    maps = dict()
    for char in tasks:
        if char in maps.keys():
            maps[char] += 1
        else:
            maps[char] = 1
    array = sorted(maps.values(), reverse=True)
    print(array)
    all = sum(array)
    lenght = len(array)
    print(all)
    print(lenght)
    total = 0
    print('---')
    while all > 0:
        for currentLoop in range(n):
            print("Retrieve: " + str(currentLoop))
            if currentLoop < lenght:
                currentIndex = 0
                while currentIndex < lenght:
                    if array[currentIndex] > 0:
                        array[currentIndex] -= 1
                        total += 1
                        all -= 1
                        break
                    else:
                        currentIndex += 1

            else:
                total += 1
            currentLoop += 1
        if all > 0:
            total += 1
        print('---n---')
    print(total)
    print('---END---')


# 2
#leastInterval(["A", "B"], 2)

# 4
#leastInterval(["A", "A", "B"], 2)

# 5
#leastInterval(["A", "B", "A", "B"], 2)

# 7
#leastInterval(["A", "A", "A", "B"], 2)

# 8
leastInterval(["A", "A", "A", "B", "B", "B"], 2)
