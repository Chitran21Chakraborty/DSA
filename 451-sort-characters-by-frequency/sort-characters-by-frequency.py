from collections import Counter,defaultdict
class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s) # char -> cnt
        bucket = defaultdict(list) # freq -> [char], good when taversing while a key is missing (no keyError)
        for char,cnt in count.items():
            bucket[cnt].append(char) # until freq is same order does not matter
        res = [] # result
        for i in range(len(s),0,-1):
            for c in bucket[i]:
                res.append(c * i)
        return "".join(res)

        