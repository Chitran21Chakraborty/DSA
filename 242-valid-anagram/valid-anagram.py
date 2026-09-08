# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         # s_sorted= sorted(s)
#         # t_sorted=sorted(t)
#         # if s_sorted==t_sorted:
#         #     return True
#         # return False
#         if len(s)!=len(t):
#             return False
#         for ch in set(s):
#             if s.count(ch)!=t.count(ch):
#                 return False
#         return True
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return Counter(s) == Counter(t)