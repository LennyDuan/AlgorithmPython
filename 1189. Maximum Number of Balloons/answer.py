def maxNumberOfBalloons(self, text: str) -> int:
    text_dict = {
        'b': 0,
        'a': 0,
        'l': 0,
        'o': 0,
        'n': 0,
    }

    for char in text:
        if char in text_dict.keys():
            text_dict[char] += 1

    text_dict['l'] //= 2
    text_dict['o'] //= 2
    return min(text_dict.values())
    #
    # for i in range(1, len(text) // 2):
    #     if text_dict['a'] >= i \
    #             and text_dict['b'] >= i \
    #             and text_dict['l'] >= i * 2 \
    #             and text_dict['o'] >= i * 2 \
    #             and text_dict['n'] >= i:
    #         res = i
    #     else:
    #         break
    return res


text = "loonbalxballpoon"
print(maxNumberOfBalloons(None, text))
