def possibleChanges(usernames):
    res = []
    for name in usernames:
        sorted_name = ''.join(sorted(name))
        if sorted_name < name:
            res.append('YES')
        else:
            res.append('NO')
    return res


name = ['hydra']
name = ['foo']
# name = ['adb']

print(possibleChanges(name))