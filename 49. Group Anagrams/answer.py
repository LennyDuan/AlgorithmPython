from collections import defaultdict


def groupAnagrams(self, strs):
    unique_dict = defaultdict(list)

    for word in strs:
        unique_dict[''.join(sorted(word))].append(word)
    return list(unique_dict.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(None, strs))
