def generateParenthesis(n: int) -> list():
    result = list()
    left = "("
    right = ")"

    def createResult(listString = list()):
        if len(listString) == 2 * n:
            if balance(listString):
                result.append("".join(listString))
        else:
            listString.append(left)
            createResult(listString)
            listString.pop()
            listString.append(right)
            createResult(listString)
            listString.pop()

    def balance(completeString):
        shouldBeZero = 0
        for item in completeString:
            if left is item:
                shouldBeZero += 1
            else:
                shouldBeZero -= 1
            if shouldBeZero < 0:
                return False
        return shouldBeZero == 0

    createResult()

    print(result)
    return result


generateParenthesis(3)
