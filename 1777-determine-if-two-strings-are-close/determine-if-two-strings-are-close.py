from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # count = defaultdict(str)
        # if len(word1) != len(word2):
        #     return False
        # for i in range(len(word1)):
        #     if count[i] != count[i+1]:
        #         return False
        # return True
        cnt1, cnt2 = Counter(word1), Counter(word2)
        return sorted(cnt1.values()) ==sorted(cnt2.values()) and set(cnt1.keys()) == set(cnt2.keys())