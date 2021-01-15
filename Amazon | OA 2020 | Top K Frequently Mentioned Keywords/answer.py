from collections import Counter


def find_k_top(keywords, k, reviews):
    sum_dict = Counter({i: 0 for i in keywords})
    for line in reviews:
        c_line_dict = {i: 0 for i in keywords}

        for word in line.split(' '):
            if word.casefold() in c_line_dict:
                c_line_dict[word.casefold()] = 1
        sum_dict += Counter(c_line_dict)

    # Sort key,value pairs descending order of frequency, ascending order of lexicographical
    sorted_dict = dict(sorted(sum_dict.items(), key=lambda kv: (-kv[1], kv[0])))

    print(sorted_dict.most_common(3))
    return list(sorted_dict.keys())[:k]


# k = 2
# keywords = ["anacell", "cetracular", "betacellular"]
# reviews = [
#     "Anacell provides the best services in the city",
#     "betacellular has awesome services",
#     "Best services provided by anacell, everyone should use anacell",
# ]

k = 2
keywords = ["anacell", "betacellular", "cetracular", "deltacellular", "eurocell"]
reviews = [
    "I love anacell Best services; Best services provided by anacell",
    "betacellular has great services",
    "deltacellular provides much better services than betacellular",
    "cetracular is worse than anacell",
    "Betacellular is better than deltacellular.",
]

print(find_k_top(keywords, k, reviews))
