import functools


def wordBreak(s: str, wordDict: list()) -> list():
    results = list()

    def index_compare(x, y):
        return s.index(x) - s.index(y)

    def backtracking(current_list, origin_str):
        if len(origin_str.strip()) == 0:
            result = ' '.join(sorted(current_list, key=functools.cmp_to_key(index_compare)))
            if result not in results:
                results.append(result)
            return

        for i in range(len(wordDict)):
            new_str = origin_str.replace(wordDict[i], ' ', 1)
            if new_str != origin_str:
                current_list.append(wordDict[i])
                backtracking(current_list, new_str)
                current_list.pop()

    backtracking([], s)
    print('-- END --')
    # print(origin_result)
    print(results)
    return results


#
# wordBreak(s="ab", wordDict=["a", "b"])

# [ "cats and dog", "cat sand dog"]
wordBreak(s="catsanddog", wordDict=["cat", "cats", "and", "sand", "dog"])

# # ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
# wordBreak(s="pineapplepenapple", wordDict=["apple", "pen", "applepen", "pine", "pineapple"])
