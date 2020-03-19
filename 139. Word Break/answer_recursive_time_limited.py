def wordBreak(total: str, words: list()) -> bool:
    matched = [False]

    def checkMatched(currentStr, total, words, index, isTrue):
        print('----')
        print(currentStr)
        if currentStr not in total:
            return

        if currentStr == total:
            matched[0] = True
            return
        elif len(currentStr) > len(total):
            matched[0] = matched[0] or False
            return

        for i in range(j, len(words)):
            checkMatched(currentStr + words[i], total, words, i, isTrue)

    for j in range(len(words)):
        # print('Start with: ' + str(words[j]))
        checkMatched('', total, words, j, False)

    print(matched[0])
    return matched[0]


#wordBreak("leetcode", ["leet", "code"])

#wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"])

#wordBreak("bb", ["a", "b", "bbb", "bbbb"])

#wordBreak("applepenapple", ["apple", "pen"])

#wordBreak("abcd", ["a", "abc", "b", "cd"])
wordBreak("bccdbacdbdacddabbaaaadababadad", ["cbc","bcda","adb","ddca","bad","bbb","dad","dac","ba","aa","bd","abab","bb","dbda","cb","caccc","d","dd","aadb","cc","b","bcc","bcd","cd","cbca","bbd","ddd","dabb","ab","acd","a","bbcc","cdcbd","cada","dbca","ac","abacd","cba","cdb","dbac","aada","cdcda","cdc","dbc","dbcb","bdb","ddbdd","cadaa","ddbc","babb"])

