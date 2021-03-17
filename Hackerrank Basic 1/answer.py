def minTime(files, numCores, limit):
    res = 0
    sorted_files = sorted(files)[::-1]
    tmp = limit
    for file in sorted_files:
        if tmp and file >= numCores and file % numCores == 0:
            res += file / numCores
            tmp -= 1
        else:
            res += file

    return int(res)


files = [4, 1, 3, 2, 8]
numCores = 4
limit = 1
# limit = 2

files = [130291875, 474356040, 1, 8]
numCores = 5
limit = 3
# res = 120929592

print(minTime(files, numCores, limit))
