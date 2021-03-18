def isBalanced(s):
    if not s:
        return False
    stack = []
    left_brackets = '({['
    for char in s:
        if char in left_brackets:
            stack.append(char)
        else:
            if not stack:
                return 'NO'
        last_input = stack[-1]
        if char == ')':
            if last_input == '(':
                stack.pop(-1)
            else:
                return 'NO'

        if char == ']':
            if last_input == '[':
                stack.pop(-1)
            else:
                return 'NO'

        if char == '}':
            if last_input == '{':
                stack.pop(-1)
            else:
                return 'NO'
    return 'YES' if len(stack) == 0 else 'NO'