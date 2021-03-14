def replaceWords(self, dictionary, sentence: str):
    res = []
    real_dictionary = set()
    for word in sorted(dictionary):
        if not any(w in word and word.index(w) == 0 for w in real_dictionary):
            real_dictionary.add(word)

    print(real_dictionary)
    sentence_arr = sentence.split(' ')

    for word in sentence_arr:
        found = False
        for dic_char in real_dictionary:
            if word.find(dic_char) == 0 and word.index(dic_char) == 0:
                found = dic_char
                break
        res.append(found if found else word)

    return ' '.join(res)


#
# dictionary = ["cat", "bat", "rat"]
# sentence = "the cattle was rattled by the battery"
# print(replaceWords(None, dictionary, sentence))
#
# dictionary = ["a", "aa", "aaa", "aaaa"]
# sentence = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"
# print(replaceWords(None, dictionary, sentence))

# dictionary = ["catt", "cat", "bat", "rat"]
# sentence = "the cattle was rattled by the battery"
# print(replaceWords(None, dictionary, sentence))
dictionary = ["e", "k", "c", "harqp", "h", "gsafc", "vn", "lqp", "soy", "mr", "x", "iitgm", "sb", "oo", "spj", "gwmly",
              "iu", "z", "f", "ha", "vds", "v", "vpx", "fir", "t", "xo", "apifm", "tlznm", "kkv", "nxyud", "j", "qp",
              "omn", "zoxp", "mutu", "i", "nxth", "dwuer", "sadl", "pv", "w", "mding", "mubem", "xsmwc", "vl", "farov",
              "twfmq", "ljhmr", "q", "bbzs", "kd", "kwc", "a", "buq", "sm", "yi", "nypa", "xwz", "si", "amqx", "iy",
              "eb", "qvgt", "twy", "rf", "dc", "utt", "mxjfu", "hm", "trz", "lzh", "lref", "qbx", "fmemr", "gil", "go",
              "qggh", "uud", "trnhf", "gels", "dfdq", "qzkx", "qxw"]
sentence = "ikkbp miszkays wqjferqoxjwvbieyk gvcfldkiavww vhokchxz dvypwyb bxahfzcfanteibiltins ueebf lqhflvwxksi dco kddxmckhvqifbuzkhstp wc ytzzlm gximjuhzfdjuamhsu gdkbmhpnvy ifvifheoxqlbosfww mengfdydekwttkhbzenk wjhmmyltmeufqvcpcxg hthcuovils ldipovluo aiprogn nusquzpmnogtjkklfhta klxvvlvyh nxzgnrveghc mpppfhzjkbucv cqcft uwmahhqradjtf iaaasabqqzmbcig zcpvpyypsmodtoiif qjuiqtfhzcpnmtk yzfragcextvx ivnvgkaqs iplazv jurtsyh gzixfeugj rnukjgtjpim hscyhgoru aledyrmzwhsz xbahcwfwm hzd ygelddphxnbh rvjxtlqfnlmwdoezh zawfkko iwhkcddxgpqtdrjrcv bbfj mhs nenrqfkbf spfpazr wrkjiwyf cw dtd cqibzmuuhukwylrnld dtaxhddidfwqs bgnnoxgyynol hg dijhrrpnwjlju muzzrrsypzgwvblf zbugltrnyzbg hktdviastoireyiqf qvufxgcixvhrjqtna ipfzhuvgo daee r nlipyfszvxlwqw yoq dewpgtcrzausqwhh qzsaobsghgm ichlpsjlsrwzhbyfhm ksenb bqprarpgnyemzwifqzz oai pnqottd nygesjtlpala qmxixtooxtbrzyorn gyvukjpc s mxhlkdaycskj uvwmerplaibeknltuvd ocnn frotscysdyclrc ckcttaceuuxzcghw pxbd oklwhcppuziixpvihihp"

print(replaceWords(None, dictionary, sentence))
