class Solution:
    def isValid(self, s: str) -> bool:
        mapp = {'(':')','{':'}','[':']'}
        stk = []
        for char in s:
            if char in mapp:
                stk.append(char)
            else:
                if stk==[] or mapp[stk.pop()]!=char:
                    return False
        return True if stk==[] else False
