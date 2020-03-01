def generateParenthesis(n: int) -> list():
    result = list()
    def backtrace(s='', l=0, r=0):
        if len(s) == 2 * n:
            result.append(s)
        if l < n:
            backtrace(s + '(', l + 1, r)
        if l < r:
            backtrace(s + ')', l, r + 1)

    backtrace()
    print(result)
    return result


generateParenthesis(3)
