import collections


def replaceWords(self, roots, sentence: str):
    Trie = lambda: collections.defaultdict(Trie)
    trie = Trie()
    END = True

    for root in roots:
        cur = trie
        for char in root:
            cur = cur[char]
        cur[END] = root

    def replace(word):
        cur = trie
        for char in word:
            if char not in cur:
                break
            cur = cur[char]
            if END in cur:
                return cur[END]
        return word

    return ' '.join([replace(w) for w in sentence.split(' ')])












#
# def replaceWords(self, roots, sentence: str):
#     _trie = lambda: collections.defaultdict(_trie)
#     trie = _trie()
#     END = True
#     for root in roots:
#         cur = trie
#         for char in root:
#             cur = cur[char]
#         cur[END] = root
#     print(trie)
#
#     def replace(word):
#         cur = trie
#         for letter in word:
#             if letter not in cur:
#                 break
#             cur = cur[letter]
#             if END in cur:
#                 return cur[END]
#         return word
#     return ' '.join(map(replace, sentence.split(' ')))


#
dictionary = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
print(replaceWords(None, dictionary, sentence))

# dictionary = ["a", "aa", "aaa", "aaaa"]
# sentence = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"
# print(replaceWords(None, dictionary, sentence))

# dictionary = ["catt", "cat", "bat", "rat"]
# sentence = "the cattle was rattled by the battery"
# print(replaceWords(None, dictionary, sentence))
# dictionary = ["e", "k", "c", "harqp", "h", "gsafc", "vn", "lqp", "soy", "mr", "x", "iitgm", "sb", "oo", "spj", "gwmly",
#               "iu", "z", "f", "ha", "vds", "v", "vpx", "fir", "t", "xo", "apifm", "tlznm", "kkv", "nxyud", "j", "qp",
#               "omn", "zoxp", "mutu", "i", "nxth", "dwuer", "sadl", "pv", "w", "mding", "mubem", "xsmwc", "vl", "farov",
#               "twfmq", "ljhmr", "q", "bbzs", "kd", "kwc", "a", "buq", "sm", "yi", "nypa", "xwz", "si", "amqx", "iy",
#               "eb", "qvgt", "twy", "rf", "dc", "utt", "mxjfu", "hm", "trz", "lzh", "lref", "qbx", "fmemr", "gil", "go",
#               "qggh", "uud", "trnhf", "gels", "dfdq", "qzkx", "qxw"]
# sentence = "ikkbp miszkays wqjferqoxjwvbieyk gvcfldkiavww vhokchxz dvypwyb bxahfzcfanteibiltins ueebf lqhflvwxksi dco kddxmckhvqifbuzkhstp wc ytzzlm gximjuhzfdjuamhsu gdkbmhpnvy ifvifheoxqlbosfww mengfdydekwttkhbzenk wjhmmyltmeufqvcpcxg hthcuovils ldipovluo aiprogn nusquzpmnogtjkklfhta klxvvlvyh nxzgnrveghc mpppfhzjkbucv cqcft uwmahhqradjtf iaaasabqqzmbcig zcpvpyypsmodtoiif qjuiqtfhzcpnmtk yzfragcextvx ivnvgkaqs iplazv jurtsyh gzixfeugj rnukjgtjpim hscyhgoru aledyrmzwhsz xbahcwfwm hzd ygelddphxnbh rvjxtlqfnlmwdoezh zawfkko iwhkcddxgpqtdrjrcv bbfj mhs nenrqfkbf spfpazr wrkjiwyf cw dtd cqibzmuuhukwylrnld dtaxhddidfwqs bgnnoxgyynol hg dijhrrpnwjlju muzzrrsypzgwvblf zbugltrnyzbg hktdviastoireyiqf qvufxgcixvhrjqtna ipfzhuvgo daee r nlipyfszvxlwqw yoq dewpgtcrzausqwhh qzsaobsghgm ichlpsjlsrwzhbyfhm ksenb bqprarpgnyemzwifqzz oai pnqottd nygesjtlpala qmxixtooxtbrzyorn gyvukjpc s mxhlkdaycskj uvwmerplaibeknltuvd ocnn frotscysdyclrc ckcttaceuuxzcghw pxbd oklwhcppuziixpvihihp"

print(replaceWords(None, dictionary, sentence))
