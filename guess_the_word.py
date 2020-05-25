import collections


class Solution1:
    def findSecretWord(self, wordlist, master):
        def matches(w1, w2):
            return sum(x == y for x, y in zip(w1, w2))

        # sorting by last character
        wordlist.sort(key=lambda x: x[-1])

        def get_word_set(word_set, word, n):
            return {w for w in word_set
                    if matches(word, wordlist[w]) == n}

        word_set = set(range(len(wordlist)))
        while word_set:
            i = word_set.pop()
            n = master.guess(wordlist[i])
            # n = 3
            word_set = get_word_set(word_set, wordlist[i], n)


class FinalSolution:
    def findSecretWord(self, wordlist, master):
        place_counts = collections.defaultdict(int)
        for w in wordlist:
            for i, c in enumerate(w):
                place_counts[str(i) + c] += 1

        def unique(word):
            return sum(place_counts[str(i) + c] for i, c in enumerate(word))

        def is_possible(w1, w2, n):
            if w1 == w2:
                return False
            return sum(x == y for x, y in zip(w1, w2)) == n

        # low score   -> high score
        # most unique -> least unique (common)
        wordlist.sort(key=unique)

        end = -1
        word_idx = list(range(len(wordlist)))
        for _ in range(10):
            guess_word = wordlist[word_idx[end]]
            matches = master.guess(guess_word)
            if matches == 6:
                break
            elif matches == 0:
                # If matches 0, guess_word was not very unique. Then it eliminates many similar words.
                word_idx = [i for i in word_idx if not any(a == b for a, b in zip(guess_word, wordlist[i]))]
                if end == 0:
                    end = -1  # guess a common word
            else:
                #  If matches 1-5, the guess_word was somehow unique. Then it eliminates many unsimilar words.
                word_idx = [i for i in word_idx if is_possible(guess_word, wordlist[i], matches)]
                if end == -1:
                    end = 0  # guess a unique word


if __name__ == '__main__':
    # secret = "acckzz"
    wordlist = ["ccbazz", "acckzz", "eiowzz", "abcczz"]

    # secret = "ccoyyo"
    wordlist = ["wichbx", "oahwep", "tpulot", "eqznzs", "vvmplb", "eywinm", "dqefpt", "kmjmxr", "ihkovg", "trbzyb", "xqulhc",
     "bcsbfw", "rwzslk", "abpjhw", "mpubps", "viyzbc", "kodlta", "ckfzjh", "phuepp", "rokoro", "nxcwmo", "awvqlr",
     "uooeon", "hhfuzz", "sajxgr", "oxgaix", "fnugyu", "lkxwru", "mhtrvb", "xxonmg", "tqxlbr", "euxtzg", "tjwvad",
     "uslult", "rtjosi", "hsygda", "vyuica", "mbnagm", "uinqur", "pikenp", "szgupv", "qpxmsw", "vunxdn", "jahhfn",
     "kmbeok", "biywow", "yvgwho", "hwzodo", "loffxk", "xavzqd", "vwzpfe", "uairjw", "itufkt", "kaklud", "jjinfa",
     "kqbttl", "zocgux", "ucwjig", "meesxb", "uysfyc", "kdfvtw", "vizxrv", "rpbdjh", "wynohw", "lhqxvx", "kaadty",
     "dxxwut", "vjtskm", "yrdswc", "byzjxm", "jeomdc", "saevda", "himevi", "ydltnu", "wrrpoc", "khuopg", "ooxarg",
     "vcvfry", "thaawc", "bssybb", "ccoyyo", "ajcwbj", "arwfnl", "nafmtm", "xoaumd", "vbejda", "kaefne", "swcrkh",
     "reeyhj", "vmcwaf", "chxitv", "qkwjna", "vklpkp", "xfnayl", "ktgmfn", "xrmzzm", "fgtuki", "zcffuv", "srxuus",
     "pydgmq"]

    # FinalSolution().findSecretWord(wordlist, None)
    w1, w2 = 'acckzz', 'ccbazz'
    r = sum(a == b for a, b in zip(w1, w2))
    print(r)
