class Solution:
    def isValid(self, s: str) -> bool:
        d = {"(":")", "{":"}","[":"]"}
        stack = []
        for char in s:
            if char in d: #if it is an opening bracket
                stack.append(char) # append the opening bracket
            else:
                if stack == [] or d[stack.pop()] != char:
                    return False
        return True if stack == [] else False