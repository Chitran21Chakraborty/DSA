class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minLength = len(strs[0])
        for s in strs:
            minLength = min(minLength,len(s))
        res = []
        for i in range(minLength):
            ch = strs[0][i]
            for s in strs:
                if s[i]!=ch:
                    return "".join(res)
            res.append(ch)
        return "".join(res)