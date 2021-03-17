def possibleChanges(usernames):
    res = []
    for name in usernames:
        find = False

        for j in range(len(name)):
            for i in range(j,len(name)):
                if name[j] > name[i]:
                    res.append('YES')
                    find = True
                    break
            if find:
                break
        if not find:
            res.append('NO')
    return res


name = ['hydra']
# name = ['foo']
# name = ['adb']

print(possibleChanges(name))