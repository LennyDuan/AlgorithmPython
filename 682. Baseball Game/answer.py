class Solution:
    def calPoints(self, ops):
        score = list()
        total = 0

        for i in ops:
            print(score)

            if i is 'D':
                score.append(2 * score[-1])
                total += score[-1]
            elif i is '+':
                score.append(score[-1] + score[-2])
                total += score[-1]
            elif i is 'C':
                total -= score.pop()
            else:
                score.append(int(i))
                total += score[-1]

        return total


print(Solution.calPoints(None, ["5", "-2", "4", "C", "D", "9", "+", "+"]
                         ))

# print(Solution.calPoints(None, ["5", "2", "C", "D", "+"]))
