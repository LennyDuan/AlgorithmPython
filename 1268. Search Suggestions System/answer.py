def suggestedProducts(self, products: [], searchWord: str) -> []:
    search = ''
    res = []
    for char in searchWord:
        search += char
        current_res = []
        for word in products:
            if word.find(search) == 0:
                current_res.append(word)
        current_res.sort()
        res.append(current_res[:3])

    return res


products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
searchWord = "mouse"

print(suggestedProducts(None, products, searchWord))
