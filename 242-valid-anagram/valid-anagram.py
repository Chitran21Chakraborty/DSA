class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s) == sorted(t)

        # if len(s)!= len(t):
        #     return False
        # set_s =  set(s)
        # for i in set_s:
        #     if s.count(i) != t.count(i):
        #         return False
        # return True

        count_s = Counter(s)
        count_t = Counter(t)
        if count_s == count_t:
            return True
        return False