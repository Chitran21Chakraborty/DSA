class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(string: str)->list:
            stk = []
            for i in string:
                if i != "#":
                    stk.append(i)
                elif stk:
                    stk.pop()
            return stk
        return build(s)==build(t)