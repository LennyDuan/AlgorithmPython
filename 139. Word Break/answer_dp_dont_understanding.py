def wordBreak(s: str, words: list()) -> bool:

    ok = [True]
    for i in range(1, len(s) + 1):

        ok += any(ok[j] and s[j:i] in words for j in range(i)),


    print(ok)
    return ok[-1]



wordBreak("leetcode", ["leet", "code"])

#wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"])
#
# wordBreak("bb", ["a", "b", "bbb", "bbbb"])
#
# wordBreak("applepenapple", ["apple", "pen"])
#
# wordBreak("abcd", ["a", "abc", "b", "cd"])
#
# wordBreak("bccdbacdbdacddabbaaaadababadad", ["cbc","bcda","adb","ddca","bad","bbb","dad","dac","ba","aa","bd","abab","bb","dbda","cb","caccc","d","dd","aadb","cc","b","bcc","bcd","cd","cbca","bbd","ddd","dabb","ab","acd","a","bbcc","cdcbd","cada","dbca","ac","abacd","cba","cdb","dbac","aada","cdcda","cdc","dbc","dbcb","bdb","ddbdd","cadaa","ddbc","babb"])
