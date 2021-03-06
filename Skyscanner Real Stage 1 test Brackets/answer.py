def solution(input):
    # Type your solution here
    if not input:
        return False
    stack = []
    left_brackets = '({['
    for char in input:
        if char in left_brackets:
            stack.append(char)
        else:
            if not stack:
                return False
        last_input = stack[-1]
        if char == ')':
            if last_input == '(':
                stack.pop(-1)
            else:
                return False

        if char == ']':
            if last_input == '[':
                stack.pop(-1)
            else:
                return False

        if char == '}':
            if last_input == '{':
                stack.pop(-1)
            else:
                return False

    return len(stack) == 0
