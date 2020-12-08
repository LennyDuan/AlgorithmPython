def myAtoi(self, s: str) -> int:
    valid = '+-1234567890'
    last = None
    s = s.lstrip()
    for i in range(len(s)):
        if s[i] not in valid:
            last = i
            break
    print(last)
    print(s[:last])
    return int(s[:last])


str = "   -42"
str = "4193 with words"
str = "words and 987"
print(myAtoi(None, str))

