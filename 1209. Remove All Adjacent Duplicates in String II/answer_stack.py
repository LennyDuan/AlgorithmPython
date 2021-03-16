def removeDuplicates(self, s: str, t_k: int) -> str:
    stack = []
    for c in s:
        if stack and stack[-1][0] == c:
            count = stack.pop()[1] + 1
            if count != k:
                stack.append((c, count))
        else:
            count = 1
            stack.append((c, count))
        print(stack)
    result = ""
    for c, count in stack:
        result += c * count
    return result


s = "deeedbbcccbdaa"
k = 3
print(removeDuplicates(None, s, k))
