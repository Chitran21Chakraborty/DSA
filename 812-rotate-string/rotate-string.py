class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # s = list(s)
        # goal = list(goal)
        # if s == goal:
        #     return True
        # length = len(s)
        # for i in range(length):
        #     s[i] ,s[length-1]= s[length-1], s[i]
        #     if s == goal:
        #         return True
        #     length -= 1
        # return False

        if len(s) != len(goal):
            return False
        return goal in s+s

        

        