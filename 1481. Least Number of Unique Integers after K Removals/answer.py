from collections import Counter


def findLeastNumOfUniqueInts(arr, k):
    counter = Counter(arr)
    print(counter)
    print(sorted(counter.items(), key=lambda x:x[1]))
    print({k:v for k, v in sorted(counter.items(), key=lambda x:x[1])})

    sorted_counter = sorted(arr, key=lambda x: (counter[x],x))

    print(sorted_counter)

    return len(set(sorted_counter[k:]))


# arr = [5, 5, 4]
# k = 1
arr = [4, 3, 1, 1, 3, 3, 2]
k = 3
print(findLeastNumOfUniqueInts(arr, k))
