class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        d = {"(":")","{":"}","[":"]"}
        for par in s:
            if par in d:
                stk.append(par)
            else:
                if stk==[] or d[stk.pop()] != par:
                    return False
        return True if stk==[] else False
