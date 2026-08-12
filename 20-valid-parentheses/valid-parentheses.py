class Solution:
    def isValid(self, s: str) -> bool:
        mapp ={'(':')','{':'}','[':']'}
        stack = []
        for c in s:
            if c in mapp:
                stack.append(c)
            else:
                if stack==[] or mapp[stack.pop()] != c:
                    return False
        return True if stack==[] else False
        