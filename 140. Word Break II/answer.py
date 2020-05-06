def wordBreak(s: str, wordDict: list()) -> list():
    results = list()

    def backtracking(current_list, origin_str):
        if len(origin_str) == 0:
            result = ' '.join(current_list)
            if result not in results:
                results.append(result)
            return
        else:
            for i in range(len(wordDict)):
                word = wordDict[i]
                if origin_str.startswith(word):
                    new_str = origin_str[len(word):]
                    current_list.append(word)
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
# wordBreak(s="catsanddog", wordDict=["cat", "cats", "and", "sand", "dog"])

# # ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
wordBreak(s="pineapplepenapple", wordDict=["apple", "pen", "applepen", "pine", "pineapple"])
