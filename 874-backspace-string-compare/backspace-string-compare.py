class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # def build(string: str)->list:
        #     stk = []
        #     for i in string:
        #         if i != "#":
        #             stk.append(i)
        #         elif stk:
        #             stk.pop()
        #     return stk
        # return build(s)==build(t)
        stk_s = []
        stk_t = []
        for i in s:
            if i != "#":
                stk_s.append(i)
            elif stk_s:
                stk_s.pop()
        for i in t:
            if i != "#":
                stk_t.append(i)
            elif stk_t:
                stk_t.pop()
        return stk_s == stk_t