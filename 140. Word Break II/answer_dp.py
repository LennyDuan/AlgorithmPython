def wordBreak(s: str, wordDict: list()) -> list():
    results = wordDict * len(wordDict)
    print(results)


    for word in range(len(results)):
        for i in range(len(wordDict)):
            word_str = wordDict[i]
            new_word_saved = str(results[word]) + ' ' + word_str
            new_word_str = new_word_saved.replace(' ', '')
            print(new_word_saved)
            if new_word_str in s:
                results[word] = new_word_saved

    print('-- END --')
    print(results)
    final_results = list(set(filter(lambda x: x.replace(' ', '') == s, results)))
    print(final_results)

    return final_results


# wordBreak(s="ab", wordDict=["a", "b"])

# ["cats and dog", "cat sand dog"]
# wordBreak(s="catsanddog", wordDict=["cat", "cats", "and", "sand", "dog"])

# ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
wordBreak(s="pineapplepenapple", wordDict=["apple", "pen", "applepen", "pine", "pineapple"])
